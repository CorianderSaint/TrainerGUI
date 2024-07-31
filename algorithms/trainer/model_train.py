import sys
import json

import torch
from PySide6.QtCore import QThread, Signal
from torch.utils import data
from torchvision import datasets
from tqdm import tqdm

from algorithms.trainer.model_options import *
from lib.Parameters import Param
from util.Util import *


class WorkerThread_ModelTrain(QThread):
    finished_signal = Signal()
    terminated_signal = Signal()
    update_epoch_lossAndAcc_signal = Signal(list, list, list)
    update_step_loss_signal = Signal(list, list, int)

    def run(self):
        try:
            running_text = f"Running {Param.net_name}" + '.' * 50
            print(running_text)
            with open(SI.log_text_path, 'a') as log_file:
                log_file.write(running_text + '\n')

            # ********************************************************************
            epoch_list = list(range(1, Param.epochs + 1))
            trainLoss_epoch_list = []
            valAcc_epoch_list = []
            # ********************************************************************

            device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
            print("using {} device.".format(device))

            data_transform = get_transform()

            train_dataset = datasets.ImageFolder(root=SI.dataset_train_path,
                                                 transform=data_transform["train"])
            train_num = len(train_dataset)

            # 获取分类文件夹的索引：{'class': index}
            classification_list = train_dataset.class_to_idx
            # 交换key和value：{index: 'class'}
            cla_dict = dict((val, key) for key, val in classification_list.items())
            # 将cla_dict编码成json格式
            json_str = json.dumps(cla_dict, indent=4)
            with open(SI.class_indices_path, 'w') as json_file:
                json_file.write(json_str)

            batch_size = Param.batch_size
            # nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])  # number of workers
            nw = 0

            train_loader = torch.utils.data.DataLoader(train_dataset,
                                                       batch_size=batch_size, shuffle=True,
                                                       num_workers=nw)
            validate_dataset = datasets.ImageFolder(root=SI.dataset_val_path,
                                                    transform=data_transform["val"])
            val_num = len(validate_dataset)
            validate_loader = torch.utils.data.DataLoader(validate_dataset,
                                                          batch_size=batch_size, shuffle=False,
                                                          num_workers=nw)

            print("using {} images for training, {} images for validation.".format(train_num, val_num))

            # 加载模型
            net = choose_net(True)
            net.to(device)

            ##########################################################
            # 损失函数
            loss_function = choose_loss_function()
            # 优化器
            optimizer = choose_optimizer(net)
            # 模型保存路径
            save_path = get_save_path(Param.net_name + ".pth")
            SI.model_save_path = save_path
            # 中间模型保存路径
            checkpoints_path = get_checkpoints_path()
            ##########################################################

            epochs = Param.epochs
            best_acc = 0.0
            train_steps = len(train_loader)
            step_count = 0

            # ********************************************************************
            step_list = list(range(1, train_steps * epochs + 1))
            stepLoss_step_list = []
            # ********************************************************************
            log_text = ""
            for epoch in range(epochs):
                # 中断检测
                if self.isInterruptionRequested():
                    break
                # train
                net.train()
                running_loss = 0.0
                train_bar = tqdm(train_loader, file=sys.stdout)
                for step, data in enumerate(train_bar):
                    # 中断检测
                    if self.isInterruptionRequested():
                        break
                    step_count += 1
                    images, labels = data
                    optimizer.zero_grad()
                    if Param.net_name == "GoogLeNet":
                        logits, aux_logits2, aux_logits1 = net(images.to(device))
                        loss0 = loss_function(logits, labels.to(device))
                        loss1 = loss_function(aux_logits1, labels.to(device))
                        loss2 = loss_function(aux_logits2, labels.to(device))
                        loss = loss0 + loss1 * 0.3 + loss2 * 0.3
                    else:
                        outputs = net(images.to(device))
                        loss = loss_function(outputs, labels.to(device))
                    loss.backward()
                    optimizer.step()
                    running_loss += loss.item()
                    train_bar.desc = "train epoch[{}/{}] loss:{:.3f}".format(epoch + 1, epochs, loss)

                    # ***************************************************************
                    stepLoss_step_list.append(loss.item())
                    self.update_step_loss_signal.emit(step_list[:step_count], stepLoss_step_list, train_steps)
                    # ***************************************************************

                # validate
                net.eval()
                acc = 0.0  # 预测正确的个数
                with torch.no_grad():
                    val_bar = tqdm(validate_loader, file=sys.stdout)
                    for val_data in val_bar:
                        # 中断检测
                        if self.isInterruptionRequested():
                            break
                        val_images, val_labels = val_data
                        outputs = net(val_images.to(device))
                        predict_y = torch.max(outputs, dim=1)[1]
                        acc += torch.eq(predict_y, val_labels.to(device)).sum().item()

                val_accurate = acc / val_num
                train_loss = running_loss / train_steps
                loss_text = '[epoch %d] train_loss: %.3f  val_accuracy: %.3f' % (epoch + 1, train_loss, val_accurate)
                log_text += loss_text + '\n'
                print(loss_text)

                # ***************************************************************
                trainLoss_epoch_list.append(train_loss)
                valAcc_epoch_list.append(val_accurate)
                self.update_epoch_lossAndAcc_signal.emit(epoch_list[:epoch + 1], trainLoss_epoch_list,
                                                         valAcc_epoch_list)
                # ***************************************************************

                # 每隔几epoch保存一次
                if (epoch + 1) % Param.save_period == 0:
                    save_name = getSaveName(Param.net_name, epoch + 1, train_loss, val_accurate)
                    save_period_path = os.path.join(os.path.abspath(checkpoints_path), save_name)
                    torch.save(net.state_dict(), save_period_path)
                # 保存验证最好的模型
                if val_accurate > best_acc:
                    best_acc = val_accurate
                    torch.save(net.state_dict(), save_path)

            with open(SI.log_text_path, 'a') as log_file:
                log_file.write(log_text + '\n')
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
                print('Finished Training.')
            else:
                self.terminated_signal.emit()
                print('Terminated Training.')


        except Exception as e:
            SI.threadMutex = False
            self.terminated_signal.emit()
            print("《Training WorkThread》时错误：", e)

    def stop(self):
        self.requestInterruption()
