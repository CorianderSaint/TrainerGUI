import cv2
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

from algorithms.ImageAugmentAlgorithms import ImageAugment
from algorithms.processTool.ImageProcessAlgorithms import ImageProcess
from algorithms.processTool.ModifySuffix import *
from lib.Share import SI
from util.MessageBox import *
from util.Util import *

# 图像处理ofImage：预处理工具预览(...) + 预处理工具运行(...) + 图像增强
class FuncProcessOfImage:
    def __init__(self, window, widgets):
        self.window = window
        self.widgets = widgets
    # ==============================================================================================================
    # ============================================    预处理工具预览    ==============================================
    # ==============================================================================================================
    def setReview(self):
        """
        实现预览框展示预览图片
        """
        # 预览-前-------------------------------------------------------------
        image_pre = QPixmap(SI.image_path)
        image_pre_width = image_pre.width()
        image_pre_height = image_pre.height()
        if SI.isMaximized:
            self.widgets.lb_pre_image.setText(f"当前窗口像素：520×520\n当前图像像素：{image_pre_width}×{image_pre_height}")
        else:
            self.widgets.lb_pre_image.setText(f"当前窗口像素：360×360\n当前图像像素：{image_pre_width}×{image_pre_height}")
        self.widgets.img_pre_image.setPixmap(image_pre.scaled(
            QSize(image_pre_width, image_pre_height), aspectMode=Qt.KeepAspectRatio))
        self.widgets.img_pre_image.update()
        # 预览-后-------------------------------------------------------------
        image_after = QPixmap(SI.review_temp_image_path)
        image_after_width = image_after.width()
        image_after_height = image_after.height()
        if SI.isMaximized:
            self.widgets.lb_after_image.setText(f"当前窗口像素：520×520\n当前图像像素：{image_after_width}×{image_after_height}")
        else:
            self.widgets.lb_after_image.setText(f"当前窗口像素：360×360\n当前图像像素：{image_after_width}×{image_after_height}")
        self.widgets.img_after_image.setPixmap(image_after.scaled(
            QSize(image_after_width, image_after_height), aspectMode=Qt.KeepAspectRatio))
        self.widgets.img_after_image.update()
        # 预览结束------------------------------------------------------------


    # *********************************************    图片方形化    *************************************************
    def square_review(self, borderType, fillColor=None):
        print("正在预览：图片方形化", borderType)
        try:
            imageProcess = ImageProcess(SI.image_path)                          # 实例化对象
            SI.review_temp_image_path = mkTempReviewImage(SI.image_path)        # 创建预览图象路径

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
            errorBox(self.window, "错误", "图片方形化预览失败")
            print("《预览图片方形化》时错误：", e)
            return False


    # **********************************************    更改大小    **************************************************
    def resize_review(self, dsize, interpolation):
        print("正在预览：更改大小")
        try:
            imageProcess = ImageProcess(SI.image_path)                      # 实例化对象
            SI.review_temp_image_path = mkTempReviewImage(SI.image_path)    # 创建预览图象路径

            if interpolation == "INTER_LINEAR":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_NEAREST":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_CUBIC":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_AREA":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_LANCZOS4":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)
            elif interpolation == "INTER_LINEAR_EXACT":
                print(f"正在预览：更改大小{interpolation}，dsize={dsize}")
                image_resize = imageProcess.resize(dsize, interpolation)
                cv2.imwrite(SI.review_temp_image_path, image_resize)

            return True
        except Exception as e:
            errorBox(self.window, "错误", "更改大小预览失败")
            print("《预览更改大小》时错误：", e)
            return False

    # ==============================================================================================================
    # ===========================================    预处理工具运行    ===============================================
    # ==============================================================================================================

    # **********************************************    更改后缀    **************************************************
    def modifySuffix_jpg_run(self):
        print("正在运行：更改后缀jpg")
        new_image_path = toJpg(SI.image_path, False)
        if new_image_path != "":
            SI.image_path = new_image_path
            print("当前图片：", SI.image_path)
            infoBox(self.window, "成功", "后缀修改完成")
        else:
            errorBox(self.window, "错误", "后缀修改失败，请检查目标文件是否已存在")

    def modifySuffix_jpeg_run(self):
        print("正在运行：更改后缀jpeg")
        new_image_path = toJpeg(SI.image_path, False)
        if new_image_path != "":
            SI.image_path = new_image_path
            print("当前图片：", SI.image_path)
            infoBox(self.window, "成功", "后缀修改完成")
        else:
            errorBox(self.window, "错误", "后缀修改失败，请检查目标文件是否已存在")

    def modifySuffix_png_run(self):
        print("正在运行：更改后缀png")
        new_image_path = toPng(SI.image_path, False)
        if new_image_path != "":
            SI.image_path = new_image_path
            print("当前图片：", SI.image_path)
            infoBox(self.window, "成功", "后缀修改完成")
        else:
            errorBox(self.window, "错误", "后缀修改失败，请检查目标文件是否已存在")

    def modifySuffix_bmp_run(self):
        print("正在运行：更改后缀bmp")
        new_image_path = toBmp(SI.image_path, False)
        if new_image_path != "":
            SI.image_path = new_image_path
            print("当前图片：", SI.image_path)
            infoBox(self.window, "成功", "后缀修改完成")
        else:
            errorBox(self.window, "错误", "后缀修改失败，请检查目标文件是否已存在")


    # *********************************************    图片方形化    *************************************************
    def square_run(self, borderType, fillColor=None):
        if SI.export_path_ofImage == "":
            errorBox(self.window, "错误", "请先设置保存路径")
            return
        else:
            try:
                imageProcess = ImageProcess(SI.image_path)
                if borderType == "BORDER_CONSTANT":
                    print("正在运行：图片方形化BORDER_CONSTANT，RGB=", fillColor)
                    image_square = imageProcess.square(borderType, fillColor)
                    cv2.imwrite(SI.export_path_ofImage, image_square)
                else:
                    print("正在运行：图片方形化", borderType)
                    image_square = imageProcess.square(borderType)
                    cv2.imwrite(SI.export_path_ofImage, image_square)
                infoBox(self.window, "成功", "图片方形化完成")
            except Exception as e:
                errorBox(self.window, "错误", "图片方形化失败")
                print("《运行图片方形化》时错误:", e)

    # **********************************************    更改大小    **************************************************
    def resize_run(self, dsize, interpolation):
        if SI.export_path_ofImage == "":
            errorBox(self.window, "错误", "请先设置保存路径")
            return
        else:
            try:
                imageProcess = ImageProcess(SI.image_path)
                if interpolation == "INTER_LINEAR":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                elif interpolation == "INTER_NEAREST":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                elif interpolation == "INTER_CUBIC":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                elif interpolation == "INTER_AREA":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                elif interpolation == "INTER_LANCZOS4":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                elif interpolation == "INTER_LINEAR_EXACT":
                    print(f"正在运行：更改大小{interpolation}，dsize={dsize}")
                    image_resize = imageProcess.resize(dsize, interpolation)
                    cv2.imwrite(SI.export_path_ofImage, image_resize)
                infoBox(self.window, "成功", "更改大小完成")

            except Exception as e:
                errorBox(self.window, "错误", "更改大小失败")
                print("《运行更改大小》时错误:", e)



    # ==============================================================================================================
    # =============================================    图像增强    ==================================================
    # ==============================================================================================================


    # *********************************************    图像旋转    *************************************************
    def rotate_review_and_run(self, image, rotateDegree, rotateScale, fillColor):
        return ImageAugment(image).rotate(angle=rotateDegree, scale=rotateScale, fillColor=fillColor)
    # *********************************************    水平翻转    *************************************************
    def HFlip_review_and_run(self, image):
        return ImageAugment(image).flip(1)
    # *********************************************    垂直翻转    *************************************************
    def VFlip_review_and_run(self, image):
        return ImageAugment(image).flip(0)
    # ***********************************************    模糊    ***************************************************
    def blur_review_and_run(self, image, blur, ksize1, ksize2):
        if blur == "均值滤波":
            return ImageAugment(image).blur((ksize1, ksize2))
        elif blur == "方框滤波":
            return ImageAugment(image).boxBlur((ksize1, ksize2))
        elif blur == "高斯滤波":
            return ImageAugment(image).gaussianBlur((ksize1, ksize2))
        elif blur == "中值滤波":
            return ImageAugment(image).medianBlur(ksize1)
    def noise_review_and_run(self, image, noiseTypeCode, sigma=0, rate=0):
        if noiseTypeCode == 1:
            return ImageAugment(image).saltPepperNoise(rate)
        elif noiseTypeCode == 2:
            return ImageAugment(image).gaussianNoise(sigma)
        elif noiseTypeCode == 3:
            image1 = ImageAugment(image).gaussianNoise(sigma)
            image2 = ImageAugment(image1).saltPepperNoise(rate)
            return image2
    def brightness_review_and_run(self, image, beta):
        return ImageAugment(image).brightness(beta)
    def contrast_review_and_run(self, image, alpha):
        return ImageAugment(image).contrast(alpha)



