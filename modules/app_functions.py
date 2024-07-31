import os
import random
from datetime import datetime

import cv2
from PySide6.QtWidgets import QFileDialog

from lib.Share import SI
from main import *
from main import MainWindow
from modules import Settings
from modules.func_process_ofDataset import FuncProcessOfDataset
from modules.func_process_ofImage import FuncProcessOfImage
from modules.func_trainer import FuncTrainer
from util.DisableWidgets import enable_widgets
from util.MessageBox import *
from util.Util import *

# 功能总调度：
# 图像处理ofImage：预览（预处理工具预览+图像增强预览） + 运行（预处理工具运行+图像增强运行）
# 图像处理ofDataset：预览（预处理工具预览+图像增强预览） + 运行（预处理工具运行+图像增强运行）
# 可视化训练器
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """


    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    图像处理 ofImage    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓


    # ==============================================================================================================
    # =================================================    MENU    =================================================
    # ==============================================================================================================
    def importSingleImage(self):
        """
        添加单张图片
        """
        try:
            SI.image_path, _ = QFileDialog.getOpenFileName(
                self,           # 父窗口对象
                "选择添加的图片",  # 标题
                "",             # 起始目录
                "图片类型 (*.jpg *.jpeg *.png *.bmp)"  # 选择类型过滤项
            )
            if SI.image_path != "":
                if isChinesePath(SI.image_path):
                    SI.image_path = ""
                    warningBox(self, "警告", "含有中文路径")
                else:
                    infoBox(self, "成功", "导入完成")
                    print("图片路径：" + SI.image_path)
        except:
            errorBox(self, "错误", "添加图片失败")

    def exportSingleImage(self):
        """
        设置导出路径
        """
        # 弹出路径选择框：
        SI.export_path_ofImage, _ = QFileDialog.getSaveFileName(
            self,       # 父窗口对象
            "保存图片",  # 标题
            "",         # 起始目录
            "图片类型 (*.jpg *.jpeg *.png *.bmp)"  # 选择类型过滤项
        )
        # 判断路径：
        if SI.export_path_ofImage != "":
            if isChinesePath(SI.export_path_ofImage):
                SI.export_path_ofImage = ""
                warningBox(self, "警告", "含有中文路径")
            else:
                infoBox(self, "成功", "设置导出路径成功")
                print("保存路径：" + SI.export_path_ofImage)

    # ==============================================================================================================
    # =================================================    预览    ==================================================
    # ==============================================================================================================

    def processAlgorithm_review_ofImage(self):
        """
        预处理工具的预览功能选择
        """
        # 算法判空--------------------------
        # 更改后缀
        if SI.current_processTool_ofImage == "更改后缀":
            warningBox(self, "警告", "更改后缀算法不支持预览")
            return
        # 图片方形化
        if SI.current_processTool_ofImage == "图片方形化" and (
                "square_BORDER_CONSTANT" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_REFLECT" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_REPLICATE" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_WRAP" not in SI.processToolAlgorithm_ofImage):
            errorBox(self, "错误", "图片方形化未选择拓展填充方式")
            return
        # 更改大小
        if SI.current_processTool_ofImage == "更改大小" and (
                "resize_INTER_LINEAR" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_NEAREST" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_CUBIC" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_AREA" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_LANCZOS4" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_LINEAR_EXACT" not in SI.processToolAlgorithm_ofImage):
            errorBox(self, "错误", "更改大小未选择插值方式")
            return

        # 执行算法--------------------------
        process = FuncProcessOfImage(self, self.ui)  # 实例化
        # 图片方形化
        if SI.processToolAlgorithm_ofImage == "square_BORDER_CONSTANT":
            r = self.ui.spinBox_square_image_R.value()
            g = self.ui.spinBox_square_image_G.value()
            b = self.ui.spinBox_square_image_B.value()
            if process.square_review("BORDER_CONSTANT", [r, g, b]):     # 执行算法
                process.setReview()  # 预览
        elif SI.processToolAlgorithm_ofImage in ["square_BORDER_REFLECT", "square_BORDER_REPLICATE", "square_BORDER_WRAP"]:
            borderType = None
            if SI.processToolAlgorithm_ofImage == "square_BORDER_REFLECT": borderType="BORDER_REFLECT"
            elif SI.processToolAlgorithm_ofImage == "square_BORDER_REPLICATE": borderType="BORDER_REPLICATE"
            elif SI.processToolAlgorithm_ofImage == "square_BORDER_WRAP": borderType="BORDER_WRAP"

            if process.square_review(borderType):   # 执行算法
                process.setReview()          # 预览

        # 更改大小
        elif SI.current_processTool_ofImage == "更改大小":
            size1 = self.ui.lineEdit_resizepx1_ofImage.text()
            size2 = self.ui.lineEdit_resizepx2_ofImage.text()
            if size1 == "" or size2 == "":
                errorBox(self, "错误", "请先输入目标图像大小")
                return
            else:
                # interpolation
                interpolation = None
                if SI.processToolAlgorithm_ofImage == "resize_INTER_LINEAR":
                    interpolation = "INTER_LINEAR"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_NEAREST":
                    interpolation = "INTER_NEAREST"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_CUBIC":
                    interpolation = "INTER_CUBIC"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_AREA":
                    interpolation = "INTER_AREA"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_LANCZOS4":
                    interpolation = "INTER_LANCZOS4"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_LINEAR_EXACT":
                    interpolation = "INTER_LINEAR_EXACT"
                # dsize
                dsize1 = int(size1)
                dsize2 = int(size2)
                dsize = (dsize1, dsize2)
                if process.resize_review(dsize, interpolation):     # 执行算法
                    process.setReview()                             # 预览
        # ELSE
        else:
            errorBox(self, "错误", "未选择算法")


    def imageAugment_review_ofImage(self):
        """
        图像增强的预览功能选择
        """
        # 算法判空--------------------------
        # 模糊
        if ("模糊" in SI.current_imageAugment_ofImage) and (
                "blur_mean" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_box" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_gaussian" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_median" not in SI.imageAugmentAlgorithm_ofImage):
            errorBox(self, "错误", "模糊操作未选择滤波方式")
            return
        if "模糊" in SI.current_imageAugment_ofImage:
            blur = None
            if "blur_mean" in SI.imageAugmentAlgorithm_ofImage: blur = "均值滤波"
            elif "blur_box" in SI.imageAugmentAlgorithm_ofImage: blur = "方框滤波"
            elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage: blur = "高斯滤波"
            elif "blur_median" in SI.imageAugmentAlgorithm_ofImage: blur = "中值滤波"
            ksize1 = self.ui.spinBox_blurKsize1_ofImage.value()
            ksize2 = self.ui.spinBox_blurKsize2_ofImage.value()
            # 判断滤波核范围
            if blur == "高斯滤波":
                if (ksize1 % 2 == 0) or (ksize2 % 2 == 0):
                    errorBox(self, "错误", "高斯滤波的滤波核必须为奇数")
                    return
            elif blur == "中值滤波":
                if (ksize1 % 2 == 0) or (ksize2 % 2 == 0) or (ksize1 == 1) or (ksize2 == 1):
                    errorBox(self, "错误", "中值滤波的滤波核必须为大于1的奇数")
                    return
        # 噪声
        if ("噪声" in SI.current_imageAugment_ofImage) and (
                "noise_gaussian" not in SI.imageAugmentAlgorithm_ofImage
                and "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofImage):
            errorBox(self, "错误", "噪声操作未选择处理方式")
            return
        # 判空
        if not SI.imageAugmentAlgorithm_ofImage:
            errorBox(self, "错误", "未选择算法")
            return

        # 依次执行算法--------------------------
        try:
            process = FuncProcessOfImage(self, self.ui)      # 实例化
            image = cv2.imread(SI.image_path)   # 读取图片

            # 执行算法
            for imageAugment in SI.current_imageAugment_ofImage:
                # 图像旋转--------------------
                if imageAugment == "图像旋转":
                    # 获取参数
                    rotateDegree = self.ui.dSpinBox_rotateDegree_ofImage.value()
                    rotateScale = self.ui.dSpinBox_rotateScale_ofImage.value()
                    R = self.ui.spinBox_rotate_ofImage_R.value()
                    G = self.ui.spinBox_rotate_ofImage_G.value()
                    B = self.ui.spinBox_rotate_ofImage_B.value()
                    # 执行算法
                    image = process.rotate_review_and_run(image, rotateDegree, rotateScale, (R, G, B))
                # 水平翻转--------------------
                elif imageAugment == "水平翻转":
                    image = process.HFlip_review_and_run(image)
                # 垂直翻转--------------------
                elif imageAugment == "垂直翻转":
                    image = process.VFlip_review_and_run(image)
                # 模糊--------------------
                elif imageAugment == "模糊":
                    # 获取参数
                    ksize1 = self.ui.spinBox_blurKsize1_ofImage.value()
                    ksize2 = self.ui.spinBox_blurKsize2_ofImage.value()
                    blur = None
                    if "blur_mean" in SI.imageAugmentAlgorithm_ofImage: blur = "均值滤波"
                    elif "blur_box" in SI.imageAugmentAlgorithm_ofImage: blur = "方框滤波"
                    elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage: blur = "高斯滤波"
                    elif "blur_median" in SI.imageAugmentAlgorithm_ofImage: blur = "中值滤波"
                    # 执行算法
                    image = process.blur_review_and_run(image, blur, ksize1, ksize2)
                # 噪声--------------------
                elif imageAugment == "噪声":
                    if ("noise_gaussian" not in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage):        # 01=1
                        # 获取参数
                        rate = self.ui.dSpinBox_noise_rate_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 1, rate=rate)
                    elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofImage):    # 10=2
                        # 获取参数
                        sigma = self.ui.dSpinBox_noise_sigma_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 2, sigma=sigma)
                    elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage):        # 11=3
                        # 获取参数
                        sigma = self.ui.dSpinBox_noise_sigma_ofImage.value()
                        rate = self.ui.dSpinBox_noise_rate_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 3, sigma=sigma, rate=rate)
                # 亮度--------------------
                elif imageAugment == "亮度":
                    # 获取参数
                    beta = self.ui.dSpinBox_brightness_ofImage.value()
                    # 执行算法
                    image = process.brightness_review_and_run(image, beta)
                # 对比度--------------------
                elif imageAugment == "对比度":
                    # 获取参数
                    alpha = self.ui.dSpinBox_contrast_ofImage.value()
                    # 执行算法
                    image = process.contrast_review_and_run(image, alpha)

            # 创建预览图象路径
            SI.review_temp_image_path = mkTempReviewImage(SI.image_path)
            # 保存预览图片
            cv2.imwrite(SI.review_temp_image_path, image)
            # 预览展示
            process.setReview()
        except Exception as e:
            errorBox(self, "错误", "该图片无法预览")
            print("《图像增强功能预览》时失败：", e)
        finally:
            del process
            del image





    # ==============================================================================================================
    # ==================================================    运行    =================================================
    # ==============================================================================================================

    def processAlgorithm_run_ofImage(self):
        """
        预处理工具的运行功能选择
        """
        # 算法判空--------------------------
        # 更改后缀
        if SI.current_processTool_ofImage == "更改后缀" and (
                "modifySuffix_jpg" not in SI.processToolAlgorithm_ofImage
                 and "modifySuffix_jpeg" not in SI.processToolAlgorithm_ofImage
                 and "modifySuffix_png" not in SI.processToolAlgorithm_ofImage
                 and "modifySuffix_bmp" not in SI.processToolAlgorithm_ofImage):
            errorBox(self, "错误", "未选择后缀形式")
            return
        # 图片方形化
        if SI.current_processTool_ofImage == "图片方形化" and (
                "square_BORDER_CONSTANT" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_REFLECT" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_REPLICATE" not in SI.processToolAlgorithm_ofImage
                and "square_BORDER_WRAP" not in SI.processToolAlgorithm_ofImage):
            errorBox(self, "错误", "图片方形化未选择拓展填充方式")
            return
        # 更改大小
        if SI.current_processTool_ofImage == "更改大小" and (
                "resize_INTER_LINEAR" not in SI.processToolAlgorithm_ofImage
                 and "resize_INTER_NEAREST" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_CUBIC" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_AREA" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_LANCZOS4" not in SI.processToolAlgorithm_ofImage
                and "resize_INTER_LINEAR_EXACT" not in SI.processToolAlgorithm_ofImage):
            errorBox(self, "错误", "更改大小未选择插值方式")
            return

        # 执行算法--------------------------
        process = FuncProcessOfImage(self, self.ui)
        # 更改后缀
        if SI.processToolAlgorithm_ofImage == "modifySuffix_jpg":
            process.modifySuffix_jpg_run()
        elif SI.processToolAlgorithm_ofImage == "modifySuffix_jpeg":
            process.modifySuffix_jpeg_run()
        elif SI.processToolAlgorithm_ofImage == "modifySuffix_png":
            process.modifySuffix_png_run()
        elif SI.processToolAlgorithm_ofImage == "modifySuffix_bmp":
            process.modifySuffix_bmp_run()

        # 图片方形化
        elif SI.processToolAlgorithm_ofImage == "square_BORDER_CONSTANT":
            r = self.ui.spinBox_square_image_R.value()
            g = self.ui.spinBox_square_image_G.value()
            b = self.ui.spinBox_square_image_B.value()
            process.square_run("BORDER_CONSTANT", [r, g, b])
        elif SI.processToolAlgorithm_ofImage == "square_BORDER_REFLECT":
            process.square_run("BORDER_REFLECT")
        elif SI.processToolAlgorithm_ofImage == "square_BORDER_REPLICATE":
            process.square_run("BORDER_REPLICATE")
        elif SI.processToolAlgorithm_ofImage == "square_BORDER_WRAP":
            process.square_run("BORDER_WRAP")

        # 更改大小
        elif SI.current_processTool_ofImage == "更改大小":
            size1 = self.ui.lineEdit_resizepx1_ofImage.text()
            size2 = self.ui.lineEdit_resizepx2_ofImage.text()
            if size1 == "" or size2 == "":
                errorBox(self, "错误", "请先输入目标图像大小")
                return
            else:
                # interpolation
                interpolation = None
                if SI.processToolAlgorithm_ofImage == "resize_INTER_LINEAR":
                    interpolation = "INTER_LINEAR"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_NEAREST":
                    interpolation = "INTER_NEAREST"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_CUBIC":
                    interpolation = "INTER_CUBIC"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_AREA":
                    interpolation = "INTER_AREA"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_LANCZOS4":
                    interpolation = "INTER_LANCZOS4"
                elif SI.processToolAlgorithm_ofImage == "resize_INTER_LINEAR_EXACT":
                    interpolation = "INTER_LINEAR_EXACT"
                # dsize
                dsize1 = int(size1)
                dsize2 = int(size2)
                dsize = (dsize1, dsize2)
                # 执行算法
                process.resize_run(dsize, interpolation)

        # ELSE
        else:
            errorBox(self, "错误", "未选择算法")

    def imageAugment_run_ofImage(self):
        """
        图像增强的运行功能选择
        """
        # 判空--------------------------
        # 路径判空
        if SI.export_path_ofImage == "":
            errorBox(self, "错误", "请先设置保存路径")
            return
        # 模糊
        if ("模糊" in SI.current_imageAugment_ofImage) and (
                "blur_mean" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_box" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_gaussian" not in SI.imageAugmentAlgorithm_ofImage
                 and "blur_median" not in SI.imageAugmentAlgorithm_ofImage):
            errorBox(self, "错误", "模糊操作未选择滤波方式")
            return
        if "模糊" in SI.current_imageAugment_ofImage:
            blur = None
            if "blur_mean" in SI.imageAugmentAlgorithm_ofImage: blur = "均值滤波"
            elif "blur_box" in SI.imageAugmentAlgorithm_ofImage: blur = "方框滤波"
            elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage: blur = "高斯滤波"
            elif "blur_median" in SI.imageAugmentAlgorithm_ofImage: blur = "中值滤波"
            ksize1 = self.ui.spinBox_blurKsize1_ofImage.value()
            ksize2 = self.ui.spinBox_blurKsize2_ofImage.value()
            # 判断滤波核范围
            if blur == "高斯滤波":
                if (ksize1 % 2 == 0) or (ksize2 % 2 == 0):
                    errorBox(self, "错误", "高斯滤波的滤波核必须为奇数")
                    return
            elif blur == "中值滤波":
                if (ksize1 % 2 == 0) or (ksize2 % 2 == 0) or (ksize1 == 1) or (ksize2 == 1):
                    errorBox(self, "错误", "中值滤波的滤波核必须为大于1的奇数")
                    return
        # 噪声
        if ("噪声" in SI.current_imageAugment_ofImage) and (
                "noise_gaussian" not in SI.imageAugmentAlgorithm_ofImage
                and "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofImage):
            errorBox(self, "错误", "噪声操作未选择处理方式")
            return
        # 算法判空
        if not SI.imageAugmentAlgorithm_ofImage:
            errorBox(self, "错误", "未选择算法")
            return

        # 执行算法--------------------------
        try:
            process = FuncProcessOfImage(self, self.ui)      # 实例化
            image = cv2.imread(SI.image_path)   # 读取图片

            # 执行算法
            for imageAugment in SI.current_imageAugment_ofImage:
                # 图像旋转--------------------
                if imageAugment == "图像旋转":
                    # 获取参数
                    rotateDegree = self.ui.dSpinBox_rotateDegree_ofImage.value()
                    rotateScale = self.ui.dSpinBox_rotateScale_ofImage.value()
                    R = self.ui.spinBox_rotate_ofImage_R.value()
                    G = self.ui.spinBox_rotate_ofImage_G.value()
                    B = self.ui.spinBox_rotate_ofImage_B.value()
                    # 执行算法
                    image = process.rotate_review_and_run(image, rotateDegree, rotateScale, (R, G, B))
                # 水平翻转--------------------
                elif imageAugment == "水平翻转":
                    image = process.HFlip_review_and_run(image)
                # 垂直翻转--------------------
                elif imageAugment == "垂直翻转":
                    image = process.VFlip_review_and_run(image)
                # 模糊--------------------
                elif imageAugment == "模糊":
                    # 获取参数
                    ksize1 = self.ui.spinBox_blurKsize1_ofImage.value()
                    ksize2 = self.ui.spinBox_blurKsize2_ofImage.value()
                    blur = None
                    if "blur_mean" in SI.imageAugmentAlgorithm_ofImage: blur = "均值滤波"
                    elif "blur_box" in SI.imageAugmentAlgorithm_ofImage: blur = "方框滤波"
                    elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage: blur = "高斯滤波"
                    elif "blur_median" in SI.imageAugmentAlgorithm_ofImage: blur = "中值滤波"
                    # 执行算法
                    image = process.blur_review_and_run(image, blur, ksize1, ksize2)
                # 噪声--------------------
                elif imageAugment == "噪声":
                    if ("noise_gaussian" not in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage):        # 01=1
                        # 获取参数
                        rate = self.ui.dSpinBox_noise_rate_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 1, rate=rate)
                    elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofImage):    # 10=2
                        # 获取参数
                        sigma = self.ui.dSpinBox_noise_sigma_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 2, sigma=sigma)
                    elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofImage) and (
                            "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage):        # 11=3
                        # 获取参数
                        sigma = self.ui.dSpinBox_noise_sigma_ofImage.value()
                        rate = self.ui.dSpinBox_noise_rate_ofImage.value()
                        # 执行算法
                        image = process.noise_review_and_run(image, 3, sigma=sigma, rate=rate)
                # 亮度--------------------
                elif imageAugment == "亮度":
                    # 获取参数
                    beta = self.ui.dSpinBox_brightness_ofImage.value()
                    # 执行算法
                    image = process.brightness_review_and_run(image, beta)
                # 对比度--------------------
                elif imageAugment == "对比度":
                    # 获取参数
                    alpha = self.ui.dSpinBox_contrast_ofImage.value()
                    # 执行算法
                    image = process.contrast_review_and_run(image, alpha)

            # 保存图片
            cv2.imwrite(SI.export_path_ofImage, image)
            del image
            infoBox(self, "成功", "处理完成")
        except Exception as e:
            errorBox(self, "错误", "该图片处理失败")
            print("《图像增强功能运行》时失败：", e)










    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    图像处理 ofDataset    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓


    # ==============================================================================================================
    # =================================================    MENU    =================================================
    # ==============================================================================================================
    def importDataset(self):
        """
        导入数据集
        """
        try:
            SI.dataset_path = QFileDialog.getExistingDirectory(self, "选择数据集文件夹")
            if SI.dataset_path != "":
                if isChinesePath(SI.dataset_path):
                    SI.dataset_path = ""
                    warningBox(self, "警告", "含有中文路径")
                else:
                    SI.dataset_images_path = getDatasetImage(SI.dataset_path)
                    infoBox(self, "成功", "导入完成")
                    print("数据集路径：" + SI.dataset_path)
        except:
            errorBox(self, "错误", "导入数据集失败，请检查数据集格式")


    def exportResult(self):
        """
        设置导出路径
        """
        # 弹出路径选择框：
        SI.export_path_ofDataset = QFileDialog.getExistingDirectory(self, "选择导出目录")
        # 判断路径：
        if SI.export_path_ofDataset != "":
            if isChinesePath(SI.export_path_ofDataset):
                SI.export_path_ofDataset = ""
                warningBox(self, "警告", "含有中文路径")
            else:
                infoBox(self, "成功", "设置导出路径成功")
                print("保存路径：" + SI.export_path_ofDataset)




    # ==============================================================================================================
    # ==============================================    预览    ====================================================
    # ==============================================================================================================

    def processAlgorithm_review_ofDataset(self):
        """
        预处理工具的预览功能选择
        """
        # 算法判空--------------------------
        # 统一后缀
        if SI.current_processTool_ofDataset == "统一后缀":
            warningBox(self, "警告", "统一后缀算法不支持预览")
            return
        # 统一命名
        if SI.current_processTool_ofDataset == "统一命名":
            warningBox(self, "警告", "统一命名算法不支持预览")
            return
        # 数据集分割
        if SI.current_processTool_ofDataset == "数据集分割":
            warningBox(self, "警告", "数据集分割算法不支持预览")
            return

        # 图片方形化
        if SI.current_processTool_ofDataset == "图片方形化" and (
                "square_BORDER_CONSTANT" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_REFLECT" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_REPLICATE" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_WRAP" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "图片方形化未选择拓展填充方式")
            return
        # 统一大小
        if SI.current_processTool_ofDataset == "统一大小" and (
                "resize_INTER_LINEAR" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_NEAREST" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_CUBIC" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_AREA" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_LANCZOS4" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_LINEAR_EXACT" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "统一大小未选择插值方式")
            return


        # 执行算法--------------------------
        image = random.choice(SI.dataset_images_path)                   # 获取图片
        process = FuncProcessOfDataset(self, self.ui, image)            # 实例化
        # 图片方形化
        if SI.processToolAlgorithm_ofDataset == "square_BORDER_CONSTANT":
            r = self.ui.spinBox_square_ofDataset_R.value()
            g = self.ui.spinBox_square_ofDataset_G.value()
            b = self.ui.spinBox_square_ofDataset_B.value()
            if process.square_review("BORDER_CONSTANT", [r, g, b]):  # 执行算法
                process.setReview()  # 预览
        elif SI.processToolAlgorithm_ofDataset in ["square_BORDER_REFLECT", "square_BORDER_REPLICATE",
                                                 "square_BORDER_WRAP"]:
            borderType = None
            if SI.processToolAlgorithm_ofDataset == "square_BORDER_REFLECT":
                borderType = "BORDER_REFLECT"
            elif SI.processToolAlgorithm_ofDataset == "square_BORDER_REPLICATE":
                borderType = "BORDER_REPLICATE"
            elif SI.processToolAlgorithm_ofDataset == "square_BORDER_WRAP":
                borderType = "BORDER_WRAP"

            if process.square_review(borderType):  # 执行算法
                process.setReview()  # 预览
        # 统一大小
        elif SI.current_processTool_ofDataset == "统一大小":
            size1 = self.ui.lineEdit_resizepx1_ofDataset.text()
            size2 = self.ui.lineEdit_resizepx2_ofDataset.text()
            if size1 == "" or size2 == "":
                errorBox(self, "错误", "请先输入目标图像大小")
                return
            else:
                # interpolation
                interpolation = None
                if SI.processToolAlgorithm_ofDataset == "resize_INTER_LINEAR":
                    interpolation = "INTER_LINEAR"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_NEAREST":
                    interpolation = "INTER_NEAREST"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_CUBIC":
                    interpolation = "INTER_CUBIC"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_AREA":
                    interpolation = "INTER_AREA"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_LANCZOS4":
                    interpolation = "INTER_LANCZOS4"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_LINEAR_EXACT":
                    interpolation = "INTER_LINEAR_EXACT"
                # dsize
                dsize1 = int(size1)
                dsize2 = int(size2)
                dsize = (dsize1, dsize2)
                if process.resize_review(dsize, interpolation):     # 执行算法
                    process.setReview()                             # 预览
        # ELSE
        else:
            errorBox(self, "错误", "未选择算法")

    def imageAugment_review_ofDataset(self):
        """
        图像增强的预览功能选择
        """
        # 算法判空--------------------------
        # 模糊
        if ("模糊" in SI.current_imageAugment_ofDataset) and (
                "blur_mean" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_box" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_gaussian" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_median" not in SI.imageAugmentAlgorithm_ofDataset):
            errorBox(self, "错误", "模糊操作未选择滤波方式")
            return
        if "模糊" in SI.current_imageAugment_ofDataset:
            blur = None
            if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset: blur = "均值滤波"
            elif "blur_box" in SI.imageAugmentAlgorithm_ofDataset: blur = "方框滤波"
            elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset: blur = "高斯滤波"
            elif "blur_median" in SI.imageAugmentAlgorithm_ofDataset: blur = "中值滤波"
            ksize_from = self.ui.spinBox_blurKsize_from1_ofDataset.value()
            ksize_to = self.ui.spinBox_blurKsize_to1_ofDataset.value()
            # 判断滤波核范围
            if blur == "高斯滤波":
                if (ksize_from == ksize_to) and (ksize_from % 2 == 0):
                    errorBox(self, "错误", "高斯滤波的滤波核必须为奇数")
                    return
            if blur == "中值滤波":
                if ((ksize_from == ksize_to) and (ksize_from % 2 == 0)) or (ksize_from == 1) or (ksize_to == 1):
                    errorBox(self, "错误", "中值滤波的滤波核必须为大于1的奇数")
                    return
        # 噪声
        if ("噪声" in SI.current_imageAugment_ofDataset) and (
                "noise_gaussian" not in SI.imageAugmentAlgorithm_ofDataset
                and "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofDataset):
            errorBox(self, "错误", "噪声操作未选择处理方式")
            return
        # 判空
        if not SI.imageAugmentAlgorithm_ofDataset:
            errorBox(self, "错误", "未选择算法")
            return

        # 依次执行算法--------------------------
        image_path = random.choice(SI.dataset_images_path)                       # 获取图片路径
        try:
            image_read = cv2.imread(image_path)                                  # 读取图片
            process = FuncProcessOfDataset(self, self.ui, image_path)            # 实例化
            # 执行算法
            for imageAugment in SI.current_imageAugment_ofDataset:
                # 图像旋转--------------------
                if imageAugment == "图像旋转":
                    probability = self.ui.dSpinBox_rotate_probability_ofDataset.value()
                    if random.uniform(0, 1) <= probability:
                        # 获取参数
                        rotateDegree1 = self.ui.dSpinBox_rotateDegree1_ofDataset.value()
                        rotateDegree2 = self.ui.dSpinBox_rotateDegree2_ofDataset.value()
                        rotateDegree = random.uniform(rotateDegree1, rotateDegree2)
                        rotateScale1 = self.ui.dSpinBox_rotateScale1_ofDataset.value()
                        rotateScale2 = self.ui.dSpinBox_rotateScale2_ofDataset.value()
                        rotateScale = random.uniform(rotateScale1, rotateScale2)
                        R = self.ui.spinBox_rotate_ofDataset_R.value()
                        G = self.ui.spinBox_rotate_ofDataset_G.value()
                        B = self.ui.spinBox_rotate_ofDataset_B.value()
                        # 执行算法
                        image_read = process.rotate_review(image_read, rotateDegree, rotateScale, (R, G, B))
                # 水平翻转--------------------
                elif imageAugment == "水平翻转":
                    # 获取参数
                    probability = self.ui.dSpinBox_HFlip_probability_ofDataset.value()
                    # 执行算法
                    if random.uniform(0, 1) <= probability:
                        image_read = process.HFlip_review(image_read)
                # 垂直翻转--------------------
                elif imageAugment == "垂直翻转":
                    # 获取参数
                    probability = self.ui.dSpinBox_VFlip_probability_ofDataset.value()
                    # 执行算法
                    if random.uniform(0, 1) <= probability:
                        image_read = process.VFlip_review(image_read)
                # 模糊--------------------
                elif imageAugment == "模糊":
                    probability = self.ui.dSpinBox_blur_probability_ofDataset.value()
                    if random.uniform(0, 1) <= probability:
                        # 获取参数
                        ksize_from = self.ui.spinBox_blurKsize_from1_ofDataset.value()
                        ksize_to = self.ui.spinBox_blurKsize_to1_ofDataset.value()
                        blur = None
                        if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset: blur = "均值滤波"
                        elif "blur_box" in SI.imageAugmentAlgorithm_ofDataset: blur = "方框滤波"
                        elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset: blur = "高斯滤波"
                        elif "blur_median" in SI.imageAugmentAlgorithm_ofDataset: blur = "中值滤波"
                        # 随机选取ksize
                        ksize = random.randint(ksize_from, ksize_to)
                        if (blur == "高斯滤波") or (blur == "中值滤波"):
                            while ksize % 2 == 0:   # 确保为奇数
                                ksize = random.randint(ksize_from, ksize_to)
                        # 执行算法
                        image_read = process.blur_review(image_read, blur, ksize, ksize)
                # 噪声--------------------
                elif imageAugment == "噪声":
                    probability = self.ui.dSpinBox_noise_probability_ofDataset.value()
                    if random.uniform(0, 1) <= probability:
                        if ("noise_gaussian" not in SI.imageAugmentAlgorithm_ofDataset) and (
                                "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset):        # 01=1
                            # 获取参数
                            rate1 = self.ui.dSpinBox_noise_rate1_ofDataset.value()
                            rate2 = self.ui.dSpinBox_noise_rate2_ofDataset.value()
                            rate = random.uniform(rate1, rate2)
                            # 执行算法
                            image_read = process.noise_review(image_read, 1, rate=rate)
                        elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset) and (
                                "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofDataset):    # 10=2
                            # 获取参数
                            sigma1 = self.ui.dSpinBox_noise_sigma1_ofDataset.value()
                            sigma2 = self.ui.dSpinBox_noise_sigma2_ofDataset.value()
                            sigma = random.uniform(sigma1, sigma2)
                            # 执行算法
                            image_read = process.noise_review(image_read, 2, sigma=sigma)
                        elif ("noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset) and (
                                "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset):        # 11=3
                            # 获取参数
                            sigma1 = self.ui.dSpinBox_noise_sigma1_ofDataset.value()
                            sigma2 = self.ui.dSpinBox_noise_sigma2_ofDataset.value()
                            sigma = random.uniform(sigma1, sigma2)
                            rate1 = self.ui.dSpinBox_noise_rate1_ofDataset.value()
                            rate2 = self.ui.dSpinBox_noise_rate2_ofDataset.value()
                            rate = random.uniform(rate1, rate2)
                            # 执行算法
                            image_read = process.noise_review(image_read, 3, sigma=sigma, rate=rate)
                # 亮度--------------------
                elif imageAugment == "亮度":
                    # 获取参数
                    probability = self.ui.dSpinBox_brightness_probability_ofDataset.value()
                    beta1 = self.ui.dSpinBox_brightness_beta1_ofDataset.value()
                    beta2 = self.ui.dSpinBox_brightness_beta2_ofDataset.value()
                    beta = random.uniform(beta1, beta2)
                    # 执行算法
                    if random.uniform(0, 1) <= probability:
                        image_read = process.brightness_review(image_read, beta)
                # 对比度--------------------
                elif imageAugment == "对比度":
                    # 获取参数
                    probability = self.ui.dSpinBox_contrast_probability_ofDataset.value()
                    alpha1 = self.ui.dSpinBox_contrast_alpha1_ofDataset.value()
                    alpha2 = self.ui.dSpinBox_contrast_alpha2_ofDataset.value()
                    alpha = random.uniform(alpha1, alpha2)
                    # 执行算法
                    if random.uniform(0, 1) <= probability:
                        image_read = process.contrast_review(image_read, alpha)

            # 创建预览图象路径
            SI.review_temp_image_path = mkTempReviewImage(image_path)
            # 保存预览图片
            cv2.imwrite(SI.review_temp_image_path, image_read)
            # 预览展示
            process.setReview()

        except Exception as e:
            errorBox(self, "错误", f"图片预览失败：\n{image_path}")
            print("《图像增强功能预览》时失败：", e)
        finally:
            del process
            del image_read
            del image_path



    # ==============================================================================================================
    # ==============================================    运行    ====================================================
    # ==============================================================================================================

    def processAlgorithm_run_ofDataset(self):
        """
        预处理工具的运行功能选择
        """
        # 算法判空--------------------------
        # 统一后缀
        if SI.current_processTool_ofDataset == "统一后缀" and (
                "modifySuffix_jpg" not in SI.processToolAlgorithm_ofDataset
                 and "modifySuffix_jpeg" not in SI.processToolAlgorithm_ofDataset
                 and "modifySuffix_png" not in SI.processToolAlgorithm_ofDataset
                 and "modifySuffix_bmp" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "未选择后缀形式")
            return
        if SI.current_processTool_ofDataset == "统一命名" and (
                "uniformName_i" not in SI.processToolAlgorithm_ofDataset
                and "uniformNamei" not in SI.processToolAlgorithm_ofDataset
                and "uniformName-i" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "未选择命名格式")
            return
        # 图片方形化
        if SI.current_processTool_ofDataset == "图片方形化" and (
                "square_BORDER_CONSTANT" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_REFLECT" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_REPLICATE" not in SI.processToolAlgorithm_ofDataset
                and "square_BORDER_WRAP" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "图片方形化未选择拓展填充方式")
            return
        # 统一大小
        if SI.current_processTool_ofDataset == "统一大小" and (
                "resize_INTER_LINEAR" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_NEAREST" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_CUBIC" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_AREA" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_LANCZOS4" not in SI.processToolAlgorithm_ofDataset
                and "resize_INTER_LINEAR_EXACT" not in SI.processToolAlgorithm_ofDataset):
            errorBox(self, "错误", "统一大小未选择插值方式")
            return


        # 执行算法--------------------------
        process = FuncProcessOfDataset(self, self.ui)
        # 统一后缀
        if SI.processToolAlgorithm_ofDataset == "modifySuffix_jpg":
            process.modifySuffix_jpg_run()
        elif SI.processToolAlgorithm_ofDataset == "modifySuffix_jpeg":
            process.modifySuffix_jpeg_run()
        elif SI.processToolAlgorithm_ofDataset == "modifySuffix_png":
            process.modifySuffix_png_run()
        elif SI.processToolAlgorithm_ofDataset == "modifySuffix_bmp":
            process.modifySuffix_bmp_run()
        # 统一命名
        elif SI.processToolAlgorithm_ofDataset == "uniformName_i":
            process.uniformName1_run()
        elif SI.processToolAlgorithm_ofDataset == "uniformNamei":
            process.uniformName2_run()
        elif SI.processToolAlgorithm_ofDataset == "uniformName-i":
            process.uniformName3_run()
        # 图片方形化
        elif SI.processToolAlgorithm_ofDataset == "square_BORDER_CONSTANT":
            r = self.ui.spinBox_square_ofDataset_R.value()
            g = self.ui.spinBox_square_ofDataset_G.value()
            b = self.ui.spinBox_square_ofDataset_B.value()
            SI.param_square_ofDataset_borderType = "BORDER_CONSTANT"
            SI.param_square_ofDataset_fillColor = [r, g, b]
            process.square_run()
        elif SI.processToolAlgorithm_ofDataset == "square_BORDER_REFLECT":
            SI.param_square_ofDataset_borderType = "BORDER_REFLECT"
            SI.param_square_ofDataset_fillColor = None
            process.square_run()
        elif SI.processToolAlgorithm_ofDataset == "square_BORDER_REPLICATE":
            SI.param_square_ofDataset_borderType = "BORDER_REPLICATE"
            SI.param_square_ofDataset_fillColor = None
            process.square_run()
        elif SI.processToolAlgorithm_ofDataset == "square_BORDER_WRAP":
            SI.param_square_ofDataset_borderType = "BORDER_WRAP"
            SI.param_square_ofDataset_fillColor = None
            process.square_run()
        # 统一大小
        elif SI.current_processTool_ofDataset == "统一大小":
            size1 = self.ui.lineEdit_resizepx1_ofDataset.text()
            size2 = self.ui.lineEdit_resizepx2_ofDataset.text()
            if size1 == "" or size2 == "":
                errorBox(self, "错误", "请先输入目标图像大小")
                return
            else:
                # interpolation
                if SI.processToolAlgorithm_ofDataset == "resize_INTER_LINEAR":
                    SI.param_resize_ofDataset_interpolation = "INTER_LINEAR"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_NEAREST":
                    SI.param_resize_ofDataset_interpolation = "INTER_NEAREST"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_CUBIC":
                    SI.param_resize_ofDataset_interpolation = "INTER_CUBIC"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_AREA":
                    SI.param_resize_ofDataset_interpolation = "INTER_AREA"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_LANCZOS4":
                    SI.param_resize_ofDataset_interpolation = "INTER_LANCZOS4"
                elif SI.processToolAlgorithm_ofDataset == "resize_INTER_LINEAR_EXACT":
                    SI.param_resize_ofDataset_interpolation = "INTER_LINEAR_EXACT"
                # dsize
                dsize1 = int(size1)
                dsize2 = int(size2)
                SI.param_resize_ofDataset_dsize = (dsize1, dsize2)
                # 执行算法
                process.resize_run()
        # 数据集分割
        elif SI.current_processTool_ofDataset == "数据集分割":
            train = self.ui.dSpinBox_split_train_ofDataset.value()
            val = self.ui.dSpinBox_split_val_ofDataset.value()
            test = self.ui.dSpinBox_split_test_ofDataset.value()
            if train + val + test != 1:
                errorBox(self, "错误", "请确保比例之和为1")
                return
            SI.param_split_ofDataset_train = train
            SI.param_split_ofDataset_val = val
            SI.param_split_ofDataset_test = test
            process.split_run()

        # ELSE
        else:
            errorBox(self, "错误", "未选择算法")



    def imageAugment_run_ofDataset(self):
        """
        图像增强的运行功能选择
        """
        # 判空--------------------------
        # 路径判空
        if SI.export_path_ofDataset == "":
            errorBox(self, "错误", "请先设置导出路径")
            return
        # 模糊
        if ("模糊" in SI.current_imageAugment_ofDataset) and (
                "blur_mean" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_box" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_gaussian" not in SI.imageAugmentAlgorithm_ofDataset
                and "blur_median" not in SI.imageAugmentAlgorithm_ofDataset):
            errorBox(self, "错误", "模糊操作未选择滤波方式")
            return
        if "模糊" in SI.current_imageAugment_ofDataset:
            blur = None
            if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset: blur = "均值滤波"
            elif "blur_box" in SI.imageAugmentAlgorithm_ofDataset: blur = "方框滤波"
            elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset: blur = "高斯滤波"
            elif "blur_median" in SI.imageAugmentAlgorithm_ofDataset: blur = "中值滤波"
            ksize_from = self.ui.spinBox_blurKsize_from1_ofDataset.value()
            ksize_to = self.ui.spinBox_blurKsize_to1_ofDataset.value()
            # 判断滤波核范围
            if blur == "高斯滤波":
                if (ksize_from == ksize_to) and (ksize_from % 2 == 0):
                    errorBox(self, "错误", "高斯滤波的滤波核必须为奇数")
                    return
            if blur == "中值滤波":
                if ((ksize_from == ksize_to) and (ksize_from % 2 == 0)) or (ksize_from == 1) or (ksize_to == 1):
                    errorBox(self, "错误", "中值滤波的滤波核必须为大于1的奇数")
                    return
        # 噪声
        if ("噪声" in SI.current_imageAugment_ofDataset) and (
                "noise_gaussian" not in SI.imageAugmentAlgorithm_ofDataset
                and "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofDataset):
            errorBox(self, "错误", "噪声操作未选择处理方式")
            return
        # 算法判空
        if not SI.imageAugmentAlgorithm_ofDataset:
            errorBox(self, "错误", "未选择算法")
            return

        # 记录参数--------------------------
        for imageAugment in SI.current_imageAugment_ofDataset:
            # 图像旋转----------
            if imageAugment == "图像旋转":
                # 概率
                probability = self.ui.dSpinBox_rotate_probability_ofDataset.value()
                SI.param_rotate_ofDataset_probability = probability
                # 旋转范围
                rotateDegree1 = self.ui.dSpinBox_rotateDegree1_ofDataset.value()
                rotateDegree2 = self.ui.dSpinBox_rotateDegree2_ofDataset.value()
                SI.param_rotate_ofDataset_degree1 = rotateDegree1
                SI.param_rotate_ofDataset_degree2 = rotateDegree2
                # 缩放范围
                rotateScale1 = self.ui.dSpinBox_rotateScale1_ofDataset.value()
                rotateScale2 = self.ui.dSpinBox_rotateScale2_ofDataset.value()
                SI.param_rotate_ofDataset_scale1 = rotateScale1
                SI.param_rotate_ofDataset_scale2 = rotateScale2
                # RGB
                R = self.ui.spinBox_rotate_ofDataset_R.value()
                G = self.ui.spinBox_rotate_ofDataset_G.value()
                B = self.ui.spinBox_rotate_ofDataset_B.value()
                SI.param_rotate_ofDataset_fillColor = (R, G, B)
            # 水平翻转----------
            elif imageAugment == "水平翻转":
                # 概率
                probability = self.ui.dSpinBox_HFlip_probability_ofDataset.value()
                SI.param_HFlip_ofDataset_probability = probability
            # 垂直翻转----------
            elif imageAugment == "垂直翻转":
                # 概率
                probability = self.ui.dSpinBox_VFlip_probability_ofDataset.value()
                SI.param_VFlip_ofDataset_probability = probability
            # 模糊----------
            elif imageAugment == "模糊":
                # 概率
                probability = self.ui.dSpinBox_blur_probability_ofDataset.value()
                SI.param_blur_ofDataset_probability = probability
                # 滤波方式
                blur = None
                if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset: blur = "均值滤波"
                elif "blur_box" in SI.imageAugmentAlgorithm_ofDataset: blur = "方框滤波"
                elif "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset: blur = "高斯滤波"
                elif "blur_median" in SI.imageAugmentAlgorithm_ofDataset: blur = "中值滤波"
                SI.param_blur_ofDataset_filter = blur
                # 滤波核
                ksize_from = self.ui.spinBox_blurKsize_from1_ofDataset.value()
                ksize_to = self.ui.spinBox_blurKsize_to1_ofDataset.value()
                SI.param_blur_ofDataset_ksizeFrom = ksize_from
                SI.param_blur_ofDataset_ksizeTo = ksize_to
            # 噪声----------
            elif imageAugment == "噪声":
                # 概率
                probability = self.ui.dSpinBox_noise_probability_ofDataset.value()
                SI.param_noise_ofDataset_probability = probability
                # sigma
                sigma1 = self.ui.dSpinBox_noise_sigma1_ofDataset.value()
                sigma2 = self.ui.dSpinBox_noise_sigma2_ofDataset.value()
                SI.param_noise_ofDataset_sigma1 = sigma1
                SI.param_noise_ofDataset_sigma2 = sigma2
                # rate
                rate1 = self.ui.dSpinBox_noise_rate1_ofDataset.value()
                rate2 = self.ui.dSpinBox_noise_rate2_ofDataset.value()
                SI.param_noise_ofDataset_rate1 = rate1
                SI.param_noise_ofDataset_rate2 = rate2
            # 亮度----------
            elif imageAugment == "亮度":
                # 概率
                probability = self.ui.dSpinBox_brightness_probability_ofDataset.value()
                SI.param_brightness_ofDataset_probability = probability
                # beta
                beta1 = self.ui.dSpinBox_brightness_beta1_ofDataset.value()
                beta2 = self.ui.dSpinBox_brightness_beta2_ofDataset.value()
                SI.param_brightness_ofDataset_beta1 = beta1
                SI.param_brightness_ofDataset_beta2 = beta2
            # 对比度----------
            elif imageAugment == "对比度":
                # 概率
                probability = self.ui.dSpinBox_contrast_probability_ofDataset.value()
                SI.param_contrast_ofDataset_probability = probability
                # alpha
                alpha1 = self.ui.dSpinBox_contrast_alpha1_ofDataset.value()
                alpha2 = self.ui.dSpinBox_contrast_alpha2_ofDataset.value()
                SI.param_contrast_ofDataset_alpha1 = alpha1
                SI.param_contrast_ofDataset_alpha2 = alpha2

        # 执行算法--------------------------
        FuncProcessOfDataset(self, self.ui).imageAugment_run()



    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    可视化训练器    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # ↓↓                                                                                                          ↓↓
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓


    # ==============================================================================================================
    # =================================================    MENU    =================================================
    # ==============================================================================================================
    def import_datasetSplit(self):
        """ 导入训练集train """
        SI.dataset_split_path = QFileDialog.getExistingDirectory(self, "选择划分数据集文件夹")
        if SI.dataset_split_path != "":
            if isChinesePath(SI.dataset_split_path):
                SI.dataset_split_path = ""
                warningBox(self, "警告", "含有中文路径")
            else:
                SI.dataset_train_path = os.path.join(os.path.abspath(SI.dataset_split_path), "train")
                SI.dataset_val_path = os.path.join(os.path.abspath(SI.dataset_split_path), "val")
                SI.dataset_test_path = os.path.join(os.path.abspath(SI.dataset_split_path), "test")
                if not (os.path.exists(SI.dataset_train_path)):
                    SI.dataset_split_path = ""
                    errorBox(self, "错误", "没有训练集train")
                    return
                if not (os.path.exists(SI.dataset_val_path)):
                    SI.dataset_split_path = ""
                    errorBox(self, "错误", "没有验证集val")
                    return
                if not (os.path.exists(SI.dataset_test_path)):
                    SI.dataset_split_path = ""
                    errorBox(self, "错误", "没有测试集test")
                    return
                # 获取分类数量
                Param.num_classes = getClassification(SI.dataset_train_path)[0]
                # 获取图片数量
                # train
                trainNum = getFileNum(SI.dataset_train_path)
                valNum = getFileNum(SI.dataset_val_path)
                testNum = getFileNum(SI.dataset_test_path)
                self.ui.lb_showDatasetNum.setText(f"Train: {trainNum}    Val: {valNum}    Test: {testNum}")
                infoBox(self, "成功", "划分数据集导入完成")
                print("划分数据集路径：" + SI.dataset_split_path)
                print("训练集train路径：" + SI.dataset_train_path)
                print("验证集val路径：" + SI.dataset_val_path)
                print("测试集test路径：" + SI.dataset_test_path)

    def output_trainer(self):
        """ 导出结果 """
        # 弹出路径选择框：
        SI.outputDir_path = QFileDialog.getExistingDirectory(self, "选择导出目录")
        # 判断路径：
        if SI.outputDir_path != "":
            if isChinesePath(SI.outputDir_path):
                SI.outputDir_path = ""
                warningBox(self, "警告", "含有中文路径")
            else:
                # log path
                SI.log_dir_path = os.path.join(os.path.abspath(SI.outputDir_path), 'log')
                if not (os.path.exists(SI.log_dir_path)):
                    os.makedirs(SI.log_dir_path)
                SI.log_text_path = os.path.join(os.path.abspath(SI.log_dir_path), 'log.txt')
                # class_indices path
                SI.class_indices_path = os.path.join(os.path.abspath(SI.outputDir_path), 'class_indices.json')
                infoBox(self, "成功", "设置导出路径成功")
                print("保存路径：" + SI.outputDir_path)

    # ==============================================================================================================
    # =================================================    运行    =================================================
    # ==============================================================================================================
    def run_nets(self):
        """ 运行训练器 """
        # 图片损坏检查
        errorImages = []
        errorImages += checkImages(SI.dataset_train_path)
        errorImages += checkImages(SI.dataset_val_path)
        errorImages += checkImages(SI.dataset_test_path)
        if errorImages:
            error_images = '\n'.join(errorImages[:])
            error_info = "以下图片有损坏：\n" + error_images
            errorBox(self, "错误", error_info)
            print('=' * 50 + '\n' + error_info + '\n' + '=' * 50)
            del errorImages
            # 启用控件
            enable_widgets(self.ui)
            return

        # 输出日志
        # 获取当前的日期和时间
        now_time = datetime.now()
        log_text = f"Time: {now_time}\n"
        log_text += f"Net: {Param.net_name}\nSave period: {Param.save_period} epoch\nUsing ImageNet: {Param.isTransferLearning}\n"
        if not Param.isTransferLearning and Param.net_name in ["AlexNet", "VGG11", "VGG13", "VGG16", "VGG19", "GoogLeNet"]:
            log_text += f"Init weights: {Param.init_weights}\n"
        log_text += f"Input size: {Param.input_size}\nLoss function: {Param.loss_function}\nOptimizer: {Param.optimizer}\n"
        log_text += f"Mean of train: {Param.train_mean}\nStd of train: {Param.train_std}\n"
        log_text += f"Mean of val: {Param.val_mean}\nStd of val: {Param.val_std}\n"
        log_text += f"Mean of test: {Param.test_mean}\nStd of test: {Param.test_std}\n"
        log_text += f"Batch size: {Param.batch_size}\nLearning rate: {Param.learning_rate}\nEpoch: {Param.epochs}\n"
        if not Param.isTransferLearning and Param.net_name in ["AlexNet", "VGG11", "VGG13", "VGG16", "VGG19", "GoogLeNet"]:
            log_text += f"Dropout: {Param.dropout}\n"
        if not os.path.exists(SI.log_dir_path):
            os.makedirs(SI.log_dir_path)
        with open(SI.log_text_path, 'w') as log_file:
            log_file.write(log_text + '\n')

        # 运行
        FuncTrainer(self, self.ui).run_net()



    def cal_normalize(self):
        """ 计算归一化 """
        # 图片损坏检查
        errorImages = []
        errorImages += checkImages(SI.dataset_train_path)
        errorImages += checkImages(SI.dataset_val_path)
        errorImages += checkImages(SI.dataset_test_path)
        if errorImages:
            error_images = '\n'.join(errorImages[:])
            error_info = "以下图片有损坏：\n" + error_images
            errorBox(self, "错误", error_info)
            print('=' * 50 + '\n' + error_info + '\n' + '=' * 50)
            del errorImages
            return
        # 运行
        FuncTrainer(self, self.ui).cal_normalize_run()



