import numpy as np
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor
from PySide6.QtCore import Signal, QThread

from lib.Parameters import Param
from lib.Share import SI


class WorkerThreadCalculateNormalize(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        current = 1

        try:
            # 执行算法
            # ==============================================    train    ===============================================
            # 初始化均值和方差
            means = [0, 0, 0]
            std = [0, 0, 0]
            # 可将图片类型转化为张量，并把0~255的像素值缩小到0~1之间
            transform = ToTensor()
            # 导入数据集的图片，并且转化为张量
            dataset = ImageFolder(SI.dataset_train_path, transform=transform)
            # 获取数据集的图片数量
            num_imgs = len(dataset)

            # 遍历数据集的张量和标签
            for img, a in dataset:
                # 中断检测
                if self.isInterruptionRequested():
                    break
                # 遍历图片的RGB三通道
                for i in range(3):
                    # 计算每一个通道的均值和标准差
                    means[i] += img[i, :, :].mean()
                    std[i] += img[i, :, :].std()
                # 发送信号
                self.update_signal.emit(current)
                current += 1

            mean = np.array(means) / num_imgs
            std = np.array(std) / num_imgs  # 要使数据集归一化，均值和方差需除以总图片数量
            # np.array --> list
            mean_list = list(mean)
            std_list = list(std)
            # 保留三位小数
            Param.train_mean = [round(x, 3) for x in mean_list]
            Param.train_std = [round(x, 3) for x in std_list]

            # ==============================================    val    ===============================================
            # 初始化均值和方差
            means = [0, 0, 0]
            std = [0, 0, 0]
            # 可将图片类型转化为张量，并把0~255的像素值缩小到0~1之间
            transform = ToTensor()
            # 导入数据集的图片，并且转化为张量
            dataset = ImageFolder(SI.dataset_val_path, transform=transform)
            # 获取数据集的图片数量
            num_imgs = len(dataset)

            # 遍历数据集的张量和标签
            for img, a in dataset:
                # 中断检测
                if self.isInterruptionRequested():
                    break
                # 遍历图片的RGB三通道
                for i in range(3):
                    # 计算每一个通道的均值和标准差
                    means[i] += img[i, :, :].mean()
                    std[i] += img[i, :, :].std()
                # 发送信号
                self.update_signal.emit(current)
                current += 1

            mean = np.array(means) / num_imgs
            std = np.array(std) / num_imgs  # 要使数据集归一化，均值和方差需除以总图片数量
            # np.array --> list
            mean_list = list(mean)
            std_list = list(std)
            # 保留三位小数
            Param.val_mean = [round(x, 3) for x in mean_list]
            Param.val_std = [round(x, 3) for x in std_list]

            # ==============================================    test    ===============================================
            # 初始化均值和方差
            means = [0, 0, 0]
            std = [0, 0, 0]
            # 可将图片类型转化为张量，并把0~255的像素值缩小到0~1之间
            transform = ToTensor()
            # 导入数据集的图片，并且转化为张量
            dataset = ImageFolder(SI.dataset_test_path, transform=transform)
            # 获取数据集的图片数量
            num_imgs = len(dataset)

            # 遍历数据集的张量和标签
            for img, a in dataset:
                # 中断检测
                if self.isInterruptionRequested():
                    break
                # 遍历图片的RGB三通道
                for i in range(3):
                    # 计算每一个通道的均值和标准差
                    means[i] += img[i, :, :].mean()
                    std[i] += img[i, :, :].std()
                # 发送信号
                self.update_signal.emit(current)
                current += 1

            mean = np.array(means) / num_imgs
            std = np.array(std) / num_imgs  # 要使数据集归一化，均值和方差需除以总图片数量
            # np.array --> list
            mean_list = list(mean)
            std_list = list(std)
            # 保留三位小数
            Param.test_mean = [round(x, 3) for x in mean_list]
            Param.test_std = [round(x, 3) for x in std_list]

            if self.isInterruptionRequested():
                self.terminate_signal.emit()
            else:
                self.finished_signal.emit()
        except Exception as e:
            print("《Calculate Normalize WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()
