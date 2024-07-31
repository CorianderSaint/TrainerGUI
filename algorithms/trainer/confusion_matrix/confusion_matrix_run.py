import json
import os

import torch
from PySide6.QtCore import QThread, Signal
from torchvision import transforms, datasets
from torch.utils import data
from tqdm import tqdm

from algorithms.trainer.confusion_matrix.confusion_matrix import ConfusionMatrix
from algorithms.trainer.model_options import choose_net
from lib.Parameters import Param
from lib.Share import SI
import torch.nn as nn


class ConfusionMatrixRun(QThread):
    finished_signal = Signal()
    terminated_signal = Signal()
    def run(self):
        try:
            print("Running confusion matrix......................................")
            device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

            data_transform = transforms.Compose([transforms.Resize(Param.input_size),
                                                 transforms.ToTensor(),
                                                 transforms.Normalize(Param.test_mean, Param.test_std)])

            test_dataset = datasets.ImageFolder(root=SI.dataset_test_path, transform=data_transform)

            batch_size = Param.batch_size
            test_loader = torch.utils.data.DataLoader(test_dataset,
                                                      batch_size=batch_size, shuffle=False,
                                                      num_workers=0)
            # load pretrain weights
            model_weight_path = SI.model_save_path
            assert os.path.exists(model_weight_path), "cannot find {} file".format(model_weight_path)

            net = choose_net(False)
            if Param.net_name == "GoogLeNet":
                net.load_state_dict(torch.load(model_weight_path, map_location=device), strict=False)
            else:
                net.load_state_dict(torch.load(model_weight_path, map_location=device))
            net.to(device)

            # read class_indict
            json_label_path = SI.class_indices_path
            assert os.path.exists(json_label_path), "cannot find {} file".format(json_label_path)
            json_file = open(json_label_path, 'r')
            class_indict = json.load(json_file)

            labels = [label for _, label in class_indict.items()]
            confusion = ConfusionMatrix(num_classes=Param.num_classes, labels=labels,
                                        matrix_save_path=SI.matrix_save_path, log_text_path=SI.log_text_path)
            net.eval()
            with torch.no_grad():
                for test_data in tqdm(test_loader):
                    # 中断检测
                    if self.isInterruptionRequested():
                        break
                    test_images, test_labels = test_data
                    outputs = net(test_images.to(device))
                    outputs = torch.softmax(outputs, dim=1)
                    outputs = torch.argmax(outputs, dim=1)
                    confusion.update(outputs.to("cpu").numpy(), test_labels.to("cpu").numpy())
            confusion.plot()
            confusion.summary()
            del confusion

            if not self.isInterruptionRequested():
                self.finished_signal.emit()
                print("Confusion matrix finished.")
            else:
                self.terminated_signal.emit()
                print("Confusion matrix terminated.")
        except Exception as e:
            print("《Confusion matrix》运行时错误：", e)
            self.terminated_signal.emit()
            SI.threadMutex = False

    def stop(self):
        self.requestInterruption()
