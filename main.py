# import sys
# import os
# import platform
#
# from PySide6.QtCore import Qt
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import QMainWindow, QApplication, QToolButton
# from PySide6.QtGui import QRegularExpressionValidator
#
# from lib.Share import SI
# from util.MessageBox import *
# from modules import *
# from modules import Ui_MainWindow, Settings
# from widgets import *
# os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
import os
import platform
import sys

import numpy as np
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QApplication, QToolButton
from PySide6.QtGui import QRegularExpressionValidator

from lib.Parameters import Param
from lib.Share import SI
from themes.widgets_style import DisabledStyle, EnabledStyle
from util.DisableWidgets import disable_widgets
from util.MessageBox import *
from modules import *

from modules import Ui_MainWindow, Settings
from widgets import *
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(QSize(1440, 810))

        global widgets
        widgets = self.ui

        self.progressBarWindow = None

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 子线程
        self.workerThread_ofDataset = None
        self.workerThread_trainerRun = None
        self.workerThread_calNormalize = None
        self.workerThread_matrix = None


        # 当前项目绝对路径
        SI.appPath = os.path.abspath(os.path.dirname(__file__))
        print("当前项目位置：", SI.appPath)

        # APP NAME
        title = "神经网络图像数据训练集成应用"
        description = "神经网络图像数据训练集成应用"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.on_pageButton_clicked)
        widgets.btn_process_image.clicked.connect(self.on_pageButton_clicked)
        widgets.btn_process_dataset.clicked.connect(self.on_pageButton_clicked)
        widgets.btn_trainer.clicked.connect(self.on_pageButton_clicked)



        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        useCustomTheme = True
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))



        # ========================================================================================================
        # ========================================    单张图片预处理控件    =========================================
        # ========================================================================================================

        ##### 初始化=================================
        # 外侧ToolBox
        widgets.toolBox_function_image.setCurrentIndex(0)
        # 内侧ToolBox1
        widgets.toolBox_process_image.setCurrentIndex(0)
        # 内侧ToolBox2
        widgets.toolBox_imageAugment_image.setCurrentIndex(0)
        # 外侧ToolBox算法
        SI.current_process_function_ofImage = "预处理工具"
        # 内侧ToolBox1算法
        SI.current_processTool_ofImage = "更改后缀"


        ##### 目录=================================
        widgets.btn_importSingleImage.clicked.connect(self.on_button_clicked_ofImage)      # 添加
        widgets.btn_exportResult_image.clicked.connect(self.on_button_clicked_ofImage)     # 保存
        widgets.btn_preview_image.clicked.connect(self.reviewAlgorithm_ofImage)            # 预览
        widgets.btn_run_image.clicked.connect(self.runAlgorithm_ofImage)                   # 执行
        widgets.toolBox_function_image.currentChanged.connect(self.on_toolBox_function_changed_ofImage)   # 外侧ToolBox
        # 预览框
        widgets.img_pre_image.setAlignment(Qt.AlignCenter)
        widgets.img_after_image.setAlignment(Qt.AlignCenter)


        ##### 预处理工具=================================
        ### ToolBox改变信号触发
        widgets.toolBox_process_image.currentChanged.connect(self.on_toolBox_process_changed_ofImage)
        ### 更改后缀---------------
        # 按钮
        widgets.btn_jpg_image.clicked.connect(self.on_button_clicked_ofImage)
        widgets.btn_jpeg_image.clicked.connect(self.on_button_clicked_ofImage)
        widgets.btn_png_image.clicked.connect(self.on_button_clicked_ofImage)
        widgets.btn_bmp_image.clicked.connect(self.on_button_clicked_ofImage)
        # 单选按钮
        widgets.rb_jpg_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rb_jpeg_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rb_png_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rb_bmp_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        ### 图片方形化---------------
        # 单选按钮
        widgets.frame_square_RGB_image.setVisible(False)
        widgets.rbtn_BORDER_CONSTANT_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_BORDER_REFLECT_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_BORDER_REPLICATE_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_BORDER_WRAP_image.clicked.connect(self.on_radioButton_clicked_ofImage)
        # 滑条
        widgets.slider_square_image_R.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        widgets.slider_square_image_G.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        widgets.slider_square_image_B.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        # spin box 信号绑定滑条
        widgets.spinBox_square_image_R.valueChanged.connect(widgets.slider_square_image_R.setValue)
        widgets.spinBox_square_image_G.valueChanged.connect(widgets.slider_square_image_G.setValue)
        widgets.spinBox_square_image_B.valueChanged.connect(widgets.slider_square_image_B.setValue)
        ### 更改大小---------------
        # 像素文本框
        widgets.lineEdit_resizepx1_ofImage.textChanged.connect(widgets.lineEdit_resizepx2_ofImage.setText)
        widgets.lineEdit_resizepx1_ofImage.setValidator(QRegularExpressionValidator(
            r"^(?:[1-9][0-9]{0,2}|[1-7]\d\d\d|80\d\d|81\d[0-2])$"   # 像素只能输入1~8192
        ))
        widgets.lineEdit_resizepx2_ofImage.setValidator(QRegularExpressionValidator(
            r"^(?:[1-9][0-9]{0,2}|[1-7]\d\d\d|80\d\d|81\d[0-2])$"   # 像素只能输入1~8192
        ))
        # 单选按钮
        widgets.rbtn_INTER_LINEAR_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_INTER_NEAREST_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_INTER_CUBIC_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_INTER_AREA_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_INTER_LANCZOS4_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_INTER_LINEAR_EXACT_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)

        ##### 图像增强=================================
        ### 图像旋转---------------
        # 初始化不可见
        widgets.frame_rotate_content_ofImage.setVisible(False)
        # switch开关 信号触发
        widgets.switchButton_rotate_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        # spin box 信号绑定滑条
        widgets.dSpinBox_rotateDegree_ofImage.valueChanged.connect(
            lambda: widgets.slider_rotateDegree_ofImage.setValue(widgets.dSpinBox_rotateDegree_ofImage.value() * 100)
        )
        widgets.dSpinBox_rotateScale_ofImage.valueChanged.connect(
            lambda: widgets.slider_rotateScale_ofImage.setValue(widgets.dSpinBox_rotateScale_ofImage.value() * 100)
        )
        widgets.spinBox_rotate_ofImage_R.valueChanged.connect(widgets.slider_rotate_ofImage_R.setValue)
        widgets.spinBox_rotate_ofImage_G.valueChanged.connect(widgets.slider_rotate_ofImage_G.setValue)
        widgets.spinBox_rotate_ofImage_B.valueChanged.connect(widgets.slider_rotate_ofImage_B.setValue)
        # 滑条 信号绑定滑条
        widgets.slider_rotateDegree_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_rotateDegree_ofImage.setValue(widgets.slider_rotateDegree_ofImage.value() / 100)
        )
        widgets.slider_rotateScale_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_rotateScale_ofImage.setValue(widgets.slider_rotateScale_ofImage.value() / 100)
        )
        widgets.slider_rotate_ofImage_R.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        widgets.slider_rotate_ofImage_G.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        widgets.slider_rotate_ofImage_B.valueChanged.connect(self.on_slider_valueChanged_ofImage)
        ### 水平翻转---------------
        widgets.switchButton_HFlip_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        ### 垂直翻转---------------
        widgets.switchButton_VFlip_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        ### 模糊---------------
        # 初始化不可见
        widgets.frame_blur_content_ofImage.setVisible(False)
        # switch开关 信号触发
        widgets.switchButton_blur_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        # 单选按钮
        widgets.rbtn_blur_mean_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_blur_box_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_blur_gaussian_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        widgets.rbtn_blur_median_ofImage.clicked.connect(self.on_radioButton_clicked_ofImage)
        # spin box
        widgets.spinBox_blurKsize1_ofImage.valueChanged.connect(widgets.spinBox_blurKsize2_ofImage.setValue)
        widgets.spinBox_blurKsize1_ofImage.valueChanged.connect(widgets.slider_blurKsize1_ofImage.setValue)
        widgets.spinBox_blurKsize2_ofImage.valueChanged.connect(widgets.slider_blurKsize2_ofImage.setValue)
        # 滑条 信号绑定
        widgets.slider_blurKsize1_ofImage.valueChanged.connect(widgets.spinBox_blurKsize1_ofImage.setValue)
        widgets.slider_blurKsize2_ofImage.valueChanged.connect(widgets.spinBox_blurKsize2_ofImage.setValue)
        ### 噪声---------------
        # 初始化不可见
        widgets.frame_noise_content_ofImage.setVisible(False)
        widgets.frame_noise_gaussian_ofImage.setVisible(False)
        widgets.frame_noise_saltPepper_ofImage.setVisible(False)
        # switch开关 信号触发
        widgets.switchButton_noise_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        # 勾选框
        widgets.cb_noise_gaussian_ofImage.clicked.connect(self.on_checkBox_clicked_ofImage)
        widgets.cb_noise_saltPepper_ofImage.clicked.connect(self.on_checkBox_clicked_ofImage)
        # spin box
        widgets.dSpinBox_noise_sigma_ofImage.valueChanged.connect(
            lambda: widgets.slider_noise_sigma_ofImage.setValue(widgets.dSpinBox_noise_sigma_ofImage.value() * 100)
        )
        widgets.dSpinBox_noise_rate_ofImage.valueChanged.connect(
            lambda: widgets.slider_noise_rate_ofImage.setValue(widgets.dSpinBox_noise_rate_ofImage.value() * 100)
        )
        # 滑条
        widgets.slider_noise_sigma_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_noise_sigma_ofImage.setValue(widgets.slider_noise_sigma_ofImage.value() / 100)
        )
        widgets.slider_noise_rate_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_noise_rate_ofImage.setValue(widgets.slider_noise_rate_ofImage.value() / 100)
        )
        ### 亮度---------------
        # 初始化不可见
        widgets.frame_brightness_content_ofImage.setVisible(False)
        # switch开关 信号触发
        widgets.switchButton_brightness_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        # spin box
        widgets.dSpinBox_brightness_ofImage.valueChanged.connect(
            lambda: widgets.slider_brightness_ofImage.setValue(widgets.dSpinBox_brightness_ofImage.value() * 100)
        )
        # 滑条
        widgets.slider_brightness_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_brightness_ofImage.setValue(widgets.slider_brightness_ofImage.value() / 100)
        )
        ### 对比度---------------
        # 初始化不可见
        widgets.frame_contrast_content_ofImage.setVisible(False)
        # switch开关 信号触发
        widgets.switchButton_contrast_ofImage.checkedChanged.connect(self.on_switchButton_checkedChanged_ofImage)
        # spin box
        widgets.dSpinBox_contrast_ofImage.valueChanged.connect(
            lambda: widgets.slider_contrast_ofImage.setValue(widgets.dSpinBox_contrast_ofImage.value() * 100)
        )
        # 滑条
        widgets.slider_contrast_ofImage.valueChanged.connect(
            lambda: widgets.dSpinBox_contrast_ofImage.setValue(widgets.slider_contrast_ofImage.value() / 100)
        )



        # ========================================================================================================
        # ============================================    数据集预处理控件    =======================================
        # ========================================================================================================

        ##### 初始化=================================
        # 外侧ToolBox
        widgets.toolBox_function_dataset.setCurrentIndex(0)
        # 内侧ToolBox1
        widgets.toolBox_process_dataset.setCurrentIndex(0)
        # 内侧ToolBox2
        widgets.toolBox_imageAugment_dataset.setCurrentIndex(0)
        # 外侧ToolBox算法
        SI.current_process_function_ofDataset = "预处理工具"
        # 内侧ToolBox1算法
        SI.current_processTool_ofDataset = "统一后缀"

        ##### 目录=================================
        widgets.btn_importDataset.clicked.connect(self.on_button_clicked_ofDataset)            # 添加
        widgets.btn_exportResult_dataset.clicked.connect(self.on_button_clicked_ofDataset)     # 保存
        widgets.btn_preview_dataset.clicked.connect(self.reviewAlgorithm_ofDataset)            # 预览
        widgets.btn_run_dataset.clicked.connect(self.runAlgorithm_ofDataset)                   # 执行
        widgets.toolBox_function_dataset.currentChanged.connect(self.on_toolBox_function_changed_ofDataset)   # 外侧ToolBox
        # 预览框
        widgets.img_pre_dataset.setAlignment(Qt.AlignCenter)
        widgets.img_after_dataset.setAlignment(Qt.AlignCenter)

        ##### 预处理工具=================================
        ### ToolBox改变信号触发
        widgets.toolBox_process_dataset.currentChanged.connect(self.on_toolBox_process_changed_ofDataset)
        ### 更改后缀-------------------------
        # 按钮
        widgets.btn_jpg_ofDataset.clicked.connect(self.on_button_clicked_ofDataset)
        widgets.btn_jpeg_ofDataset.clicked.connect(self.on_button_clicked_ofDataset)
        widgets.btn_png_ofDataset.clicked.connect(self.on_button_clicked_ofDataset)
        widgets.btn_bmp_ofDataset.clicked.connect(self.on_button_clicked_ofDataset)
        # 单选按钮
        widgets.rb_jpg_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rb_jpeg_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rb_png_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rb_bmp_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        ### 统一命名-------------------------
        # 勾选框
        widgets.cb_rename0_ofDataset.clicked.connect(self.on_checkBox_clicked_ofDataset)
        # 单选按钮
        widgets.rbtn_rename1_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_rename2_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_rename3_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        ### 图片方形化-------------------------
        # 单选按钮
        widgets.frame_square_RGB_ofDataset.setVisible(False)
        widgets.rbtn_BORDER_CONSTANT_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_BORDER_REFLECT_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_BORDER_REPLICATE_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_BORDER_WRAP_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        # 滑条
        widgets.slider_square_ofDataset_R.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_square_ofDataset_G.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_square_ofDataset_B.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        # spin box 信号绑定滑条
        widgets.spinBox_square_ofDataset_R.valueChanged.connect(widgets.slider_square_ofDataset_R.setValue)
        widgets.spinBox_square_ofDataset_G.valueChanged.connect(widgets.slider_square_ofDataset_G.setValue)
        widgets.spinBox_square_ofDataset_B.valueChanged.connect(widgets.slider_square_ofDataset_B.setValue)
        ### 更改大小-------------------------
        # 像素文本框
        widgets.lineEdit_resizepx1_ofDataset.textChanged.connect(widgets.lineEdit_resizepx2_ofDataset.setText)
        widgets.lineEdit_resizepx1_ofDataset.setValidator(QRegularExpressionValidator(
            r"^(?:[1-9][0-9]{0,2}|[1-7]\d\d\d|80\d\d|81\d[0-2])$"   # 像素只能输入1~8192
        ))
        widgets.lineEdit_resizepx2_ofDataset.setValidator(QRegularExpressionValidator(
            r"^(?:[1-9][0-9]{0,2}|[1-7]\d\d\d|80\d\d|81\d[0-2])$"   # 像素只能输入1~8192
        ))
        # 单选按钮
        widgets.rbtn_INTER_LINEAR_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_INTER_NEAREST_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_INTER_CUBIC_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_INTER_AREA_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_INTER_LANCZOS4_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_INTER_LINEAR_EXACT_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        ### 数据集分割-------------------------
        # spin box 信号绑定滑条
        widgets.dSpinBox_split_train_ofDataset.valueChanged.connect(
            lambda: widgets.slider_split_train_ofDataset.setValue(
                widgets.dSpinBox_split_train_ofDataset.value() * 100)
        )
        widgets.dSpinBox_split_val_ofDataset.valueChanged.connect(
            lambda: widgets.slider_split_val_ofDataset.setValue(
                widgets.dSpinBox_split_val_ofDataset.value() * 100)
        )
        widgets.dSpinBox_split_test_ofDataset.valueChanged.connect(
            lambda: widgets.slider_split_test_ofDataset.setValue(
                widgets.dSpinBox_split_test_ofDataset.value() * 100)
        )
        # 滑条 信号spin box
        widgets.slider_split_train_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_split_train_ofDataset.setValue(
                widgets.slider_split_train_ofDataset.value() / 100)
        )
        widgets.slider_split_val_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_split_val_ofDataset.setValue(
                widgets.slider_split_val_ofDataset.value() / 100)
        )
        widgets.slider_split_test_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_split_test_ofDataset.setValue(
                widgets.slider_split_test_ofDataset.value() / 100)
        )


        ##### 图像增强=================================
        ### 图像旋转====================
        ## 初始化不可见-----
        widgets.frame_rotate_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_rotate_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box 信号绑定-----
        # 概率
        widgets.dSpinBox_rotate_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_rotate_probability_ofDataset.setValue(
                widgets.dSpinBox_rotate_probability_ofDataset.value() * 100))
        # 旋转范围
        widgets.dSpinBox_rotateDegree1_ofDataset.setMaximum(0)
        widgets.dSpinBox_rotateDegree2_ofDataset.setMinimum(0)
        widgets.dSpinBox_rotateDegree1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_rotateDegree2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        # 缩放范围
        widgets.dSpinBox_rotateScale1_ofDataset.setMaximum(1)
        widgets.dSpinBox_rotateScale2_ofDataset.setMinimum(1)
        widgets.dSpinBox_rotateScale1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_rotateScale2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        # RGB
        widgets.spinBox_rotate_ofDataset_R.valueChanged.connect(widgets.slider_rotate_ofDataset_R.setValue)
        widgets.spinBox_rotate_ofDataset_G.valueChanged.connect(widgets.slider_rotate_ofDataset_G.setValue)
        widgets.spinBox_rotate_ofDataset_B.valueChanged.connect(widgets.slider_rotate_ofDataset_B.setValue)
        ## 滑条 信号绑定滑条-----
        # 概率
        widgets.slider_rotate_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_rotate_probability_ofDataset.setValue(
                widgets.slider_rotate_probability_ofDataset.value() / 100))
        # 旋转范围
        widgets.slider_rotateDegree1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_rotateDegree2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        # 缩放范围
        widgets.slider_rotateScale1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_rotateScale2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        # RGB
        widgets.slider_rotate_ofDataset_R.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_rotate_ofDataset_G.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_rotate_ofDataset_B.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        ### 水平翻转====================
        ## 初始化不可见-----
        widgets.frame_HFlip_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_HFlip_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box 信号绑定-----
        # 概率
        widgets.dSpinBox_HFlip_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_HFlip_probability_ofDataset.setValue(
                widgets.dSpinBox_HFlip_probability_ofDataset.value() * 100))
        ## 滑条 信号绑定滑条-----
        # 概率
        widgets.slider_HFlip_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_HFlip_probability_ofDataset.setValue(
                widgets.slider_HFlip_probability_ofDataset.value() / 100))
        ### 垂直翻转====================
        ## 初始化不可见-----
        widgets.frame_VFlip_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_VFlip_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box 信号绑定-----
        # 概率
        widgets.dSpinBox_VFlip_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_VFlip_probability_ofDataset.setValue(
                widgets.dSpinBox_VFlip_probability_ofDataset.value() * 100))
        ## 滑条 信号绑定滑条-----
        # 概率
        widgets.slider_VFlip_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_VFlip_probability_ofDataset.setValue(
                widgets.slider_VFlip_probability_ofDataset.value() / 100))
        ### 模糊====================
        ## 初始化不可见-----
        widgets.frame_blur_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_blur_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box 信号绑定-----
        # 概率
        widgets.dSpinBox_blur_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_blur_probability_ofDataset.setValue(
                widgets.dSpinBox_blur_probability_ofDataset.value() * 100))
        # From
        widgets.spinBox_blurKsize_from1_ofDataset.setMaximum(1)
        widgets.spinBox_blurKsize_from2_ofDataset.setMaximum(1)
        widgets.spinBox_blurKsize_from1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.spinBox_blurKsize_from2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        # To
        widgets.spinBox_blurKsize_to1_ofDataset.setMinimum(1)
        widgets.spinBox_blurKsize_to2_ofDataset.setMinimum(1)
        widgets.spinBox_blurKsize_to1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.spinBox_blurKsize_to2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        ## 滑条 信号绑定滑条-----
        # 概率
        widgets.slider_blur_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_blur_probability_ofDataset.setValue(
                widgets.slider_blur_probability_ofDataset.value() / 100))
        # From
        widgets.slider_blurKsize_from_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        # To
        widgets.slider_blurKsize_to_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        ## 单选按钮-----
        widgets.rbtn_blur_mean_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_blur_box_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_blur_gaussian_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        widgets.rbtn_blur_median_ofDataset.clicked.connect(self.on_radioButton_clicked_ofDataset)
        ### 噪声====================
        ## 初始化不可见-----
        widgets.frame_noise_content_ofDataset.setVisible(False)
        widgets.frame_noise_gaussian_ofDataset.setVisible(False)
        widgets.frame_noise_saltPepper_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_noise_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## 勾选框-----
        widgets.cb_noise_gaussian_ofDataset.clicked.connect(self.on_checkBox_clicked_ofDataset)
        widgets.cb_noise_saltPepper_ofDataset.clicked.connect(self.on_checkBox_clicked_ofDataset)
        ## spin box-----
        # 概率
        widgets.dSpinBox_noise_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_noise_probability_ofDataset.setValue(
                widgets.dSpinBox_noise_probability_ofDataset.value() * 100))
        # sigma
        widgets.dSpinBox_noise_sigma1_ofDataset.setMaximum(0)
        widgets.dSpinBox_noise_sigma2_ofDataset.setMinimum(0)
        widgets.dSpinBox_noise_sigma1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_noise_sigma2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        # rate
        widgets.dSpinBox_noise_rate1_ofDataset.setMaximum(0)
        widgets.dSpinBox_noise_rate2_ofDataset.setMinimum(0)
        widgets.dSpinBox_noise_rate1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_noise_rate2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        ## 滑条-----
        # 概率
        widgets.slider_noise_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_noise_probability_ofDataset.setValue(
                widgets.slider_noise_probability_ofDataset.value() / 100))
        # sigma
        widgets.slider_noise_sigma1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_noise_sigma2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        # rate
        widgets.slider_noise_rate1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_noise_rate2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        ### 亮度====================
        ## 初始化不可见-----
        widgets.frame_brightness_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_brightness_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box-----
        # 概率
        widgets.dSpinBox_brightness_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_brightness_probability_ofDataset.setValue(
                widgets.dSpinBox_brightness_probability_ofDataset.value() * 100))
        # beta
        widgets.dSpinBox_brightness_beta1_ofDataset.setMaximum(0)
        widgets.dSpinBox_brightness_beta2_ofDataset.setMinimum(0)
        widgets.dSpinBox_brightness_beta1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_brightness_beta2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        ## 滑条-----
        # 概率
        widgets.slider_brightness_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_brightness_probability_ofDataset.setValue(
                widgets.slider_brightness_probability_ofDataset.value() / 100))
        # beta
        widgets.slider_brightness_beta1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_brightness_beta2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        ### 对比度====================
        ## 初始化不可见-----
        widgets.frame_contrast_content_ofDataset.setVisible(False)
        ## switch开关 信号触发-----
        widgets.switchButton_contrast_ofDataset.checkedChanged.connect(self.on_switchButton_checkedChanged_ofDataset)
        ## spin box-----
        # 概率
        widgets.dSpinBox_contrast_probability_ofDataset.valueChanged.connect(
            lambda: widgets.slider_contrast_probability_ofDataset.setValue(
                widgets.dSpinBox_contrast_probability_ofDataset.value() * 100))
        # alpha
        widgets.dSpinBox_contrast_alpha1_ofDataset.setMaximum(1)
        widgets.dSpinBox_contrast_alpha2_ofDataset.setMinimum(1)
        widgets.dSpinBox_contrast_alpha1_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        widgets.dSpinBox_contrast_alpha2_ofDataset.valueChanged.connect(self.on_spinBox_valueChanged_ofDataset)
        ## 滑条-----
        # 概率
        widgets.slider_contrast_probability_ofDataset.valueChanged.connect(
            lambda: widgets.dSpinBox_contrast_probability_ofDataset.setValue(
                widgets.slider_contrast_probability_ofDataset.value() / 100))
        # alpha
        widgets.slider_contrast_alpha1_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)
        widgets.slider_contrast_alpha2_ofDataset.valueChanged.connect(self.on_slider_valueChanged_ofDataset)


        # ========================================================================================================
        # ============================================    可视化训练器控件    =======================================
        # ========================================================================================================
        ##### 初始化=================================
        widgets.toolBox_trainer.setCurrentIndex(0)
        widgets.stackedWidget_canvas.setCurrentWidget(widgets.pgView_step_loss)
        ##### 目录=================================
        widgets.btn_import_datasetSplit.clicked.connect(self.on_button_clicked_trainer)     # 导入划分数据集
        widgets.btn_output.clicked.connect(self.on_button_clicked_trainer)                  # output
        widgets.btn_terminate.clicked.connect(self.terminate_trainer)                       # 终止
        widgets.btn_run_trainer.clicked.connect(self.run_trainer)                           # 运行
        ##### 画布=================================
        # 重置按钮
        widgets.btn_trainer_rangeReset.clicked.connect(self.reset_view_trainer)
        # Step按钮
        widgets.btn_trainer_showStep.clicked.connect(self.show_step_trainer)
        # Epoch按钮
        widgets.btn_trainer_showEpoch.clicked.connect(self.show_epoch_trainer)
        # 混淆矩阵按钮
        widgets.btn_trainer_matrix.clicked.connect(self.show_confusionMatrix_trainer)
        widgets.btn_trainer_matrix.setEnabled(False)
        ##### 模型设置=================================
        # 网络选择
        widgets.comboBox_trainer_net.currentTextChanged.connect(self.on_netname_changed)
        # 保存间隔
        widgets.lineEdit_trainer_period.setValidator(QRegularExpressionValidator(r"^(?:\d|[1-9][0-9]{0,3})$"))  # 0-9999
        # ImageNet
        widgets.switchButton_trainer_imageNet.checkedChanged.connect(self.on_switchButton_checkedChanged_trainer)
        # initWeights
        widgets.switchButton_trainer_initWeights.setChecked(True)
        widgets.switchButton_trainer_initWeights.checkedChanged.connect(self.on_switchButton_checkedChanged_trainer)
        ##### 模型参数=================================
        # 图像大小
        widgets.lineEdit_trainer_inputSize1.setValidator(QRegularExpressionValidator(r"^(?:[1-9][0-9]{0,3})$"))  # 1-9999
        widgets.lineEdit_trainer_inputSize2.setValidator(QRegularExpressionValidator(r"^(?:[1-9][0-9]{0,3})$"))  # 1-9999
        widgets.lineEdit_trainer_inputSize1.textChanged.connect(widgets.lineEdit_trainer_inputSize2.setText)
        widgets.lineEdit_trainer_inputSize2.textChanged.connect(widgets.lineEdit_trainer_inputSize1.setText)
        # 归一化参数
        widgets.btn_trainer_normalize_default.clicked.connect(self.on_button_clicked_trainer)
        widgets.btn_trainer_normalize_pretrain.clicked.connect(self.on_button_clicked_trainer)
        widgets.btn_trainer_normalize_cal.clicked.connect(self.on_button_clicked_trainer)
        ##### 超参数调优=================================
        # Batch Size
        widgets.lineEdit_trainer_batchSize.setValidator(QRegularExpressionValidator(r"^(?:[1-9][0-9]{0,3})$"))  # 1-9999
        # Learning Rate
        widgets.lineEdit_trainer_learningRate.setValidator(QRegularExpressionValidator(r"^0\.\d+$"))  # (0, 1)
        # Epoch
        widgets.lineEdit_trainer_epoch.setValidator(QRegularExpressionValidator(r"^(?:[1-9][0-9]{0,3})$"))  # 1-9999
        # 失活比例
        widgets.dSpinBox_trainer_dropout.valueChanged.connect(
            lambda: widgets.slider_trainer_dropout.setValue(widgets.dSpinBox_trainer_dropout.value() * 100)
        )
        widgets.slider_trainer_dropout.valueChanged.connect(
            lambda: widgets.dSpinBox_trainer_dropout.setValue(widgets.slider_trainer_dropout.value() / 100)
        )








    # ***************************************************************************************************************
    # ************************************************    UI界面函数    **********************************************
    # ***************************************************************************************************************
    def on_pageButton_clicked(self):
        """ 界面控件点击 """
        btn = self.sender()
        btnName = btn.objectName()
        # 清除页面
        if btnName != "btn_process_image":
            self.clear_modifySuffix_ofImage()
            self.clear_resize_ofImage()
            self.clear_square_ofImage()
            self.clear_switch_ofImage()
            widgets.toolBox_function_image.setCurrentIndex(0)
            widgets.toolBox_imageAugment_image.setCurrentIndex(0)
            widgets.toolBox_process_image.setCurrentIndex(0)
        if btnName != "btn_process_dataset":
            self.clear_modifySuffix_ofDataset()
            self.clear_uniformName_ofDataset()
            self.clear_resize_ofDataset()
            self.clear_square_ofDataset()
            self.clear_switch_ofDataset()
            widgets.toolBox_function_dataset.setCurrentIndex(0)
            widgets.toolBox_imageAugment_dataset.setCurrentIndex(0)
            widgets.toolBox_process_dataset.setCurrentIndex(0)
        if btnName != "btn_trainer":
            widgets.toolBox_trainer.setCurrentIndex(0)

        # 主页
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # 单张图片预处理
        elif btnName == "btn_process_image":
            SI.current_page = "process_image"
            print("当前页面：" + SI.current_page)
            widgets.stackedWidget.setCurrentWidget(widgets.processPage_image)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # 数据集预处理
        elif btnName == "btn_process_dataset":
            SI.current_page = "process_dataset"
            print("当前页面：" + SI.current_page)
            widgets.stackedWidget.setCurrentWidget(widgets.processPage_dataset)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # 可视化训练器
        elif btnName == "btn_trainer":
            SI.current_page = "trainer"
            print("当前页面：" + SI.current_page)
            widgets.stackedWidget.setCurrentWidget(widgets.trainer)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))




    def resizeEvent(self, event):
        """ 窗口大小改变事件 """
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        """ 鼠标点击事件 """
        self.dragPos = event.globalPosition().toPoint()

    def closeEvent(self, event):
        """ 主窗口关闭事件 """
        # 关闭子线程
        if self.workerThread_ofDataset:
            self.workerThread_ofDataset.requestInterruption()
            self.workerThread_ofDataset.quit()
            self.workerThread_ofDataset.wait()
        if self.workerThread_trainerRun:
            self.workerThread_trainerRun.requestInterruption()
            self.workerThread_trainerRun.quit()
            self.workerThread_trainerRun.wait()
        if self.workerThread_calNormalize:
            self.workerThread_calNormalize.requestInterruption()
            self.workerThread_calNormalize.quit()
            self.workerThread_calNormalize.wait()
        if self.workerThread_matrix:
            self.workerThread_matrix.requestInterruption()
            self.workerThread_matrix.quit()
            self.workerThread_matrix.wait()






    # ***************************************************************************************************************
    # ******************************************       单张图片处理函数     ********************************************
    # ***************************************************************************************************************

    def reviewAlgorithm_ofImage(self):
        """
        预览按钮点击
        """
        if (not SI.functionMutex) and (not SI.threadMutex):
            try:
                SI.functionMutex = True
                if SI.image_path == "":
                    errorBox(self, "错误", "请先添加图片")
                else:
                    # 预处理工具
                    if SI.current_process_function_ofImage == "预处理工具":
                        AppFunctions.processAlgorithm_review_ofImage(self)
                    # 图像增强
                    elif SI.current_process_function_ofImage == "图像增强":
                        AppFunctions.imageAugment_review_ofImage(self)
                    else:
                        errorBox(self, "错误", "未选择算法")
            except Exception as e:
                errorBox(self, "错误", "预览失败")
                print("《预览单张图像预处理》时错误:", e)
            finally:
                SI.functionMutex = False
        else:
            warningBox(self, "警告", "其它功能正在执行")


    def runAlgorithm_ofImage(self):
        """
        运行按钮点击
        """
        if (not SI.functionMutex) and (not SI.threadMutex):
            try:
                SI.functionMutex = True
                if SI.image_path == "":
                    errorBox(self, "错误", "请先添加图片")
                else:
                    # 预处理工具
                    if SI.current_process_function_ofImage == "预处理工具":
                        AppFunctions.processAlgorithm_run_ofImage(self)
                    # 图像增强
                    elif SI.current_process_function_ofImage == "图像增强":
                        AppFunctions.imageAugment_run_ofImage(self)
                    else:
                        errorBox(self, "错误", "未选择算法")
            except Exception as e:
                errorBox(self, "错误", "运行失败")
                print("《运行单张图像预处理》时错误:", e)
            finally:
                SI.functionMutex = False
        else:
            warningBox(self, "警告", "其它功能正在执行")



    # ------------------------------------  信号触发  ------------------------------------
    def on_button_clicked_ofImage(self):
        """
        按钮 的信号触发函数
        """
        btn = self.sender()
        btnName = btn.objectName()

        # 目录
        if btnName == "btn_importSingleImage":
            AppFunctions.importSingleImage(self)
        elif btnName == "btn_exportResult_image":
            AppFunctions.exportSingleImage(self)
        # 更改后缀
        elif btnName == "btn_jpg_image":
            widgets.rb_jpg_image.setChecked(True)
            SI.processToolAlgorithm_ofImage = "modifySuffix_jpg"
            self.show_current_algorithm_ofImage(1, "更改后缀 --> jpg")
            self.print_current_algorithm_ofImage(1)
        elif btnName == "btn_jpeg_image":
            widgets.rb_jpeg_image.setChecked(True)
            SI.processToolAlgorithm_ofImage = "modifySuffix_jpeg"
            self.show_current_algorithm_ofImage(1, "更改后缀 --> jpeg")
            self.print_current_algorithm_ofImage(1)
        elif btnName == "btn_png_image":
            widgets.rb_png_image.setChecked(True)
            SI.processToolAlgorithm_ofImage = "modifySuffix_png"
            self.show_current_algorithm_ofImage(1, "更改后缀 --> png")
            self.print_current_algorithm_ofImage(1)
        elif btnName == "btn_bmp_image":
            widgets.rb_bmp_image.setChecked(True)
            SI.processToolAlgorithm_ofImage = "modifySuffix_bmp"
            self.show_current_algorithm_ofImage(1, "更改后缀 --> bmp")
            self.print_current_algorithm_ofImage(1)

    def on_radioButton_clicked_ofImage(self):
        """
        单选按钮 的信号触发函数
        """
        rb = self.sender()
        rbName = rb.objectName()
        # 预处理工具------------------------
        # 更改后缀
        if rbName == "rb_jpg_image":
            if widgets.rb_jpg_image.isChecked():
                SI.processToolAlgorithm_ofImage = "modifySuffix_jpg"
                self.show_current_algorithm_ofImage(1, "更改后缀 --> jpg")
                self.print_current_algorithm_ofImage(1)
        elif rbName == "rb_jpeg_image":
            if widgets.rb_jpeg_image.isChecked():
                SI.processToolAlgorithm_ofImage = "modifySuffix_jpeg"
                self.show_current_algorithm_ofImage(1, "更改后缀 --> jpeg")
                self.print_current_algorithm_ofImage(1)
        elif rbName == "rb_png_image":
            if widgets.rb_png_image.isChecked():
                SI.processToolAlgorithm_ofImage = "modifySuffix_png"
                self.show_current_algorithm_ofImage(1, "更改后缀 --> png")
                self.print_current_algorithm_ofImage(1)
        elif rbName == "rb_bmp_image":
            if widgets.rb_bmp_image.isChecked():
                SI.processToolAlgorithm_ofImage = "modifySuffix_bmp"
                self.show_current_algorithm_ofImage(1, "更改后缀 --> bmp")
                self.print_current_algorithm_ofImage(1)
        # 图片方形化
        elif rbName == "rbtn_BORDER_CONSTANT_image":
            widgets.frame_square_RGB_image.setVisible(True)
            SI.processToolAlgorithm_ofImage = "square_BORDER_CONSTANT"
            self.show_current_algorithm_ofImage(1, "图片方形化 --> BORDER_CONSTANT")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_BORDER_REFLECT_image":
            widgets.frame_square_RGB_image.setVisible(False)
            SI.processToolAlgorithm_ofImage = "square_BORDER_REFLECT"
            self.show_current_algorithm_ofImage(1, "图片方形化 --> BORDER_REFLECT")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_BORDER_REPLICATE_image":
            widgets.frame_square_RGB_image.setVisible(False)
            SI.processToolAlgorithm_ofImage = "square_BORDER_REPLICATE"
            self.show_current_algorithm_ofImage(1, "图片方形化 --> BORDER_REPLICATE")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_BORDER_WRAP_image":
            widgets.frame_square_RGB_image.setVisible(False)
            SI.processToolAlgorithm_ofImage = "square_BORDER_WRAP"
            self.show_current_algorithm_ofImage(1, "图片方形化 --> BORDER_WRAP")
            self.print_current_algorithm_ofImage(1)
        # 更改大小
        elif rbName == "rbtn_INTER_LINEAR_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_LINEAR"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_LINEAR")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_INTER_NEAREST_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_NEAREST"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_NEAREST")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_INTER_CUBIC_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_CUBIC"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_CUBIC")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_INTER_AREA_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_AREA"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_AREA")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_INTER_LANCZOS4_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_LANCZOS4"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_LANCZOS4")
            self.print_current_algorithm_ofImage(1)
        elif rbName == "rbtn_INTER_LINEAR_EXACT_ofImage":
            SI.processToolAlgorithm_ofImage = "resize_INTER_LINEAR_EXACT"
            self.show_current_algorithm_ofImage(1, "更改大小 --> INTER_LINEAR_EXACT")
            self.print_current_algorithm_ofImage(1)
        # 图像增强------------------------
        # 模糊
        elif rbName == "rbtn_blur_mean_ofImage":
            if "blur_mean" not in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.append("blur_mean")
            if "blur_box" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_box")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_gaussian")
            if "blur_median" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_median")
            self.print_current_algorithm_ofImage(2)
            if SI.syncFlag_blur_ofImage: self.forbid_blur_ofImage(False)    # 恢复中值滤波下禁止第二个滤波核设置参数
        elif rbName == "rbtn_blur_box_ofImage":
            if "blur_box" not in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.append("blur_box")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_mean")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_gaussian")
            if "blur_median" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_median")
            self.print_current_algorithm_ofImage(2)
            if SI.syncFlag_blur_ofImage: self.forbid_blur_ofImage(False)    # 恢复中值滤波下禁止第二个滤波核设置参数
        elif rbName == "rbtn_blur_gaussian_ofImage":
            if "blur_gaussian" not in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.append("blur_gaussian")
            if "blur_box" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_box")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_mean")
            if "blur_median" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_median")
            self.print_current_algorithm_ofImage(2)
            if SI.syncFlag_blur_ofImage: self.forbid_blur_ofImage(False)    # 恢复中值滤波下禁止第二个滤波核设置参数
        elif rbName == "rbtn_blur_median_ofImage":
            if "blur_median" not in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.append("blur_median")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_gaussian")
            if "blur_box" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_box")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofImage:
                SI.imageAugmentAlgorithm_ofImage.remove("blur_mean")
            self.print_current_algorithm_ofImage(2)
            if not SI.syncFlag_blur_ofImage: self.forbid_blur_ofImage(True) # 禁止中值滤波下禁止第二个滤波核设置参数

    def on_checkBox_clicked_ofImage(self):
        """
        勾选框 的信号触发激活函数
        """
        checkBox = self.sender()
        checkBoxName = checkBox.objectName()
        # 噪声
        if checkBoxName == "cb_noise_gaussian_ofImage":
            if checkBox.isChecked():
                widgets.frame_noise_gaussian_ofImage.setVisible(True)
                if "noise_gaussian" not in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.append("noise_gaussian")
            else:
                widgets.frame_noise_gaussian_ofImage.setVisible(False)
                if "noise_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("noise_gaussian")
            self.print_current_algorithm_ofImage(2)
        elif checkBoxName == "cb_noise_saltPepper_ofImage":
            if checkBox.isChecked():
                widgets.frame_noise_saltPepper_ofImage.setVisible(True)
                if "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.append("noise_saltPepper")
            else:
                widgets.frame_noise_saltPepper_ofImage.setVisible(False)
                if "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("noise_saltPepper")
            self.print_current_algorithm_ofImage(2)

    def on_slider_valueChanged_ofImage(self):
        """
        滑条 的信号触发激活函数
        """
        slider = self.sender()
        sliderName = slider.objectName()
        # 图片方形化
        if sliderName == "slider_square_image_R":
            R = widgets.slider_square_image_R.value()
            G = widgets.slider_square_image_G.value()
            B = widgets.slider_square_image_B.value()
            widgets.spinBox_square_image_R.setValue(R)
            widgets.squre_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_square_image_G":
            R = widgets.slider_square_image_R.value()
            G = widgets.slider_square_image_G.value()
            B = widgets.slider_square_image_B.value()
            widgets.spinBox_square_image_G.setValue(G)
            widgets.squre_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_square_image_B":
            R = widgets.slider_square_image_R.value()
            G = widgets.slider_square_image_G.value()
            B = widgets.slider_square_image_B.value()
            widgets.spinBox_square_image_B.setValue(B)
            widgets.squre_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        # 图像旋转
        elif sliderName == "slider_rotate_ofImage_R":
            R = widgets.slider_rotate_ofImage_R.value()
            G = widgets.slider_rotate_ofImage_G.value()
            B = widgets.slider_rotate_ofImage_B.value()
            widgets.spinBox_rotate_ofImage_R.setValue(R)
            widgets.rotate_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_rotate_ofImage_G":
            R = widgets.slider_rotate_ofImage_R.value()
            G = widgets.slider_rotate_ofImage_G.value()
            B = widgets.slider_rotate_ofImage_B.value()
            widgets.spinBox_rotate_ofImage_G.setValue(G)
            widgets.rotate_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_rotate_ofImage_B":
            R = widgets.slider_rotate_ofImage_R.value()
            G = widgets.slider_rotate_ofImage_G.value()
            B = widgets.slider_rotate_ofImage_B.value()
            widgets.spinBox_rotate_ofImage_B.setValue(B)
            widgets.rotate_showRGB_ofImage.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")


    def on_switchButton_checkedChanged_ofImage(self, isChecked: bool):
        """
        开关 的信号触发函数
        """
        switchButton = self.sender()
        switchButtonName = switchButton.objectName()
        # 图像旋转
        if switchButtonName == "switchButton_rotate_ofImage":
            if isChecked:
                widgets.frame_rotate_content_ofImage.setVisible(True)
                SI.imageAugmentAlgorithm_ofImage.append("rotate")
                SI.current_imageAugment_ofImage.append("图像旋转")
                self.show_current_algorithm_ofImage(2)
                self.print_current_algorithm_ofImage(2)
            else:
                widgets.frame_rotate_content_ofImage.setVisible(False)
                if "rotate" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("rotate")
                if "图像旋转" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("图像旋转")
                self.show_current_algorithm_ofImage(2)
                self.print_current_algorithm_ofImage(2)
        # 水平翻转
        elif switchButtonName == "switchButton_HFlip_ofImage":
            if isChecked:
                SI.imageAugmentAlgorithm_ofImage.append("HFlip")
                SI.current_imageAugment_ofImage.append("水平翻转")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
            else:
                if "HFlip" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("HFlip")
                if "水平翻转" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("水平翻转")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
        # 垂直翻转
        elif switchButtonName == "switchButton_VFlip_ofImage":
            if isChecked:
                SI.imageAugmentAlgorithm_ofImage.append("VFlip")
                SI.current_imageAugment_ofImage.append("垂直翻转")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
            else:
                if "VFlip" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("VFlip")
                if "垂直翻转" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("垂直翻转")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
        # 模糊
        elif switchButtonName == "switchButton_blur_ofImage":
            if isChecked:
                widgets.frame_blur_content_ofImage.setVisible(True)
                SI.current_imageAugment_ofImage.append("模糊")
                self.show_current_algorithm_ofImage(2)
            else:
                widgets.frame_blur_content_ofImage.setVisible(False)
                # 清空单选
                widgets.rbtn_blur_mean_ofImage.setChecked(True)
                widgets.rbtn_blur_mean_ofImage.setCheckable(False)
                widgets.rbtn_blur_mean_ofImage.setCheckable(True)
                # 清空算法选择
                if "模糊" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("模糊")
                if "blur_mean" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("blur_mean")
                if "blur_box" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("blur_box")
                if "blur_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("blur_gaussian")
                if "blur_median" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("blur_median")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
        # 噪声
        elif switchButtonName == "switchButton_noise_ofImage":
            if isChecked:
                widgets.frame_noise_content_ofImage.setVisible(True)
                SI.current_imageAugment_ofImage.append("噪声")
                self.show_current_algorithm_ofImage(2)
            else:
                widgets.frame_noise_content_ofImage.setVisible(False)
                # 清空勾选框
                widgets.cb_noise_gaussian_ofImage.setChecked(False)
                widgets.cb_noise_saltPepper_ofImage.setChecked(False)
                # 隐藏参数框
                widgets.frame_noise_gaussian_ofImage.setVisible(False)
                widgets.frame_noise_saltPepper_ofImage.setVisible(False)
                # 清空算法选择
                if "噪声" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("噪声")
                if "noise_gaussian" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("noise_gaussian")
                if "noise_saltPepper" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("noise_saltPepper")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
        # 亮度
        elif switchButtonName == "switchButton_brightness_ofImage":
            if isChecked:
                widgets.frame_brightness_content_ofImage.setVisible(True)
                SI.current_imageAugment_ofImage.append("亮度")
                SI.imageAugmentAlgorithm_ofImage.append("brightness")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
            else:
                widgets.frame_brightness_content_ofImage.setVisible(False)
                # 清空算法选择
                if "亮度" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("亮度")
                if "brightness" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("brightness")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
        # 对比度
        elif switchButtonName == "switchButton_contrast_ofImage":
            if isChecked:
                widgets.frame_contrast_content_ofImage.setVisible(True)
                SI.current_imageAugment_ofImage.append("对比度")
                SI.imageAugmentAlgorithm_ofImage.append("contrast")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)
            else:
                widgets.frame_contrast_content_ofImage.setVisible(False)
                # 清空算法选择
                if "对比度" in SI.current_imageAugment_ofImage:
                    SI.current_imageAugment_ofImage.remove("对比度")
                if "contrast" in SI.imageAugmentAlgorithm_ofImage:
                    SI.imageAugmentAlgorithm_ofImage.remove("contrast")
                self.print_current_algorithm_ofImage(2)
                self.show_current_algorithm_ofImage(2)


    def forbid_blur_ofImage(self, forbid: bool):
        """
        中值滤波下禁止/恢复第二个滤波核设置参数
        """
        # 禁止
        if forbid:
            SI.syncFlag_blur_ofImage = True
            # spinbox
            widgets.spinBox_blurKsize2_ofImage.setValue(widgets.spinBox_blurKsize1_ofImage.value())
            widgets.spinBox_blurKsize2_ofImage.setReadOnly(True)
            widgets.spinBox_blurKsize2_ofImage.setCursor(QCursor(Qt.ForbiddenCursor))
            # slider
            widgets.slider_blurKsize2_ofImage.setCursor(QCursor(Qt.ForbiddenCursor))
            widgets.spinBox_blurKsize2_ofImage.valueChanged.connect(self.sync_sliders_blur_ofImage)
        # 恢复
        else:
            SI.syncFlag_blur_ofImage = False
            # spinbox
            widgets.spinBox_blurKsize2_ofImage.setReadOnly(False)
            widgets.spinBox_blurKsize2_ofImage.setCursor(QCursor(Qt.ArrowCursor))
            # slider
            widgets.slider_blurKsize2_ofImage.setCursor(QCursor(Qt.ArrowCursor))
            widgets.spinBox_blurKsize2_ofImage.valueChanged.disconnect(self.sync_sliders_blur_ofImage)
    def sync_sliders_blur_ofImage(self):
        """
        模糊操作禁止滑块的信号
        """
        widgets.spinBox_blurKsize2_ofImage.setValue(widgets.spinBox_blurKsize1_ofImage.value())



    # ------------------------------------  ToolBox改变  ------------------------------------
    def on_toolBox_function_changed_ofImage(self, index):
        """
        外侧ToolBox ofImage
        """
        # 清除页面
        if index != 0:
            self.clear_modifySuffix_ofImage()
            self.clear_resize_ofImage()
            self.clear_square_ofImage()
            widgets.toolBox_imageAugment_image.setCurrentIndex(0)
        if index != 1:
            self.clear_switch_ofImage()
            widgets.toolBox_process_image.setCurrentIndex(0)

        # 记录算法
        if index == 0:
            SI.current_process_function_ofImage = "预处理工具"
            print("当前外侧ToolBox：", SI.current_process_function_ofImage)
        elif index == 1:
            SI.current_process_function_ofImage = "图像增强"
            print("当前外侧ToolBox：", SI.current_process_function_ofImage)

    def on_toolBox_process_changed_ofImage(self, index):
        """
        内侧ToolBox1  预处理工具  ofImage
        """
        # 清除页面
        if index != 0:
            self.clear_modifySuffix_ofImage()
        if index != 1:
            self.clear_resize_ofImage()
        if index != 2:
            self.clear_square_ofImage()

        # 记录算法
        if index == 0:
            SI.current_processTool_ofImage = "更改后缀"
            print("当前内侧ToolBox：", SI.current_processTool_ofImage)
        elif index == 1:
            SI.current_processTool_ofImage = "更改大小"
            print("当前内侧ToolBox：", SI.current_processTool_ofImage)
        elif index == 2:
            SI.current_processTool_ofImage = "图片方形化"
            print("当前内侧ToolBox：", SI.current_processTool_ofImage)



    # ------------------------------------  清除控件  ------------------------------------
    # 预处理工具页面--------------------
    def clear_modifySuffix_ofImage(self):
        """
        清除 更改后缀 页面
        """
        widgets.rb_jpg_image.setChecked(True)
        widgets.rb_jpg_image.setCheckable(False)
        widgets.rb_jpg_image.setCheckable(True)
        SI.processToolAlgorithm_ofImage = ""
        self.show_current_algorithm_ofImage(clear=True)
    def clear_square_ofImage(self):
        """
        清除 图片方形化 页面
        """
        widgets.rbtn_BORDER_CONSTANT_image.setChecked(True)
        widgets.rbtn_BORDER_CONSTANT_image.setCheckable(False)
        widgets.rbtn_BORDER_CONSTANT_image.setCheckable(True)
        widgets.frame_square_RGB_image.setVisible(False)
        SI.processToolAlgorithm_ofImage = ""
        self.show_current_algorithm_ofImage(clear=True)
    def clear_resize_ofImage(self):
        """
        清除 更改大小 页面
        """
        # 清空输入框
        widgets.lineEdit_resizepx1_ofImage.setText(None)
        widgets.lineEdit_resizepx2_ofImage.setText(None)
        # 清空单选
        widgets.rbtn_INTER_LINEAR_ofImage.setChecked(True)
        widgets.rbtn_INTER_LINEAR_ofImage.setCheckable(False)
        widgets.rbtn_INTER_LINEAR_ofImage.setCheckable(True)
        SI.processToolAlgorithm_ofImage = ""
        self.show_current_algorithm_ofImage(clear=True)
    # 图像增强页面--------------------
    def clear_switch_ofImage(self):
        """
        关闭所有开关
        """
        SI.imageAugmentAlgorithm_ofImage = []
        widgets.switchButton_rotate_ofImage.setChecked(False)
        widgets.switchButton_HFlip_ofImage.setChecked(False)
        widgets.switchButton_VFlip_ofImage.setChecked(False)
        widgets.switchButton_blur_ofImage.setChecked(False)
        widgets.switchButton_noise_ofImage.setChecked(False)
        widgets.switchButton_brightness_ofImage.setChecked(False)
        widgets.switchButton_contrast_ofImage.setChecked(False)
        self.show_current_algorithm_ofImage(clear=True)

    # ------------------------------------  打印当前算法  ------------------------------------
    def print_current_algorithm_ofImage(self, mode: int):
        """
        打印当前算法
        :param mode: 1表示预处理工具部分，2表示图像增强部分
        """
        if mode == 1:
            print("当前为预处理工具算法：", SI.processToolAlgorithm_ofImage)
        elif mode == 2:
            print("当前为图像增强算法：", SI.imageAugmentAlgorithm_ofImage)

    def show_current_algorithm_ofImage(self, mode=0, text="", clear=False):
        """
        展示当前选择的功能
        :param mode: 1表示预处理工具，2表示图像增强
        :param text: 展示的内容
        :param clear: 是否清除
        """
        if clear:
            self.ui.show_algorithm_ofImage.clear()
        else:
            if mode == 1:
                self.ui.show_algorithm_ofImage.setText("当前选择的功能：预处理工具\n当前算法：" + text)
            elif mode == 2:
                algorithms = " --> ".join(SI.current_imageAugment_ofImage[:])
                self.ui.show_algorithm_ofImage.setText("当前选择的功能：图像增强\n依次执行的算法顺序：" + algorithms)


    # ***************************************************************************************************************
    # ******************************************       数据集处理函数     *********************************************
    # ***************************************************************************************************************
    def reviewAlgorithm_ofDataset(self):
        """
        预览按钮点击
        """
        if (not SI.functionMutex) and (not SI.threadMutex):
            try:
                SI.functionMutex = True
                if SI.dataset_path == "":
                    errorBox(self, "错误", "请先导入数据集")
                else:
                    # 预处理工具
                    if SI.current_process_function_ofDataset == "预处理工具":
                        AppFunctions.processAlgorithm_review_ofDataset(self)
                    # 图像增强
                    elif SI.current_process_function_ofDataset == "图像增强":
                        AppFunctions.imageAugment_review_ofDataset(self)
                    else:
                        errorBox(self, "错误", "未选择算法")
            except Exception as e:
                errorBox(self, "错误", "预览失败")
                print("《预览数据集预处理》时错误:", e)
            finally:
                SI.functionMutex = False
        else:
            warningBox(self, "警告", "其它功能正在执行")


    def runAlgorithm_ofDataset(self):
        """
        运行按钮点击
        """
        if (not SI.functionMutex) and (not SI.threadMutex):
            try:
                SI.functionMutex = True
                if SI.dataset_path == "":
                    errorBox(self, "错误", "请先导入数据集")
                else:
                    # 预处理工具
                    if SI.current_process_function_ofDataset == "预处理工具":
                        AppFunctions.processAlgorithm_run_ofDataset(self)
                    # 图像增强
                    elif SI.current_process_function_ofDataset == "图像增强":
                        AppFunctions.imageAugment_run_ofDataset(self)
                    else:
                        errorBox(self, "错误", "未选择算法")
            except Exception as e:
                errorBox(self, "错误", "运行失败")
                print("《运行数据集预处理》时错误:", e)
            finally:
                SI.functionMutex = False
        else:
            warningBox(self, "警告", "其它功能正在执行")



    # ------------------------------------  信号触发  ------------------------------------
    def on_button_clicked_ofDataset(self):
        """
        按钮 的信号触发函数
        """
        btn = self.sender()
        btnName = btn.objectName()
        # 目录
        if btnName == "btn_importDataset":
            AppFunctions.importDataset(self)
        elif btnName == "btn_exportResult_dataset":
            AppFunctions.exportResult(self)
        # 统一后缀
        elif btnName == "btn_jpg_ofDataset":
            widgets.rb_jpg_ofDataset.setChecked(True)
            SI.processToolAlgorithm_ofDataset = "modifySuffix_jpg"
            self.show_current_algorithm_ofDataset(1, "更改后缀 --> jpg")
            self.print_current_algorithm_ofDataset(1)
        elif btnName == "btn_jpeg_ofDataset":
            widgets.rb_jpeg_ofDataset.setChecked(True)
            SI.processToolAlgorithm_ofDataset = "modifySuffix_jpeg"
            self.show_current_algorithm_ofDataset(1, "更改后缀 --> jpeg")
            self.print_current_algorithm_ofDataset(1)
        elif btnName == "btn_png_ofDataset":
            widgets.rb_png_ofDataset.setChecked(True)
            SI.processToolAlgorithm_ofDataset = "modifySuffix_png"
            self.show_current_algorithm_ofDataset(1, "更改后缀 --> png")
            self.print_current_algorithm_ofDataset(1)
        elif btnName == "btn_bmp_ofDataset":
            widgets.rb_bmp_ofDataset.setChecked(True)
            SI.processToolAlgorithm_ofDataset = "modifySuffix_bmp"
            self.show_current_algorithm_ofDataset(1, "更改后缀 --> bmp")
            self.print_current_algorithm_ofDataset(1)



    def on_radioButton_clicked_ofDataset(self):
        """
        单选按钮 的信号触发函数
        """
        rb = self.sender()
        rbName = rb.objectName()
        # 预处理工具------------------------
        # 更改后缀
        if rbName == "rb_jpg_ofDataset":
            if widgets.rb_jpg_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "modifySuffix_jpg"
                self.show_current_algorithm_ofDataset(1, "统一后缀 --> jpg")
                self.print_current_algorithm_ofDataset(1)
        elif rbName == "rb_jpeg_ofDataset":
            if widgets.rb_jpeg_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "modifySuffix_jpeg"
                self.show_current_algorithm_ofDataset(1, "统一后缀 --> jpeg")
                self.print_current_algorithm_ofDataset(1)
        elif rbName == "rb_png_ofDataset":
            if widgets.rb_png_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "modifySuffix_png"
                self.show_current_algorithm_ofDataset(1, "统一后缀 --> png")
                self.print_current_algorithm_ofDataset(1)
        elif rbName == "rb_bmp_ofDataset":
            if widgets.rb_bmp_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "modifySuffix_bmp"
                self.show_current_algorithm_ofDataset(1, "统一后缀 --> bmp")
                self.print_current_algorithm_ofDataset(1)
        # 统一命名
        elif rbName == "rbtn_rename1_ofDataset":
            if widgets.rbtn_rename1_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "uniformName_i"
                self.show_current_algorithm_ofDataset(1, "统一命名 --> 分类_i")
                self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_rename2_ofDataset":
            if widgets.rbtn_rename2_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "uniformNamei"
                self.show_current_algorithm_ofDataset(1, "统一命名 --> 分类i")
                self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_rename3_ofDataset":
            if widgets.rbtn_rename3_ofDataset.isChecked():
                SI.processToolAlgorithm_ofDataset = "uniformName-i"
                self.show_current_algorithm_ofDataset(1, "统一命名 --> 分类-i")
                self.print_current_algorithm_ofDataset(1)
        # 图片方形化
        elif rbName == "rbtn_BORDER_CONSTANT_ofDataset":
            widgets.frame_square_RGB_ofDataset.setVisible(True)
            SI.processToolAlgorithm_ofDataset = "square_BORDER_CONSTANT"
            self.show_current_algorithm_ofDataset(1, "图片方形化 --> BORDER_CONSTANT")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_BORDER_REFLECT_ofDataset":
            widgets.frame_square_RGB_ofDataset.setVisible(False)
            SI.processToolAlgorithm_ofDataset = "square_BORDER_REFLECT"
            self.show_current_algorithm_ofDataset(1, "图片方形化 --> BORDER_REFLECT")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_BORDER_REPLICATE_ofDataset":
            widgets.frame_square_RGB_ofDataset.setVisible(False)
            SI.processToolAlgorithm_ofDataset = "square_BORDER_REPLICATE"
            self.show_current_algorithm_ofDataset(1, "图片方形化 --> BORDER_REPLICATE")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_BORDER_WRAP_ofDataset":
            widgets.frame_square_RGB_ofDataset.setVisible(False)
            SI.processToolAlgorithm_ofDataset = "square_BORDER_WRAP"
            self.show_current_algorithm_ofDataset(1, "图片方形化 --> BORDER_WRAP")
            self.print_current_algorithm_ofDataset(1)
        # 统一大小
        elif rbName == "rbtn_INTER_LINEAR_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_LINEAR"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_LINEAR")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_INTER_NEAREST_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_NEAREST"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_NEAREST")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_INTER_CUBIC_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_CUBIC"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_CUBIC")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_INTER_AREA_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_AREA"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_AREA")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_INTER_LANCZOS4_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_LANCZOS4"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_LANCZOS4")
            self.print_current_algorithm_ofDataset(1)
        elif rbName == "rbtn_INTER_LINEAR_EXACT_ofDataset":
            SI.processToolAlgorithm_ofDataset = "resize_INTER_LINEAR_EXACT"
            self.show_current_algorithm_ofDataset(1, "统一大小 --> INTER_LINEAR_EXACT")
            self.print_current_algorithm_ofDataset(1)
        # 模糊
        elif rbName == "rbtn_blur_mean_ofDataset":
            if "blur_mean" not in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.append("blur_mean")
            if "blur_box" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_box")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_gaussian")
            if "blur_median" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_median")
            self.print_current_algorithm_ofDataset(2)
        elif rbName == "rbtn_blur_box_ofDataset":
            if "blur_box" not in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.append("blur_box")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_mean")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_gaussian")
            if "blur_median" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_median")
            self.print_current_algorithm_ofDataset(2)
        elif rbName == "rbtn_blur_gaussian_ofDataset":
            if "blur_gaussian" not in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.append("blur_gaussian")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_mean")
            if "blur_box" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_box")
            if "blur_median" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_median")
            self.print_current_algorithm_ofDataset(2)
        elif rbName == "rbtn_blur_median_ofDataset":
            if "blur_median" not in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.append("blur_median")
            if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_mean")
            if "blur_box" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_box")
            if "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                SI.imageAugmentAlgorithm_ofDataset.remove("blur_gaussian")
            self.print_current_algorithm_ofDataset(2)







    def on_checkBox_clicked_ofDataset(self):
        """
        勾选框 的信号触发激活函数
        """
        checkBox = self.sender()
        checkBoxName = checkBox.objectName()
        # 统一命名
        if checkBoxName == "cb_rename0_ofDataset":
            if checkBox.isChecked():
                SI.flag_rename0 = True
            else:
                SI.flag_rename0 = False
        # 噪声
        elif checkBoxName == "cb_noise_gaussian_ofDataset":
            if checkBox.isChecked():
                widgets.frame_noise_gaussian_ofDataset.setVisible(True)
                if "noise_gaussian" not in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.append("noise_gaussian")
            else:
                widgets.frame_noise_gaussian_ofDataset.setVisible(False)
                if "noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("noise_gaussian")
            self.print_current_algorithm_ofDataset(2)
        elif checkBoxName == "cb_noise_saltPepper_ofDataset":
            if checkBox.isChecked():
                widgets.frame_noise_saltPepper_ofDataset.setVisible(True)
                if "noise_saltPepper" not in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.append("noise_saltPepper")
            else:
                widgets.frame_noise_saltPepper_ofDataset.setVisible(False)
                if "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("noise_saltPepper")
            self.print_current_algorithm_ofDataset(2)



    def on_spinBox_valueChanged_ofDataset(self):
        """
        旋转框 的信号触发激活函数
        """
        sb = self.sender()
        sbName = sb.objectName()
        ### 图像旋转----------
        # 旋转范围
        if sbName == "dSpinBox_rotateDegree1_ofDataset":
            value1 = widgets.dSpinBox_rotateDegree1_ofDataset.value()
            widgets.dSpinBox_rotateDegree2_ofDataset.setMinimum(value1)
            widgets.slider_rotateDegree1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_rotateDegree2_ofDataset":
            value2 = widgets.dSpinBox_rotateDegree2_ofDataset.value()
            widgets.dSpinBox_rotateDegree1_ofDataset.setMaximum(value2)
            widgets.slider_rotateDegree2_ofDataset.setValue(value2 * 100)
        # 缩放范围
        elif sbName == "dSpinBox_rotateScale1_ofDataset":
            value1 = widgets.dSpinBox_rotateScale1_ofDataset.value()
            widgets.dSpinBox_rotateScale2_ofDataset.setMinimum(value1)
            widgets.slider_rotateScale1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_rotateScale2_ofDataset":
            value2 = widgets.dSpinBox_rotateScale2_ofDataset.value()
            widgets.dSpinBox_rotateScale1_ofDataset.setMaximum(value2)
            widgets.slider_rotateScale2_ofDataset.setValue(value2 * 100)
        ### 模糊----------
        # From
        elif sbName == "spinBox_blurKsize_from1_ofDataset":
            value_from = widgets.spinBox_blurKsize_from1_ofDataset.value()
            widgets.spinBox_blurKsize_from2_ofDataset.setValue(value_from)
            widgets.slider_blurKsize_from_ofDataset.setValue(value_from)
            widgets.spinBox_blurKsize_to1_ofDataset.setMinimum(value_from)
            widgets.spinBox_blurKsize_to2_ofDataset.setMinimum(value_from)
        elif sbName == "spinBox_blurKsize_from2_ofDataset":
            value_from = widgets.spinBox_blurKsize_from2_ofDataset.value()
            widgets.spinBox_blurKsize_from1_ofDataset.setValue(value_from)
            widgets.slider_blurKsize_from_ofDataset.setValue(value_from)
            widgets.spinBox_blurKsize_to1_ofDataset.setMinimum(value_from)
            widgets.spinBox_blurKsize_to2_ofDataset.setMinimum(value_from)
        # To
        elif sbName == "spinBox_blurKsize_to1_ofDataset":
            value_to = widgets.spinBox_blurKsize_to1_ofDataset.value()
            widgets.spinBox_blurKsize_to2_ofDataset.setValue(value_to)
            widgets.slider_blurKsize_to_ofDataset.setValue(value_to)
            widgets.spinBox_blurKsize_from1_ofDataset.setMaximum(value_to)
            widgets.spinBox_blurKsize_from2_ofDataset.setMaximum(value_to)
        elif sbName == "spinBox_blurKsize_to2_ofDataset":
            value_to = widgets.spinBox_blurKsize_to2_ofDataset.value()
            widgets.spinBox_blurKsize_to1_ofDataset.setValue(value_to)
            widgets.slider_blurKsize_to_ofDataset.setValue(value_to)
            widgets.spinBox_blurKsize_from1_ofDataset.setMaximum(value_to)
            widgets.spinBox_blurKsize_from2_ofDataset.setMaximum(value_to)
        ### 模糊----------
        # sigma
        elif sbName == "dSpinBox_noise_sigma1_ofDataset":
            value1 = widgets.dSpinBox_noise_sigma1_ofDataset.value()
            widgets.dSpinBox_noise_sigma2_ofDataset.setMinimum(value1)
            widgets.slider_noise_sigma1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_noise_sigma2_ofDataset":
            value2 = widgets.dSpinBox_noise_sigma2_ofDataset.value()
            widgets.dSpinBox_noise_sigma1_ofDataset.setMaximum(value2)
            widgets.slider_noise_sigma2_ofDataset.setValue(value2 * 100)
        # rate
        elif sbName == "dSpinBox_noise_rate1_ofDataset":
            value1 = widgets.dSpinBox_noise_rate1_ofDataset.value()
            widgets.dSpinBox_noise_rate2_ofDataset.setMinimum(value1)
            widgets.slider_noise_rate1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_noise_rate2_ofDataset":
            value2 = widgets.dSpinBox_noise_rate2_ofDataset.value()
            widgets.dSpinBox_noise_rate1_ofDataset.setMaximum(value2)
            widgets.slider_noise_rate2_ofDataset.setValue(value2 * 100)
        ### 亮度----------
        # beta
        elif sbName == "dSpinBox_brightness_beta1_ofDataset":
            value1 = widgets.dSpinBox_brightness_beta1_ofDataset.value()
            widgets.dSpinBox_brightness_beta2_ofDataset.setMinimum(value1)
            widgets.slider_brightness_beta1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_brightness_beta2_ofDataset":
            value2 = widgets.dSpinBox_brightness_beta2_ofDataset.value()
            widgets.dSpinBox_brightness_beta1_ofDataset.setMaximum(value2)
            widgets.slider_brightness_beta2_ofDataset.setValue(value2 * 100)
        ### 对比度----------
        # alpha
        elif sbName == "dSpinBox_contrast_alpha1_ofDataset":
            value1 = widgets.dSpinBox_contrast_alpha1_ofDataset.value()
            widgets.dSpinBox_contrast_alpha2_ofDataset.setMinimum(value1)
            widgets.slider_contrast_alpha1_ofDataset.setValue(value1 * 100)
        elif sbName == "dSpinBox_contrast_alpha2_ofDataset":
            value2 = widgets.dSpinBox_contrast_alpha2_ofDataset.value()
            widgets.dSpinBox_contrast_alpha1_ofDataset.setMaximum(value2)
            widgets.slider_contrast_alpha2_ofDataset.setValue(value2 * 100)



    def on_slider_valueChanged_ofDataset(self):
        """
        滑条 的信号触发激活函数
        """
        slider = self.sender()
        sliderName = slider.objectName()
        ### 图片方形化----------
        if sliderName == "slider_square_ofDataset_R":
            R = widgets.slider_square_ofDataset_R.value()
            G = widgets.slider_square_ofDataset_G.value()
            B = widgets.slider_square_ofDataset_B.value()
            widgets.spinBox_square_ofDataset_R.setValue(R)
            widgets.squre_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_square_ofDataset_G":
            R = widgets.slider_square_ofDataset_R.value()
            G = widgets.slider_square_ofDataset_G.value()
            B = widgets.slider_square_ofDataset_B.value()
            widgets.spinBox_square_ofDataset_G.setValue(G)
            widgets.squre_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_square_ofDataset_B":
            R = widgets.slider_square_ofDataset_R.value()
            G = widgets.slider_square_ofDataset_G.value()
            B = widgets.slider_square_ofDataset_B.value()
            widgets.spinBox_square_ofDataset_B.setValue(B)
            widgets.squre_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        ### 图像旋转----------
        # 旋转范围
        elif sliderName == "slider_rotateDegree1_ofDataset":
            value1 = widgets.slider_rotateDegree1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_rotateDegree2_ofDataset.value()
            if value1 > value2:
                widgets.slider_rotateDegree1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_rotateDegree1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_rotateDegree1_ofDataset.setValue(value1)
        elif sliderName == "slider_rotateDegree2_ofDataset":
            value1 = widgets.dSpinBox_rotateDegree1_ofDataset.value()
            value2 = widgets.slider_rotateDegree2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_rotateDegree2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_rotateDegree2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_rotateDegree2_ofDataset.setValue(value2)
        # 缩放范围
        elif sliderName == "slider_rotateScale1_ofDataset":
            value1 = widgets.slider_rotateScale1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_rotateScale2_ofDataset.value()
            if value1 > value2:
                widgets.slider_rotateScale1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_rotateScale1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_rotateScale1_ofDataset.setValue(value1)
        elif sliderName == "slider_rotateScale2_ofDataset":
            value1 = widgets.dSpinBox_rotateScale1_ofDataset.value()
            value2 = widgets.slider_rotateScale2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_rotateScale2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_rotateScale2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_rotateScale2_ofDataset.setValue(value2)
        # RGB
        elif sliderName == "slider_rotate_ofDataset_R":
            R = widgets.slider_rotate_ofDataset_R.value()
            G = widgets.slider_rotate_ofDataset_G.value()
            B = widgets.slider_rotate_ofDataset_B.value()
            widgets.spinBox_rotate_ofDataset_R.setValue(R)
            widgets.rotate_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_rotate_ofDataset_G":
            R = widgets.slider_rotate_ofDataset_R.value()
            G = widgets.slider_rotate_ofDataset_G.value()
            B = widgets.slider_rotate_ofDataset_B.value()
            widgets.spinBox_rotate_ofDataset_G.setValue(G)
            widgets.rotate_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        elif sliderName == "slider_rotate_ofDataset_B":
            R = widgets.slider_rotate_ofDataset_R.value()
            G = widgets.slider_rotate_ofDataset_G.value()
            B = widgets.slider_rotate_ofDataset_B.value()
            widgets.spinBox_rotate_ofDataset_B.setValue(B)
            widgets.rotate_showRGB_ofDataset.setStyleSheet(f"background-color: rgb({R}, {G}, {B});")
        ### 模糊----------
        # From
        elif sliderName == "slider_blurKsize_from_ofDataset":
            value_from = widgets.slider_blurKsize_from_ofDataset.value()
            value_to = widgets.slider_blurKsize_to_ofDataset.value()
            if value_from <= value_to:
                widgets.spinBox_blurKsize_from1_ofDataset.setValue(value_from)
                widgets.spinBox_blurKsize_from2_ofDataset.setValue(value_from)
            else:
                widgets.slider_blurKsize_from_ofDataset.setValue(value_to)
                widgets.spinBox_blurKsize_from1_ofDataset.setValue(value_to)
                widgets.spinBox_blurKsize_from2_ofDataset.setValue(value_to)
        # To
        elif sliderName == "slider_blurKsize_to_ofDataset":
            value_from = widgets.slider_blurKsize_from_ofDataset.value()
            value_to = widgets.slider_blurKsize_to_ofDataset.value()
            if value_to >= value_from:
                widgets.spinBox_blurKsize_to1_ofDataset.setValue(value_to)
                widgets.spinBox_blurKsize_to2_ofDataset.setValue(value_to)
            else:
                widgets.slider_blurKsize_to_ofDataset.setValue(value_from)
                widgets.spinBox_blurKsize_to1_ofDataset.setValue(value_from)
                widgets.spinBox_blurKsize_to2_ofDataset.setValue(value_from)
        ### 噪声----------
        # sigma
        elif sliderName == "slider_noise_sigma1_ofDataset":
            value1 = widgets.slider_noise_sigma1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_noise_sigma2_ofDataset.value()
            if value1 > value2:
                widgets.slider_noise_sigma1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_noise_sigma1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_noise_sigma1_ofDataset.setValue(value1)
        elif sliderName == "slider_noise_sigma2_ofDataset":
            value1 = widgets.dSpinBox_noise_sigma1_ofDataset.value()
            value2 = widgets.slider_noise_sigma2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_noise_sigma2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_noise_sigma2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_noise_sigma2_ofDataset.setValue(value2)
        # rate
        elif sliderName == "slider_noise_rate1_ofDataset":
            value1 = widgets.slider_noise_rate1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_noise_rate2_ofDataset.value()
            if value1 > value2:
                widgets.slider_noise_rate1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_noise_rate1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_noise_rate1_ofDataset.setValue(value1)
        elif sliderName == "slider_noise_rate2_ofDataset":
            value1 = widgets.dSpinBox_noise_rate1_ofDataset.value()
            value2 = widgets.slider_noise_rate2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_noise_rate2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_noise_rate2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_noise_rate2_ofDataset.setValue(value2)
        ### 亮度----------
        # beta
        elif sliderName == "slider_brightness_beta1_ofDataset":
            value1 = widgets.slider_brightness_beta1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_brightness_beta2_ofDataset.value()
            if value1 > value2:
                widgets.slider_brightness_beta1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_brightness_beta1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_brightness_beta1_ofDataset.setValue(value1)
        elif sliderName == "slider_brightness_beta2_ofDataset":
            value1 = widgets.dSpinBox_brightness_beta1_ofDataset.value()
            value2 = widgets.slider_brightness_beta2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_brightness_beta2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_brightness_beta2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_brightness_beta2_ofDataset.setValue(value2)
        ### 对比度----------
        # alpha
        elif sliderName == "slider_contrast_alpha1_ofDataset":
            value1 = widgets.slider_contrast_alpha1_ofDataset.value() / 100
            value2 = widgets.dSpinBox_contrast_alpha2_ofDataset.value()
            if value1 > value2:
                widgets.slider_contrast_alpha1_ofDataset.setValue(value2 * 100)
                widgets.dSpinBox_contrast_alpha1_ofDataset.setValue(value2)
            else:
                widgets.dSpinBox_contrast_alpha1_ofDataset.setValue(value1)
        elif sliderName == "slider_contrast_alpha2_ofDataset":
            value1 = widgets.dSpinBox_contrast_alpha1_ofDataset.value()
            value2 = widgets.slider_contrast_alpha2_ofDataset.value() / 100
            if value2 < value1:
                widgets.slider_contrast_alpha2_ofDataset.setValue(value1 * 100)
                widgets.dSpinBox_contrast_alpha2_ofDataset.setValue(value1)
            else:
                widgets.dSpinBox_contrast_alpha2_ofDataset.setValue(value2)





    def on_switchButton_checkedChanged_ofDataset(self, isChecked: bool):
        """
        开关 的信号触发函数
        """
        switchButton = self.sender()
        switchButtonName = switchButton.objectName()
        # 图像旋转
        if switchButtonName == "switchButton_rotate_ofDataset":
            if isChecked:
                widgets.frame_rotate_content_ofDataset.setVisible(True)
                SI.imageAugmentAlgorithm_ofDataset.append("rotate")
                SI.current_imageAugment_ofDataset.append("图像旋转")
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
            else:
                widgets.frame_rotate_content_ofDataset.setVisible(False)
                # 清除算法
                if "rotate" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("rotate")
                if "图像旋转" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("图像旋转")
                # 清除参数
                SI.param_rotate_ofDataset_probability = None
                SI.param_rotate_ofDataset_degree1 = None
                SI.param_rotate_ofDataset_degree2 = None
                SI.param_rotate_ofDataset_scale1 = None
                SI.param_rotate_ofDataset_scale2 = None
                SI.param_rotate_ofDataset_fillColor = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 水平翻转
        elif switchButtonName == "switchButton_HFlip_ofDataset":
            if isChecked:
                widgets.frame_HFlip_content_ofDataset.setVisible(True)
                SI.imageAugmentAlgorithm_ofDataset.append("HFlip")
                SI.current_imageAugment_ofDataset.append("水平翻转")
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
            else:
                widgets.frame_HFlip_content_ofDataset.setVisible(False)
                # 清除算法
                if "HFlip" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("HFlip")
                if "水平翻转" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("水平翻转")
                # 清除参数
                SI.param_HFlip_ofDataset_probability = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 垂直翻转
        elif switchButtonName == "switchButton_VFlip_ofDataset":
            if isChecked:
                widgets.frame_VFlip_content_ofDataset.setVisible(True)
                SI.imageAugmentAlgorithm_ofDataset.append("VFlip")
                SI.current_imageAugment_ofDataset.append("垂直翻转")
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
            else:
                widgets.frame_VFlip_content_ofDataset.setVisible(False)
                # 清除算法
                if "VFlip" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("VFlip")
                if "垂直翻转" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("垂直翻转")
                # 清除参数
                SI.param_VFlip_ofDataset_probability = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 模糊
        elif switchButtonName == "switchButton_blur_ofDataset":
            if isChecked:
                widgets.frame_blur_content_ofDataset.setVisible(True)
                SI.current_imageAugment_ofDataset.append("模糊")
                self.show_current_algorithm_ofDataset(2)
            else:
                widgets.frame_blur_content_ofDataset.setVisible(False)
                # 清空单选
                widgets.rbtn_blur_mean_ofDataset.setChecked(True)
                widgets.rbtn_blur_mean_ofDataset.setCheckable(False)
                widgets.rbtn_blur_mean_ofDataset.setCheckable(True)
                # 清除算法
                if "模糊" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("模糊")
                if "blur_mean" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("blur_mean")
                if "blur_box" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("blur_box")
                if "blur_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("blur_gaussian")
                if "blur_median" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("blur_median")
                # 清除参数
                SI.param_blur_ofDataset_probability = None
                SI.param_blur_ofDataset_filter = None
                SI.param_blur_ofDataset_ksizeFrom = None
                SI.param_blur_ofDataset_ksizeTo = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 噪声
        elif switchButtonName == "switchButton_noise_ofDataset":
            if isChecked:
                widgets.frame_noise_content_ofDataset.setVisible(True)
                SI.current_imageAugment_ofDataset.append("噪声")
                self.show_current_algorithm_ofDataset(2)
            else:
                widgets.frame_noise_content_ofDataset.setVisible(False)
                # 清空勾选框
                widgets.cb_noise_gaussian_ofDataset.setChecked(False)
                widgets.cb_noise_saltPepper_ofDataset.setChecked(False)
                # 隐藏参数框
                widgets.frame_noise_gaussian_ofDataset.setVisible(False)
                widgets.frame_noise_saltPepper_ofDataset.setVisible(False)
                # 清除算法
                if "噪声" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("噪声")
                if "noise_gaussian" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("noise_gaussian")
                if "noise_saltPepper" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("noise_saltPepper")
                # 清除参数
                SI.param_noise_ofDataset_probability = None
                SI.param_noise_ofDataset_sigma1 = None
                SI.param_noise_ofDataset_sigma2 = None
                SI.param_noise_ofDataset_rate1 = None
                SI.param_noise_ofDataset_rate2 = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 亮度
        elif switchButtonName == "switchButton_brightness_ofDataset":
            if isChecked:
                widgets.frame_brightness_content_ofDataset.setVisible(True)
                SI.imageAugmentAlgorithm_ofDataset.append("brightness")
                SI.current_imageAugment_ofDataset.append("亮度")
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
            else:
                widgets.frame_brightness_content_ofDataset.setVisible(False)
                # 清除算法
                if "brightness" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("brightness")
                if "亮度" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("亮度")
                # 清除参数
                SI.param_brightness_ofDataset_probability = None
                SI.param_brightness_ofDataset_beta1 = None
                SI.param_brightness_ofDataset_beta2 = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
        # 对比度
        elif switchButtonName == "switchButton_contrast_ofDataset":
            if isChecked:
                widgets.frame_contrast_content_ofDataset.setVisible(True)
                SI.imageAugmentAlgorithm_ofDataset.append("contrast")
                SI.current_imageAugment_ofDataset.append("对比度")
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)
            else:
                widgets.frame_contrast_content_ofDataset.setVisible(False)
                # 清除算法
                if "contrast" in SI.imageAugmentAlgorithm_ofDataset:
                    SI.imageAugmentAlgorithm_ofDataset.remove("contrast")
                if "对比度" in SI.current_imageAugment_ofDataset:
                    SI.current_imageAugment_ofDataset.remove("对比度")
                # 清除参数
                SI.param_contrast_ofDataset_probability = None
                SI.param_contrast_ofDataset_alpha1 = None
                SI.param_contrast_ofDataset_alpha2 = None
                # 打印展示
                self.show_current_algorithm_ofDataset(2)
                self.print_current_algorithm_ofDataset(2)


    # ------------------------------------  ToolBox改变  ------------------------------------
    def on_toolBox_function_changed_ofDataset(self, index):
        """
        外侧ToolBox ofImage
        """
        # 清除页面
        if index != 0:
            self.clear_modifySuffix_ofDataset()
            self.clear_uniformName_ofDataset()
            self.clear_resize_ofDataset()
            self.clear_square_ofDataset()
            widgets.toolBox_imageAugment_dataset.setCurrentIndex(0)
        if index != 1:
            self.clear_switch_ofDataset()
            widgets.toolBox_process_dataset.setCurrentIndex(0)

        # 记录算法
        if index == 0:
            SI.current_process_function_ofDataset = "预处理工具"
            print("当前外侧ToolBox：", SI.current_process_function_ofDataset)
        elif index == 1:
            SI.current_process_function_ofDataset = "图像增强"
            print("当前外侧ToolBox：", SI.current_process_function_ofDataset)

    def on_toolBox_process_changed_ofDataset(self, index):
        """
        内侧ToolBox1  预处理工具  ofImage
        """
        # 清除页面
        if index != 0:
            self.clear_modifySuffix_ofDataset()
        if index != 1:
            self.clear_uniformName_ofDataset()
        if index != 2:
            self.clear_resize_ofDataset()
        if index != 3:
            self.clear_square_ofDataset()
        if index != 4:
            self.clear_split_ofDataset()

        # 记录算法
        if index == 0:
            SI.current_processTool_ofDataset = "统一后缀"
            print("当前内侧ToolBox：", SI.current_processTool_ofDataset)
        elif index == 1:
            SI.current_processTool_ofDataset = "统一命名"
            print("当前内侧ToolBox：", SI.current_processTool_ofDataset)
        elif index == 2:
            SI.current_processTool_ofDataset = "统一大小"
            print("当前内侧ToolBox：", SI.current_processTool_ofDataset)
        elif index == 3:
            SI.current_processTool_ofDataset = "图片方形化"
            print("当前内侧ToolBox：", SI.current_processTool_ofDataset)
        elif index == 4:
            SI.current_processTool_ofDataset = "数据集分割"
            self.show_current_algorithm_ofDataset(1, "数据集分割")
            print("当前内侧ToolBox：", SI.current_processTool_ofDataset)

    # ------------------------------------  清除控件  ------------------------------------
    # 预处理工具页面--------------------
    def clear_modifySuffix_ofDataset(self):
        """
        清除 统一后缀 页面
        """
        widgets.rb_jpg_ofDataset.setChecked(True)
        widgets.rb_jpg_ofDataset.setCheckable(False)
        widgets.rb_jpg_ofDataset.setCheckable(True)
        SI.processToolAlgorithm_ofDataset = ""
        self.show_current_algorithm_ofDataset(clear=True)

    def clear_uniformName_ofDataset(self):
        """
        清除 统一命名 页面
        """
        widgets.rbtn_rename1_ofDataset.setChecked(True)
        widgets.rbtn_rename1_ofDataset.setCheckable(False)
        widgets.rbtn_rename1_ofDataset.setCheckable(True)
        SI.processToolAlgorithm_ofDataset = ""
        self.show_current_algorithm_ofDataset(clear=True)

    def clear_square_ofDataset(self):
        """
        清除 图片方形化 页面
        """
        widgets.rbtn_BORDER_CONSTANT_ofDataset.setChecked(True)
        widgets.rbtn_BORDER_CONSTANT_ofDataset.setCheckable(False)
        widgets.rbtn_BORDER_CONSTANT_ofDataset.setCheckable(True)
        widgets.frame_square_RGB_ofDataset.setVisible(False)
        SI.processToolAlgorithm_ofDataset = ""
        SI.param_square_ofDataset_borderType = ""
        SI.param_square_ofDataset_fillColor = None
        self.show_current_algorithm_ofDataset(clear=True)

    def clear_resize_ofDataset(self):
        """
        清除 统一大小 页面
        """
        # 清空输入框
        widgets.lineEdit_resizepx1_ofDataset.setText(None)
        widgets.lineEdit_resizepx2_ofDataset.setText(None)
        # 清空单选
        widgets.rbtn_INTER_LINEAR_ofDataset.setChecked(True)
        widgets.rbtn_INTER_LINEAR_ofDataset.setCheckable(False)
        widgets.rbtn_INTER_LINEAR_ofDataset.setCheckable(True)
        SI.processToolAlgorithm_ofDataset = ""
        SI.param_resize_ofDataset_dsize = None
        SI.param_resize_ofDataset_interpolation = ""
        self.show_current_algorithm_ofImage(clear=True)

    def clear_split_ofDataset(self):
        """
        清除 数据集分割 页面
        """
        SI.processToolAlgorithm_ofDataset = ""
        SI.param_split_ofDataset_train = None
        SI.param_split_ofDataset_val = None
        SI.param_split_ofDataset_test = None
        SI.train_path_ofDataset = None
        SI.val_path_ofDataset = None
        SI.test_path_ofDataset = None
        self.show_current_algorithm_ofDataset(clear=True)

    # 图像增强页面--------------------
    def clear_switch_ofDataset(self):
        """
        关闭所有开关
        """
        SI.imageAugmentAlgorithm_ofDataset = []
        widgets.switchButton_rotate_ofDataset.setChecked(False)
        widgets.switchButton_HFlip_ofDataset.setChecked(False)
        widgets.switchButton_VFlip_ofDataset.setChecked(False)
        widgets.switchButton_blur_ofDataset.setChecked(False)
        widgets.switchButton_noise_ofDataset.setChecked(False)
        widgets.switchButton_brightness_ofDataset.setChecked(False)
        widgets.switchButton_contrast_ofDataset.setChecked(False)
        self.show_current_algorithm_ofDataset(clear=True)

    # ------------------------------------  打印当前算法  ------------------------------------
    def print_current_algorithm_ofDataset(self, mode: int):
        """
        打印当前算法
        :param mode: 1表示预处理工具部分，2表示图像增强部分
        """
        if mode == 1:
            print("当前为预处理工具算法：", SI.processToolAlgorithm_ofDataset)
        elif mode == 2:
            print("当前为图像增强算法：", SI.imageAugmentAlgorithm_ofDataset)

    def show_current_algorithm_ofDataset(self, mode=0, text="", clear=False):
        """
        展示当前选择的功能
        :param mode: 1表示预处理工具，2表示图像增强
        :param text: 展示的内容
        :param clear: 是否清除
        """
        if clear:
            self.ui.show_algorithm_ofDataset.clear()
        else:
            if mode == 1:
                self.ui.show_algorithm_ofDataset.setText("当前选择的功能：预处理工具\n当前算法：" + text)
            elif mode == 2:
                algorithms = " --> ".join(SI.current_imageAugment_ofDataset[:])
                self.ui.show_algorithm_ofDataset.setText("当前选择的功能：图像增强\n依次执行的算法顺序：" + algorithms)



    # ***************************************************************************************************************
    # ******************************************       可视化训练器函数     ********************************************
    # ***************************************************************************************************************
    def terminate_trainer(self):
        """ 终止 """
        if self.workerThread_trainerRun:
            self.workerThread_trainerRun.requestInterruption()
            self.workerThread_trainerRun.quit()
            self.workerThread_trainerRun.wait()
            self.workerThread_trainerRun.deleteLater()
            self.workerThread_trainerRun = None
        if self.workerThread_matrix:
            self.workerThread_matrix.requestInterruption()
            self.workerThread_matrix.quit()
            self.workerThread_matrix.wait()
            self.workerThread_matrix.deleteLater()
            self.workerThread_matrix = None

    def run_trainer(self):
        """ 运行 """
        if (not SI.functionMutex) and (not SI.threadMutex):
            try:
                SI.functionMutex = True
                # 终止线程------------------
                if self.workerThread_ofDataset:
                    self.workerThread_ofDataset.requestInterruption()
                    self.workerThread_ofDataset.quit()
                    self.workerThread_ofDataset.wait()
                if self.workerThread_trainerRun:
                    self.workerThread_trainerRun.requestInterruption()
                    self.workerThread_trainerRun.quit()
                    self.workerThread_trainerRun.wait()
                if self.workerThread_calNormalize:
                    self.workerThread_calNormalize.requestInterruption()
                    self.workerThread_calNormalize.quit()
                    self.workerThread_calNormalize.wait()
                if self.workerThread_matrix:
                    self.workerThread_matrix.requestInterruption()
                    self.workerThread_matrix.quit()
                    self.workerThread_matrix.wait()
                # 路径判空------------------
                if SI.dataset_split_path == "":
                    errorBox(self, "错误", "请先导入划分数据集")
                    return
                if SI.outputDir_path == "":
                    errorBox(self, "错误", "请先设置导出路径")
                    return

                # 获取参数--------------------
                # 网络选择
                Param.net_name = widgets.comboBox_trainer_net.currentText()
                # 保存间隔
                Param.save_period = int(widgets.lineEdit_trainer_period.text())
                # 图像大小
                input_size = widgets.lineEdit_trainer_inputSize1.text()
                if input_size == "":
                    errorBox(self, "错误", "请先输入图像数据大小")
                    return
                Param.input_size = int(input_size)
                # 损失函数
                Param.loss_function = widgets.comboBox_trainer_lossFunction.currentText()
                # 优化器
                Param.optimizer = widgets.comboBox_trainer_optimizer.currentText()
                # Batch Size
                Param.batch_size = int(widgets.lineEdit_trainer_batchSize.text())
                # Learning Rate
                Param.learning_rate = float(widgets.lineEdit_trainer_learningRate.text())
                # Epoch
                Param.epochs = int(widgets.lineEdit_trainer_epoch.text())
                # Dropout
                Param.dropout = widgets.dSpinBox_trainer_dropout.value()

                # 输入大小判断-------------------
                if Param.net_name == "AlexNet":
                    if Param.input_size < 64:
                        warningBox(self, "警告", "输入图像数据不小于64")
                        return
                elif Param.net_name in ["VGG11", "VGG13", "VGG16", "VGG19"]:
                    if Param.input_size < 32:
                        warningBox(self, "警告", "输入图像数据不小于32")
                        return
                elif Param.net_name == "GoogLeNet":
                    if Param.isTransferLearning and Param.input_size < 224:
                        warningBox(self, "警告", "输入图像数据不小于224")
                        return
                else:
                    if Param.input_size < 16:
                        warningBox(self, "警告", "输入图像数据过小")
                        return

                # 迁移学习模型存在判断--------------
                if Param.isTransferLearning:
                    if Param.net_name == "AlexNet":
                        if not self.check_pth_exists("alexnet.pth"):
                            return

                    elif Param.net_name == "VGG11":
                        if not self.check_pth_exists("vgg11.pth"):
                            return
                    elif Param.net_name == "VGG13":
                        if not self.check_pth_exists("vgg13.pth"):
                            return
                    elif Param.net_name == "VGG16":
                        if not self.check_pth_exists("vgg16.pth"):
                            return
                    elif Param.net_name == "VGG19":
                        if not self.check_pth_exists("vgg19.pth"):
                            return

                    elif Param.net_name == "GoogLeNet":
                        if not self.check_pth_exists("googlenet.pth"):
                            return

                    elif Param.net_name == "ResNet18":
                        if not self.check_pth_exists("resnet18.pth"):
                            return
                    elif Param.net_name == "ResNet34":
                        if not self.check_pth_exists("resnet34.pth"):
                            return
                    elif Param.net_name == "ResNet50":
                        if not self.check_pth_exists("resnet50.pth"):
                            return
                    elif Param.net_name == "ResNet101":
                        if not self.check_pth_exists("resnet101.pth"):
                            return
                    elif Param.net_name == "ResNet152":
                        if not self.check_pth_exists("resnet152.pth"):
                            return

                    elif Param.net_name == "ResNeXt50(32x4d)":
                        if not self.check_pth_exists("resnext50_32x4d.pth"):
                            return
                    elif Param.net_name == "ResNeXt101(32x8d)":
                        if not self.check_pth_exists("resnext101_32x8d.pth"):
                            return

                    elif Param.net_name == "MobileNetV2":
                        if not self.check_pth_exists("mobilenet_v2.pth"):
                            return
                    elif Param.net_name == "MobileNetV3(large)":
                        if not self.check_pth_exists("mobilenet_v3_large.pth"):
                            return
                    elif Param.net_name == "MobileNetV3(small)":
                        if not self.check_pth_exists("mobilenet_v3_small.pth"):
                            return

                    elif Param.net_name == "ShuffleNetV2(x0.5)":
                        if not self.check_pth_exists("shufflenetv2_x0_5.pth"):
                            return
                    elif Param.net_name == "ShuffleNetV2(x1.0)":
                        if not self.check_pth_exists("shufflenetv2_x1_0.pth"):
                            return
                    elif Param.net_name == "ShuffleNetV2(x1.5)":
                        if not self.check_pth_exists("shufflenetv2_x1_5.pth"):
                            return
                    elif Param.net_name == "ShuffleNetV2(x2.0)":
                        if not self.check_pth_exists("shufflenetv2_x2_0.pth"):
                            return

                    elif Param.net_name == "EfficientNetB0":
                        if not self.check_pth_exists("efficientnet_b0.pth"):
                            return
                    elif Param.net_name == "EfficientNetB1":
                        if not self.check_pth_exists("efficientnet_b1.pth"):
                            return
                    elif Param.net_name == "EfficientNetB2":
                        if not self.check_pth_exists("efficientnet_b2.pth"):
                            return
                    elif Param.net_name == "EfficientNetB3":
                        if not self.check_pth_exists("efficientnet_b3.pth"):
                            return
                    elif Param.net_name == "EfficientNetB4":
                        if not self.check_pth_exists("efficientnet_b4.pth"):
                            return
                    elif Param.net_name == "EfficientNetB5":
                        if not self.check_pth_exists("efficientnet_b5.pth"):
                            return
                    elif Param.net_name == "EfficientNetB6":
                        if not self.check_pth_exists("efficientnet_b6.pth"):
                            return
                    elif Param.net_name == "EfficientNetB7":
                        if not self.check_pth_exists("efficientnet_b7.pth"):
                            return

                    elif Param.net_name == "EfficientNetV2-S":
                        if not self.check_pth_exists("efficientnet_v2_s.pth"):
                            return
                    elif Param.net_name == "EfficientNetV2-M":
                        if not self.check_pth_exists("efficientnet_v2_m.pth"):
                            return
                    elif Param.net_name == "EfficientNetV2-L":
                        if not self.check_pth_exists("efficientnet_v2_l.pth"):
                            return

                    elif Param.net_name == "VisionTransformer(b16)":
                        if not self.check_pth_exists("vit_b_16.pth"):
                            return
                    elif Param.net_name == "VisionTransformer(b32)":
                        if not self.check_pth_exists("vit_b_32.pth"):
                            return

                    elif Param.net_name == "SwinTransformer(t)":
                        if not self.check_pth_exists("swin_t.pth"):
                            return
                    elif Param.net_name == "SwinTransformer(s)":
                        if not self.check_pth_exists("swin_s.pth"):
                            return
                    elif Param.net_name == "SwinTransformer(b)":
                        if not self.check_pth_exists("swin_b.pth"):
                            return

                # 禁用控件--------------------
                # 禁用参数控件
                disable_widgets(self.ui)
                # 禁用混淆矩阵按钮
                widgets.stackedWidget_canvas.setCurrentWidget(widgets.pgView_step_loss)
                widgets.btn_trainer_matrix.setStyleSheet(DisabledStyle.pushbutton)
                widgets.btn_trainer_matrix.setEnabled(False)

                # 运行模型--------------------
                AppFunctions.run_nets(self)


            except Exception as e:
                errorBox(self, "错误", "运行失败")
                enable_widgets(self.ui)
                print("《运行可视化训练器》时错误:", e)
            finally:
                SI.functionMutex = False
        else:
            warningBox(self, "警告", "其它功能正在执行")

    def check_pth_exists(self, pth_name):
        """
        查看pth文件是否存在
        """
        pth_path = f"algorithms/trainer/imagenet/{pth_name}"
        if not os.path.exists(pth_path):
            warningBox(self, "警告", f"{pth_path}文件不存在")
            return False
        return True

    def on_switchButton_checkedChanged_trainer(self, isChecked: bool):
        """
        开关 的信号触发函数
        """
        switchButton = self.sender()
        switchButtonName = switchButton.objectName()
        # 迁移学习
        if switchButtonName == "switchButton_trainer_imageNet":
            if isChecked:
                Param.isTransferLearning = True
                # initWeights & dropout
                widgets.frame_trainer_initWeights.setVisible(False)
                widgets.switchButton_trainer_initWeights.setChecked(False)
                widgets.frame_trainer_dropout.setVisible(False)
                Param.init_weights = False
                # 设置归一化参数
                if widgets.comboBox_trainer_net.currentText() in ["EfficientNetV2-S", "EfficientNetV2-M",
                                                                  "EfficientNetV2-L", "VisionTransformer(b16)",
                                                                  "VisionTransformer(b32)"]:
                    widgets.btn_trainer_normalize_default.click()
                    widgets.btn_trainer_normalize_cal.setStyleSheet(DisabledStyle.pushbutton)
                    widgets.btn_trainer_normalize_cal.setEnabled(False)
                    widgets.btn_trainer_normalize_pretrain.setStyleSheet(DisabledStyle.pushbutton)
                    widgets.btn_trainer_normalize_pretrain.setEnabled(False)
                else:
                    widgets.btn_trainer_normalize_pretrain.click()
                    widgets.btn_trainer_normalize_default.setStyleSheet(DisabledStyle.pushbutton)
                    widgets.btn_trainer_normalize_default.setEnabled(False)
                    widgets.btn_trainer_normalize_cal.setStyleSheet(DisabledStyle.pushbutton)
                    widgets.btn_trainer_normalize_cal.setEnabled(False)
            else:
                Param.isTransferLearning = False
                # initWeights & dropout
                if widgets.comboBox_trainer_net.currentText() in ["AlexNet", "VGG11", "VGG13",
                                                                  "VGG16", "VGG19", "GoogLeNet"]:
                    widgets.switchButton_trainer_initWeights.setChecked(True)
                    widgets.frame_trainer_initWeights.setVisible(True)
                    widgets.frame_trainer_dropout.setVisible(True)
                    Param.init_weights = True
                # 设置归一化参数
                self.enable_normalize_button()

        # 初始化权重
        elif switchButtonName == "switchButton_trainer_initWeights":
            if isChecked:
                Param.init_weights = True
            else:
                Param.init_weights = False

    def on_button_clicked_trainer(self):
        """
        按钮 的信号触发函数
        """
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_import_datasetSplit":
            AppFunctions.import_datasetSplit(self)
        elif btnName == "btn_output":
            AppFunctions.output_trainer(self)
        # 归一化
        elif btnName == "btn_trainer_normalize_default":
            Param.train_mean = [0.5, 0.5, 0.5]
            Param.train_std = [0.5, 0.5, 0.5]
            Param.val_mean = [0.5, 0.5, 0.5]
            Param.val_std = [0.5, 0.5, 0.5]
            Param.test_mean = [0.5, 0.5, 0.5]
            Param.test_std = [0.5, 0.5, 0.5]
            widgets.lineEdit_trainer_train_mean.setText("[0.5, 0.5, 0.5]")
            widgets.lineEdit_trainer_train_std.setText("[0.5, 0.5, 0.5]")
            widgets.lineEdit_trainer_val_mean.setText("[0.5, 0.5, 0.5]")
            widgets.lineEdit_trainer_val_std.setText("[0.5, 0.5, 0.5]")
            widgets.lineEdit_trainer_test_mean.setText("[0.5, 0.5, 0.5]")
            widgets.lineEdit_trainer_test_std.setText("[0.5, 0.5, 0.5]")
        elif btnName == "btn_trainer_normalize_pretrain":
            Param.train_mean = [0.485, 0.456, 0.406]
            Param.train_std = [0.229, 0.224, 0.225]
            Param.val_mean = [0.485, 0.456, 0.406]
            Param.val_std = [0.229, 0.224, 0.225]
            Param.test_mean = [0.485, 0.456, 0.406]
            Param.test_std = [0.229, 0.224, 0.225]
            widgets.lineEdit_trainer_train_mean.setText("[0.485, 0.456, 0.406]")
            widgets.lineEdit_trainer_train_std.setText("[0.229, 0.224, 0.225]")
            widgets.lineEdit_trainer_val_mean.setText("[0.485, 0.456, 0.406]")
            widgets.lineEdit_trainer_val_std.setText("[0.229, 0.224, 0.225]")
            widgets.lineEdit_trainer_test_mean.setText("[0.485, 0.456, 0.406]")
            widgets.lineEdit_trainer_test_std.setText("[0.229, 0.224, 0.225]")
        elif btnName == "btn_trainer_normalize_cal":
            if (not SI.functionMutex) and (not SI.threadMutex):
                try:
                    SI.functionMutex = True
                    # 路径判空------------------
                    if SI.dataset_split_path == "":
                        errorBox(self, "错误", "请先导入划分数据集")
                        return
                    # 执行算法------------------
                    AppFunctions.cal_normalize(self)
                except Exception as e:
                    errorBox(self, "错误", "运行失败")
                    print("《运行归一化计算》时错误:", e)
                finally:
                    SI.functionMutex = False
            else:
                warningBox(self, "警告", "其它功能正在执行")

    def on_netname_changed(self, netName):
        """ combobox-netname """
        # initWeights & dropout
        if netName in ["AlexNet", "VGG11", "VGG13", "VGG16", "VGG19", "GoogLeNet"]:
            if not Param.isTransferLearning:
                widgets.switchButton_trainer_initWeights.setChecked(True)
                widgets.frame_trainer_initWeights.setVisible(True)
                widgets.frame_trainer_dropout.setVisible(True)
        else:
            widgets.frame_trainer_initWeights.setVisible(False)
            widgets.frame_trainer_dropout.setVisible(False)
        # normalize
        if netName in ["EfficientNetV2-S", "EfficientNetV2-M", "EfficientNetV2-L", "VisionTransformer(b16)", "VisionTransformer(b32)"]:
            self.enable_normalize_button()
            if Param.isTransferLearning:
                widgets.btn_trainer_normalize_default.click()
                widgets.btn_trainer_normalize_cal.setStyleSheet(DisabledStyle.pushbutton)
                widgets.btn_trainer_normalize_cal.setEnabled(False)
                widgets.btn_trainer_normalize_pretrain.setStyleSheet(DisabledStyle.pushbutton)
                widgets.btn_trainer_normalize_pretrain.setEnabled(False)
        else:
            self.enable_normalize_button()
            if Param.isTransferLearning:
                widgets.btn_trainer_normalize_pretrain.click()
                widgets.btn_trainer_normalize_default.setStyleSheet(DisabledStyle.pushbutton)
                widgets.btn_trainer_normalize_default.setEnabled(False)
                widgets.btn_trainer_normalize_cal.setStyleSheet(DisabledStyle.pushbutton)
                widgets.btn_trainer_normalize_cal.setEnabled(False)
        # input_size
        if netName in ["VisionTransformer(b16)", "VisionTransformer(b32)"]:
            widgets.lineEdit_trainer_inputSize1.setText("224")
            widgets.lineEdit_trainer_inputSize2.setText("224")
            widgets.lineEdit_trainer_inputSize1.setStyleSheet(DisabledStyle.lineedit)
            widgets.lineEdit_trainer_inputSize2.setStyleSheet(DisabledStyle.lineedit)
            widgets.lineEdit_trainer_inputSize1.setEnabled(False)
            widgets.lineEdit_trainer_inputSize2.setEnabled(False)
        else:
            widgets.lineEdit_trainer_inputSize1.setStyleSheet(EnabledStyle.lineedit)
            widgets.lineEdit_trainer_inputSize2.setStyleSheet(EnabledStyle.lineedit)
            widgets.lineEdit_trainer_inputSize1.setEnabled(True)
            widgets.lineEdit_trainer_inputSize2.setEnabled(True)

    def enable_normalize_button(self):
        """
        恢复归一化按钮
        """
        widgets.btn_trainer_normalize_default.setStyleSheet(EnabledStyle.pushbutton)
        widgets.btn_trainer_normalize_default.setEnabled(True)
        widgets.btn_trainer_normalize_cal.setStyleSheet(EnabledStyle.pushbutton)
        widgets.btn_trainer_normalize_cal.setEnabled(True)
        widgets.btn_trainer_normalize_pretrain.setStyleSheet(EnabledStyle.pushbutton)
        widgets.btn_trainer_normalize_pretrain.setEnabled(True)



    def reset_view_trainer(self):
        """
        范围重置按钮点击
        """
        try:
            if SI.current_canvas == "step":
                widgets.canvas_step_loss.restore_view_limits()
            elif SI.current_canvas == "epoch":
                widgets.canvas_epoch_loss_acc.restore_view_limits()
        except:
            pass

    def show_step_trainer(self):
        """
        Step按钮点击
        """
        SI.current_canvas = "step"
        widgets.stackedWidget_canvas.setCurrentWidget(widgets.pgView_step_loss)


    def show_epoch_trainer(self):
        """
        Epoch按钮点击
        """
        SI.current_canvas = "epoch"
        widgets.stackedWidget_canvas.setCurrentWidget(widgets.pgView_epoch_loss_acc)

    def show_confusionMatrix_trainer(self):
        """
        混淆矩阵按钮点击
        """
        SI.current_canvas = 'matrix'
        widgets.stackedWidget_canvas.setCurrentWidget(widgets.pgView_confusionMatrix)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
