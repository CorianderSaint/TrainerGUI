import random

import cv2
from PySide6.QtCore import Signal, QThread

from algorithms.ImageAugmentAlgorithms import ImageAugment
from algorithms.processTool.ImageProcessAlgorithms import ImageProcess
from algorithms.processTool.ModifySuffix import *
from algorithms.processTool.SplitDataset import splitDataset
from algorithms.processTool.UniformName import *
from lib.Share import SI
from util.Util import *

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    预处理工具运行    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

# ===================================================    统一后缀    ==================================================
class WorkerThread_modifySuffix_jpg_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                # 执行算法
                new_path = toJpg(image_path, False)
                # 错误图片
                if new_path == "":
                    SI.error_images_path.append(image_path)
                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《toJpg WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()


class WorkerThread_modifySuffix_jpeg_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                # 执行算法
                new_path = toJpeg(image_path, False)
                # 错误图片
                if new_path == "":
                    SI.error_images_path.append(image_path)
                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《toJpeg WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()

class WorkerThread_modifySuffix_png_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                # 执行算法
                new_path = toPng(image_path, False)
                # 错误图片
                if new_path == "":
                    SI.error_images_path.append(image_path)
                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《toPng WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()

class WorkerThread_modifySuffix_bmp_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                # 执行算法
                new_path = toBmp(image_path, False)
                # 错误图片
                if new_path == "":
                    SI.error_images_path.append(image_path)
                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《toBmp WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()

