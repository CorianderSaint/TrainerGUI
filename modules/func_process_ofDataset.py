import time
from shutil import rmtree

import cv2
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QPixmap

from algorithms.ImageAugmentAlgorithms import ImageAugment
from algorithms.processTool.ImageProcessAlgorithms import ImageProcess
from lib.Share import SI
from modules.circular_progress_bar.CircularProgressBarWindow import CircularProgressBarWindow
from modules.workerThreaed_process_ofDataset import *
from util.MessageBox import *
from util.Util import *


# 图像处理ofDataset：预处理工具预览(...) + 预处理工具运行(...) + 图像增强预览(...) + 图像增强运行
class FuncProcessOfDataset:
    def __init__(self, window, widgets, preImage_path=None):
        self.window = window
        self.widgets = widgets
        self.preImage_path = preImage_path


    # ==============================================================================================================
    # ============================================    预处理工具预览    ==============================================
    # ==============================================================================================================
    def setReview(self):
        """
        实现预览框展示预览图片
        """
        # 预览-前-------------------------------------------------------------
        image_pre = QPixmap(self.preImage_path)
        image_pre_width = image_pre.width()
        image_pre_height = image_pre.height()
        if SI.isMaximized:
            self.widgets.lb_pre_dataset.setText(f"当前窗口像素：520×520\n当前图像像素：{image_pre_width}×{image_pre_height}")
        else:
            self.widgets.lb_pre_dataset.setText(f"当前窗口像素：360×360\n当前图像像素：{image_pre_width}×{image_pre_height}")
        self.widgets.img_pre_dataset.setPixmap(image_pre.scaled(
            QSize(image_pre_width, image_pre_height), aspectMode=Qt.KeepAspectRatio))
        self.widgets.img_pre_dataset.update()
        # 预览-后-------------------------------------------------------------
        image_after = QPixmap(SI.review_temp_image_path)
        image_after_width = image_after.width()
        image_after_height = image_after.height()
        if SI.isMaximized:
            self.widgets.lb_after_dataset.setText(f"当前窗口像素：520×520\n当前图像像素：{image_after_width}×{image_after_height}")
        else:
            self.widgets.lb_after_dataset.setText(f"当前窗口像素：360×360\n当前图像像素：{image_after_width}×{image_after_height}")
        self.widgets.img_after_dataset.setPixmap(image_after.scaled(
            QSize(image_after_width, image_after_height), aspectMode=Qt.KeepAspectRatio))
        self.widgets.img_after_dataset.update()
        # 预览结束------------------------------------------------------------

    # *********************************************    图片方形化    *************************************************
    def square_review(self, borderType, fillColor=None):
        print("正在预览：图片方形化", borderType)
        try:
            imageProcess = ImageProcess(self.preImage_path)                          # 实例化对象
            SI.review_temp_image_path = mkTempReviewImage(self.preImage_path)        # 创建预览图象路径

            if borderType == "BORDER_CONSTANT":
                print("正在预览：图片方形化 BORDER_CONSTANT，RGB=", fillColor)
                image_square = imageProcess.square(borderType, fillColor)
                cv2.imwrite(SI.review_temp_image_path, image_square)
            else:
                print("正在预览：图片方形化", borderType)
                image_square = imageProcess.square(borderType)
                cv2.imwrite(SI.review_temp_image_path, image_square)
            return True
        except Exception as e:
            errorBox(self.window, "错误", f"图片方形化预览失败：\n{self.preImage_path}")
            print("《预览图片方形化》时错误：", e)
            return False


    # **********************************************    统一大小    **************************************************
    def resize_review(self, dsize, interpolation):
        print("正在预览：更改大小")
        try:
            imageProcess = ImageProcess(self.preImage_path)                      # 实例化对象
            SI.review_temp_image_path = mkTempReviewImage(self.preImage_path)    # 创建预览图象路径

            if interpolation == "INTER_LINEAR":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_NEAREST":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_CUBIC":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_AREA":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_LANCZOS4":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_LINEAR_EXACT":
                print(f"正在预览：统一大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)

            return True
        except Exception as e:
            errorBox(self.window, "错误", f"统一大小预览失败：\n{self.preImage_path}")
            print("《预览统一大小》时错误：", e)
            return False



    # ==============================================================================================================
    # ===========================================    预处理工具运行    ===============================================
    # ==============================================================================================================
    def runningThread(self, threadClass, runningFunction, runningText):
        SI.threadMutex = True
        print(f"正在运行：{runningText}")
        try:
            # 获取图片总量
            total = len(SI.dataset_images_path)
            if runningFunction == "数据集分割":
                total = getClassification(SI.dataset_path)[0]
            # 执行多线程
            self.window.workerThread_ofDataset = threadClass()
            self.window.progress_window = CircularProgressBarWindow(self.window.workerThread_ofDataset, f"正在运行：{runningText}")
            self.window.progress_window.show()
            self.window.workerThread_ofDataset.update_signal.connect(
                lambda i: self.window.progress_window.update_progress(int(round(i / total, 2) * 100)))
            self.window.workerThread_ofDataset.update_signal.connect(
                lambda i: self.window.progress_window.progress_bar.Loading(f"{i}/{total}"))
            self.window.workerThread_ofDataset.finished_signal.connect(self.window.progress_window.task_finished)
            self.window.workerThread_ofDataset.finished_signal.connect(lambda: self.progress_finished(runningFunction))
            self.window.workerThread_ofDataset.terminate_signal.connect(lambda: self.progress_terminate(runningFunction))
            self.window.workerThread_ofDataset.start()

        except Exception as e:
            print(f"《{runningText}-run》时错误：", e)


    def progress_finished(self, runningFunction):
        """ 子线程运行完成后 """
        SI.threadMutex = False
        self.window.workerThread_ofDataset = None
        # 判断错误图片
        if SI.error_images_path:
            self.print_error_images()
        else:
            if runningFunction == "数据集分割":
                # 获取分割数量
                trainNum = getFileNum(SI.train_path_ofDataset)
                valNum = getFileNum(SI.val_path_ofDataset)
                testNum = getFileNum(SI.test_path_ofDataset)
                infoBox(self.window, "成功", f"{runningFunction}完成\nTrain: {trainNum}\nVal: {valNum}\nTest: {testNum}")
            else:
                infoBox(self.window, "成功", f"{runningFunction}完成")
        # 3秒后释放进度条窗口
        timer = QTimer(self.window.progress_window)
        timer.timeout.connect(self.window.progress_window.deleteLater)
        timer.start(3000)

    def progress_terminate(self, runningFunction):
        """ 子线程中断 """
        SI.threadMutex = False
        errorBox(self.window, "错误", f"{runningFunction}运行中断")
        self.window.progress_window.deleteLater()


    def print_error_images(self):
        """ 打印出错图片 """
        error_images = '\n'.join(SI.error_images_path[:])
        error_info = "以下图片处理失败：\n" + error_images
        errorBox(self.window, "错误", error_info)
        print('=' * 50 + '\n' + error_info + '\n' + '=' * 50)
        SI.error_images_path = []


    # **********************************************    统一后缀    **************************************************
    def modifySuffix_jpg_run(self):
        self.runningThread(WorkerThread_modifySuffix_jpg_run, "统一后缀", "统一后缀jpg")

    def modifySuffix_jpeg_run(self):
        self.runningThread(WorkerThread_modifySuffix_jpeg_run, "统一后缀", "统一后缀jpeg")

    def modifySuffix_png_run(self):
        self.runningThread(WorkerThread_modifySuffix_png_run, "统一后缀", "统一后缀png")

    def modifySuffix_bmp_run(self):
        self.runningThread(WorkerThread_modifySuffix_bmp_run, "统一后缀", "统一后缀bmp")

    # **********************************************    统一命名    **************************************************
    def uniformName1_run(self):
        self.runningThread(WorkerThread_uniformName1_run, "统一命名", "统一命名分类_i")

    def uniformName2_run(self):
        self.runningThread(WorkerThread_uniformName2_run, "统一命名", "统一命名分类i")

    def uniformName3_run(self):
        self.runningThread(WorkerThread_uniformName3_run, "统一命名", "统一命名分类-i")

    # *********************************************    图片方形化    *************************************************
    def square_run(self):
        if SI.export_path_ofDataset == "":
            errorBox(self.window, "错误", "请先设置导出路径")
            return
        else:
            if mkClassificationDir(SI.dataset_path, SI.export_path_ofDataset):
                borderType = SI.param_square_ofDataset_borderType
                if borderType == "BORDER_CONSTANT": borderType = "CONSTANT"
                elif borderType == "BORDER_REFLECT": borderType = "REFLECT"
                elif borderType == "BORDER_REPLICATE": borderType = "REPLICATE"
                elif borderType == "BORDER_WRAP": borderType = "WRAP"
                self.runningThread(WorkerThread_square_run, "图片方形化", f"图片方形化{borderType}")
            else:
                errorBox(self.window, "错误", "保存路径下无法创建分类文件夹")

    # **********************************************    统一大小    **************************************************
    def resize_run(self):
        if SI.export_path_ofDataset == "":
            errorBox(self.window, "错误", "请先设置导出路径")
            return
        else:
            if mkClassificationDir(SI.dataset_path, SI.export_path_ofDataset):
                interpolation = SI.param_resize_ofDataset_interpolation
                if interpolation == "INTER_LINEAR": interpolation = "LINEAR"
                elif interpolation == "INTER_NEAREST": interpolation = "NEAREST"
                elif interpolation == "INTER_CUBIC": interpolation = "CUBIC"
                elif interpolation == "INTER_AREA": interpolation = "AREA"
                elif interpolation == "INTER_LANCZOS4": interpolation = "LANCZOS4"
                elif interpolation == "INTER_LINEAR_EXACT": interpolation = "EXACT"
                self.runningThread(WorkerThread_resize_run, "统一大小", f"统一大小{interpolation}")
            else:
                errorBox(self.window, "错误", "保存路径下无法创建分类文件夹")

    # **********************************************    数据集分割    **************************************************
    def split_run(self):
        if SI.export_path_ofDataset == "":
            errorBox(self.window, "错误", "请先设置导出路径")
            return
        try:
            # 获取分割路径
            train_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), "train")
            val_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), "val")
            test_path = os.path.join(os.path.abspath(SI.export_path_ofDataset), "test")
            # 如果存在，则先删除
            if os.path.exists(train_path):
                rmtree(train_path)
            if os.path.exists(val_path):
                rmtree(val_path)
            if os.path.exists(test_path):
                rmtree(test_path)
            # 建立分割文件夹
            os.makedirs(train_path)
            os.makedirs(val_path)
            os.makedirs(test_path)
            # 建立分类文件夹
            mkClassificationDir(SI.dataset_path, train_path)
            mkClassificationDir(SI.dataset_path, val_path)
            mkClassificationDir(SI.dataset_path, test_path)
            SI.train_path_ofDataset = train_path
            SI.val_path_ofDataset = val_path
            SI.test_path_ofDataset = test_path
            self.runningThread(WorkerThread_split_run, "数据集分割", "数据集分割")
        except Exception as e:
            errorBox(self.window, "错误", "创建分割文件夹失败")
            print("《创建分割文件夹》时失败：", e)

    # ==============================================================================================================
    # ===========================================    图像增强预览    =================================================
    # ==============================================================================================================

    # *********************************************    图像旋转    *************************************************
    def rotate_review(self, image, rotateDegree, rotateScale, fillColor):
        return ImageAugment(image).rotate(angle=rotateDegree, scale=rotateScale, fillColor=fillColor)
    # *********************************************    水平翻转    *************************************************
    def HFlip_review(self, image):
        return ImageAugment(image).flip(1)
    # *********************************************    垂直翻转    *************************************************
    def VFlip_review(self, image):
        return ImageAugment(image).flip(0)
    # ***********************************************    模糊    ***************************************************
    def blur_review(self, image, blur, ksize1, ksize2):
        if blur == "均值滤波":
            return ImageAugment(image).blur((ksize1, ksize2))
        elif blur == "方框滤波":
            return ImageAugment(image).boxBlur((ksize1, ksize2))
        elif blur == "高斯滤波":
            return ImageAugment(image).gaussianBlur((ksize1, ksize2))
        elif blur == "中值滤波":
            return ImageAugment(image).medianBlur(ksize1)
    def noise_review(self, image, noiseTypeCode, sigma=0, rate=0):
        if noiseTypeCode == 1:
            return ImageAugment(image).saltPepperNoise(rate)
        elif noiseTypeCode == 2:
            return ImageAugment(image).gaussianNoise(sigma)
        elif noiseTypeCode == 3:
            image1 = ImageAugment(image).gaussianNoise(sigma)
            image2 = ImageAugment(image1).saltPepperNoise(rate)
            return image2
    def brightness_review(self, image, beta):
        return ImageAugment(image).brightness(beta)
    def contrast_review(self, image, alpha):
        return ImageAugment(image).contrast(alpha)


    # ==============================================================================================================
    # ===========================================    图像增强运行    =================================================
    # ==============================================================================================================
    def imageAugment_run(self):
        if mkClassificationDir(SI.dataset_path, SI.export_path_ofDataset):
            self.runningThread(WorkerThread_imageAugment_run, "图像增强", "图像增强")
        else:
            errorBox(self.window, "错误", "保存路径下无法创建分类文件夹")