# ===================================================    统一后缀    ==================================================
class WorkerThread_uniformName1_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            # 先以当前时间戳重命名，防止重复
            temp_images = uniformName_temp(SI.dataset_path)
            if temp_images:
                SI.dataset_images_path = temp_images
            # 按格式重命名
            current = 1
            classificationNameList = os.listdir(SI.dataset_path)
            for classificationName in classificationNameList:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                if SI.flag_rename0:
                    index = 0
                else:
                    index = 1
                classificationNamePath = os.path.join(os.path.abspath(SI.dataset_path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 中断检测
                    if self.isInterruptionRequested():
                        break
                    # 执行算法
                    src = os.path.join(os.path.abspath(classificationNamePath), img)
                    suffix = os.path.splitext(src)[1]
                    if uniformName_image(src, classificationNamePath, classificationName, suffix, index, "分类_i"):
                        index += 1
                    else:
                        SI.error_images_path.append(src)
                    # 发送信号
                    self.update_signal.emit(current)
                    current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《uniformName1 WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()


class WorkerThread_uniformName2_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            # 先以当前时间戳重命名，防止重复
            temp_images = uniformName_temp(SI.dataset_path)
            if temp_images:
                SI.dataset_images_path = temp_images
            # 按格式重命名
            current = 1
            classificationNameList = os.listdir(SI.dataset_path)
            for classificationName in classificationNameList:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                if SI.flag_rename0:
                    index = 0
                else:
                    index = 1
                classificationNamePath = os.path.join(os.path.abspath(SI.dataset_path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 中断检测
                    if self.isInterruptionRequested():
                        break
                    # 执行算法
                    src = os.path.join(os.path.abspath(classificationNamePath), img)
                    suffix = os.path.splitext(src)[1]
                    if uniformName_image(src, classificationNamePath, classificationName, suffix, index, "分类i"):
                        index += 1
                    else:
                        SI.error_images_path.append(src)
                    # 发送信号
                    self.update_signal.emit(current)
                    current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《uniformName2 WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()

class WorkerThread_uniformName3_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            # 先以当前时间戳重命名，防止重复
            temp_images = uniformName_temp(SI.dataset_path)
            if temp_images:
                SI.dataset_images_path = temp_images
            # 按格式重命名
            current = 1
            classificationNameList = os.listdir(SI.dataset_path)
            for classificationName in classificationNameList:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                if SI.flag_rename0:
                    index = 0
                else:
                    index = 1
                classificationNamePath = os.path.join(os.path.abspath(SI.dataset_path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 中断检测
                    if self.isInterruptionRequested():
                        break
                    # 执行算法
                    src = os.path.join(os.path.abspath(classificationNamePath), img)
                    suffix = os.path.splitext(src)[1]
                    if uniformName_image(src, classificationNamePath, classificationName, suffix, index, "分类-i"):
                        index += 1
                    else:
                        SI.error_images_path.append(src)
                    # 发送信号
                    self.update_signal.emit(current)
                    current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《uniformName3 WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()


# ===================================================    图片方形化    ==================================================
class WorkerThread_square_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            borderType = SI.param_square_ofDataset_borderType
            fillColor = SI.param_square_ofDataset_fillColor
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break

                # 实例化
                imageProcess = ImageProcess(image_path)
                # 保存路径
                classificationName = os.path.basename(os.path.dirname(image_path))
                image_name = os.path.basename(image_path)
                output_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), classificationName, image_name)
                # 执行算法
                try:
                    image_square = imageProcess.square(borderType, fillColor)
                    cv2.imwrite(output_path, image_square)
                except:
                    SI.error_images_path.append(image_path)

                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《square WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()

# ===================================================    统一大小    ==================================================
class WorkerThread_resize_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            dsize = SI.param_resize_ofDataset_dsize
            interpolation = SI.param_resize_ofDataset_interpolation
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break

                # 实例化
                imageProcess = ImageProcess(image_path)
                # 保存路径
                classificationName = os.path.basename(os.path.dirname(image_path))
                image_name = os.path.basename(image_path)
                output_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), classificationName, image_name)
                # 执行算法
                try:
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(output_path, image_resize)
                except:
                    SI.error_images_path.append(image_path)

                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《resize WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()


# ===================================================    数据集分割    ==================================================
class WorkerThread_split_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            current = 1
            classificationNameList = getClassification(SI.dataset_path)[1]
            for classificationName in classificationNameList:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break
                classificationNamePath = os.path.join(os.path.abspath(SI.dataset_path), classificationName)
                train_path = SI.train_path_ofDataset
                val_path = SI.val_path_ofDataset
                test_path = SI.test_path_ofDataset
                train_rate = SI.param_split_ofDataset_train
                val_rate = SI.param_split_ofDataset_val
                test_rate = SI.param_split_ofDataset_test
                splitDataset(classificationNamePath, train_path, val_path, test_path,
                             train_rate, val_rate, test_rate)
                # 发送信号
                self.update_signal.emit(current)
                current += 1
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《split WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()









# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    图像增强运行    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
class WorkerThread_imageAugment_run(QThread):
    update_signal = Signal(int)
    finished_signal = Signal()
    terminate_signal = Signal()
    def run(self):
        try:
            SI.error_images_path = []
            current = 1
            for image_path in SI.dataset_images_path:
                # 中断检测
                if self.isInterruptionRequested():
                    self.terminate_signal.emit()
                    break

                try:
                    # 读取图片
                    image_read = cv2.imread(image_path)
                    # 保存路径
                    classificationName = os.path.basename(os.path.dirname(image_path))
                    image_name = os.path.basename(image_path)
                    output_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), classificationName, image_name)
                    # 依次执行算法
                    for imageAugment in SI.current_imageAugment_ofDataset:
                        # 图像旋转
                        if imageAugment == "图像旋转":
                            # 获取参数
                            probability = SI.param_rotate_ofDataset_probability
                            degree1 = SI.param_rotate_ofDataset_degree1
                            degree2 = SI.param_rotate_ofDataset_degree2
                            degree = random.uniform(degree1, degree2)
                            scale1 = SI.param_rotate_ofDataset_scale1
                            scale2 = SI.param_rotate_ofDataset_scale2
                            scale = random.uniform(scale1, scale2)
                            fillColor = SI.param_rotate_ofDataset_fillColor
                            # 执行算法
                            if random.uniform(0, 1) <= probability:
                                image_read = ImageAugment(image_read).rotate(angle=degree, scale=scale, fillColor=fillColor)
                        # 水平翻转
                        elif imageAugment == "水平翻转":
                            # 获取参数
                            probability = SI.param_HFlip_ofDataset_probability
                            # 执行算法
                            if random.uniform(0, 1) <= probability:
                                image_read = ImageAugment(image_read).flip(1)
                        # 垂直翻转
                        elif imageAugment == "垂直翻转":
                            # 获取参数
                            probability = SI.param_VFlip_ofDataset_probability
                            # 执行算法
                            if random.uniform(0, 1) <= probability:
                                image_read = ImageAugment(image_read).flip(0)
                        # 模糊
                        elif imageAugment == "模糊":
                            probability = SI.param_blur_ofDataset_probability
                            if random.uniform(0, 1) <= probability:
                                # 获取参数
                                blur = SI.param_blur_ofDataset_filter
                                ksize_from = SI.param_blur_ofDataset_ksizeFrom
                                ksize_to = SI.param_blur_ofDataset_ksizeTo
                                # 随机选取ksize
                                ksize = random.randint(ksize_from, ksize_to)
                                if (blur == "高斯滤波") or (blur == "中值滤波"):
                                    while ksize % 2 == 0:  # 确保为奇数
                                        ksize = random.randint(ksize_from, ksize_to)
                                # 执行算法
                                if blur == "均值滤波":
                                    image_read = ImageAugment(image_read).blur((ksize, ksize))
                                elif blur == "方框滤波":
                                    image_read = ImageAugment(image_read).boxBlur((ksize, ksize))
                                elif blur == "高斯滤波":
                                    image_read = ImageAugment(image_read).gaussianBlur((ksize, ksize))
                                elif blur == "中值滤波":
                                    image_read = ImageAugment(image_read).medianBlur(ksize)
                        # 噪声
                        elif imageAugment == "噪声":
                            probability = SI.param_noise_ofDataset_probability
                            if random.uniform(0, 1) <= probability:
                                # 获取参数
                                sigma1 = SI.param_noise_ofDataset_sigma1
                                sigma2 = SI.param_noise_ofDataset_sigma2
                                rate1 = SI.param_noise_ofDataset_rate1
                                rate2 = SI.param_noise_ofDataset_rate2
                                # 执行算法
                                if ("noise_gaussian" not in SI.imageAugmentAlgorithm_ofDataset) and (
                                        "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset):  # 01=1
                                    rate = random.uniform(rate1, rate2)
                                    image_read = ImageAugment(image_read).saltPepperNoise(rate=rate)
                                elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset) and (
                                        "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofDataset):  # 10=2
                                    sigma = random.uniform(sigma1, sigma2)
                                    image_read = ImageAugment(image_read).gaussianNoise(sigma=sigma)
                                elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset) and (
                                        "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset):  # 11=3
                                    sigma = random.uniform(sigma1, sigma2)
                                    rate = random.uniform(rate1, rate2)
                                    image_read = ImageAugment(image_read).gaussianNoise(sigma=sigma)
                                    image_read = ImageAugment(image_read).saltPepperNoise(rate=rate)
                        # 亮度
                        elif imageAugment == "亮度":
                            # 获取参数
                            probability = SI.param_brightness_ofDataset_probability
                            beta1 = SI.param_brightness_ofDataset_beta1
                            beta2 = SI.param_brightness_ofDataset_beta2
                            # 执行算法
                            if random.uniform(0, 1) <= probability:
                                beta = random.uniform(beta1, beta2)
                                image_read = ImageAugment(image_read).brightness(beta)
                        # 对比度
                        elif imageAugment == "对比度":
                            # 获取参数
                            probability = SI.param_contrast_ofDataset_probability
                            alpha1 = SI.param_contrast_ofDataset_alpha1
                            alpha2 = SI.param_contrast_ofDataset_alpha2
                            # 执行算法
                            if random.uniform(0, 1) <= probability:
                                alpha = random.uniform(alpha1, alpha2)
                                image_read = ImageAugment(image_read).brightness(alpha)

                    # 保存图片
                    cv2.imwrite(output_path, image_read)
                except:
                    SI.error_images_path.append(image_path)
                finally:
                    del image_read

                # 发送信号
                self.update_signal.emit(current)
                current += 1
            SI.dataset_images_path = getDatasetImage(SI.dataset_path)
            if not self.isInterruptionRequested():
                self.finished_signal.emit()
        except Exception as e:
            print("《imageAugment WorkThread》时错误：", e)
    def stop(self):
        self.requestInterruption()