# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QToolBox, QVBoxLayout, QWidget)

from . figure_canvas import MplCanvas
from . switch_button.SwitchButton import SwitchButton
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1440, 810))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"	background-color: #6272a4;\n"
"	background-image: url(:/images/ima"
                        "ges/images/AUST_Logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomM"
                        "enu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189"
                        ", 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8"
                        "f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Botto"
                        "m Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::ite"
                        "m{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255,"
                        " 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    borde"
                        "r: none;\n"
"    background: #6272a4;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
""
                        "	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* //////////"
                        "///////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox {\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton {\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 18"
                        "7);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	p"
                        "adding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:ver"
                        "tical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button "
                        "*/\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272A4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_process_image = QPushButton(self.topMenu)
        self.btn_process_image.setObjectName(u"btn_process_image")
        sizePolicy1.setHeightForWidth(self.btn_process_image.sizePolicy().hasHeightForWidth())
        self.btn_process_image.setSizePolicy(sizePolicy1)
        self.btn_process_image.setMinimumSize(QSize(0, 45))
        self.btn_process_image.setFont(font)
        self.btn_process_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_process_image.setLayoutDirection(Qt.LeftToRight)
        self.btn_process_image.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-satelite.png);")

        self.verticalLayout_8.addWidget(self.btn_process_image)

        self.btn_process_dataset = QPushButton(self.topMenu)
        self.btn_process_dataset.setObjectName(u"btn_process_dataset")
        sizePolicy1.setHeightForWidth(self.btn_process_dataset.sizePolicy().hasHeightForWidth())
        self.btn_process_dataset.setSizePolicy(sizePolicy1)
        self.btn_process_dataset.setMinimumSize(QSize(0, 45))
        self.btn_process_dataset.setFont(font)
        self.btn_process_dataset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_process_dataset.setLayoutDirection(Qt.LeftToRight)
        self.btn_process_dataset.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder.png);")

        self.verticalLayout_8.addWidget(self.btn_process_dataset)

        self.btn_trainer = QPushButton(self.topMenu)
        self.btn_trainer.setObjectName(u"btn_trainer")
        sizePolicy1.setHeightForWidth(self.btn_trainer.sizePolicy().hasHeightForWidth())
        self.btn_trainer.setSizePolicy(sizePolicy1)
        self.btn_trainer.setMinimumSize(QSize(0, 45))
        self.btn_trainer.setFont(font)
        self.btn_trainer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trainer.setLayoutDirection(Qt.LeftToRight)
        self.btn_trainer.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_trainer)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(0, 0))
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(360, 0))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.verticalLayout_97 = QVBoxLayout(self.home)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalSpacer_28 = QSpacerItem(20, 646, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_97.addItem(self.verticalSpacer_28)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_59)

        self.label_100 = QLabel(self.home)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"	background: none;\n"
"}")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_107.addWidget(self.label_100)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_70)


        self.verticalLayout_97.addLayout(self.horizontalLayout_107)

        self.stackedWidget.addWidget(self.home)
        self.processPage_image = QWidget()
        self.processPage_image.setObjectName(u"processPage_image")
        self.processPage_image.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272A4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.processPage_image)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 10)
        self.btn_importSingleImage = QPushButton(self.processPage_image)
        self.btn_importSingleImage.setObjectName(u"btn_importSingleImage")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_importSingleImage.sizePolicy().hasHeightForWidth())
        self.btn_importSingleImage.setSizePolicy(sizePolicy4)
        self.btn_importSingleImage.setMinimumSize(QSize(150, 30))
        self.btn_importSingleImage.setMaximumSize(QSize(150, 30))
        self.btn_importSingleImage.setFont(font)
        self.btn_importSingleImage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importSingleImage.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_importSingleImage.setIcon(icon3)

        self.horizontalLayout_17.addWidget(self.btn_importSingleImage)

        self.btn_exportResult_image = QPushButton(self.processPage_image)
        self.btn_exportResult_image.setObjectName(u"btn_exportResult_image")
        sizePolicy4.setHeightForWidth(self.btn_exportResult_image.sizePolicy().hasHeightForWidth())
        self.btn_exportResult_image.setSizePolicy(sizePolicy4)
        self.btn_exportResult_image.setMinimumSize(QSize(150, 30))
        self.btn_exportResult_image.setMaximumSize(QSize(150, 30))
        self.btn_exportResult_image.setFont(font)
        self.btn_exportResult_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportResult_image.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exportResult_image.setIcon(icon4)

        self.horizontalLayout_17.addWidget(self.btn_exportResult_image)

        self.horizontalSpacer_14 = QSpacerItem(781, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.btn_preview_image = QPushButton(self.processPage_image)
        self.btn_preview_image.setObjectName(u"btn_preview_image")
        sizePolicy4.setHeightForWidth(self.btn_preview_image.sizePolicy().hasHeightForWidth())
        self.btn_preview_image.setSizePolicy(sizePolicy4)
        self.btn_preview_image.setMinimumSize(QSize(80, 30))
        self.btn_preview_image.setMaximumSize(QSize(80, 30))
        self.btn_preview_image.setFont(font)
        self.btn_preview_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_preview_image.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_preview_image.setIcon(icon5)

        self.horizontalLayout_17.addWidget(self.btn_preview_image)

        self.btn_run_image = QPushButton(self.processPage_image)
        self.btn_run_image.setObjectName(u"btn_run_image")
        sizePolicy4.setHeightForWidth(self.btn_run_image.sizePolicy().hasHeightForWidth())
        self.btn_run_image.setSizePolicy(sizePolicy4)
        self.btn_run_image.setMinimumSize(QSize(80, 30))
        self.btn_run_image.setMaximumSize(QSize(80, 30))
        self.btn_run_image.setFont(font)
        self.btn_run_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_run_image.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run_image.setIcon(icon6)

        self.horizontalLayout_17.addWidget(self.btn_run_image)


        self.verticalLayout_27.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.toolBox_function_image = QToolBox(self.processPage_image)
        self.toolBox_function_image.setObjectName(u"toolBox_function_image")
        self.toolBox_function_image.setMinimumSize(QSize(360, 0))
        self.toolBox_function_image.setMaximumSize(QSize(360, 16777215))
        self.toolBox_function_image.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton*/\n"
"#toolBox_function QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 8px;	\n"
"	background-color: #7f94d5;\n"
"	font-size: 16px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#toolBox_function QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#toolBox_function QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ToolBox*/\n"
"QToolBox::tab { \n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"	font-weight: 900;\n"
"	padding-right: 10px;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	bac"
                        "kground-color: #495474;\n"
"	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QToolBoxButton {\n"
"	min-height: 46px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:"
                        "/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(226, 135, 249);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QLabel */\n"
"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-pos"
                        "ition: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QDoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255)"
                        ";\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:focus {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:hover {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"")
        self.toolBox_function_image.setFrameShape(QFrame.Box)
        self.tbpg_processTool_image = QWidget()
        self.tbpg_processTool_image.setObjectName(u"tbpg_processTool_image")
        self.tbpg_processTool_image.setGeometry(QRect(0, 0, 92, 40))
        self.verticalLayout_46 = QVBoxLayout(self.tbpg_processTool_image)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.toolBox_process_image = QToolBox(self.tbpg_processTool_image)
        self.toolBox_process_image.setObjectName(u"toolBox_process_image")
        self.toolBox_process_image.setMinimumSize(QSize(0, 22))
        self.toolBox_process_image.setStyleSheet(u"QToolBoxButton {\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QToolBox QScrollArea {	\n"
"	background-color: rgb(226, 234, 255);\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	background-color: #495474;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-right.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}")
        self.toolBox_process_image.setFrameShape(QFrame.NoFrame)
        self.tbpg_suffix_image = QWidget()
        self.tbpg_suffix_image.setObjectName(u"tbpg_suffix_image")
        self.tbpg_suffix_image.setGeometry(QRect(0, 0, 92, 210))
        self.tbpg_suffix_image.setStyleSheet(u"\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #6272a4;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.tbpg_suffix_image)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_jpg_image = QPushButton(self.tbpg_suffix_image)
        self.btn_jpg_image.setObjectName(u"btn_jpg_image")
        self.btn_jpg_image.setMinimumSize(QSize(0, 40))
        self.btn_jpg_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_27.addWidget(self.btn_jpg_image)

        self.rb_jpg_image = QRadioButton(self.tbpg_suffix_image)
        self.rb_jpg_image.setObjectName(u"rb_jpg_image")
        self.rb_jpg_image.setMinimumSize(QSize(30, 30))
        self.rb_jpg_image.setMaximumSize(QSize(30, 30))
        self.rb_jpg_image.setCheckable(True)

        self.horizontalLayout_27.addWidget(self.rb_jpg_image)


        self.verticalLayout_33.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.btn_jpeg_image = QPushButton(self.tbpg_suffix_image)
        self.btn_jpeg_image.setObjectName(u"btn_jpeg_image")
        self.btn_jpeg_image.setMinimumSize(QSize(0, 40))
        self.btn_jpeg_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.btn_jpeg_image)

        self.rb_jpeg_image = QRadioButton(self.tbpg_suffix_image)
        self.rb_jpeg_image.setObjectName(u"rb_jpeg_image")
        self.rb_jpeg_image.setMinimumSize(QSize(30, 30))
        self.rb_jpeg_image.setMaximumSize(QSize(30, 30))
        self.rb_jpeg_image.setCheckable(True)

        self.horizontalLayout_28.addWidget(self.rb_jpeg_image)


        self.verticalLayout_33.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_png_image = QPushButton(self.tbpg_suffix_image)
        self.btn_png_image.setObjectName(u"btn_png_image")
        self.btn_png_image.setMinimumSize(QSize(0, 40))
        self.btn_png_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_29.addWidget(self.btn_png_image)

        self.rb_png_image = QRadioButton(self.tbpg_suffix_image)
        self.rb_png_image.setObjectName(u"rb_png_image")
        self.rb_png_image.setMinimumSize(QSize(30, 30))
        self.rb_png_image.setMaximumSize(QSize(30, 30))
        self.rb_png_image.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.rb_png_image)


        self.verticalLayout_33.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_bmp_image = QPushButton(self.tbpg_suffix_image)
        self.btn_bmp_image.setObjectName(u"btn_bmp_image")
        self.btn_bmp_image.setMinimumSize(QSize(0, 40))
        self.btn_bmp_image.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_30.addWidget(self.btn_bmp_image)

        self.rb_bmp_image = QRadioButton(self.tbpg_suffix_image)
        self.rb_bmp_image.setObjectName(u"rb_bmp_image")
        self.rb_bmp_image.setMinimumSize(QSize(30, 30))
        self.rb_bmp_image.setMaximumSize(QSize(30, 30))
        self.rb_bmp_image.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.rb_bmp_image)


        self.verticalLayout_33.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_8)

        self.toolBox_process_image.addItem(self.tbpg_suffix_image, u"\u66f4\u6539\u540e\u7f00")
        self.tbpg_resize_image = QWidget()
        self.tbpg_resize_image.setObjectName(u"tbpg_resize_image")
        self.tbpg_resize_image.setGeometry(QRect(0, 0, 204, 273))
        self.verticalLayout_37 = QVBoxLayout(self.tbpg_resize_image)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_30 = QLabel(self.tbpg_resize_image)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_37.addWidget(self.label_30)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lineEdit_resizepx1_ofImage = QLineEdit(self.tbpg_resize_image)
        self.lineEdit_resizepx1_ofImage.setObjectName(u"lineEdit_resizepx1_ofImage")
        self.lineEdit_resizepx1_ofImage.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_resizepx1_ofImage.setMaxLength(4)
        self.lineEdit_resizepx1_ofImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.lineEdit_resizepx1_ofImage)

        self.label_31 = QLabel(self.tbpg_resize_image)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")

        self.horizontalLayout_22.addWidget(self.label_31)

        self.lineEdit_resizepx2_ofImage = QLineEdit(self.tbpg_resize_image)
        self.lineEdit_resizepx2_ofImage.setObjectName(u"lineEdit_resizepx2_ofImage")
        self.lineEdit_resizepx2_ofImage.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_resizepx2_ofImage.setMaxLength(4)
        self.lineEdit_resizepx2_ofImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.lineEdit_resizepx2_ofImage)

        self.label_32 = QLabel(self.tbpg_resize_image)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")

        self.horizontalLayout_22.addWidget(self.label_32)


        self.verticalLayout_37.addLayout(self.horizontalLayout_22)

        self.label_33 = QLabel(self.tbpg_resize_image)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 20))

        self.verticalLayout_37.addWidget(self.label_33)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.rbtn_INTER_LINEAR_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_LINEAR_ofImage.setObjectName(u"rbtn_INTER_LINEAR_ofImage")
        self.rbtn_INTER_LINEAR_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_LINEAR_ofImage)

        self.rbtn_INTER_NEAREST_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_NEAREST_ofImage.setObjectName(u"rbtn_INTER_NEAREST_ofImage")
        self.rbtn_INTER_NEAREST_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_NEAREST_ofImage)

        self.rbtn_INTER_CUBIC_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_CUBIC_ofImage.setObjectName(u"rbtn_INTER_CUBIC_ofImage")
        self.rbtn_INTER_CUBIC_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_CUBIC_ofImage)

        self.rbtn_INTER_AREA_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_AREA_ofImage.setObjectName(u"rbtn_INTER_AREA_ofImage")
        self.rbtn_INTER_AREA_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_AREA_ofImage)

        self.rbtn_INTER_LANCZOS4_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_LANCZOS4_ofImage.setObjectName(u"rbtn_INTER_LANCZOS4_ofImage")
        self.rbtn_INTER_LANCZOS4_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_LANCZOS4_ofImage)

        self.rbtn_INTER_LINEAR_EXACT_ofImage = QRadioButton(self.tbpg_resize_image)
        self.rbtn_INTER_LINEAR_EXACT_ofImage.setObjectName(u"rbtn_INTER_LINEAR_EXACT_ofImage")
        self.rbtn_INTER_LINEAR_EXACT_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_29.addWidget(self.rbtn_INTER_LINEAR_EXACT_ofImage)


        self.verticalLayout_37.addLayout(self.verticalLayout_29)

        self.verticalSpacer_11 = QSpacerItem(20, 207, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_11)

        self.toolBox_process_image.addItem(self.tbpg_resize_image, u"\u66f4\u6539\u5927\u5c0f")
        self.tbpg_square_image = QWidget()
        self.tbpg_square_image.setObjectName(u"tbpg_square_image")
        self.tbpg_square_image.setGeometry(QRect(0, 0, 233, 378))
        self.verticalLayout_32 = QVBoxLayout(self.tbpg_square_image)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_square_method_image = QFrame(self.tbpg_square_image)
        self.frame_square_method_image.setObjectName(u"frame_square_method_image")
        self.frame_square_method_image.setFrameShape(QFrame.StyledPanel)
        self.frame_square_method_image.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_square_method_image)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_24 = QLabel(self.frame_square_method_image)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_31.addWidget(self.label_24)

        self.rbtn_BORDER_CONSTANT_image = QRadioButton(self.frame_square_method_image)
        self.rbtn_BORDER_CONSTANT_image.setObjectName(u"rbtn_BORDER_CONSTANT_image")
        self.rbtn_BORDER_CONSTANT_image.setMinimumSize(QSize(0, 22))
        self.rbtn_BORDER_CONSTANT_image.setCheckable(True)
        self.rbtn_BORDER_CONSTANT_image.setChecked(False)

        self.verticalLayout_31.addWidget(self.rbtn_BORDER_CONSTANT_image)

        self.rbtn_BORDER_REFLECT_image = QRadioButton(self.frame_square_method_image)
        self.rbtn_BORDER_REFLECT_image.setObjectName(u"rbtn_BORDER_REFLECT_image")
        self.rbtn_BORDER_REFLECT_image.setMinimumSize(QSize(0, 22))

        self.verticalLayout_31.addWidget(self.rbtn_BORDER_REFLECT_image)

        self.rbtn_BORDER_REPLICATE_image = QRadioButton(self.frame_square_method_image)
        self.rbtn_BORDER_REPLICATE_image.setObjectName(u"rbtn_BORDER_REPLICATE_image")
        self.rbtn_BORDER_REPLICATE_image.setMinimumSize(QSize(0, 22))

        self.verticalLayout_31.addWidget(self.rbtn_BORDER_REPLICATE_image)

        self.rbtn_BORDER_WRAP_image = QRadioButton(self.frame_square_method_image)
        self.rbtn_BORDER_WRAP_image.setObjectName(u"rbtn_BORDER_WRAP_image")
        self.rbtn_BORDER_WRAP_image.setMinimumSize(QSize(0, 22))

        self.verticalLayout_31.addWidget(self.rbtn_BORDER_WRAP_image)


        self.verticalLayout_32.addWidget(self.frame_square_method_image)

        self.frame_square_RGB_image = QFrame(self.tbpg_square_image)
        self.frame_square_RGB_image.setObjectName(u"frame_square_RGB_image")
        self.frame_square_RGB_image.setStyleSheet(u"")
        self.frame_square_RGB_image.setFrameShape(QFrame.StyledPanel)
        self.frame_square_RGB_image.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_square_RGB_image)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_29 = QLabel(self.frame_square_RGB_image)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_23.addWidget(self.label_29)

        self.squre_showRGB_ofImage = QLabel(self.frame_square_RGB_image)
        self.squre_showRGB_ofImage.setObjectName(u"squre_showRGB_ofImage")
        self.squre_showRGB_ofImage.setMinimumSize(QSize(72, 20))
        self.squre_showRGB_ofImage.setMaximumSize(QSize(72, 20))
        self.squre_showRGB_ofImage.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.squre_showRGB_ofImage)


        self.verticalLayout_30.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_28 = QLabel(self.frame_square_RGB_image)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_18)

        self.spinBox_square_image_R = QSpinBox(self.frame_square_RGB_image)
        self.spinBox_square_image_R.setObjectName(u"spinBox_square_image_R")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.spinBox_square_image_R.sizePolicy().hasHeightForWidth())
        self.spinBox_square_image_R.setSizePolicy(sizePolicy5)
        self.spinBox_square_image_R.setMinimumSize(QSize(72, 20))
        self.spinBox_square_image_R.setAlignment(Qt.AlignCenter)
        self.spinBox_square_image_R.setMaximum(255)
        self.spinBox_square_image_R.setValue(255)

        self.horizontalLayout_24.addWidget(self.spinBox_square_image_R)


        self.verticalLayout_30.addLayout(self.horizontalLayout_24)

        self.slider_square_image_R = QSlider(self.frame_square_RGB_image)
        self.slider_square_image_R.setObjectName(u"slider_square_image_R")
        self.slider_square_image_R.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"")
        self.slider_square_image_R.setMaximum(255)
        self.slider_square_image_R.setSliderPosition(255)
        self.slider_square_image_R.setOrientation(Qt.Horizontal)

        self.verticalLayout_30.addWidget(self.slider_square_image_R)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_26 = QLabel(self.frame_square_RGB_image)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_25.addWidget(self.label_26)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_19)

        self.spinBox_square_image_G = QSpinBox(self.frame_square_RGB_image)
        self.spinBox_square_image_G.setObjectName(u"spinBox_square_image_G")
        sizePolicy5.setHeightForWidth(self.spinBox_square_image_G.sizePolicy().hasHeightForWidth())
        self.spinBox_square_image_G.setSizePolicy(sizePolicy5)
        self.spinBox_square_image_G.setMinimumSize(QSize(72, 20))
        self.spinBox_square_image_G.setAlignment(Qt.AlignCenter)
        self.spinBox_square_image_G.setMaximum(255)
        self.spinBox_square_image_G.setValue(255)

        self.horizontalLayout_25.addWidget(self.spinBox_square_image_G)


        self.verticalLayout_30.addLayout(self.horizontalLayout_25)

        self.slider_square_image_G = QSlider(self.frame_square_RGB_image)
        self.slider_square_image_G.setObjectName(u"slider_square_image_G")
        self.slider_square_image_G.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #17ffb9;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #17ffb9;\n"
"}\n"
"")
        self.slider_square_image_G.setMaximum(255)
        self.slider_square_image_G.setSliderPosition(255)
        self.slider_square_image_G.setOrientation(Qt.Horizontal)

        self.verticalLayout_30.addWidget(self.slider_square_image_G)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.frame_square_RGB_image)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_26.addWidget(self.label_25)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_20)

        self.spinBox_square_image_B = QSpinBox(self.frame_square_RGB_image)
        self.spinBox_square_image_B.setObjectName(u"spinBox_square_image_B")
        sizePolicy5.setHeightForWidth(self.spinBox_square_image_B.sizePolicy().hasHeightForWidth())
        self.spinBox_square_image_B.setSizePolicy(sizePolicy5)
        self.spinBox_square_image_B.setMinimumSize(QSize(72, 20))
        self.spinBox_square_image_B.setAlignment(Qt.AlignCenter)
        self.spinBox_square_image_B.setMaximum(255)
        self.spinBox_square_image_B.setValue(255)

        self.horizontalLayout_26.addWidget(self.spinBox_square_image_B)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.slider_square_image_B = QSlider(self.frame_square_RGB_image)
        self.slider_square_image_B.setObjectName(u"slider_square_image_B")
        self.slider_square_image_B.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"")
        self.slider_square_image_B.setMaximum(255)
        self.slider_square_image_B.setSliderPosition(255)
        self.slider_square_image_B.setOrientation(Qt.Horizontal)

        self.verticalLayout_30.addWidget(self.slider_square_image_B)


        self.verticalLayout_32.addWidget(self.frame_square_RGB_image)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_10)

        self.toolBox_process_image.addItem(self.tbpg_square_image, u"\u56fe\u7247\u65b9\u5f62\u5316")

        self.verticalLayout_46.addWidget(self.toolBox_process_image)

        self.toolBox_function_image.addItem(self.tbpg_processTool_image, u"\u9884\u5904\u7406\u5de5\u5177")
        self.tbpg_imageAugment_image = QWidget()
        self.tbpg_imageAugment_image.setObjectName(u"tbpg_imageAugment_image")
        self.tbpg_imageAugment_image.setGeometry(QRect(0, 0, 92, 319))
        self.verticalLayout_47 = QVBoxLayout(self.tbpg_imageAugment_image)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.toolBox_imageAugment_image = QToolBox(self.tbpg_imageAugment_image)
        self.toolBox_imageAugment_image.setObjectName(u"toolBox_imageAugment_image")
        self.toolBox_imageAugment_image.setStyleSheet(u"QToolBoxButton {\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QToolBox QScrollArea {\n"
"	background-color: rgb(226, 234, 255);\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	background-color: #495474;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-right.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}")
        self.tbpg_rotate_image = QWidget()
        self.tbpg_rotate_image.setObjectName(u"tbpg_rotate_image")
        self.tbpg_rotate_image.setGeometry(QRect(0, 0, 224, 378))
        self.verticalLayout_17 = QVBoxLayout(self.tbpg_rotate_image)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_rotate_switch_ofImage = QFrame(self.tbpg_rotate_image)
        self.frame_rotate_switch_ofImage.setObjectName(u"frame_rotate_switch_ofImage")
        self.frame_rotate_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_rotate_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_rotate_switch_ofImage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.frame_rotate_switch_ofImage)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.label_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.switchButton_rotate_ofImage = SwitchButton(self.frame_rotate_switch_ofImage)
        self.switchButton_rotate_ofImage.setObjectName(u"switchButton_rotate_ofImage")
        self.switchButton_rotate_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_11.addWidget(self.switchButton_rotate_ofImage)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)


        self.verticalLayout_17.addWidget(self.frame_rotate_switch_ofImage)

        self.frame_rotate_content_ofImage = QFrame(self.tbpg_rotate_image)
        self.frame_rotate_content_ofImage.setObjectName(u"frame_rotate_content_ofImage")
        self.frame_rotate_content_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_rotate_content_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_rotate_content_ofImage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_37 = QLabel(self.frame_rotate_content_ofImage)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_6.addWidget(self.label_37)

        self.horizontalSpacer_9 = QSpacerItem(78, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.dSpinBox_rotateDegree_ofImage = QDoubleSpinBox(self.frame_rotate_content_ofImage)
        self.dSpinBox_rotateDegree_ofImage.setObjectName(u"dSpinBox_rotateDegree_ofImage")
        sizePolicy5.setHeightForWidth(self.dSpinBox_rotateDegree_ofImage.sizePolicy().hasHeightForWidth())
        self.dSpinBox_rotateDegree_ofImage.setSizePolicy(sizePolicy5)
        self.dSpinBox_rotateDegree_ofImage.setMinimumSize(QSize(100, 20))
        self.dSpinBox_rotateDegree_ofImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dSpinBox_rotateDegree_ofImage.setMinimum(-180.000000000000000)
        self.dSpinBox_rotateDegree_ofImage.setMaximum(180.000000000000000)
        self.dSpinBox_rotateDegree_ofImage.setSingleStep(10.000000000000000)

        self.horizontalLayout_6.addWidget(self.dSpinBox_rotateDegree_ofImage)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.slider_rotateDegree_ofImage = QSlider(self.frame_rotate_content_ofImage)
        self.slider_rotateDegree_ofImage.setObjectName(u"slider_rotateDegree_ofImage")
        self.slider_rotateDegree_ofImage.setMinimum(-18000)
        self.slider_rotateDegree_ofImage.setMaximum(18000)
        self.slider_rotateDegree_ofImage.setSingleStep(100)
        self.slider_rotateDegree_ofImage.setPageStep(1000)
        self.slider_rotateDegree_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_rotateDegree_ofImage)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_40 = QLabel(self.frame_rotate_content_ofImage)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_7.addWidget(self.label_40)

        self.horizontalSpacer_8 = QSpacerItem(78, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.dSpinBox_rotateScale_ofImage = QDoubleSpinBox(self.frame_rotate_content_ofImage)
        self.dSpinBox_rotateScale_ofImage.setObjectName(u"dSpinBox_rotateScale_ofImage")
        sizePolicy5.setHeightForWidth(self.dSpinBox_rotateScale_ofImage.sizePolicy().hasHeightForWidth())
        self.dSpinBox_rotateScale_ofImage.setSizePolicy(sizePolicy5)
        self.dSpinBox_rotateScale_ofImage.setMinimumSize(QSize(86, 20))
        self.dSpinBox_rotateScale_ofImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dSpinBox_rotateScale_ofImage.setMinimum(0.010000000000000)
        self.dSpinBox_rotateScale_ofImage.setMaximum(10.000000000000000)
        self.dSpinBox_rotateScale_ofImage.setSingleStep(0.100000000000000)
        self.dSpinBox_rotateScale_ofImage.setValue(1.000000000000000)

        self.horizontalLayout_7.addWidget(self.dSpinBox_rotateScale_ofImage)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.slider_rotateScale_ofImage = QSlider(self.frame_rotate_content_ofImage)
        self.slider_rotateScale_ofImage.setObjectName(u"slider_rotateScale_ofImage")
        self.slider_rotateScale_ofImage.setMinimum(1)
        self.slider_rotateScale_ofImage.setMaximum(1000)
        self.slider_rotateScale_ofImage.setSingleStep(10)
        self.slider_rotateScale_ofImage.setValue(100)
        self.slider_rotateScale_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_rotateScale_ofImage)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_39 = QLabel(self.frame_rotate_content_ofImage)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_12.addWidget(self.label_39)

        self.rotate_showRGB_ofImage = QLabel(self.frame_rotate_content_ofImage)
        self.rotate_showRGB_ofImage.setObjectName(u"rotate_showRGB_ofImage")
        sizePolicy5.setHeightForWidth(self.rotate_showRGB_ofImage.sizePolicy().hasHeightForWidth())
        self.rotate_showRGB_ofImage.setSizePolicy(sizePolicy5)
        self.rotate_showRGB_ofImage.setMinimumSize(QSize(72, 20))
        self.rotate_showRGB_ofImage.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.rotate_showRGB_ofImage)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_35 = QLabel(self.frame_rotate_content_ofImage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_8.addWidget(self.label_35)

        self.horizontalSpacer_10 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.spinBox_rotate_ofImage_R = QSpinBox(self.frame_rotate_content_ofImage)
        self.spinBox_rotate_ofImage_R.setObjectName(u"spinBox_rotate_ofImage_R")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofImage_R.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofImage_R.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofImage_R.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofImage_R.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_rotate_ofImage_R.setMaximum(255)
        self.spinBox_rotate_ofImage_R.setValue(255)

        self.horizontalLayout_8.addWidget(self.spinBox_rotate_ofImage_R)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.slider_rotate_ofImage_R = QSlider(self.frame_rotate_content_ofImage)
        self.slider_rotate_ofImage_R.setObjectName(u"slider_rotate_ofImage_R")
        self.slider_rotate_ofImage_R.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"")
        self.slider_rotate_ofImage_R.setMaximum(255)
        self.slider_rotate_ofImage_R.setSliderPosition(255)
        self.slider_rotate_ofImage_R.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_rotate_ofImage_R)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_38 = QLabel(self.frame_rotate_content_ofImage)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_9.addWidget(self.label_38)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.spinBox_rotate_ofImage_G = QSpinBox(self.frame_rotate_content_ofImage)
        self.spinBox_rotate_ofImage_G.setObjectName(u"spinBox_rotate_ofImage_G")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofImage_G.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofImage_G.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofImage_G.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofImage_G.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_rotate_ofImage_G.setMaximum(255)
        self.spinBox_rotate_ofImage_G.setValue(255)

        self.horizontalLayout_9.addWidget(self.spinBox_rotate_ofImage_G)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.slider_rotate_ofImage_G = QSlider(self.frame_rotate_content_ofImage)
        self.slider_rotate_ofImage_G.setObjectName(u"slider_rotate_ofImage_G")
        self.slider_rotate_ofImage_G.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #17ffb9;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #17ffb9;\n"
"}\n"
"")
        self.slider_rotate_ofImage_G.setMaximum(255)
        self.slider_rotate_ofImage_G.setSliderPosition(255)
        self.slider_rotate_ofImage_G.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_rotate_ofImage_G)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_36 = QLabel(self.frame_rotate_content_ofImage)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_10.addWidget(self.label_36)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.spinBox_rotate_ofImage_B = QSpinBox(self.frame_rotate_content_ofImage)
        self.spinBox_rotate_ofImage_B.setObjectName(u"spinBox_rotate_ofImage_B")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofImage_B.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofImage_B.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofImage_B.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofImage_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_rotate_ofImage_B.setMaximum(255)
        self.spinBox_rotate_ofImage_B.setValue(255)

        self.horizontalLayout_10.addWidget(self.spinBox_rotate_ofImage_B)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.slider_rotate_ofImage_B = QSlider(self.frame_rotate_content_ofImage)
        self.slider_rotate_ofImage_B.setObjectName(u"slider_rotate_ofImage_B")
        self.slider_rotate_ofImage_B.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"")
        self.slider_rotate_ofImage_B.setMaximum(255)
        self.slider_rotate_ofImage_B.setSliderPosition(255)
        self.slider_rotate_ofImage_B.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_rotate_ofImage_B)


        self.verticalLayout_17.addWidget(self.frame_rotate_content_ofImage)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)

        self.toolBox_imageAugment_image.addItem(self.tbpg_rotate_image, u"\u56fe\u50cf\u65cb\u8f6c")
        self.tbpg_HFlip_image = QWidget()
        self.tbpg_HFlip_image.setObjectName(u"tbpg_HFlip_image")
        self.tbpg_HFlip_image.setGeometry(QRect(0, 0, 180, 76))
        self.verticalLayout_21 = QVBoxLayout(self.tbpg_HFlip_image)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_HFlip_switch_ofImage = QFrame(self.tbpg_HFlip_image)
        self.frame_HFlip_switch_ofImage.setObjectName(u"frame_HFlip_switch_ofImage")
        self.frame_HFlip_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_HFlip_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_HFlip_switch_ofImage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_23 = QLabel(self.frame_HFlip_switch_ofImage)
        self.label_23.setObjectName(u"label_23")
        sizePolicy6.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy6)
        self.label_23.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.label_23)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.switchButton_HFlip_ofImage = SwitchButton(self.frame_HFlip_switch_ofImage)
        self.switchButton_HFlip_ofImage.setObjectName(u"switchButton_HFlip_ofImage")
        self.switchButton_HFlip_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_14.addWidget(self.switchButton_HFlip_ofImage)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)


        self.verticalLayout_21.addWidget(self.frame_HFlip_switch_ofImage)

        self.verticalSpacer_9 = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)

        self.toolBox_imageAugment_image.addItem(self.tbpg_HFlip_image, u"\u6c34\u5e73\u7ffb\u8f6c")
        self.tbpg_VFlip_image = QWidget()
        self.tbpg_VFlip_image.setObjectName(u"tbpg_VFlip_image")
        self.tbpg_VFlip_image.setGeometry(QRect(0, 0, 180, 76))
        self.verticalLayout_23 = QVBoxLayout(self.tbpg_VFlip_image)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_VFlip_switch_ofImage = QFrame(self.tbpg_VFlip_image)
        self.frame_VFlip_switch_ofImage.setObjectName(u"frame_VFlip_switch_ofImage")
        self.frame_VFlip_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_VFlip_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_VFlip_switch_ofImage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_34 = QLabel(self.frame_VFlip_switch_ofImage)
        self.label_34.setObjectName(u"label_34")
        sizePolicy6.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy6)
        self.label_34.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.label_34)

        self.horizontalSpacer_16 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.switchButton_VFlip_ofImage = SwitchButton(self.frame_VFlip_switch_ofImage)
        self.switchButton_VFlip_ofImage.setObjectName(u"switchButton_VFlip_ofImage")
        self.switchButton_VFlip_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_13.addWidget(self.switchButton_VFlip_ofImage)


        self.verticalLayout_19.addLayout(self.horizontalLayout_13)


        self.verticalLayout_23.addWidget(self.frame_VFlip_switch_ofImage)

        self.verticalSpacer_12 = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_12)

        self.toolBox_imageAugment_image.addItem(self.tbpg_VFlip_image, u"\u5782\u76f4\u7ffb\u8f6c")
        self.tbpg_blur_image = QWidget()
        self.tbpg_blur_image.setObjectName(u"tbpg_blur_image")
        self.tbpg_blur_image.setGeometry(QRect(0, 0, 331, 229))
        self.verticalLayout_26 = QVBoxLayout(self.tbpg_blur_image)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_blur_switch_ofImage = QFrame(self.tbpg_blur_image)
        self.frame_blur_switch_ofImage.setObjectName(u"frame_blur_switch_ofImage")
        self.frame_blur_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_blur_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_blur_switch_ofImage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_41 = QLabel(self.frame_blur_switch_ofImage)
        self.label_41.setObjectName(u"label_41")
        sizePolicy6.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy6)
        self.label_41.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.label_41)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)

        self.switchButton_blur_ofImage = SwitchButton(self.frame_blur_switch_ofImage)
        self.switchButton_blur_ofImage.setObjectName(u"switchButton_blur_ofImage")
        self.switchButton_blur_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_15.addWidget(self.switchButton_blur_ofImage)


        self.verticalLayout_24.addLayout(self.horizontalLayout_15)


        self.verticalLayout_26.addWidget(self.frame_blur_switch_ofImage)

        self.frame_blur_content_ofImage = QFrame(self.tbpg_blur_image)
        self.frame_blur_content_ofImage.setObjectName(u"frame_blur_content_ofImage")
        self.frame_blur_content_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_blur_content_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_blur_content_ofImage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_42 = QLabel(self.frame_blur_content_ofImage)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_25.addWidget(self.label_42)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rbtn_blur_mean_ofImage = QRadioButton(self.frame_blur_content_ofImage)
        self.rbtn_blur_mean_ofImage.setObjectName(u"rbtn_blur_mean_ofImage")
        self.rbtn_blur_mean_ofImage.setMinimumSize(QSize(0, 22))

        self.gridLayout.addWidget(self.rbtn_blur_mean_ofImage, 0, 0, 1, 1)

        self.rbtn_blur_box_ofImage = QRadioButton(self.frame_blur_content_ofImage)
        self.rbtn_blur_box_ofImage.setObjectName(u"rbtn_blur_box_ofImage")
        self.rbtn_blur_box_ofImage.setMinimumSize(QSize(0, 22))

        self.gridLayout.addWidget(self.rbtn_blur_box_ofImage, 0, 1, 1, 1)

        self.rbtn_blur_gaussian_ofImage = QRadioButton(self.frame_blur_content_ofImage)
        self.rbtn_blur_gaussian_ofImage.setObjectName(u"rbtn_blur_gaussian_ofImage")
        self.rbtn_blur_gaussian_ofImage.setMinimumSize(QSize(0, 22))

        self.gridLayout.addWidget(self.rbtn_blur_gaussian_ofImage, 1, 0, 1, 1)

        self.rbtn_blur_median_ofImage = QRadioButton(self.frame_blur_content_ofImage)
        self.rbtn_blur_median_ofImage.setObjectName(u"rbtn_blur_median_ofImage")
        self.rbtn_blur_median_ofImage.setMinimumSize(QSize(0, 22))

        self.gridLayout.addWidget(self.rbtn_blur_median_ofImage, 1, 1, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_45 = QLabel(self.frame_blur_content_ofImage)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_16.addWidget(self.label_45)

        self.spinBox_blurKsize1_ofImage = QSpinBox(self.frame_blur_content_ofImage)
        self.spinBox_blurKsize1_ofImage.setObjectName(u"spinBox_blurKsize1_ofImage")
        self.spinBox_blurKsize1_ofImage.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize1_ofImage.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize1_ofImage.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize1_ofImage.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize1_ofImage.setMinimum(1)

        self.horizontalLayout_16.addWidget(self.spinBox_blurKsize1_ofImage)

        self.label_46 = QLabel(self.frame_blur_content_ofImage)
        self.label_46.setObjectName(u"label_46")
        sizePolicy5.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy5)
        self.label_46.setMinimumSize(QSize(16, 16))
        self.label_46.setMaximumSize(QSize(16, 16))
        self.label_46.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_46)

        self.spinBox_blurKsize2_ofImage = QSpinBox(self.frame_blur_content_ofImage)
        self.spinBox_blurKsize2_ofImage.setObjectName(u"spinBox_blurKsize2_ofImage")
        self.spinBox_blurKsize2_ofImage.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize2_ofImage.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize2_ofImage.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize2_ofImage.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize2_ofImage.setMinimum(1)

        self.horizontalLayout_16.addWidget(self.spinBox_blurKsize2_ofImage)


        self.verticalLayout_25.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.slider_blurKsize1_ofImage = QSlider(self.frame_blur_content_ofImage)
        self.slider_blurKsize1_ofImage.setObjectName(u"slider_blurKsize1_ofImage")
        self.slider_blurKsize1_ofImage.setMinimum(1)
        self.slider_blurKsize1_ofImage.setPageStep(5)
        self.slider_blurKsize1_ofImage.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.slider_blurKsize1_ofImage)

        self.slider_blurKsize2_ofImage = QSlider(self.frame_blur_content_ofImage)
        self.slider_blurKsize2_ofImage.setObjectName(u"slider_blurKsize2_ofImage")
        self.slider_blurKsize2_ofImage.setMinimum(1)
        self.slider_blurKsize2_ofImage.setPageStep(5)
        self.slider_blurKsize2_ofImage.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.slider_blurKsize2_ofImage)


        self.verticalLayout_25.addLayout(self.horizontalLayout_21)


        self.verticalLayout_26.addWidget(self.frame_blur_content_ofImage)

        self.verticalSpacer_14 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_14)

        self.toolBox_imageAugment_image.addItem(self.tbpg_blur_image, u"\u6a21\u7cca")
        self.tbpg_noise_image = QWidget()
        self.tbpg_noise_image.setObjectName(u"tbpg_noise_image")
        self.tbpg_noise_image.setGeometry(QRect(0, 0, 256, 310))
        self.verticalLayout_36 = QVBoxLayout(self.tbpg_noise_image)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_noise_switch_ofImage = QFrame(self.tbpg_noise_image)
        self.frame_noise_switch_ofImage.setObjectName(u"frame_noise_switch_ofImage")
        self.frame_noise_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_noise_switch_ofImage)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_47 = QLabel(self.frame_noise_switch_ofImage)
        self.label_47.setObjectName(u"label_47")
        sizePolicy6.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy6)
        self.label_47.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_31.addWidget(self.label_47)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_21)

        self.switchButton_noise_ofImage = SwitchButton(self.frame_noise_switch_ofImage)
        self.switchButton_noise_ofImage.setObjectName(u"switchButton_noise_ofImage")
        self.switchButton_noise_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_31.addWidget(self.switchButton_noise_ofImage)


        self.verticalLayout_34.addLayout(self.horizontalLayout_31)


        self.verticalLayout_36.addWidget(self.frame_noise_switch_ofImage)

        self.frame_noise_content_ofImage = QFrame(self.tbpg_noise_image)
        self.frame_noise_content_ofImage.setObjectName(u"frame_noise_content_ofImage")
        self.frame_noise_content_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_content_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_noise_content_ofImage)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_48 = QLabel(self.frame_noise_content_ofImage)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_39.addWidget(self.label_48)

        self.cb_noise_gaussian_ofImage = QCheckBox(self.frame_noise_content_ofImage)
        self.cb_noise_gaussian_ofImage.setObjectName(u"cb_noise_gaussian_ofImage")
        self.cb_noise_gaussian_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_39.addWidget(self.cb_noise_gaussian_ofImage)

        self.frame_noise_gaussian_ofImage = QFrame(self.frame_noise_content_ofImage)
        self.frame_noise_gaussian_ofImage.setObjectName(u"frame_noise_gaussian_ofImage")
        self.frame_noise_gaussian_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_gaussian_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_noise_gaussian_ofImage)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 4, 0, 12)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_49 = QLabel(self.frame_noise_gaussian_ofImage)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font-family: none;\n"
"font-weight: 400;\n"
"font-family: \"Microsoft Yahei\";")

        self.horizontalLayout_32.addWidget(self.label_49)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_22)

        self.dSpinBox_noise_sigma_ofImage = QDoubleSpinBox(self.frame_noise_gaussian_ofImage)
        self.dSpinBox_noise_sigma_ofImage.setObjectName(u"dSpinBox_noise_sigma_ofImage")
        self.dSpinBox_noise_sigma_ofImage.setMinimumSize(QSize(92, 20))
        self.dSpinBox_noise_sigma_ofImage.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_sigma_ofImage.setMaximum(100.000000000000000)
        self.dSpinBox_noise_sigma_ofImage.setSingleStep(0.100000000000000)

        self.horizontalLayout_32.addWidget(self.dSpinBox_noise_sigma_ofImage)


        self.verticalLayout_35.addLayout(self.horizontalLayout_32)

        self.slider_noise_sigma_ofImage = QSlider(self.frame_noise_gaussian_ofImage)
        self.slider_noise_sigma_ofImage.setObjectName(u"slider_noise_sigma_ofImage")
        self.slider_noise_sigma_ofImage.setMaximum(10000)
        self.slider_noise_sigma_ofImage.setSingleStep(10)
        self.slider_noise_sigma_ofImage.setPageStep(100)
        self.slider_noise_sigma_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_35.addWidget(self.slider_noise_sigma_ofImage)


        self.verticalLayout_39.addWidget(self.frame_noise_gaussian_ofImage)

        self.cb_noise_saltPepper_ofImage = QCheckBox(self.frame_noise_content_ofImage)
        self.cb_noise_saltPepper_ofImage.setObjectName(u"cb_noise_saltPepper_ofImage")
        self.cb_noise_saltPepper_ofImage.setMinimumSize(QSize(0, 22))

        self.verticalLayout_39.addWidget(self.cb_noise_saltPepper_ofImage)

        self.frame_noise_saltPepper_ofImage = QFrame(self.frame_noise_content_ofImage)
        self.frame_noise_saltPepper_ofImage.setObjectName(u"frame_noise_saltPepper_ofImage")
        self.frame_noise_saltPepper_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_saltPepper_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_noise_saltPepper_ofImage)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 4, 0, 12)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_50 = QLabel(self.frame_noise_saltPepper_ofImage)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font-family: none;\n"
"font-weight: 400;\n"
"font-family: \"Microsoft Yahei\";")

        self.horizontalLayout_33.addWidget(self.label_50)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_23)

        self.dSpinBox_noise_rate_ofImage = QDoubleSpinBox(self.frame_noise_saltPepper_ofImage)
        self.dSpinBox_noise_rate_ofImage.setObjectName(u"dSpinBox_noise_rate_ofImage")
        self.dSpinBox_noise_rate_ofImage.setMinimumSize(QSize(80, 20))
        self.dSpinBox_noise_rate_ofImage.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_rate_ofImage.setMaximum(1.000000000000000)
        self.dSpinBox_noise_rate_ofImage.setSingleStep(0.010000000000000)

        self.horizontalLayout_33.addWidget(self.dSpinBox_noise_rate_ofImage)


        self.verticalLayout_38.addLayout(self.horizontalLayout_33)

        self.slider_noise_rate_ofImage = QSlider(self.frame_noise_saltPepper_ofImage)
        self.slider_noise_rate_ofImage.setObjectName(u"slider_noise_rate_ofImage")
        self.slider_noise_rate_ofImage.setMaximum(100)
        self.slider_noise_rate_ofImage.setSingleStep(1)
        self.slider_noise_rate_ofImage.setPageStep(1)
        self.slider_noise_rate_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_38.addWidget(self.slider_noise_rate_ofImage)


        self.verticalLayout_39.addWidget(self.frame_noise_saltPepper_ofImage)


        self.verticalLayout_36.addWidget(self.frame_noise_content_ofImage)

        self.verticalSpacer_15 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_15)

        self.toolBox_imageAugment_image.addItem(self.tbpg_noise_image, u"\u566a\u58f0")
        self.tbpg_brightness_image = QWidget()
        self.tbpg_brightness_image.setObjectName(u"tbpg_brightness_image")
        self.tbpg_brightness_image.setGeometry(QRect(0, 0, 224, 145))
        self.verticalLayout_42 = QVBoxLayout(self.tbpg_brightness_image)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_brightness_switch_ofImage = QFrame(self.tbpg_brightness_image)
        self.frame_brightness_switch_ofImage.setObjectName(u"frame_brightness_switch_ofImage")
        self.frame_brightness_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_brightness_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_brightness_switch_ofImage)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_51 = QLabel(self.frame_brightness_switch_ofImage)
        self.label_51.setObjectName(u"label_51")
        sizePolicy6.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy6)
        self.label_51.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_34.addWidget(self.label_51)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_24)

        self.switchButton_brightness_ofImage = SwitchButton(self.frame_brightness_switch_ofImage)
        self.switchButton_brightness_ofImage.setObjectName(u"switchButton_brightness_ofImage")
        self.switchButton_brightness_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_34.addWidget(self.switchButton_brightness_ofImage)


        self.verticalLayout_40.addLayout(self.horizontalLayout_34)


        self.verticalLayout_42.addWidget(self.frame_brightness_switch_ofImage)

        self.frame_brightness_content_ofImage = QFrame(self.tbpg_brightness_image)
        self.frame_brightness_content_ofImage.setObjectName(u"frame_brightness_content_ofImage")
        self.frame_brightness_content_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_brightness_content_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_brightness_content_ofImage)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_52 = QLabel(self.frame_brightness_content_ofImage)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_35.addWidget(self.label_52)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_25)

        self.dSpinBox_brightness_ofImage = QDoubleSpinBox(self.frame_brightness_content_ofImage)
        self.dSpinBox_brightness_ofImage.setObjectName(u"dSpinBox_brightness_ofImage")
        self.dSpinBox_brightness_ofImage.setMinimumSize(QSize(100, 20))
        self.dSpinBox_brightness_ofImage.setAlignment(Qt.AlignCenter)
        self.dSpinBox_brightness_ofImage.setMinimum(-200.000000000000000)
        self.dSpinBox_brightness_ofImage.setMaximum(200.000000000000000)
        self.dSpinBox_brightness_ofImage.setSingleStep(5.000000000000000)

        self.horizontalLayout_35.addWidget(self.dSpinBox_brightness_ofImage)


        self.verticalLayout_41.addLayout(self.horizontalLayout_35)

        self.slider_brightness_ofImage = QSlider(self.frame_brightness_content_ofImage)
        self.slider_brightness_ofImage.setObjectName(u"slider_brightness_ofImage")
        self.slider_brightness_ofImage.setMinimum(-20000)
        self.slider_brightness_ofImage.setMaximum(20000)
        self.slider_brightness_ofImage.setSingleStep(100)
        self.slider_brightness_ofImage.setPageStep(500)
        self.slider_brightness_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_41.addWidget(self.slider_brightness_ofImage)


        self.verticalLayout_42.addWidget(self.frame_brightness_content_ofImage)

        self.verticalSpacer_16 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_16)

        self.toolBox_imageAugment_image.addItem(self.tbpg_brightness_image, u"\u4eae\u5ea6")
        self.tbpg_contrast_image = QWidget()
        self.tbpg_contrast_image.setObjectName(u"tbpg_contrast_image")
        self.tbpg_contrast_image.setGeometry(QRect(0, 0, 218, 145))
        self.verticalLayout_45 = QVBoxLayout(self.tbpg_contrast_image)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_contrast_switch_ofImage = QFrame(self.tbpg_contrast_image)
        self.frame_contrast_switch_ofImage.setObjectName(u"frame_contrast_switch_ofImage")
        self.frame_contrast_switch_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_contrast_switch_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_contrast_switch_ofImage)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_53 = QLabel(self.frame_contrast_switch_ofImage)
        self.label_53.setObjectName(u"label_53")
        sizePolicy6.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy6)
        self.label_53.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_36.addWidget(self.label_53)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_26)

        self.switchButton_contrast_ofImage = SwitchButton(self.frame_contrast_switch_ofImage)
        self.switchButton_contrast_ofImage.setObjectName(u"switchButton_contrast_ofImage")
        self.switchButton_contrast_ofImage.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_36.addWidget(self.switchButton_contrast_ofImage)


        self.verticalLayout_43.addLayout(self.horizontalLayout_36)


        self.verticalLayout_45.addWidget(self.frame_contrast_switch_ofImage)

        self.frame_contrast_content_ofImage = QFrame(self.tbpg_contrast_image)
        self.frame_contrast_content_ofImage.setObjectName(u"frame_contrast_content_ofImage")
        self.frame_contrast_content_ofImage.setFrameShape(QFrame.StyledPanel)
        self.frame_contrast_content_ofImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_contrast_content_ofImage)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_54 = QLabel(self.frame_contrast_content_ofImage)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_37.addWidget(self.label_54)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_27)

        self.dSpinBox_contrast_ofImage = QDoubleSpinBox(self.frame_contrast_content_ofImage)
        self.dSpinBox_contrast_ofImage.setObjectName(u"dSpinBox_contrast_ofImage")
        self.dSpinBox_contrast_ofImage.setMinimumSize(QSize(80, 20))
        self.dSpinBox_contrast_ofImage.setAlignment(Qt.AlignCenter)
        self.dSpinBox_contrast_ofImage.setMaximum(2.000000000000000)
        self.dSpinBox_contrast_ofImage.setSingleStep(0.100000000000000)
        self.dSpinBox_contrast_ofImage.setValue(1.000000000000000)

        self.horizontalLayout_37.addWidget(self.dSpinBox_contrast_ofImage)


        self.verticalLayout_44.addLayout(self.horizontalLayout_37)

        self.slider_contrast_ofImage = QSlider(self.frame_contrast_content_ofImage)
        self.slider_contrast_ofImage.setObjectName(u"slider_contrast_ofImage")
        self.slider_contrast_ofImage.setMaximum(200)
        self.slider_contrast_ofImage.setSingleStep(10)
        self.slider_contrast_ofImage.setValue(100)
        self.slider_contrast_ofImage.setOrientation(Qt.Horizontal)

        self.verticalLayout_44.addWidget(self.slider_contrast_ofImage)


        self.verticalLayout_45.addWidget(self.frame_contrast_content_ofImage)

        self.verticalSpacer_17 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_17)

        self.toolBox_imageAugment_image.addItem(self.tbpg_contrast_image, u"\u5bf9\u6bd4\u5ea6")

        self.verticalLayout_47.addWidget(self.toolBox_imageAugment_image)

        self.toolBox_function_image.addItem(self.tbpg_imageAugment_image, u"\u56fe\u50cf\u589e\u5f3a")

        self.horizontalLayout_18.addWidget(self.toolBox_function_image)

        self.frame_3 = QFrame(self.processPage_image)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_70 = QVBoxLayout(self.frame_3)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_70.addItem(self.verticalSpacer_26)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.lb_preTitle_image = QLabel(self.frame_3)
        self.lb_preTitle_image.setObjectName(u"lb_preTitle_image")
        sizePolicy6.setHeightForWidth(self.lb_preTitle_image.sizePolicy().hasHeightForWidth())
        self.lb_preTitle_image.setSizePolicy(sizePolicy6)
        self.lb_preTitle_image.setMaximumSize(QSize(16777215, 16777215))
        self.lb_preTitle_image.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.lb_preTitle_image.setFont(font4)
        self.lb_preTitle_image.setStyleSheet(u"font-size: 38px;\n"
"font-weight: 900;\n"
"color: #495474;\n"
"margin-bottom: 20px;")
        self.lb_preTitle_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.lb_preTitle_image)

        self.lb_pre_image = QLabel(self.frame_3)
        self.lb_pre_image.setObjectName(u"lb_pre_image")
        sizePolicy6.setHeightForWidth(self.lb_pre_image.sizePolicy().hasHeightForWidth())
        self.lb_pre_image.setSizePolicy(sizePolicy6)
        self.lb_pre_image.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pre_image.setStyleSheet(u"color: #BD93F9;\n"
"font-family: \"Microsoft Yahei\";\n"
"font-size: 20px;\n"
"margin-bottom: 30px;")
        self.lb_pre_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.lb_pre_image)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_41)

        self.img_pre_image = QLabel(self.frame_3)
        self.img_pre_image.setObjectName(u"img_pre_image")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.img_pre_image.sizePolicy().hasHeightForWidth())
        self.img_pre_image.setSizePolicy(sizePolicy7)
        self.img_pre_image.setMinimumSize(QSize(360, 360))
        self.img_pre_image.setMaximumSize(QSize(360, 360))
        self.img_pre_image.setStyleSheet(u"background-color: #f0f0f0;")
        self.img_pre_image.setFrameShape(QFrame.Box)

        self.horizontalLayout_61.addWidget(self.img_pre_image)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_40)


        self.verticalLayout_67.addLayout(self.horizontalLayout_61)


        self.horizontalLayout_66.addLayout(self.verticalLayout_67)

        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.lb_afterTitle_image = QLabel(self.frame_3)
        self.lb_afterTitle_image.setObjectName(u"lb_afterTitle_image")
        sizePolicy6.setHeightForWidth(self.lb_afterTitle_image.sizePolicy().hasHeightForWidth())
        self.lb_afterTitle_image.setSizePolicy(sizePolicy6)
        self.lb_afterTitle_image.setMaximumSize(QSize(16777215, 16777215))
        self.lb_afterTitle_image.setSizeIncrement(QSize(0, 0))
        self.lb_afterTitle_image.setFont(font4)
        self.lb_afterTitle_image.setStyleSheet(u"font-size: 38px;\n"
"font-weight: 900;\n"
"color: #495474;\n"
"margin-bottom: 20px;")
        self.lb_afterTitle_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.lb_afterTitle_image)

        self.lb_after_image = QLabel(self.frame_3)
        self.lb_after_image.setObjectName(u"lb_after_image")
        sizePolicy6.setHeightForWidth(self.lb_after_image.sizePolicy().hasHeightForWidth())
        self.lb_after_image.setSizePolicy(sizePolicy6)
        self.lb_after_image.setMaximumSize(QSize(16777215, 16777215))
        self.lb_after_image.setStyleSheet(u"color: #BD93F9;\n"
"font-family: \"Microsoft Yahei\";\n"
"font-size: 20px;\n"
"margin-bottom: 30px;")
        self.lb_after_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.lb_after_image)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_48)

        self.img_after_image = QLabel(self.frame_3)
        self.img_after_image.setObjectName(u"img_after_image")
        sizePolicy7.setHeightForWidth(self.img_after_image.sizePolicy().hasHeightForWidth())
        self.img_after_image.setSizePolicy(sizePolicy7)
        self.img_after_image.setMinimumSize(QSize(360, 360))
        self.img_after_image.setMaximumSize(QSize(360, 360))
        self.img_after_image.setStyleSheet(u"background-color: #f0f0f0;")
        self.img_after_image.setFrameShape(QFrame.Box)

        self.horizontalLayout_65.addWidget(self.img_after_image)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_49)


        self.verticalLayout_69.addLayout(self.horizontalLayout_65)


        self.horizontalLayout_66.addLayout(self.verticalLayout_69)


        self.verticalLayout_70.addLayout(self.horizontalLayout_66)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_70.addItem(self.verticalSpacer_27)

        self.show_algorithm_ofImage = QLabel(self.frame_3)
        self.show_algorithm_ofImage.setObjectName(u"show_algorithm_ofImage")
        self.show_algorithm_ofImage.setMinimumSize(QSize(0, 40))
        self.show_algorithm_ofImage.setMaximumSize(QSize(16777215, 40))
        self.show_algorithm_ofImage.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}")
        self.show_algorithm_ofImage.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_70.addWidget(self.show_algorithm_ofImage)


        self.horizontalLayout_18.addWidget(self.frame_3)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.processPage_image)
        self.processPage_dataset = QWidget()
        self.processPage_dataset.setObjectName(u"processPage_dataset")
        self.processPage_dataset.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272A4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")
        self.verticalLayout_28 = QVBoxLayout(self.processPage_dataset)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 10)
        self.btn_importDataset = QPushButton(self.processPage_dataset)
        self.btn_importDataset.setObjectName(u"btn_importDataset")
        sizePolicy4.setHeightForWidth(self.btn_importDataset.sizePolicy().hasHeightForWidth())
        self.btn_importDataset.setSizePolicy(sizePolicy4)
        self.btn_importDataset.setMinimumSize(QSize(150, 30))
        self.btn_importDataset.setMaximumSize(QSize(150, 30))
        self.btn_importDataset.setFont(font)
        self.btn_importDataset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importDataset.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_importDataset.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.btn_importDataset)

        self.btn_exportResult_dataset = QPushButton(self.processPage_dataset)
        self.btn_exportResult_dataset.setObjectName(u"btn_exportResult_dataset")
        sizePolicy4.setHeightForWidth(self.btn_exportResult_dataset.sizePolicy().hasHeightForWidth())
        self.btn_exportResult_dataset.setSizePolicy(sizePolicy4)
        self.btn_exportResult_dataset.setMinimumSize(QSize(150, 30))
        self.btn_exportResult_dataset.setMaximumSize(QSize(150, 30))
        self.btn_exportResult_dataset.setFont(font)
        self.btn_exportResult_dataset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportResult_dataset.setStyleSheet(u"")
        self.btn_exportResult_dataset.setIcon(icon4)

        self.horizontalLayout_19.addWidget(self.btn_exportResult_dataset)

        self.horizontalSpacer = QSpacerItem(677, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)

        self.btn_preview_dataset = QPushButton(self.processPage_dataset)
        self.btn_preview_dataset.setObjectName(u"btn_preview_dataset")
        sizePolicy4.setHeightForWidth(self.btn_preview_dataset.sizePolicy().hasHeightForWidth())
        self.btn_preview_dataset.setSizePolicy(sizePolicy4)
        self.btn_preview_dataset.setMinimumSize(QSize(80, 30))
        self.btn_preview_dataset.setMaximumSize(QSize(80, 30))
        self.btn_preview_dataset.setFont(font)
        self.btn_preview_dataset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_preview_dataset.setStyleSheet(u"")
        self.btn_preview_dataset.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.btn_preview_dataset)

        self.btn_run_dataset = QPushButton(self.processPage_dataset)
        self.btn_run_dataset.setObjectName(u"btn_run_dataset")
        sizePolicy4.setHeightForWidth(self.btn_run_dataset.sizePolicy().hasHeightForWidth())
        self.btn_run_dataset.setSizePolicy(sizePolicy4)
        self.btn_run_dataset.setMinimumSize(QSize(80, 30))
        self.btn_run_dataset.setMaximumSize(QSize(80, 30))
        self.btn_run_dataset.setFont(font)
        self.btn_run_dataset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_run_dataset.setStyleSheet(u"")
        self.btn_run_dataset.setIcon(icon6)

        self.horizontalLayout_19.addWidget(self.btn_run_dataset)


        self.verticalLayout_28.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.toolBox_function_dataset = QToolBox(self.processPage_dataset)
        self.toolBox_function_dataset.setObjectName(u"toolBox_function_dataset")
        self.toolBox_function_dataset.setMinimumSize(QSize(360, 0))
        self.toolBox_function_dataset.setMaximumSize(QSize(360, 16777215))
        self.toolBox_function_dataset.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton*/\n"
"#toolBox_function QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 8px;	\n"
"	background-color: #7f94d5;\n"
"	font-size: 16px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#toolBox_function QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#toolBox_function QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ToolBox*/\n"
"QToolBox::tab { \n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"	font-weight: 900;\n"
"	padding-right: 10px;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	bac"
                        "kground-color: #495474;\n"
"	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QToolBoxButton {\n"
"	min-height: 46px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:"
                        "/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(226, 135, 249);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QLabel */\n"
"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-pos"
                        "ition: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QDoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255,"
                        " 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:focus {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:hover {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"")
        self.toolBox_function_dataset.setFrameShape(QFrame.Box)
        self.tbpg_processTool = QWidget()
        self.tbpg_processTool.setObjectName(u"tbpg_processTool")
        self.tbpg_processTool.setGeometry(QRect(0, 0, 92, 247))
        self.verticalLayout_48 = QVBoxLayout(self.tbpg_processTool)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.toolBox_process_dataset = QToolBox(self.tbpg_processTool)
        self.toolBox_process_dataset.setObjectName(u"toolBox_process_dataset")
        self.toolBox_process_dataset.setStyleSheet(u"QToolBoxButton {\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QToolBox QScrollArea {	\n"
"	background-color: rgb(226, 234, 255);\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	background-color: #495474;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-right.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}")
        self.toolBox_process_dataset.setFrameShape(QFrame.NoFrame)
        self.tbpg_suffix_dataset = QWidget()
        self.tbpg_suffix_dataset.setObjectName(u"tbpg_suffix_dataset")
        self.tbpg_suffix_dataset.setGeometry(QRect(0, 0, 92, 210))
        self.tbpg_suffix_dataset.setStyleSheet(u"\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #6272a4;\n"
"}")
        self.verticalLayout_50 = QVBoxLayout(self.tbpg_suffix_dataset)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.btn_jpg_ofDataset = QPushButton(self.tbpg_suffix_dataset)
        self.btn_jpg_ofDataset.setObjectName(u"btn_jpg_ofDataset")
        self.btn_jpg_ofDataset.setMinimumSize(QSize(0, 40))
        self.btn_jpg_ofDataset.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_38.addWidget(self.btn_jpg_ofDataset)

        self.rb_jpg_ofDataset = QRadioButton(self.tbpg_suffix_dataset)
        self.rb_jpg_ofDataset.setObjectName(u"rb_jpg_ofDataset")
        self.rb_jpg_ofDataset.setMinimumSize(QSize(30, 30))
        self.rb_jpg_ofDataset.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_38.addWidget(self.rb_jpg_ofDataset)


        self.verticalLayout_50.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.btn_jpeg_ofDataset = QPushButton(self.tbpg_suffix_dataset)
        self.btn_jpeg_ofDataset.setObjectName(u"btn_jpeg_ofDataset")
        self.btn_jpeg_ofDataset.setMinimumSize(QSize(0, 40))
        self.btn_jpeg_ofDataset.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_39.addWidget(self.btn_jpeg_ofDataset)

        self.rb_jpeg_ofDataset = QRadioButton(self.tbpg_suffix_dataset)
        self.rb_jpeg_ofDataset.setObjectName(u"rb_jpeg_ofDataset")
        self.rb_jpeg_ofDataset.setMinimumSize(QSize(30, 30))
        self.rb_jpeg_ofDataset.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_39.addWidget(self.rb_jpeg_ofDataset)


        self.verticalLayout_50.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.btn_png_ofDataset = QPushButton(self.tbpg_suffix_dataset)
        self.btn_png_ofDataset.setObjectName(u"btn_png_ofDataset")
        self.btn_png_ofDataset.setMinimumSize(QSize(0, 40))
        self.btn_png_ofDataset.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_40.addWidget(self.btn_png_ofDataset)

        self.rb_png_ofDataset = QRadioButton(self.tbpg_suffix_dataset)
        self.rb_png_ofDataset.setObjectName(u"rb_png_ofDataset")
        self.rb_png_ofDataset.setMinimumSize(QSize(30, 30))
        self.rb_png_ofDataset.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_40.addWidget(self.rb_png_ofDataset)


        self.verticalLayout_50.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.btn_bmp_ofDataset = QPushButton(self.tbpg_suffix_dataset)
        self.btn_bmp_ofDataset.setObjectName(u"btn_bmp_ofDataset")
        self.btn_bmp_ofDataset.setMinimumSize(QSize(0, 40))
        self.btn_bmp_ofDataset.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_41.addWidget(self.btn_bmp_ofDataset)

        self.rb_bmp_ofDataset = QRadioButton(self.tbpg_suffix_dataset)
        self.rb_bmp_ofDataset.setObjectName(u"rb_bmp_ofDataset")
        self.rb_bmp_ofDataset.setMinimumSize(QSize(30, 30))
        self.rb_bmp_ofDataset.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_41.addWidget(self.rb_bmp_ofDataset)


        self.verticalLayout_50.addLayout(self.horizontalLayout_41)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_2)

        self.toolBox_process_dataset.addItem(self.tbpg_suffix_dataset, u"\u7edf\u4e00\u540e\u7f00")
        self.tbpg_name_dataset = QWidget()
        self.tbpg_name_dataset.setObjectName(u"tbpg_name_dataset")
        self.tbpg_name_dataset.setGeometry(QRect(0, 0, 161, 197))
        self.verticalLayout_52 = QVBoxLayout(self.tbpg_name_dataset)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_2 = QFrame(self.tbpg_name_dataset)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_2)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_51.addWidget(self.label_4)

        self.rbtn_rename1_ofDataset = QRadioButton(self.frame_2)
        self.rbtn_rename1_ofDataset.setObjectName(u"rbtn_rename1_ofDataset")
        self.rbtn_rename1_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_51.addWidget(self.rbtn_rename1_ofDataset)

        self.rbtn_rename2_ofDataset = QRadioButton(self.frame_2)
        self.rbtn_rename2_ofDataset.setObjectName(u"rbtn_rename2_ofDataset")
        self.rbtn_rename2_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_51.addWidget(self.rbtn_rename2_ofDataset)

        self.rbtn_rename3_ofDataset = QRadioButton(self.frame_2)
        self.rbtn_rename3_ofDataset.setObjectName(u"rbtn_rename3_ofDataset")
        self.rbtn_rename3_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_51.addWidget(self.rbtn_rename3_ofDataset)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_51.addWidget(self.label_3)

        self.cb_rename0_ofDataset = QCheckBox(self.frame_2)
        self.cb_rename0_ofDataset.setObjectName(u"cb_rename0_ofDataset")

        self.verticalLayout_51.addWidget(self.cb_rename0_ofDataset)


        self.verticalLayout_52.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 204, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_3)

        self.toolBox_process_dataset.addItem(self.tbpg_name_dataset, u"\u7edf\u4e00\u547d\u540d")
        self.tbpg_resize_dataset = QWidget()
        self.tbpg_resize_dataset.setObjectName(u"tbpg_resize_dataset")
        self.tbpg_resize_dataset.setGeometry(QRect(0, 0, 204, 273))
        self.verticalLayout_57 = QVBoxLayout(self.tbpg_resize_dataset)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_57 = QLabel(self.tbpg_resize_dataset)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_57.addWidget(self.label_57)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.lineEdit_resizepx1_ofDataset = QLineEdit(self.tbpg_resize_dataset)
        self.lineEdit_resizepx1_ofDataset.setObjectName(u"lineEdit_resizepx1_ofDataset")
        self.lineEdit_resizepx1_ofDataset.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_resizepx1_ofDataset.setMaxLength(4)
        self.lineEdit_resizepx1_ofDataset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.lineEdit_resizepx1_ofDataset)

        self.label_55 = QLabel(self.tbpg_resize_dataset)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")

        self.horizontalLayout_46.addWidget(self.label_55)

        self.lineEdit_resizepx2_ofDataset = QLineEdit(self.tbpg_resize_dataset)
        self.lineEdit_resizepx2_ofDataset.setObjectName(u"lineEdit_resizepx2_ofDataset")
        self.lineEdit_resizepx2_ofDataset.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_resizepx2_ofDataset.setMaxLength(4)
        self.lineEdit_resizepx2_ofDataset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.lineEdit_resizepx2_ofDataset)

        self.label_56 = QLabel(self.tbpg_resize_dataset)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")

        self.horizontalLayout_46.addWidget(self.label_56)


        self.verticalLayout_57.addLayout(self.horizontalLayout_46)

        self.label_14 = QLabel(self.tbpg_resize_dataset)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))

        self.verticalLayout_57.addWidget(self.label_14)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.rbtn_INTER_LINEAR_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_LINEAR_ofDataset.setObjectName(u"rbtn_INTER_LINEAR_ofDataset")
        self.rbtn_INTER_LINEAR_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_LINEAR_ofDataset)

        self.rbtn_INTER_NEAREST_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_NEAREST_ofDataset.setObjectName(u"rbtn_INTER_NEAREST_ofDataset")
        self.rbtn_INTER_NEAREST_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_NEAREST_ofDataset)

        self.rbtn_INTER_CUBIC_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_CUBIC_ofDataset.setObjectName(u"rbtn_INTER_CUBIC_ofDataset")
        self.rbtn_INTER_CUBIC_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_CUBIC_ofDataset)

        self.rbtn_INTER_AREA_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_AREA_ofDataset.setObjectName(u"rbtn_INTER_AREA_ofDataset")
        self.rbtn_INTER_AREA_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_AREA_ofDataset)

        self.rbtn_INTER_LANCZOS4_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_LANCZOS4_ofDataset.setObjectName(u"rbtn_INTER_LANCZOS4_ofDataset")
        self.rbtn_INTER_LANCZOS4_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_LANCZOS4_ofDataset)

        self.rbtn_INTER_LINEAR_EXACT_ofDataset = QRadioButton(self.tbpg_resize_dataset)
        self.rbtn_INTER_LINEAR_EXACT_ofDataset.setObjectName(u"rbtn_INTER_LINEAR_EXACT_ofDataset")
        self.rbtn_INTER_LINEAR_EXACT_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_56.addWidget(self.rbtn_INTER_LINEAR_EXACT_ofDataset)


        self.verticalLayout_57.addLayout(self.verticalLayout_56)

        self.verticalSpacer_5 = QSpacerItem(20, 77, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacer_5)

        self.toolBox_process_dataset.addItem(self.tbpg_resize_dataset, u"\u7edf\u4e00\u5927\u5c0f")
        self.tbpg_square_dataset = QWidget()
        self.tbpg_square_dataset.setObjectName(u"tbpg_square_dataset")
        self.tbpg_square_dataset.setGeometry(QRect(0, 0, 239, 374))
        self.verticalLayout_55 = QVBoxLayout(self.tbpg_square_dataset)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.frame_square_method_ofDataset = QFrame(self.tbpg_square_dataset)
        self.frame_square_method_ofDataset.setObjectName(u"frame_square_method_ofDataset")
        self.frame_square_method_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_square_method_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_square_method_ofDataset)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_5 = QLabel(self.frame_square_method_ofDataset)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_53.addWidget(self.label_5)

        self.rbtn_BORDER_CONSTANT_ofDataset = QRadioButton(self.frame_square_method_ofDataset)
        self.rbtn_BORDER_CONSTANT_ofDataset.setObjectName(u"rbtn_BORDER_CONSTANT_ofDataset")
        self.rbtn_BORDER_CONSTANT_ofDataset.setCheckable(True)
        self.rbtn_BORDER_CONSTANT_ofDataset.setChecked(False)

        self.verticalLayout_53.addWidget(self.rbtn_BORDER_CONSTANT_ofDataset)

        self.rbtn_BORDER_REFLECT_ofDataset = QRadioButton(self.frame_square_method_ofDataset)
        self.rbtn_BORDER_REFLECT_ofDataset.setObjectName(u"rbtn_BORDER_REFLECT_ofDataset")

        self.verticalLayout_53.addWidget(self.rbtn_BORDER_REFLECT_ofDataset)

        self.rbtn_BORDER_REPLICATE_ofDataset = QRadioButton(self.frame_square_method_ofDataset)
        self.rbtn_BORDER_REPLICATE_ofDataset.setObjectName(u"rbtn_BORDER_REPLICATE_ofDataset")

        self.verticalLayout_53.addWidget(self.rbtn_BORDER_REPLICATE_ofDataset)

        self.rbtn_BORDER_WRAP_ofDataset = QRadioButton(self.frame_square_method_ofDataset)
        self.rbtn_BORDER_WRAP_ofDataset.setObjectName(u"rbtn_BORDER_WRAP_ofDataset")

        self.verticalLayout_53.addWidget(self.rbtn_BORDER_WRAP_ofDataset)


        self.verticalLayout_55.addWidget(self.frame_square_method_ofDataset)

        self.frame_square_RGB_ofDataset = QFrame(self.tbpg_square_dataset)
        self.frame_square_RGB_ofDataset.setObjectName(u"frame_square_RGB_ofDataset")
        self.frame_square_RGB_ofDataset.setStyleSheet(u"")
        self.frame_square_RGB_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_square_RGB_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_square_RGB_ofDataset)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_7 = QLabel(self.frame_square_RGB_ofDataset)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_45.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_5)

        self.squre_showRGB_ofDataset = QLabel(self.frame_square_RGB_ofDataset)
        self.squre_showRGB_ofDataset.setObjectName(u"squre_showRGB_ofDataset")
        self.squre_showRGB_ofDataset.setMinimumSize(QSize(72, 20))
        self.squre_showRGB_ofDataset.setMaximumSize(QSize(72, 20))
        self.squre_showRGB_ofDataset.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_45.addWidget(self.squre_showRGB_ofDataset)


        self.verticalLayout_54.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_10 = QLabel(self.frame_square_RGB_ofDataset)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_42.addWidget(self.label_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_2)

        self.spinBox_square_ofDataset_R = QSpinBox(self.frame_square_RGB_ofDataset)
        self.spinBox_square_ofDataset_R.setObjectName(u"spinBox_square_ofDataset_R")
        sizePolicy5.setHeightForWidth(self.spinBox_square_ofDataset_R.sizePolicy().hasHeightForWidth())
        self.spinBox_square_ofDataset_R.setSizePolicy(sizePolicy5)
        self.spinBox_square_ofDataset_R.setMinimumSize(QSize(72, 20))
        self.spinBox_square_ofDataset_R.setAlignment(Qt.AlignCenter)
        self.spinBox_square_ofDataset_R.setMaximum(255)
        self.spinBox_square_ofDataset_R.setValue(255)

        self.horizontalLayout_42.addWidget(self.spinBox_square_ofDataset_R)


        self.verticalLayout_54.addLayout(self.horizontalLayout_42)

        self.slider_square_ofDataset_R = QSlider(self.frame_square_RGB_ofDataset)
        self.slider_square_ofDataset_R.setObjectName(u"slider_square_ofDataset_R")
        self.slider_square_ofDataset_R.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"")
        self.slider_square_ofDataset_R.setMaximum(255)
        self.slider_square_ofDataset_R.setSliderPosition(255)
        self.slider_square_ofDataset_R.setOrientation(Qt.Horizontal)

        self.verticalLayout_54.addWidget(self.slider_square_ofDataset_R)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_8 = QLabel(self.frame_square_RGB_ofDataset)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_43.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_3)

        self.spinBox_square_ofDataset_G = QSpinBox(self.frame_square_RGB_ofDataset)
        self.spinBox_square_ofDataset_G.setObjectName(u"spinBox_square_ofDataset_G")
        sizePolicy5.setHeightForWidth(self.spinBox_square_ofDataset_G.sizePolicy().hasHeightForWidth())
        self.spinBox_square_ofDataset_G.setSizePolicy(sizePolicy5)
        self.spinBox_square_ofDataset_G.setMinimumSize(QSize(72, 20))
        self.spinBox_square_ofDataset_G.setAlignment(Qt.AlignCenter)
        self.spinBox_square_ofDataset_G.setMaximum(255)
        self.spinBox_square_ofDataset_G.setValue(255)

        self.horizontalLayout_43.addWidget(self.spinBox_square_ofDataset_G)


        self.verticalLayout_54.addLayout(self.horizontalLayout_43)

        self.slider_square_ofDataset_G = QSlider(self.frame_square_RGB_ofDataset)
        self.slider_square_ofDataset_G.setObjectName(u"slider_square_ofDataset_G")
        self.slider_square_ofDataset_G.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #17ffb9;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #17ffb9;\n"
"}\n"
"")
        self.slider_square_ofDataset_G.setMaximum(255)
        self.slider_square_ofDataset_G.setSliderPosition(255)
        self.slider_square_ofDataset_G.setOrientation(Qt.Horizontal)

        self.verticalLayout_54.addWidget(self.slider_square_ofDataset_G)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_9 = QLabel(self.frame_square_RGB_ofDataset)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_44.addWidget(self.label_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_4)

        self.spinBox_square_ofDataset_B = QSpinBox(self.frame_square_RGB_ofDataset)
        self.spinBox_square_ofDataset_B.setObjectName(u"spinBox_square_ofDataset_B")
        sizePolicy5.setHeightForWidth(self.spinBox_square_ofDataset_B.sizePolicy().hasHeightForWidth())
        self.spinBox_square_ofDataset_B.setSizePolicy(sizePolicy5)
        self.spinBox_square_ofDataset_B.setMinimumSize(QSize(72, 20))
        self.spinBox_square_ofDataset_B.setAlignment(Qt.AlignCenter)
        self.spinBox_square_ofDataset_B.setMaximum(255)
        self.spinBox_square_ofDataset_B.setValue(255)

        self.horizontalLayout_44.addWidget(self.spinBox_square_ofDataset_B)


        self.verticalLayout_54.addLayout(self.horizontalLayout_44)

        self.slider_square_ofDataset_B = QSlider(self.frame_square_RGB_ofDataset)
        self.slider_square_ofDataset_B.setObjectName(u"slider_square_ofDataset_B")
        self.slider_square_ofDataset_B.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"")
        self.slider_square_ofDataset_B.setMaximum(255)
        self.slider_square_ofDataset_B.setSliderPosition(255)
        self.slider_square_ofDataset_B.setOrientation(Qt.Horizontal)

        self.verticalLayout_54.addWidget(self.slider_square_ofDataset_B)


        self.verticalLayout_55.addWidget(self.frame_square_RGB_ofDataset)

        self.verticalSpacer_4 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_4)

        self.toolBox_process_dataset.addItem(self.tbpg_square_dataset, u"\u56fe\u7247\u65b9\u5f62\u5316")
        self.tbpg_split_dataset = QWidget()
        self.tbpg_split_dataset.setObjectName(u"tbpg_split_dataset")
        self.tbpg_split_dataset.setGeometry(QRect(0, 0, 222, 189))
        self.verticalLayout_88 = QVBoxLayout(self.tbpg_split_dataset)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_6 = QLabel(self.tbpg_split_dataset)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_88.addWidget(self.label_6)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_27 = QLabel(self.tbpg_split_dataset)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_73.addWidget(self.label_27)

        self.dSpinBox_split_train_ofDataset = QDoubleSpinBox(self.tbpg_split_dataset)
        self.dSpinBox_split_train_ofDataset.setObjectName(u"dSpinBox_split_train_ofDataset")
        self.dSpinBox_split_train_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_split_train_ofDataset.setMaximumSize(QSize(100, 16777215))
        self.dSpinBox_split_train_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_split_train_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_split_train_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_split_train_ofDataset.setValue(0.800000000000000)

        self.horizontalLayout_73.addWidget(self.dSpinBox_split_train_ofDataset)


        self.verticalLayout_88.addLayout(self.horizontalLayout_73)

        self.slider_split_train_ofDataset = QSlider(self.tbpg_split_dataset)
        self.slider_split_train_ofDataset.setObjectName(u"slider_split_train_ofDataset")
        self.slider_split_train_ofDataset.setMaximum(100)
        self.slider_split_train_ofDataset.setSingleStep(10)
        self.slider_split_train_ofDataset.setValue(80)
        self.slider_split_train_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_88.addWidget(self.slider_split_train_ofDataset)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_43 = QLabel(self.tbpg_split_dataset)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_75.addWidget(self.label_43)

        self.dSpinBox_split_val_ofDataset = QDoubleSpinBox(self.tbpg_split_dataset)
        self.dSpinBox_split_val_ofDataset.setObjectName(u"dSpinBox_split_val_ofDataset")
        self.dSpinBox_split_val_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_split_val_ofDataset.setMaximumSize(QSize(100, 16777215))
        self.dSpinBox_split_val_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_split_val_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_split_val_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_split_val_ofDataset.setValue(0.100000000000000)

        self.horizontalLayout_75.addWidget(self.dSpinBox_split_val_ofDataset)


        self.verticalLayout_88.addLayout(self.horizontalLayout_75)

        self.slider_split_val_ofDataset = QSlider(self.tbpg_split_dataset)
        self.slider_split_val_ofDataset.setObjectName(u"slider_split_val_ofDataset")
        self.slider_split_val_ofDataset.setMaximum(100)
        self.slider_split_val_ofDataset.setSingleStep(10)
        self.slider_split_val_ofDataset.setValue(10)
        self.slider_split_val_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_88.addWidget(self.slider_split_val_ofDataset)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_44 = QLabel(self.tbpg_split_dataset)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_82.addWidget(self.label_44)

        self.dSpinBox_split_test_ofDataset = QDoubleSpinBox(self.tbpg_split_dataset)
        self.dSpinBox_split_test_ofDataset.setObjectName(u"dSpinBox_split_test_ofDataset")
        self.dSpinBox_split_test_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_split_test_ofDataset.setMaximumSize(QSize(100, 16777215))
        self.dSpinBox_split_test_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_split_test_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_split_test_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_split_test_ofDataset.setValue(0.100000000000000)

        self.horizontalLayout_82.addWidget(self.dSpinBox_split_test_ofDataset)


        self.verticalLayout_88.addLayout(self.horizontalLayout_82)

        self.slider_split_test_ofDataset = QSlider(self.tbpg_split_dataset)
        self.slider_split_test_ofDataset.setObjectName(u"slider_split_test_ofDataset")
        self.slider_split_test_ofDataset.setMaximum(100)
        self.slider_split_test_ofDataset.setSingleStep(10)
        self.slider_split_test_ofDataset.setValue(10)
        self.slider_split_test_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_88.addWidget(self.slider_split_test_ofDataset)

        self.verticalSpacer = QSpacerItem(20, 102, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacer)

        self.toolBox_process_dataset.addItem(self.tbpg_split_dataset, u"\u6570\u636e\u96c6\u5206\u5272")

        self.verticalLayout_48.addWidget(self.toolBox_process_dataset)

        self.toolBox_function_dataset.addItem(self.tbpg_processTool, u"\u9884\u5904\u7406\u5de5\u5177")
        self.tbpg_imageAugment_dataset = QWidget()
        self.tbpg_imageAugment_dataset.setObjectName(u"tbpg_imageAugment_dataset")
        self.tbpg_imageAugment_dataset.setGeometry(QRect(0, 0, 92, 319))
        self.verticalLayout_49 = QVBoxLayout(self.tbpg_imageAugment_dataset)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.toolBox_imageAugment_dataset = QToolBox(self.tbpg_imageAugment_dataset)
        self.toolBox_imageAugment_dataset.setObjectName(u"toolBox_imageAugment_dataset")
        self.toolBox_imageAugment_dataset.setStyleSheet(u"QToolBoxButton {\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QToolBox QScrollArea {\n"
"	background-color: rgb(226, 234, 255);\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	background-color: #495474;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-caret-right.png);\n"
"	image-position: left;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}")
        self.tbpg_rotate_dataset = QWidget()
        self.tbpg_rotate_dataset.setObjectName(u"tbpg_rotate_dataset")
        self.tbpg_rotate_dataset.setGeometry(QRect(0, 0, 289, 479))
        self.verticalLayout_59 = QVBoxLayout(self.tbpg_rotate_dataset)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_rotate_switch_ofDataset = QFrame(self.tbpg_rotate_dataset)
        self.frame_rotate_switch_ofDataset.setObjectName(u"frame_rotate_switch_ofDataset")
        self.frame_rotate_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_rotate_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_rotate_switch_ofDataset)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_18 = QLabel(self.frame_rotate_switch_ofDataset)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_56.addWidget(self.label_18)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_33)

        self.switchButton_rotate_ofDataset = SwitchButton(self.frame_rotate_switch_ofDataset)
        self.switchButton_rotate_ofDataset.setObjectName(u"switchButton_rotate_ofDataset")
        self.switchButton_rotate_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_56.addWidget(self.switchButton_rotate_ofDataset)


        self.verticalLayout_60.addLayout(self.horizontalLayout_56)


        self.verticalLayout_59.addWidget(self.frame_rotate_switch_ofDataset)

        self.frame_rotate_content_ofDataset = QFrame(self.tbpg_rotate_dataset)
        self.frame_rotate_content_ofDataset.setObjectName(u"frame_rotate_content_ofDataset")
        self.frame_rotate_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_rotate_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_rotate_content_ofDataset)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_11 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_47.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_6)

        self.dSpinBox_rotate_probability_ofDataset = QDoubleSpinBox(self.frame_rotate_content_ofDataset)
        self.dSpinBox_rotate_probability_ofDataset.setObjectName(u"dSpinBox_rotate_probability_ofDataset")
        self.dSpinBox_rotate_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_rotate_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_rotate_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_rotate_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_rotate_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_47.addWidget(self.dSpinBox_rotate_probability_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_47)

        self.slider_rotate_probability_ofDataset = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotate_probability_ofDataset.setObjectName(u"slider_rotate_probability_ofDataset")
        self.slider_rotate_probability_ofDataset.setMaximum(100)
        self.slider_rotate_probability_ofDataset.setSingleStep(10)
        self.slider_rotate_probability_ofDataset.setValue(100)
        self.slider_rotate_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_58.addWidget(self.slider_rotate_probability_ofDataset)

        self.label_12 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_58.addWidget(self.label_12)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.dSpinBox_rotateDegree1_ofDataset = QDoubleSpinBox(self.frame_rotate_content_ofDataset)
        self.dSpinBox_rotateDegree1_ofDataset.setObjectName(u"dSpinBox_rotateDegree1_ofDataset")
        self.dSpinBox_rotateDegree1_ofDataset.setMinimumSize(QSize(0, 20))
        self.dSpinBox_rotateDegree1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_rotateDegree1_ofDataset.setMinimum(-180.000000000000000)
        self.dSpinBox_rotateDegree1_ofDataset.setMaximum(180.000000000000000)
        self.dSpinBox_rotateDegree1_ofDataset.setSingleStep(10.000000000000000)

        self.horizontalLayout_48.addWidget(self.dSpinBox_rotateDegree1_ofDataset)

        self.label_13 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(16, 16))
        self.label_13.setMaximumSize(QSize(16, 16))
        self.label_13.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_13)

        self.dSpinBox_rotateDegree2_ofDataset = QDoubleSpinBox(self.frame_rotate_content_ofDataset)
        self.dSpinBox_rotateDegree2_ofDataset.setObjectName(u"dSpinBox_rotateDegree2_ofDataset")
        self.dSpinBox_rotateDegree2_ofDataset.setMinimumSize(QSize(0, 20))
        self.dSpinBox_rotateDegree2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_rotateDegree2_ofDataset.setMinimum(-180.000000000000000)
        self.dSpinBox_rotateDegree2_ofDataset.setMaximum(180.000000000000000)
        self.dSpinBox_rotateDegree2_ofDataset.setSingleStep(10.000000000000000)

        self.horizontalLayout_48.addWidget(self.dSpinBox_rotateDegree2_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.slider_rotateDegree1_ofDataset = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotateDegree1_ofDataset.setObjectName(u"slider_rotateDegree1_ofDataset")
        self.slider_rotateDegree1_ofDataset.setMinimum(-18000)
        self.slider_rotateDegree1_ofDataset.setMaximum(18000)
        self.slider_rotateDegree1_ofDataset.setSingleStep(100)
        self.slider_rotateDegree1_ofDataset.setPageStep(1000)
        self.slider_rotateDegree1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_49.addWidget(self.slider_rotateDegree1_ofDataset)

        self.slider_rotateDegree2_ofDataset = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotateDegree2_ofDataset.setObjectName(u"slider_rotateDegree2_ofDataset")
        self.slider_rotateDegree2_ofDataset.setMinimum(-18000)
        self.slider_rotateDegree2_ofDataset.setMaximum(18000)
        self.slider_rotateDegree2_ofDataset.setSingleStep(100)
        self.slider_rotateDegree2_ofDataset.setPageStep(1000)
        self.slider_rotateDegree2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_49.addWidget(self.slider_rotateDegree2_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_49)

        self.label_15 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_58.addWidget(self.label_15)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.dSpinBox_rotateScale1_ofDataset = QDoubleSpinBox(self.frame_rotate_content_ofDataset)
        self.dSpinBox_rotateScale1_ofDataset.setObjectName(u"dSpinBox_rotateScale1_ofDataset")
        self.dSpinBox_rotateScale1_ofDataset.setMinimumSize(QSize(0, 20))
        self.dSpinBox_rotateScale1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_rotateScale1_ofDataset.setMinimum(0.010000000000000)
        self.dSpinBox_rotateScale1_ofDataset.setMaximum(10.000000000000000)
        self.dSpinBox_rotateScale1_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_rotateScale1_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_50.addWidget(self.dSpinBox_rotateScale1_ofDataset)

        self.label_16 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(16, 16))
        self.label_16.setMaximumSize(QSize(16, 16))
        self.label_16.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_16)

        self.dSpinBox_rotateScale2_ofDataset = QDoubleSpinBox(self.frame_rotate_content_ofDataset)
        self.dSpinBox_rotateScale2_ofDataset.setObjectName(u"dSpinBox_rotateScale2_ofDataset")
        self.dSpinBox_rotateScale2_ofDataset.setMinimumSize(QSize(0, 20))
        self.dSpinBox_rotateScale2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_rotateScale2_ofDataset.setMinimum(0.010000000000000)
        self.dSpinBox_rotateScale2_ofDataset.setMaximum(10.000000000000000)
        self.dSpinBox_rotateScale2_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_rotateScale2_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_50.addWidget(self.dSpinBox_rotateScale2_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.slider_rotateScale1_ofDataset = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotateScale1_ofDataset.setObjectName(u"slider_rotateScale1_ofDataset")
        self.slider_rotateScale1_ofDataset.setMinimum(1)
        self.slider_rotateScale1_ofDataset.setMaximum(1000)
        self.slider_rotateScale1_ofDataset.setSingleStep(10)
        self.slider_rotateScale1_ofDataset.setValue(100)
        self.slider_rotateScale1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_51.addWidget(self.slider_rotateScale1_ofDataset)

        self.slider_rotateScale2_ofDataset = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotateScale2_ofDataset.setObjectName(u"slider_rotateScale2_ofDataset")
        self.slider_rotateScale2_ofDataset.setMinimum(1)
        self.slider_rotateScale2_ofDataset.setMaximum(1000)
        self.slider_rotateScale2_ofDataset.setSingleStep(10)
        self.slider_rotateScale2_ofDataset.setValue(100)
        self.slider_rotateScale2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_51.addWidget(self.slider_rotateScale2_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_17 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_52.addWidget(self.label_17)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_29)

        self.rotate_showRGB_ofDataset = QLabel(self.frame_rotate_content_ofDataset)
        self.rotate_showRGB_ofDataset.setObjectName(u"rotate_showRGB_ofDataset")
        sizePolicy5.setHeightForWidth(self.rotate_showRGB_ofDataset.sizePolicy().hasHeightForWidth())
        self.rotate_showRGB_ofDataset.setSizePolicy(sizePolicy5)
        self.rotate_showRGB_ofDataset.setMinimumSize(QSize(72, 20))
        self.rotate_showRGB_ofDataset.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_52.addWidget(self.rotate_showRGB_ofDataset)


        self.verticalLayout_58.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_58 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_53.addWidget(self.label_58)

        self.horizontalSpacer_30 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_30)

        self.spinBox_rotate_ofDataset_R = QSpinBox(self.frame_rotate_content_ofDataset)
        self.spinBox_rotate_ofDataset_R.setObjectName(u"spinBox_rotate_ofDataset_R")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofDataset_R.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofDataset_R.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofDataset_R.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofDataset_R.setAlignment(Qt.AlignCenter)
        self.spinBox_rotate_ofDataset_R.setMaximum(255)
        self.spinBox_rotate_ofDataset_R.setValue(255)

        self.horizontalLayout_53.addWidget(self.spinBox_rotate_ofDataset_R)


        self.verticalLayout_58.addLayout(self.horizontalLayout_53)

        self.slider_rotate_ofDataset_R = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotate_ofDataset_R.setObjectName(u"slider_rotate_ofDataset_R")
        self.slider_rotate_ofDataset_R.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #ff2a5c;\n"
"}\n"
"")
        self.slider_rotate_ofDataset_R.setMaximum(255)
        self.slider_rotate_ofDataset_R.setSliderPosition(255)
        self.slider_rotate_ofDataset_R.setOrientation(Qt.Horizontal)

        self.verticalLayout_58.addWidget(self.slider_rotate_ofDataset_R)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_59 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_54.addWidget(self.label_59)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_31)

        self.spinBox_rotate_ofDataset_G = QSpinBox(self.frame_rotate_content_ofDataset)
        self.spinBox_rotate_ofDataset_G.setObjectName(u"spinBox_rotate_ofDataset_G")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofDataset_G.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofDataset_G.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofDataset_G.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofDataset_G.setAlignment(Qt.AlignCenter)
        self.spinBox_rotate_ofDataset_G.setMaximum(255)
        self.spinBox_rotate_ofDataset_G.setValue(255)

        self.horizontalLayout_54.addWidget(self.spinBox_rotate_ofDataset_G)


        self.verticalLayout_58.addLayout(self.horizontalLayout_54)

        self.slider_rotate_ofDataset_G = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotate_ofDataset_G.setObjectName(u"slider_rotate_ofDataset_G")
        self.slider_rotate_ofDataset_G.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #17ffb9;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #17ffb9;\n"
"}\n"
"")
        self.slider_rotate_ofDataset_G.setMaximum(255)
        self.slider_rotate_ofDataset_G.setSliderPosition(255)
        self.slider_rotate_ofDataset_G.setOrientation(Qt.Horizontal)

        self.verticalLayout_58.addWidget(self.slider_rotate_ofDataset_G)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_60 = QLabel(self.frame_rotate_content_ofDataset)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 18px;")

        self.horizontalLayout_55.addWidget(self.label_60)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_32)

        self.spinBox_rotate_ofDataset_B = QSpinBox(self.frame_rotate_content_ofDataset)
        self.spinBox_rotate_ofDataset_B.setObjectName(u"spinBox_rotate_ofDataset_B")
        sizePolicy5.setHeightForWidth(self.spinBox_rotate_ofDataset_B.sizePolicy().hasHeightForWidth())
        self.spinBox_rotate_ofDataset_B.setSizePolicy(sizePolicy5)
        self.spinBox_rotate_ofDataset_B.setMinimumSize(QSize(72, 20))
        self.spinBox_rotate_ofDataset_B.setAlignment(Qt.AlignCenter)
        self.spinBox_rotate_ofDataset_B.setMaximum(255)
        self.spinBox_rotate_ofDataset_B.setValue(255)

        self.horizontalLayout_55.addWidget(self.spinBox_rotate_ofDataset_B)


        self.verticalLayout_58.addLayout(self.horizontalLayout_55)

        self.slider_rotate_ofDataset_B = QSlider(self.frame_rotate_content_ofDataset)
        self.slider_rotate_ofDataset_B.setObjectName(u"slider_rotate_ofDataset_B")
        self.slider_rotate_ofDataset_B.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #0ce7ff;\n"
"}\n"
"")
        self.slider_rotate_ofDataset_B.setMaximum(255)
        self.slider_rotate_ofDataset_B.setSliderPosition(255)
        self.slider_rotate_ofDataset_B.setOrientation(Qt.Horizontal)

        self.verticalLayout_58.addWidget(self.slider_rotate_ofDataset_B)


        self.verticalLayout_59.addWidget(self.frame_rotate_content_ofDataset)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_6)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_rotate_dataset, u"\u56fe\u50cf\u65cb\u8f6c")
        self.tbpg_HFlip_dataset = QWidget()
        self.tbpg_HFlip_dataset.setObjectName(u"tbpg_HFlip_dataset")
        self.tbpg_HFlip_dataset.setGeometry(QRect(0, 0, 289, 145))
        self.verticalLayout_63 = QVBoxLayout(self.tbpg_HFlip_dataset)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_HFlip_switch_ofDataset = QFrame(self.tbpg_HFlip_dataset)
        self.frame_HFlip_switch_ofDataset.setObjectName(u"frame_HFlip_switch_ofDataset")
        self.frame_HFlip_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_HFlip_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_HFlip_switch_ofDataset)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_19 = QLabel(self.frame_HFlip_switch_ofDataset)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_57.addWidget(self.label_19)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_34)

        self.switchButton_HFlip_ofDataset = SwitchButton(self.frame_HFlip_switch_ofDataset)
        self.switchButton_HFlip_ofDataset.setObjectName(u"switchButton_HFlip_ofDataset")
        self.switchButton_HFlip_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_57.addWidget(self.switchButton_HFlip_ofDataset)


        self.verticalLayout_61.addLayout(self.horizontalLayout_57)


        self.verticalLayout_63.addWidget(self.frame_HFlip_switch_ofDataset)

        self.frame_HFlip_content_ofDataset = QFrame(self.tbpg_HFlip_dataset)
        self.frame_HFlip_content_ofDataset.setObjectName(u"frame_HFlip_content_ofDataset")
        self.frame_HFlip_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_HFlip_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_HFlip_content_ofDataset)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_20 = QLabel(self.frame_HFlip_content_ofDataset)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_58.addWidget(self.label_20)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_7)

        self.dSpinBox_HFlip_probability_ofDataset = QDoubleSpinBox(self.frame_HFlip_content_ofDataset)
        self.dSpinBox_HFlip_probability_ofDataset.setObjectName(u"dSpinBox_HFlip_probability_ofDataset")
        self.dSpinBox_HFlip_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_HFlip_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_HFlip_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_HFlip_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_HFlip_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_58.addWidget(self.dSpinBox_HFlip_probability_ofDataset)


        self.verticalLayout_62.addLayout(self.horizontalLayout_58)

        self.slider_HFlip_probability_ofDataset = QSlider(self.frame_HFlip_content_ofDataset)
        self.slider_HFlip_probability_ofDataset.setObjectName(u"slider_HFlip_probability_ofDataset")
        self.slider_HFlip_probability_ofDataset.setMaximum(100)
        self.slider_HFlip_probability_ofDataset.setSingleStep(10)
        self.slider_HFlip_probability_ofDataset.setValue(100)
        self.slider_HFlip_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_62.addWidget(self.slider_HFlip_probability_ofDataset)


        self.verticalLayout_63.addWidget(self.frame_HFlip_content_ofDataset)

        self.verticalSpacer_18 = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_18)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_HFlip_dataset, u"\u6c34\u5e73\u7ffb\u8f6c")
        self.tbpg_VFlip_dataset = QWidget()
        self.tbpg_VFlip_dataset.setObjectName(u"tbpg_VFlip_dataset")
        self.tbpg_VFlip_dataset.setGeometry(QRect(0, 0, 289, 145))
        self.verticalLayout_66 = QVBoxLayout(self.tbpg_VFlip_dataset)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_VFlip_switch_ofDataset = QFrame(self.tbpg_VFlip_dataset)
        self.frame_VFlip_switch_ofDataset.setObjectName(u"frame_VFlip_switch_ofDataset")
        self.frame_VFlip_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_VFlip_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_VFlip_switch_ofDataset)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_22 = QLabel(self.frame_VFlip_switch_ofDataset)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_60.addWidget(self.label_22)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_35)

        self.switchButton_VFlip_ofDataset = SwitchButton(self.frame_VFlip_switch_ofDataset)
        self.switchButton_VFlip_ofDataset.setObjectName(u"switchButton_VFlip_ofDataset")
        self.switchButton_VFlip_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_60.addWidget(self.switchButton_VFlip_ofDataset)


        self.verticalLayout_65.addLayout(self.horizontalLayout_60)


        self.verticalLayout_66.addWidget(self.frame_VFlip_switch_ofDataset)

        self.frame_VFlip_content_ofDataset = QFrame(self.tbpg_VFlip_dataset)
        self.frame_VFlip_content_ofDataset.setObjectName(u"frame_VFlip_content_ofDataset")
        self.frame_VFlip_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_VFlip_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_VFlip_content_ofDataset)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_21 = QLabel(self.frame_VFlip_content_ofDataset)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_59.addWidget(self.label_21)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_28)

        self.dSpinBox_VFlip_probability_ofDataset = QDoubleSpinBox(self.frame_VFlip_content_ofDataset)
        self.dSpinBox_VFlip_probability_ofDataset.setObjectName(u"dSpinBox_VFlip_probability_ofDataset")
        self.dSpinBox_VFlip_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_VFlip_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_VFlip_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_VFlip_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_VFlip_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_59.addWidget(self.dSpinBox_VFlip_probability_ofDataset)


        self.verticalLayout_64.addLayout(self.horizontalLayout_59)

        self.slider_VFlip_probability_ofDataset = QSlider(self.frame_VFlip_content_ofDataset)
        self.slider_VFlip_probability_ofDataset.setObjectName(u"slider_VFlip_probability_ofDataset")
        self.slider_VFlip_probability_ofDataset.setMaximum(100)
        self.slider_VFlip_probability_ofDataset.setSingleStep(10)
        self.slider_VFlip_probability_ofDataset.setValue(100)
        self.slider_VFlip_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_64.addWidget(self.slider_VFlip_probability_ofDataset)


        self.verticalLayout_66.addWidget(self.frame_VFlip_content_ofDataset)

        self.verticalSpacer_19 = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_19)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_VFlip_dataset, u"\u5782\u76f4\u7ffb\u8f6c")
        self.tbpg_blur_dataset = QWidget()
        self.tbpg_blur_dataset.setObjectName(u"tbpg_blur_dataset")
        self.tbpg_blur_dataset.setGeometry(QRect(0, 0, 289, 353))
        self.verticalLayout_74 = QVBoxLayout(self.tbpg_blur_dataset)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.frame_blur_switch_ofDataset = QFrame(self.tbpg_blur_dataset)
        self.frame_blur_switch_ofDataset.setObjectName(u"frame_blur_switch_ofDataset")
        self.frame_blur_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_blur_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_blur_switch_ofDataset)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_74 = QLabel(self.frame_blur_switch_ofDataset)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_72.addWidget(self.label_74)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_44)

        self.switchButton_blur_ofDataset = SwitchButton(self.frame_blur_switch_ofDataset)
        self.switchButton_blur_ofDataset.setObjectName(u"switchButton_blur_ofDataset")
        self.switchButton_blur_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_72.addWidget(self.switchButton_blur_ofDataset)


        self.verticalLayout_73.addLayout(self.horizontalLayout_72)


        self.verticalLayout_74.addWidget(self.frame_blur_switch_ofDataset)

        self.frame_blur_content_ofDataset = QFrame(self.tbpg_blur_dataset)
        self.frame_blur_content_ofDataset.setObjectName(u"frame_blur_content_ofDataset")
        self.frame_blur_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_blur_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_blur_content_ofDataset)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_70 = QLabel(self.frame_blur_content_ofDataset)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_69.addWidget(self.label_70)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_42)

        self.dSpinBox_blur_probability_ofDataset = QDoubleSpinBox(self.frame_blur_content_ofDataset)
        self.dSpinBox_blur_probability_ofDataset.setObjectName(u"dSpinBox_blur_probability_ofDataset")
        self.dSpinBox_blur_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_blur_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_blur_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_blur_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_blur_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_69.addWidget(self.dSpinBox_blur_probability_ofDataset)


        self.verticalLayout_72.addLayout(self.horizontalLayout_69)

        self.slider_blur_probability_ofDataset = QSlider(self.frame_blur_content_ofDataset)
        self.slider_blur_probability_ofDataset.setObjectName(u"slider_blur_probability_ofDataset")
        self.slider_blur_probability_ofDataset.setMaximum(100)
        self.slider_blur_probability_ofDataset.setSingleStep(10)
        self.slider_blur_probability_ofDataset.setValue(100)
        self.slider_blur_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_72.addWidget(self.slider_blur_probability_ofDataset)

        self.label_71 = QLabel(self.frame_blur_content_ofDataset)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_72.addWidget(self.label_71)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.rbtn_blur_mean_ofDataset = QRadioButton(self.frame_blur_content_ofDataset)
        self.rbtn_blur_mean_ofDataset.setObjectName(u"rbtn_blur_mean_ofDataset")

        self.gridLayout_6.addWidget(self.rbtn_blur_mean_ofDataset, 0, 0, 1, 1)

        self.rbtn_blur_box_ofDataset = QRadioButton(self.frame_blur_content_ofDataset)
        self.rbtn_blur_box_ofDataset.setObjectName(u"rbtn_blur_box_ofDataset")

        self.gridLayout_6.addWidget(self.rbtn_blur_box_ofDataset, 0, 1, 1, 1)

        self.rbtn_blur_gaussian_ofDataset = QRadioButton(self.frame_blur_content_ofDataset)
        self.rbtn_blur_gaussian_ofDataset.setObjectName(u"rbtn_blur_gaussian_ofDataset")

        self.gridLayout_6.addWidget(self.rbtn_blur_gaussian_ofDataset, 1, 0, 1, 1)

        self.rbtn_blur_median_ofDataset = QRadioButton(self.frame_blur_content_ofDataset)
        self.rbtn_blur_median_ofDataset.setObjectName(u"rbtn_blur_median_ofDataset")

        self.gridLayout_6.addWidget(self.rbtn_blur_median_ofDataset, 1, 1, 1, 1)


        self.verticalLayout_72.addLayout(self.gridLayout_6)

        self.label_72 = QLabel(self.frame_blur_content_ofDataset)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_72.addWidget(self.label_72)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_77 = QLabel(self.frame_blur_content_ofDataset)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_70.addWidget(self.label_77)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_43)

        self.spinBox_blurKsize_from1_ofDataset = QSpinBox(self.frame_blur_content_ofDataset)
        self.spinBox_blurKsize_from1_ofDataset.setObjectName(u"spinBox_blurKsize_from1_ofDataset")
        self.spinBox_blurKsize_from1_ofDataset.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize_from1_ofDataset.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize_from1_ofDataset.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize_from1_ofDataset.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize_from1_ofDataset.setMinimum(1)

        self.horizontalLayout_70.addWidget(self.spinBox_blurKsize_from1_ofDataset)

        self.label_73 = QLabel(self.frame_blur_content_ofDataset)
        self.label_73.setObjectName(u"label_73")
        sizePolicy5.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy5)
        self.label_73.setMinimumSize(QSize(16, 16))
        self.label_73.setMaximumSize(QSize(16, 16))
        self.label_73.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.label_73)

        self.spinBox_blurKsize_from2_ofDataset = QSpinBox(self.frame_blur_content_ofDataset)
        self.spinBox_blurKsize_from2_ofDataset.setObjectName(u"spinBox_blurKsize_from2_ofDataset")
        self.spinBox_blurKsize_from2_ofDataset.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize_from2_ofDataset.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize_from2_ofDataset.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize_from2_ofDataset.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize_from2_ofDataset.setMinimum(1)

        self.horizontalLayout_70.addWidget(self.spinBox_blurKsize_from2_ofDataset)


        self.verticalLayout_72.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.slider_blurKsize_from_ofDataset = QSlider(self.frame_blur_content_ofDataset)
        self.slider_blurKsize_from_ofDataset.setObjectName(u"slider_blurKsize_from_ofDataset")
        self.slider_blurKsize_from_ofDataset.setMinimum(1)
        self.slider_blurKsize_from_ofDataset.setPageStep(1)
        self.slider_blurKsize_from_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_71.addWidget(self.slider_blurKsize_from_ofDataset)


        self.verticalLayout_72.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_78 = QLabel(self.frame_blur_content_ofDataset)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_74.addWidget(self.label_78)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_45)

        self.spinBox_blurKsize_to1_ofDataset = QSpinBox(self.frame_blur_content_ofDataset)
        self.spinBox_blurKsize_to1_ofDataset.setObjectName(u"spinBox_blurKsize_to1_ofDataset")
        self.spinBox_blurKsize_to1_ofDataset.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize_to1_ofDataset.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize_to1_ofDataset.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize_to1_ofDataset.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize_to1_ofDataset.setMinimum(1)

        self.horizontalLayout_74.addWidget(self.spinBox_blurKsize_to1_ofDataset)

        self.label_79 = QLabel(self.frame_blur_content_ofDataset)
        self.label_79.setObjectName(u"label_79")
        sizePolicy5.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy5)
        self.label_79.setMinimumSize(QSize(16, 16))
        self.label_79.setMaximumSize(QSize(16, 16))
        self.label_79.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_79)

        self.spinBox_blurKsize_to2_ofDataset = QSpinBox(self.frame_blur_content_ofDataset)
        self.spinBox_blurKsize_to2_ofDataset.setObjectName(u"spinBox_blurKsize_to2_ofDataset")
        self.spinBox_blurKsize_to2_ofDataset.setMinimumSize(QSize(64, 20))
        self.spinBox_blurKsize_to2_ofDataset.setMaximumSize(QSize(16777215, 20))
        self.spinBox_blurKsize_to2_ofDataset.setStyleSheet(u"font-size: 18px;")
        self.spinBox_blurKsize_to2_ofDataset.setAlignment(Qt.AlignCenter)
        self.spinBox_blurKsize_to2_ofDataset.setMinimum(1)

        self.horizontalLayout_74.addWidget(self.spinBox_blurKsize_to2_ofDataset)


        self.verticalLayout_72.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.slider_blurKsize_to_ofDataset = QSlider(self.frame_blur_content_ofDataset)
        self.slider_blurKsize_to_ofDataset.setObjectName(u"slider_blurKsize_to_ofDataset")
        self.slider_blurKsize_to_ofDataset.setMinimum(1)
        self.slider_blurKsize_to_ofDataset.setPageStep(1)
        self.slider_blurKsize_to_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_76.addWidget(self.slider_blurKsize_to_ofDataset)


        self.verticalLayout_72.addLayout(self.horizontalLayout_76)


        self.verticalLayout_74.addWidget(self.frame_blur_content_ofDataset)

        self.verticalSpacer_20 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_74.addItem(self.verticalSpacer_20)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_blur_dataset, u"\u6a21\u7cca")
        self.tbpg_noise_dataset = QWidget()
        self.tbpg_noise_dataset.setObjectName(u"tbpg_noise_dataset")
        self.tbpg_noise_dataset.setGeometry(QRect(0, 0, 289, 391))
        self.verticalLayout_78 = QVBoxLayout(self.tbpg_noise_dataset)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_noise_switch_ofDataset = QFrame(self.tbpg_noise_dataset)
        self.frame_noise_switch_ofDataset.setObjectName(u"frame_noise_switch_ofDataset")
        self.frame_noise_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_noise_switch_ofDataset)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_80 = QLabel(self.frame_noise_switch_ofDataset)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_77.addWidget(self.label_80)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_46)

        self.switchButton_noise_ofDataset = SwitchButton(self.frame_noise_switch_ofDataset)
        self.switchButton_noise_ofDataset.setObjectName(u"switchButton_noise_ofDataset")
        self.switchButton_noise_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_77.addWidget(self.switchButton_noise_ofDataset)


        self.verticalLayout_75.addLayout(self.horizontalLayout_77)


        self.verticalLayout_78.addWidget(self.frame_noise_switch_ofDataset)

        self.frame_noise_content_ofDataset = QFrame(self.tbpg_noise_dataset)
        self.frame_noise_content_ofDataset.setObjectName(u"frame_noise_content_ofDataset")
        self.frame_noise_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_noise_content_ofDataset)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_81 = QLabel(self.frame_noise_content_ofDataset)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_78.addWidget(self.label_81)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_47)

        self.dSpinBox_noise_probability_ofDataset = QDoubleSpinBox(self.frame_noise_content_ofDataset)
        self.dSpinBox_noise_probability_ofDataset.setObjectName(u"dSpinBox_noise_probability_ofDataset")
        self.dSpinBox_noise_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_noise_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_noise_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_noise_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_78.addWidget(self.dSpinBox_noise_probability_ofDataset)


        self.verticalLayout_77.addLayout(self.horizontalLayout_78)

        self.slider_noise_probability_ofDataset = QSlider(self.frame_noise_content_ofDataset)
        self.slider_noise_probability_ofDataset.setObjectName(u"slider_noise_probability_ofDataset")
        self.slider_noise_probability_ofDataset.setMaximum(100)
        self.slider_noise_probability_ofDataset.setSingleStep(10)
        self.slider_noise_probability_ofDataset.setValue(100)
        self.slider_noise_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_77.addWidget(self.slider_noise_probability_ofDataset)

        self.cb_noise_gaussian_ofDataset = QCheckBox(self.frame_noise_content_ofDataset)
        self.cb_noise_gaussian_ofDataset.setObjectName(u"cb_noise_gaussian_ofDataset")
        self.cb_noise_gaussian_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_77.addWidget(self.cb_noise_gaussian_ofDataset)

        self.frame_noise_gaussian_ofDataset = QFrame(self.frame_noise_content_ofDataset)
        self.frame_noise_gaussian_ofDataset.setObjectName(u"frame_noise_gaussian_ofDataset")
        self.frame_noise_gaussian_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_gaussian_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_noise_gaussian_ofDataset)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 4, 0, 12)
        self.label_82 = QLabel(self.frame_noise_gaussian_ofDataset)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"font-family: none;\n"
"font-weight: 400;\n"
"font-family: \"Microsoft Yahei\";")

        self.verticalLayout_68.addWidget(self.label_82)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.dSpinBox_noise_sigma1_ofDataset = QDoubleSpinBox(self.frame_noise_gaussian_ofDataset)
        self.dSpinBox_noise_sigma1_ofDataset.setObjectName(u"dSpinBox_noise_sigma1_ofDataset")
        self.dSpinBox_noise_sigma1_ofDataset.setMinimumSize(QSize(92, 20))
        self.dSpinBox_noise_sigma1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_sigma1_ofDataset.setMaximum(100.000000000000000)
        self.dSpinBox_noise_sigma1_ofDataset.setSingleStep(0.100000000000000)

        self.horizontalLayout_79.addWidget(self.dSpinBox_noise_sigma1_ofDataset)

        self.label_83 = QLabel(self.frame_noise_gaussian_ofDataset)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(16, 16))
        self.label_83.setMaximumSize(QSize(16, 16))
        self.label_83.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_83)

        self.dSpinBox_noise_sigma2_ofDataset = QDoubleSpinBox(self.frame_noise_gaussian_ofDataset)
        self.dSpinBox_noise_sigma2_ofDataset.setObjectName(u"dSpinBox_noise_sigma2_ofDataset")
        self.dSpinBox_noise_sigma2_ofDataset.setMinimumSize(QSize(92, 20))
        self.dSpinBox_noise_sigma2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_sigma2_ofDataset.setMaximum(100.000000000000000)
        self.dSpinBox_noise_sigma2_ofDataset.setSingleStep(0.100000000000000)

        self.horizontalLayout_79.addWidget(self.dSpinBox_noise_sigma2_ofDataset)


        self.verticalLayout_68.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.slider_noise_sigma1_ofDataset = QSlider(self.frame_noise_gaussian_ofDataset)
        self.slider_noise_sigma1_ofDataset.setObjectName(u"slider_noise_sigma1_ofDataset")
        self.slider_noise_sigma1_ofDataset.setMaximum(10000)
        self.slider_noise_sigma1_ofDataset.setSingleStep(10)
        self.slider_noise_sigma1_ofDataset.setPageStep(100)
        self.slider_noise_sigma1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_80.addWidget(self.slider_noise_sigma1_ofDataset)

        self.slider_noise_sigma2_ofDataset = QSlider(self.frame_noise_gaussian_ofDataset)
        self.slider_noise_sigma2_ofDataset.setObjectName(u"slider_noise_sigma2_ofDataset")
        self.slider_noise_sigma2_ofDataset.setMaximum(10000)
        self.slider_noise_sigma2_ofDataset.setSingleStep(10)
        self.slider_noise_sigma2_ofDataset.setPageStep(100)
        self.slider_noise_sigma2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_80.addWidget(self.slider_noise_sigma2_ofDataset)


        self.verticalLayout_68.addLayout(self.horizontalLayout_80)


        self.verticalLayout_77.addWidget(self.frame_noise_gaussian_ofDataset)

        self.cb_noise_saltPepper_ofDataset = QCheckBox(self.frame_noise_content_ofDataset)
        self.cb_noise_saltPepper_ofDataset.setObjectName(u"cb_noise_saltPepper_ofDataset")
        self.cb_noise_saltPepper_ofDataset.setMinimumSize(QSize(0, 22))

        self.verticalLayout_77.addWidget(self.cb_noise_saltPepper_ofDataset)

        self.frame_noise_saltPepper_ofDataset = QFrame(self.frame_noise_content_ofDataset)
        self.frame_noise_saltPepper_ofDataset.setObjectName(u"frame_noise_saltPepper_ofDataset")
        self.frame_noise_saltPepper_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_noise_saltPepper_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_noise_saltPepper_ofDataset)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 6, 0, 12)
        self.label_86 = QLabel(self.frame_noise_saltPepper_ofDataset)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font-family: none;\n"
"font-weight: 400;\n"
"font-family: \"Microsoft Yahei\";")

        self.verticalLayout_76.addWidget(self.label_86)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.dSpinBox_noise_rate1_ofDataset = QDoubleSpinBox(self.frame_noise_saltPepper_ofDataset)
        self.dSpinBox_noise_rate1_ofDataset.setObjectName(u"dSpinBox_noise_rate1_ofDataset")
        self.dSpinBox_noise_rate1_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_noise_rate1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_rate1_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_noise_rate1_ofDataset.setSingleStep(0.010000000000000)

        self.horizontalLayout_83.addWidget(self.dSpinBox_noise_rate1_ofDataset)

        self.label_87 = QLabel(self.frame_noise_saltPepper_ofDataset)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(16, 16))
        self.label_87.setMaximumSize(QSize(16, 16))
        self.label_87.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_83.addWidget(self.label_87)

        self.dSpinBox_noise_rate2_ofDataset = QDoubleSpinBox(self.frame_noise_saltPepper_ofDataset)
        self.dSpinBox_noise_rate2_ofDataset.setObjectName(u"dSpinBox_noise_rate2_ofDataset")
        self.dSpinBox_noise_rate2_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_noise_rate2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_noise_rate2_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_noise_rate2_ofDataset.setSingleStep(0.010000000000000)

        self.horizontalLayout_83.addWidget(self.dSpinBox_noise_rate2_ofDataset)


        self.verticalLayout_76.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.slider_noise_rate1_ofDataset = QSlider(self.frame_noise_saltPepper_ofDataset)
        self.slider_noise_rate1_ofDataset.setObjectName(u"slider_noise_rate1_ofDataset")
        self.slider_noise_rate1_ofDataset.setMaximum(100)
        self.slider_noise_rate1_ofDataset.setSingleStep(1)
        self.slider_noise_rate1_ofDataset.setPageStep(1)
        self.slider_noise_rate1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_84.addWidget(self.slider_noise_rate1_ofDataset)

        self.slider_noise_rate2_ofDataset = QSlider(self.frame_noise_saltPepper_ofDataset)
        self.slider_noise_rate2_ofDataset.setObjectName(u"slider_noise_rate2_ofDataset")
        self.slider_noise_rate2_ofDataset.setMaximum(100)
        self.slider_noise_rate2_ofDataset.setSingleStep(1)
        self.slider_noise_rate2_ofDataset.setPageStep(1)
        self.slider_noise_rate2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_84.addWidget(self.slider_noise_rate2_ofDataset)


        self.verticalLayout_76.addLayout(self.horizontalLayout_84)


        self.verticalLayout_77.addWidget(self.frame_noise_saltPepper_ofDataset)


        self.verticalLayout_78.addWidget(self.frame_noise_content_ofDataset)

        self.verticalSpacer_21 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_78.addItem(self.verticalSpacer_21)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_noise_dataset, u"\u566a\u58f0")
        self.tbpg_brightness_dataset = QWidget()
        self.tbpg_brightness_dataset.setObjectName(u"tbpg_brightness_dataset")
        self.tbpg_brightness_dataset.setGeometry(QRect(0, 0, 289, 220))
        self.verticalLayout_81 = QVBoxLayout(self.tbpg_brightness_dataset)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_brightness_switch_ofDataset = QFrame(self.tbpg_brightness_dataset)
        self.frame_brightness_switch_ofDataset.setObjectName(u"frame_brightness_switch_ofDataset")
        self.frame_brightness_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_brightness_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_brightness_switch_ofDataset)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_88 = QLabel(self.frame_brightness_switch_ofDataset)
        self.label_88.setObjectName(u"label_88")
        sizePolicy6.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy6)
        self.label_88.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_85.addWidget(self.label_88)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_50)

        self.switchButton_brightness_ofDataset = SwitchButton(self.frame_brightness_switch_ofDataset)
        self.switchButton_brightness_ofDataset.setObjectName(u"switchButton_brightness_ofDataset")
        self.switchButton_brightness_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_85.addWidget(self.switchButton_brightness_ofDataset)


        self.verticalLayout_79.addLayout(self.horizontalLayout_85)


        self.verticalLayout_81.addWidget(self.frame_brightness_switch_ofDataset)

        self.frame_brightness_content_ofDataset = QFrame(self.tbpg_brightness_dataset)
        self.frame_brightness_content_ofDataset.setObjectName(u"frame_brightness_content_ofDataset")
        self.frame_brightness_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_brightness_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_brightness_content_ofDataset)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_84 = QLabel(self.frame_brightness_content_ofDataset)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_81.addWidget(self.label_84)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_52)

        self.dSpinBox_brightness_probability_ofDataset = QDoubleSpinBox(self.frame_brightness_content_ofDataset)
        self.dSpinBox_brightness_probability_ofDataset.setObjectName(u"dSpinBox_brightness_probability_ofDataset")
        self.dSpinBox_brightness_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_brightness_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_brightness_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_brightness_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_brightness_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_81.addWidget(self.dSpinBox_brightness_probability_ofDataset)


        self.verticalLayout_80.addLayout(self.horizontalLayout_81)

        self.slider_brightness_probability_ofDataset = QSlider(self.frame_brightness_content_ofDataset)
        self.slider_brightness_probability_ofDataset.setObjectName(u"slider_brightness_probability_ofDataset")
        self.slider_brightness_probability_ofDataset.setMaximum(100)
        self.slider_brightness_probability_ofDataset.setSingleStep(10)
        self.slider_brightness_probability_ofDataset.setValue(100)
        self.slider_brightness_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_80.addWidget(self.slider_brightness_probability_ofDataset)

        self.label_89 = QLabel(self.frame_brightness_content_ofDataset)
        self.label_89.setObjectName(u"label_89")

        self.verticalLayout_80.addWidget(self.label_89)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.dSpinBox_brightness_beta1_ofDataset = QDoubleSpinBox(self.frame_brightness_content_ofDataset)
        self.dSpinBox_brightness_beta1_ofDataset.setObjectName(u"dSpinBox_brightness_beta1_ofDataset")
        self.dSpinBox_brightness_beta1_ofDataset.setMinimumSize(QSize(100, 20))
        self.dSpinBox_brightness_beta1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_brightness_beta1_ofDataset.setMinimum(-200.000000000000000)
        self.dSpinBox_brightness_beta1_ofDataset.setMaximum(200.000000000000000)
        self.dSpinBox_brightness_beta1_ofDataset.setSingleStep(5.000000000000000)

        self.horizontalLayout_86.addWidget(self.dSpinBox_brightness_beta1_ofDataset)

        self.label_90 = QLabel(self.frame_brightness_content_ofDataset)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(16, 16))
        self.label_90.setMaximumSize(QSize(16, 16))
        self.label_90.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.label_90)

        self.dSpinBox_brightness_beta2_ofDataset = QDoubleSpinBox(self.frame_brightness_content_ofDataset)
        self.dSpinBox_brightness_beta2_ofDataset.setObjectName(u"dSpinBox_brightness_beta2_ofDataset")
        self.dSpinBox_brightness_beta2_ofDataset.setMinimumSize(QSize(100, 20))
        self.dSpinBox_brightness_beta2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_brightness_beta2_ofDataset.setMinimum(-200.000000000000000)
        self.dSpinBox_brightness_beta2_ofDataset.setMaximum(200.000000000000000)
        self.dSpinBox_brightness_beta2_ofDataset.setSingleStep(5.000000000000000)

        self.horizontalLayout_86.addWidget(self.dSpinBox_brightness_beta2_ofDataset)


        self.verticalLayout_80.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.slider_brightness_beta1_ofDataset = QSlider(self.frame_brightness_content_ofDataset)
        self.slider_brightness_beta1_ofDataset.setObjectName(u"slider_brightness_beta1_ofDataset")
        self.slider_brightness_beta1_ofDataset.setMinimum(-20000)
        self.slider_brightness_beta1_ofDataset.setMaximum(20000)
        self.slider_brightness_beta1_ofDataset.setSingleStep(100)
        self.slider_brightness_beta1_ofDataset.setPageStep(500)
        self.slider_brightness_beta1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_87.addWidget(self.slider_brightness_beta1_ofDataset)

        self.slider_brightness_beta2_ofDataset = QSlider(self.frame_brightness_content_ofDataset)
        self.slider_brightness_beta2_ofDataset.setObjectName(u"slider_brightness_beta2_ofDataset")
        self.slider_brightness_beta2_ofDataset.setMinimum(-20000)
        self.slider_brightness_beta2_ofDataset.setMaximum(20000)
        self.slider_brightness_beta2_ofDataset.setSingleStep(100)
        self.slider_brightness_beta2_ofDataset.setPageStep(500)
        self.slider_brightness_beta2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_87.addWidget(self.slider_brightness_beta2_ofDataset)


        self.verticalLayout_80.addLayout(self.horizontalLayout_87)


        self.verticalLayout_81.addWidget(self.frame_brightness_content_ofDataset)

        self.verticalSpacer_22 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_22)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_brightness_dataset, u"\u4eae\u5ea6")
        self.tbpg_contrast_dataset = QWidget()
        self.tbpg_contrast_dataset.setObjectName(u"tbpg_contrast_dataset")
        self.tbpg_contrast_dataset.setGeometry(QRect(0, 0, 289, 220))
        self.verticalLayout_84 = QVBoxLayout(self.tbpg_contrast_dataset)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_contrast_switch_ofDataset = QFrame(self.tbpg_contrast_dataset)
        self.frame_contrast_switch_ofDataset.setObjectName(u"frame_contrast_switch_ofDataset")
        self.frame_contrast_switch_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_contrast_switch_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_contrast_switch_ofDataset)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_91 = QLabel(self.frame_contrast_switch_ofDataset)
        self.label_91.setObjectName(u"label_91")
        sizePolicy6.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy6)
        self.label_91.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_88.addWidget(self.label_91)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_51)

        self.switchButton_contrast_ofDataset = SwitchButton(self.frame_contrast_switch_ofDataset)
        self.switchButton_contrast_ofDataset.setObjectName(u"switchButton_contrast_ofDataset")
        self.switchButton_contrast_ofDataset.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_88.addWidget(self.switchButton_contrast_ofDataset)


        self.verticalLayout_82.addLayout(self.horizontalLayout_88)


        self.verticalLayout_84.addWidget(self.frame_contrast_switch_ofDataset)

        self.frame_contrast_content_ofDataset = QFrame(self.tbpg_contrast_dataset)
        self.frame_contrast_content_ofDataset.setObjectName(u"frame_contrast_content_ofDataset")
        self.frame_contrast_content_ofDataset.setFrameShape(QFrame.StyledPanel)
        self.frame_contrast_content_ofDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_contrast_content_ofDataset)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_94 = QLabel(self.frame_contrast_content_ofDataset)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_91.addWidget(self.label_94)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_54)

        self.dSpinBox_contrast_probability_ofDataset = QDoubleSpinBox(self.frame_contrast_content_ofDataset)
        self.dSpinBox_contrast_probability_ofDataset.setObjectName(u"dSpinBox_contrast_probability_ofDataset")
        self.dSpinBox_contrast_probability_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_contrast_probability_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_contrast_probability_ofDataset.setMaximum(1.000000000000000)
        self.dSpinBox_contrast_probability_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_contrast_probability_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_91.addWidget(self.dSpinBox_contrast_probability_ofDataset)


        self.verticalLayout_83.addLayout(self.horizontalLayout_91)

        self.slider_contrast_probability_ofDataset = QSlider(self.frame_contrast_content_ofDataset)
        self.slider_contrast_probability_ofDataset.setObjectName(u"slider_contrast_probability_ofDataset")
        self.slider_contrast_probability_ofDataset.setMaximum(100)
        self.slider_contrast_probability_ofDataset.setSingleStep(10)
        self.slider_contrast_probability_ofDataset.setValue(100)
        self.slider_contrast_probability_ofDataset.setOrientation(Qt.Horizontal)

        self.verticalLayout_83.addWidget(self.slider_contrast_probability_ofDataset)

        self.label_92 = QLabel(self.frame_contrast_content_ofDataset)
        self.label_92.setObjectName(u"label_92")

        self.verticalLayout_83.addWidget(self.label_92)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.dSpinBox_contrast_alpha1_ofDataset = QDoubleSpinBox(self.frame_contrast_content_ofDataset)
        self.dSpinBox_contrast_alpha1_ofDataset.setObjectName(u"dSpinBox_contrast_alpha1_ofDataset")
        self.dSpinBox_contrast_alpha1_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_contrast_alpha1_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_contrast_alpha1_ofDataset.setMaximum(2.000000000000000)
        self.dSpinBox_contrast_alpha1_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_contrast_alpha1_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_89.addWidget(self.dSpinBox_contrast_alpha1_ofDataset)

        self.label_93 = QLabel(self.frame_contrast_content_ofDataset)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(16, 16))
        self.label_93.setMaximumSize(QSize(16, 16))
        self.label_93.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.label_93)

        self.dSpinBox_contrast_alpha2_ofDataset = QDoubleSpinBox(self.frame_contrast_content_ofDataset)
        self.dSpinBox_contrast_alpha2_ofDataset.setObjectName(u"dSpinBox_contrast_alpha2_ofDataset")
        self.dSpinBox_contrast_alpha2_ofDataset.setMinimumSize(QSize(80, 20))
        self.dSpinBox_contrast_alpha2_ofDataset.setAlignment(Qt.AlignCenter)
        self.dSpinBox_contrast_alpha2_ofDataset.setMaximum(2.000000000000000)
        self.dSpinBox_contrast_alpha2_ofDataset.setSingleStep(0.100000000000000)
        self.dSpinBox_contrast_alpha2_ofDataset.setValue(1.000000000000000)

        self.horizontalLayout_89.addWidget(self.dSpinBox_contrast_alpha2_ofDataset)


        self.verticalLayout_83.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.slider_contrast_alpha1_ofDataset = QSlider(self.frame_contrast_content_ofDataset)
        self.slider_contrast_alpha1_ofDataset.setObjectName(u"slider_contrast_alpha1_ofDataset")
        self.slider_contrast_alpha1_ofDataset.setMaximum(200)
        self.slider_contrast_alpha1_ofDataset.setSingleStep(10)
        self.slider_contrast_alpha1_ofDataset.setValue(100)
        self.slider_contrast_alpha1_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_90.addWidget(self.slider_contrast_alpha1_ofDataset)

        self.slider_contrast_alpha2_ofDataset = QSlider(self.frame_contrast_content_ofDataset)
        self.slider_contrast_alpha2_ofDataset.setObjectName(u"slider_contrast_alpha2_ofDataset")
        self.slider_contrast_alpha2_ofDataset.setMaximum(200)
        self.slider_contrast_alpha2_ofDataset.setSingleStep(10)
        self.slider_contrast_alpha2_ofDataset.setValue(100)
        self.slider_contrast_alpha2_ofDataset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_90.addWidget(self.slider_contrast_alpha2_ofDataset)


        self.verticalLayout_83.addLayout(self.horizontalLayout_90)


        self.verticalLayout_84.addWidget(self.frame_contrast_content_ofDataset)

        self.verticalSpacer_23 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_84.addItem(self.verticalSpacer_23)

        self.toolBox_imageAugment_dataset.addItem(self.tbpg_contrast_dataset, u"\u5bf9\u6bd4\u5ea6")

        self.verticalLayout_49.addWidget(self.toolBox_imageAugment_dataset)

        self.toolBox_function_dataset.addItem(self.tbpg_imageAugment_dataset, u"\u56fe\u50cf\u589e\u5f3a")

        self.horizontalLayout_20.addWidget(self.toolBox_function_dataset)

        self.frame = QFrame(self.processPage_dataset)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_86 = QVBoxLayout(self.frame)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_86.addItem(self.verticalSpacer_25)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.lb_preTitle_dataset = QLabel(self.frame)
        self.lb_preTitle_dataset.setObjectName(u"lb_preTitle_dataset")
        sizePolicy6.setHeightForWidth(self.lb_preTitle_dataset.sizePolicy().hasHeightForWidth())
        self.lb_preTitle_dataset.setSizePolicy(sizePolicy6)
        self.lb_preTitle_dataset.setSizeIncrement(QSize(0, 0))
        self.lb_preTitle_dataset.setFont(font4)
        self.lb_preTitle_dataset.setStyleSheet(u"font-size: 38px;\n"
"font-weight: 900;\n"
"color: #495474;\n"
"margin-bottom: 20px;")
        self.lb_preTitle_dataset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.lb_preTitle_dataset)

        self.lb_pre_dataset = QLabel(self.frame)
        self.lb_pre_dataset.setObjectName(u"lb_pre_dataset")
        sizePolicy6.setHeightForWidth(self.lb_pre_dataset.sizePolicy().hasHeightForWidth())
        self.lb_pre_dataset.setSizePolicy(sizePolicy6)
        self.lb_pre_dataset.setStyleSheet(u"color: #BD93F9;\n"
"font-family: \"Microsoft Yahei\";\n"
"font-size: 20px;\n"
"margin-bottom: 30px;")
        self.lb_pre_dataset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.lb_pre_dataset)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_36)

        self.img_pre_dataset = QLabel(self.frame)
        self.img_pre_dataset.setObjectName(u"img_pre_dataset")
        sizePolicy7.setHeightForWidth(self.img_pre_dataset.sizePolicy().hasHeightForWidth())
        self.img_pre_dataset.setSizePolicy(sizePolicy7)
        self.img_pre_dataset.setMinimumSize(QSize(360, 360))
        self.img_pre_dataset.setMaximumSize(QSize(360, 360))
        self.img_pre_dataset.setStyleSheet(u"background-color: #f0f0f0;")
        self.img_pre_dataset.setFrameShape(QFrame.Box)

        self.horizontalLayout_62.addWidget(self.img_pre_dataset)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_37)


        self.verticalLayout_71.addLayout(self.horizontalLayout_62)


        self.horizontalLayout_64.addLayout(self.verticalLayout_71)

        self.verticalLayout_85 = QVBoxLayout()
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.lb_afterTitle_dataset = QLabel(self.frame)
        self.lb_afterTitle_dataset.setObjectName(u"lb_afterTitle_dataset")
        sizePolicy6.setHeightForWidth(self.lb_afterTitle_dataset.sizePolicy().hasHeightForWidth())
        self.lb_afterTitle_dataset.setSizePolicy(sizePolicy6)
        self.lb_afterTitle_dataset.setSizeIncrement(QSize(0, 0))
        self.lb_afterTitle_dataset.setFont(font4)
        self.lb_afterTitle_dataset.setStyleSheet(u"font-size: 38px;\n"
"font-weight: 900;\n"
"color: #495474;\n"
"margin-bottom: 20px;")
        self.lb_afterTitle_dataset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.lb_afterTitle_dataset)

        self.lb_after_dataset = QLabel(self.frame)
        self.lb_after_dataset.setObjectName(u"lb_after_dataset")
        sizePolicy6.setHeightForWidth(self.lb_after_dataset.sizePolicy().hasHeightForWidth())
        self.lb_after_dataset.setSizePolicy(sizePolicy6)
        self.lb_after_dataset.setStyleSheet(u"color: #BD93F9;\n"
"font-family: \"Microsoft Yahei\";\n"
"font-size: 20px;\n"
"margin-bottom: 30px;")
        self.lb_after_dataset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.lb_after_dataset)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_38)

        self.img_after_dataset = QLabel(self.frame)
        self.img_after_dataset.setObjectName(u"img_after_dataset")
        sizePolicy7.setHeightForWidth(self.img_after_dataset.sizePolicy().hasHeightForWidth())
        self.img_after_dataset.setSizePolicy(sizePolicy7)
        self.img_after_dataset.setMinimumSize(QSize(360, 360))
        self.img_after_dataset.setMaximumSize(QSize(360, 360))
        self.img_after_dataset.setStyleSheet(u"background-color: #f0f0f0;")
        self.img_after_dataset.setFrameShape(QFrame.Box)

        self.horizontalLayout_63.addWidget(self.img_after_dataset)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_39)


        self.verticalLayout_85.addLayout(self.horizontalLayout_63)


        self.horizontalLayout_64.addLayout(self.verticalLayout_85)


        self.verticalLayout_86.addLayout(self.horizontalLayout_64)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_86.addItem(self.verticalSpacer_24)

        self.show_algorithm_ofDataset = QLabel(self.frame)
        self.show_algorithm_ofDataset.setObjectName(u"show_algorithm_ofDataset")
        self.show_algorithm_ofDataset.setMinimumSize(QSize(0, 40))
        self.show_algorithm_ofDataset.setMaximumSize(QSize(16777215, 40))
        self.show_algorithm_ofDataset.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}")
        self.show_algorithm_ofDataset.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_86.addWidget(self.show_algorithm_ofDataset)


        self.horizontalLayout_20.addWidget(self.frame)


        self.verticalLayout_28.addLayout(self.horizontalLayout_20)

        self.stackedWidget.addWidget(self.processPage_dataset)
        self.trainer = QWidget()
        self.trainer.setObjectName(u"trainer")
        self.trainer.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272A4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.trainer)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(-1, -1, -1, 10)
        self.btn_import_datasetSplit = QPushButton(self.trainer)
        self.btn_import_datasetSplit.setObjectName(u"btn_import_datasetSplit")
        sizePolicy4.setHeightForWidth(self.btn_import_datasetSplit.sizePolicy().hasHeightForWidth())
        self.btn_import_datasetSplit.setSizePolicy(sizePolicy4)
        self.btn_import_datasetSplit.setMinimumSize(QSize(150, 30))
        self.btn_import_datasetSplit.setMaximumSize(QSize(150, 30))
        self.btn_import_datasetSplit.setFont(font)
        self.btn_import_datasetSplit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import_datasetSplit.setStyleSheet(u"")
        self.btn_import_datasetSplit.setIcon(icon7)

        self.horizontalLayout_67.addWidget(self.btn_import_datasetSplit)

        self.btn_output = QPushButton(self.trainer)
        self.btn_output.setObjectName(u"btn_output")
        sizePolicy4.setHeightForWidth(self.btn_output.sizePolicy().hasHeightForWidth())
        self.btn_output.setSizePolicy(sizePolicy4)
        self.btn_output.setMinimumSize(QSize(150, 30))
        self.btn_output.setMaximumSize(QSize(150, 30))
        self.btn_output.setFont(font)
        self.btn_output.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_output.setStyleSheet(u"")
        self.btn_output.setIcon(icon4)

        self.horizontalLayout_67.addWidget(self.btn_output)

        self.horizontalSpacer_53 = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_53)

        self.btn_terminate = QPushButton(self.trainer)
        self.btn_terminate.setObjectName(u"btn_terminate")
        sizePolicy4.setHeightForWidth(self.btn_terminate.sizePolicy().hasHeightForWidth())
        self.btn_terminate.setSizePolicy(sizePolicy4)
        self.btn_terminate.setMinimumSize(QSize(80, 30))
        self.btn_terminate.setMaximumSize(QSize(80, 30))
        self.btn_terminate.setFont(font)
        self.btn_terminate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_terminate.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_terminate.setIcon(icon8)

        self.horizontalLayout_67.addWidget(self.btn_terminate)

        self.btn_run_trainer = QPushButton(self.trainer)
        self.btn_run_trainer.setObjectName(u"btn_run_trainer")
        sizePolicy4.setHeightForWidth(self.btn_run_trainer.sizePolicy().hasHeightForWidth())
        self.btn_run_trainer.setSizePolicy(sizePolicy4)
        self.btn_run_trainer.setMinimumSize(QSize(80, 30))
        self.btn_run_trainer.setMaximumSize(QSize(80, 30))
        self.btn_run_trainer.setFont(font)
        self.btn_run_trainer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_run_trainer.setStyleSheet(u"")
        self.btn_run_trainer.setIcon(icon6)

        self.horizontalLayout_67.addWidget(self.btn_run_trainer)


        self.verticalLayout_89.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.toolBox_trainer = QToolBox(self.trainer)
        self.toolBox_trainer.setObjectName(u"toolBox_trainer")
        self.toolBox_trainer.setMinimumSize(QSize(360, 0))
        self.toolBox_trainer.setMaximumSize(QSize(360, 16777215))
        self.toolBox_trainer.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton*/\n"
"#toolBox_function QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 8px;	\n"
"	background-color: #7f94d5;\n"
"	font-size: 16px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#toolBox_function QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#toolBox_function QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ToolBox*/\n"
"QToolBox::tab { \n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"	font-weight: 900;\n"
"	padding-right: 10px;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	bac"
                        "kground-color: #495474;\n"
"	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;\n"
"	padding-left: 8px;\n"
"}\n"
"QToolBox::tab:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QToolBoxButton {\n"
"	min-height: 46px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"	font-size: 14px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:"
                        "/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(226, 135, 249);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QLabel */\n"
"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-pos"
                        "ition: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QDoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 0;\n"
"	selection-color: rgb(255, 255, 255);\n"
""
                        "	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:focus {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:hover {\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"")
        self.toolBox_trainer.setFrameShape(QFrame.Box)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 358, 470))
        self.verticalLayout_91 = QVBoxLayout(self.page)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_61 = QLabel(self.page)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_94.addWidget(self.label_61)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_64)

        self.comboBox_trainer_net = QComboBox(self.page)
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.addItem("")
        self.comboBox_trainer_net.setObjectName(u"comboBox_trainer_net")
        self.comboBox_trainer_net.setMinimumSize(QSize(210, 0))

        self.horizontalLayout_94.addWidget(self.comboBox_trainer_net)


        self.verticalLayout_91.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setSpacing(2)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(-1, 10, -1, -1)
        self.label_68 = QLabel(self.page)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_99.addWidget(self.label_68)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_60)

        self.lineEdit_trainer_period = QLineEdit(self.page)
        self.lineEdit_trainer_period.setObjectName(u"lineEdit_trainer_period")
        self.lineEdit_trainer_period.setMinimumSize(QSize(80, 30))
        self.lineEdit_trainer_period.setMaximumSize(QSize(80, 30))
        self.lineEdit_trainer_period.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_99.addWidget(self.lineEdit_trainer_period)

        self.label_69 = QLabel(self.page)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_99.addWidget(self.label_69)


        self.verticalLayout_91.addLayout(self.horizontalLayout_99)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(-1, 10, -1, -1)
        self.label_62 = QLabel(self.page)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_95.addWidget(self.label_62)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_63)

        self.switchButton_trainer_imageNet = SwitchButton(self.page)
        self.switchButton_trainer_imageNet.setObjectName(u"switchButton_trainer_imageNet")
        self.switchButton_trainer_imageNet.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_95.addWidget(self.switchButton_trainer_imageNet)


        self.verticalLayout_91.addLayout(self.horizontalLayout_95)

        self.frame_trainer_initWeights = QFrame(self.page)
        self.frame_trainer_initWeights.setObjectName(u"frame_trainer_initWeights")
        self.frame_trainer_initWeights.setFrameShape(QFrame.StyledPanel)
        self.frame_trainer_initWeights.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_trainer_initWeights)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(-1, 0, -1, -1)
        self.label_63 = QLabel(self.frame_trainer_initWeights)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_96.addWidget(self.label_63)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_65)

        self.switchButton_trainer_initWeights = SwitchButton(self.frame_trainer_initWeights)
        self.switchButton_trainer_initWeights.setObjectName(u"switchButton_trainer_initWeights")
        self.switchButton_trainer_initWeights.setMinimumSize(QSize(56, 30))

        self.horizontalLayout_96.addWidget(self.switchButton_trainer_initWeights)


        self.verticalLayout_93.addLayout(self.horizontalLayout_96)


        self.verticalLayout_91.addWidget(self.frame_trainer_initWeights)

        self.verticalSpacer_13 = QSpacerItem(20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_91.addItem(self.verticalSpacer_13)

        self.toolBox_trainer.addItem(self.page, u"\u6a21\u578b\u8bbe\u7f6e")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 286, 562))
        self.verticalLayout_94 = QVBoxLayout(self.page_2)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.label_64 = QLabel(self.page_2)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_94.addWidget(self.label_64)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setSpacing(4)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.lineEdit_trainer_inputSize1 = QLineEdit(self.page_2)
        self.lineEdit_trainer_inputSize1.setObjectName(u"lineEdit_trainer_inputSize1")
        self.lineEdit_trainer_inputSize1.setMinimumSize(QSize(0, 30))
        self.lineEdit_trainer_inputSize1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_97.addWidget(self.lineEdit_trainer_inputSize1)

        self.label_65 = QLabel(self.page_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(16, 16))
        self.label_65.setMaximumSize(QSize(16, 16))
        self.label_65.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_97.addWidget(self.label_65)

        self.lineEdit_trainer_inputSize2 = QLineEdit(self.page_2)
        self.lineEdit_trainer_inputSize2.setObjectName(u"lineEdit_trainer_inputSize2")
        self.lineEdit_trainer_inputSize2.setMinimumSize(QSize(0, 30))
        self.lineEdit_trainer_inputSize2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_97.addWidget(self.lineEdit_trainer_inputSize2)

        self.label_66 = QLabel(self.page_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(16, 16))
        self.label_66.setMaximumSize(QSize(16, 16))
        self.label_66.setStyleSheet(u"font-size: 20px;\n"
"color: #6272A4;\n"
"font-family: \"Arial\";\n"
"font-weight: 500;")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_97.addWidget(self.label_66)

        self.lineEdit_trainer_inputSize3 = QLineEdit(self.page_2)
        self.lineEdit_trainer_inputSize3.setObjectName(u"lineEdit_trainer_inputSize3")
        self.lineEdit_trainer_inputSize3.setMinimumSize(QSize(0, 30))
        self.lineEdit_trainer_inputSize3.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_inputSize3.setReadOnly(True)

        self.horizontalLayout_97.addWidget(self.lineEdit_trainer_inputSize3)


        self.verticalLayout_94.addLayout(self.horizontalLayout_97)

        self.frame_lossfunctionAndOptimizer = QFrame(self.page_2)
        self.frame_lossfunctionAndOptimizer.setObjectName(u"frame_lossfunctionAndOptimizer")
        self.frame_lossfunctionAndOptimizer.setFrameShape(QFrame.StyledPanel)
        self.frame_lossfunctionAndOptimizer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_lossfunctionAndOptimizer)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(-1, 10, -1, -1)
        self.label_75 = QLabel(self.frame_lossfunctionAndOptimizer)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_100.addWidget(self.label_75)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_62)

        self.comboBox_trainer_lossFunction = QComboBox(self.frame_lossfunctionAndOptimizer)
        self.comboBox_trainer_lossFunction.addItem("")
        self.comboBox_trainer_lossFunction.addItem("")
        self.comboBox_trainer_lossFunction.setObjectName(u"comboBox_trainer_lossFunction")
        self.comboBox_trainer_lossFunction.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_100.addWidget(self.comboBox_trainer_lossFunction)


        self.verticalLayout_92.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(-1, 10, -1, -1)
        self.label_76 = QLabel(self.frame_lossfunctionAndOptimizer)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_101.addWidget(self.label_76)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_66)

        self.comboBox_trainer_optimizer = QComboBox(self.frame_lossfunctionAndOptimizer)
        self.comboBox_trainer_optimizer.addItem("")
        self.comboBox_trainer_optimizer.addItem("")
        self.comboBox_trainer_optimizer.setObjectName(u"comboBox_trainer_optimizer")
        self.comboBox_trainer_optimizer.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_101.addWidget(self.comboBox_trainer_optimizer)


        self.verticalLayout_92.addLayout(self.horizontalLayout_101)


        self.verticalLayout_94.addWidget(self.frame_lossfunctionAndOptimizer)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(-1, 10, -1, -1)
        self.label_97 = QLabel(self.page_2)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"font-size: 16px;")

        self.horizontalLayout_115.addWidget(self.label_97)


        self.verticalLayout_94.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.btn_trainer_normalize_default = QPushButton(self.page_2)
        self.btn_trainer_normalize_default.setObjectName(u"btn_trainer_normalize_default")
        self.btn_trainer_normalize_default.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_106.addWidget(self.btn_trainer_normalize_default)

        self.btn_trainer_normalize_pretrain = QPushButton(self.page_2)
        self.btn_trainer_normalize_pretrain.setObjectName(u"btn_trainer_normalize_pretrain")
        self.btn_trainer_normalize_pretrain.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_106.addWidget(self.btn_trainer_normalize_pretrain)

        self.btn_trainer_normalize_cal = QPushButton(self.page_2)
        self.btn_trainer_normalize_cal.setObjectName(u"btn_trainer_normalize_cal")
        self.btn_trainer_normalize_cal.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_106.addWidget(self.btn_trainer_normalize_cal)


        self.verticalLayout_94.addLayout(self.horizontalLayout_106)

        self.label_104 = QLabel(self.page_2)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_94.addWidget(self.label_104)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_98 = QLabel(self.page_2)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_68.addWidget(self.label_98)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_55)

        self.lineEdit_trainer_train_mean = QLineEdit(self.page_2)
        self.lineEdit_trainer_train_mean.setObjectName(u"lineEdit_trainer_train_mean")
        self.lineEdit_trainer_train_mean.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_train_mean.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_train_mean.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_train_mean.setReadOnly(True)

        self.horizontalLayout_68.addWidget(self.lineEdit_trainer_train_mean)


        self.verticalLayout_94.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.label_99 = QLabel(self.page_2)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_105.addWidget(self.label_99)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_56)

        self.lineEdit_trainer_train_std = QLineEdit(self.page_2)
        self.lineEdit_trainer_train_std.setObjectName(u"lineEdit_trainer_train_std")
        self.lineEdit_trainer_train_std.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_train_std.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_train_std.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_train_std.setReadOnly(True)

        self.horizontalLayout_105.addWidget(self.lineEdit_trainer_train_std)


        self.verticalLayout_94.addLayout(self.horizontalLayout_105)

        self.label_110 = QLabel(self.page_2)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_94.addWidget(self.label_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.label_105 = QLabel(self.page_2)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_111.addWidget(self.label_105)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_74)

        self.lineEdit_trainer_val_mean = QLineEdit(self.page_2)
        self.lineEdit_trainer_val_mean.setObjectName(u"lineEdit_trainer_val_mean")
        self.lineEdit_trainer_val_mean.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_val_mean.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_val_mean.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_val_mean.setReadOnly(True)

        self.horizontalLayout_111.addWidget(self.lineEdit_trainer_val_mean)


        self.verticalLayout_94.addLayout(self.horizontalLayout_111)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.label_106 = QLabel(self.page_2)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_112.addWidget(self.label_106)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_75)

        self.lineEdit_trainer_val_std = QLineEdit(self.page_2)
        self.lineEdit_trainer_val_std.setObjectName(u"lineEdit_trainer_val_std")
        self.lineEdit_trainer_val_std.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_val_std.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_val_std.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_val_std.setReadOnly(True)

        self.horizontalLayout_112.addWidget(self.lineEdit_trainer_val_std)


        self.verticalLayout_94.addLayout(self.horizontalLayout_112)

        self.label_111 = QLabel(self.page_2)
        self.label_111.setObjectName(u"label_111")

        self.verticalLayout_94.addWidget(self.label_111)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.label_108 = QLabel(self.page_2)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_113.addWidget(self.label_108)

        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_76)

        self.lineEdit_trainer_test_mean = QLineEdit(self.page_2)
        self.lineEdit_trainer_test_mean.setObjectName(u"lineEdit_trainer_test_mean")
        self.lineEdit_trainer_test_mean.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_test_mean.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_test_mean.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_test_mean.setReadOnly(True)

        self.horizontalLayout_113.addWidget(self.lineEdit_trainer_test_mean)


        self.verticalLayout_94.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.label_109 = QLabel(self.page_2)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"color: #BD93F9;\n"
"font-size: 16px;")

        self.horizontalLayout_114.addWidget(self.label_109)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_77)

        self.lineEdit_trainer_test_std = QLineEdit(self.page_2)
        self.lineEdit_trainer_test_std.setObjectName(u"lineEdit_trainer_test_std")
        self.lineEdit_trainer_test_std.setMinimumSize(QSize(180, 30))
        self.lineEdit_trainer_test_std.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_test_std.setAlignment(Qt.AlignCenter)
        self.lineEdit_trainer_test_std.setReadOnly(True)

        self.horizontalLayout_114.addWidget(self.lineEdit_trainer_test_std)


        self.verticalLayout_94.addLayout(self.horizontalLayout_114)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_30)

        self.toolBox_trainer.addItem(self.page_2, u"\u6a21\u578b\u53c2\u6570")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 287, 221))
        self.verticalLayout_99 = QVBoxLayout(self.page_5)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_85 = QLabel(self.page_5)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_102.addWidget(self.label_85)

        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_67)

        self.lineEdit_trainer_batchSize = QLineEdit(self.page_5)
        self.lineEdit_trainer_batchSize.setObjectName(u"lineEdit_trainer_batchSize")
        self.lineEdit_trainer_batchSize.setMinimumSize(QSize(150, 30))
        self.lineEdit_trainer_batchSize.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_batchSize.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.lineEdit_trainer_batchSize)


        self.verticalLayout_99.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(-1, 10, -1, -1)
        self.label_95 = QLabel(self.page_5)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_103.addWidget(self.label_95)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_68)

        self.lineEdit_trainer_learningRate = QLineEdit(self.page_5)
        self.lineEdit_trainer_learningRate.setObjectName(u"lineEdit_trainer_learningRate")
        self.lineEdit_trainer_learningRate.setMinimumSize(QSize(150, 30))
        self.lineEdit_trainer_learningRate.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_learningRate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.lineEdit_trainer_learningRate)


        self.verticalLayout_99.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(-1, 10, -1, -1)
        self.label_96 = QLabel(self.page_5)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_104.addWidget(self.label_96)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_69)

        self.lineEdit_trainer_epoch = QLineEdit(self.page_5)
        self.lineEdit_trainer_epoch.setObjectName(u"lineEdit_trainer_epoch")
        self.lineEdit_trainer_epoch.setMinimumSize(QSize(150, 30))
        self.lineEdit_trainer_epoch.setMaximumSize(QSize(150, 30))
        self.lineEdit_trainer_epoch.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_104.addWidget(self.lineEdit_trainer_epoch)


        self.verticalLayout_99.addLayout(self.horizontalLayout_104)

        self.frame_trainer_dropout = QFrame(self.page_5)
        self.frame_trainer_dropout.setObjectName(u"frame_trainer_dropout")
        self.frame_trainer_dropout.setFrameShape(QFrame.StyledPanel)
        self.frame_trainer_dropout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_trainer_dropout)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_67 = QLabel(self.frame_trainer_dropout)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_98.addWidget(self.label_67)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_61)

        self.dSpinBox_trainer_dropout = QDoubleSpinBox(self.frame_trainer_dropout)
        self.dSpinBox_trainer_dropout.setObjectName(u"dSpinBox_trainer_dropout")
        self.dSpinBox_trainer_dropout.setMinimumSize(QSize(150, 30))
        self.dSpinBox_trainer_dropout.setMaximumSize(QSize(150, 30))
        self.dSpinBox_trainer_dropout.setAlignment(Qt.AlignCenter)
        self.dSpinBox_trainer_dropout.setMaximum(1.000000000000000)
        self.dSpinBox_trainer_dropout.setSingleStep(0.100000000000000)
        self.dSpinBox_trainer_dropout.setValue(0.500000000000000)

        self.horizontalLayout_98.addWidget(self.dSpinBox_trainer_dropout)


        self.verticalLayout_95.addLayout(self.horizontalLayout_98)

        self.slider_trainer_dropout = QSlider(self.frame_trainer_dropout)
        self.slider_trainer_dropout.setObjectName(u"slider_trainer_dropout")
        self.slider_trainer_dropout.setMaximum(100)
        self.slider_trainer_dropout.setSingleStep(10)
        self.slider_trainer_dropout.setValue(50)
        self.slider_trainer_dropout.setOrientation(Qt.Horizontal)

        self.verticalLayout_95.addWidget(self.slider_trainer_dropout)


        self.verticalLayout_99.addWidget(self.frame_trainer_dropout)

        self.verticalSpacer_29 = QSpacerItem(20, 317, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_99.addItem(self.verticalSpacer_29)

        self.toolBox_trainer.addItem(self.page_5, u"\u8d85\u53c2\u6570\u8c03\u4f18")

        self.horizontalLayout_93.addWidget(self.toolBox_trainer)

        self.verticalLayout_87 = QVBoxLayout()
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_57)

        self.btn_trainer_showStep = QPushButton(self.trainer)
        self.btn_trainer_showStep.setObjectName(u"btn_trainer_showStep")
        self.btn_trainer_showStep.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_92.addWidget(self.btn_trainer_showStep)

        self.btn_trainer_showEpoch = QPushButton(self.trainer)
        self.btn_trainer_showEpoch.setObjectName(u"btn_trainer_showEpoch")
        self.btn_trainer_showEpoch.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_92.addWidget(self.btn_trainer_showEpoch)

        self.btn_trainer_matrix = QPushButton(self.trainer)
        self.btn_trainer_matrix.setObjectName(u"btn_trainer_matrix")
        self.btn_trainer_matrix.setMinimumSize(QSize(80, 30))
        self.btn_trainer_matrix.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #aaaaaa;\n"
"	border-radius: 5px;	\n"
"	background-color: #aaaaaa;\n"
"    color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #aaaaaa;\n"
"	border: 2px solid #aaaaaa;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #aaaaaa;\n"
"	border: 2px solid #aaaaaa;\n"
"}")

        self.horizontalLayout_92.addWidget(self.btn_trainer_matrix)

        self.btn_trainer_rangeReset = QPushButton(self.trainer)
        self.btn_trainer_rangeReset.setObjectName(u"btn_trainer_rangeReset")
        self.btn_trainer_rangeReset.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_92.addWidget(self.btn_trainer_rangeReset)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_58)


        self.verticalLayout_87.addLayout(self.horizontalLayout_92)

        self.stackedWidget_canvas = QStackedWidget(self.trainer)
        self.stackedWidget_canvas.setObjectName(u"stackedWidget_canvas")
        self.stackedWidget_canvas.setFrameShape(QFrame.Box)
        self.pgView_step_loss = QWidget()
        self.pgView_step_loss.setObjectName(u"pgView_step_loss")
        self.verticalLayout_96 = QVBoxLayout(self.pgView_step_loss)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.canvas_step_loss = MplCanvas(self.pgView_step_loss)
        self.canvas_step_loss.setObjectName(u"canvas_step_loss")

        self.verticalLayout_96.addWidget(self.canvas_step_loss)

        self.stackedWidget_canvas.addWidget(self.pgView_step_loss)
        self.pgView_confusionMatrix = QWidget()
        self.pgView_confusionMatrix.setObjectName(u"pgView_confusionMatrix")
        self.verticalLayout_98 = QVBoxLayout(self.pgView_confusionMatrix)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.lb_showAcc = QLabel(self.pgView_confusionMatrix)
        self.lb_showAcc.setObjectName(u"lb_showAcc")
        self.lb_showAcc.setMinimumSize(QSize(0, 20))
        self.lb_showAcc.setMaximumSize(QSize(16777215, 20))
        self.lb_showAcc.setStyleSheet(u"font-family: \"Microsoft Yahei\";\n"
"font-weight: 500;\n"
"font-size: 16px;")

        self.verticalLayout_98.addWidget(self.lb_showAcc)

        self.img_confusionMatrix = QLabel(self.pgView_confusionMatrix)
        self.img_confusionMatrix.setObjectName(u"img_confusionMatrix")

        self.verticalLayout_98.addWidget(self.img_confusionMatrix)

        self.stackedWidget_canvas.addWidget(self.pgView_confusionMatrix)
        self.pgView_epoch_loss_acc = QWidget()
        self.pgView_epoch_loss_acc.setObjectName(u"pgView_epoch_loss_acc")
        self.verticalLayout_90 = QVBoxLayout(self.pgView_epoch_loss_acc)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.canvas_epoch_loss_acc = MplCanvas(self.pgView_epoch_loss_acc)
        self.canvas_epoch_loss_acc.setObjectName(u"canvas_epoch_loss_acc")

        self.verticalLayout_90.addWidget(self.canvas_epoch_loss_acc)

        self.stackedWidget_canvas.addWidget(self.pgView_epoch_loss_acc)

        self.verticalLayout_87.addWidget(self.stackedWidget_canvas)

        self.lb_showDatasetNum = QLabel(self.trainer)
        self.lb_showDatasetNum.setObjectName(u"lb_showDatasetNum")
        self.lb_showDatasetNum.setMinimumSize(QSize(0, 40))
        self.lb_showDatasetNum.setMaximumSize(QSize(16777215, 40))
        self.lb_showDatasetNum.setStyleSheet(u"font-size: 16px;")

        self.verticalLayout_87.addWidget(self.lb_showDatasetNum)


        self.horizontalLayout_93.addLayout(self.verticalLayout_87)


        self.verticalLayout_89.addLayout(self.horizontalLayout_93)

        self.stackedWidget.addWidget(self.trainer)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
#if QT_CONFIG(shortcut)
        self.img_after_image.setBuddy(self.img_after_dataset)
        self.img_after_dataset.setBuddy(self.img_after_dataset)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.toolBox_function_image.setCurrentIndex(0)
        self.toolBox_process_image.setCurrentIndex(0)
        self.toolBox_imageAugment_image.setCurrentIndex(0)
        self.toolBox_function_dataset.setCurrentIndex(0)
        self.toolBox_process_dataset.setCurrentIndex(3)
        self.toolBox_imageAugment_dataset.setCurrentIndex(0)
        self.toolBox_trainer.setCurrentIndex(0)
        self.stackedWidget_canvas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u795e\u7ecf\u7f51\u7edc\u56fe\u50cf\u6570\u636e\u8bad\u7ec3\u96c6\u6210\u5e94\u7528", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QPushButton*/\n"
"#toolBox_function QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 8px;	\n"
"	background-color: #7f94d5;\n"
"	font-size: 16px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#toolBox_function QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#toolBox_function QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ToolBox*/\n"
"QToolBox::tab { \n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft Yahei\";\n"
"	font-weight: 900;\n"
"	padding-right: 10px;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	background-color: #6272A4;\n"
"/*	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	image-position: right;*/\n"
"	image: url(:/icons/images/icons/cil-signal-cellular-0.png);"
                        "\n"
"	image-position: left;\n"
"	padding-left: 4px;\n"
"}\n"
"QToolBox::tab:!selected {\n"
"	background-color: #495474;\n"
"	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	image-position: right;\n"
"}\n"
"QToolBox::tab:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QToolBoxButton {\n"
"	min-height: 46px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"	font-size: 18px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3"
                        "px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QLabel */\n"
"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: 900;\n"
"	font-family: \"Microsoft Yahei\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QSpinBox */\n"
"QSpinBox {\n"
"	color: #ffffff;\n"
"	font-size: 16px;\n"
"	background-color: #6272A4;\n"
"	border-radius: 4px;\n"
"	padding: 0 4px;\n"
"}\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-left-alt.png);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-ori"
                        "gin: content;\n"
"	subcontrol-position: right;\n"
"	image: url(:/icons/images/icons/cil-chevron-circle-right-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:focus {\n"
"	border: none;\n"
"}\n"
"QLineEdit[readOnly=\"true\"]:hover {\n"
"	border: none;\n"
"}\n"
"", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u83dc\u5355", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Choose the function", None))
        self.toggleButton.setText("")
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#if QT_CONFIG(tooltip)
        self.btn_process_image.setToolTip(QCoreApplication.translate("MainWindow", u"\u5355\u5f20\u56fe\u7247\u9884\u5904\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.btn_process_image.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5f20\u56fe\u7247\u9884\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.btn_process_dataset.setToolTip(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u9884\u5904\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.btn_process_dataset.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u9884\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.btn_trainer.setToolTip(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316\u8bad\u7ec3\u5668", None))
#endif // QT_CONFIG(tooltip)
        self.btn_trainer.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316\u8bad\u7ec3\u5668", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u795e\u7ecf\u7f51\u7edc\u56fe\u50cf\u6570\u636e\u8bad\u7ec3\u96c6\u6210\u5e94\u7528", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5e94\u7528\u57fa\u4e8e\u5f00\u6e90UI\u6846\u67b6PyDracula\u5f00\u53d1", None))
        self.btn_importSingleImage.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u56fe\u7247", None))
        self.btn_exportResult_image.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u4fdd\u5b58\u8def\u5f84", None))
        self.btn_preview_image.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.btn_run_image.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.btn_jpg_image.setText(QCoreApplication.translate("MainWindow", u"jpg", None))
        self.rb_jpg_image.setText("")
        self.btn_jpeg_image.setText(QCoreApplication.translate("MainWindow", u"jpeg", None))
        self.rb_jpeg_image.setText("")
        self.btn_png_image.setText(QCoreApplication.translate("MainWindow", u"png", None))
        self.rb_png_image.setText("")
        self.btn_bmp_image.setText(QCoreApplication.translate("MainWindow", u"bmp", None))
        self.rb_bmp_image.setText("")
        self.toolBox_process_image.setItemText(self.toolBox_process_image.indexOf(self.tbpg_suffix_image), QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u540e\u7f00", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6e\u56fe\u50cf\u7684\u5927\u5c0f\uff1a", None))
        self.lineEdit_resizepx1_ofImage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1~8192", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"px \u00d7 ", None))
        self.lineEdit_resizepx2_ofImage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1~8192", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u63d2\u503c\u65b9\u5f0f\uff1a", None))
        self.rbtn_INTER_LINEAR_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_LINEAR", None))
        self.rbtn_INTER_NEAREST_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_NEAREST", None))
        self.rbtn_INTER_CUBIC_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_CUBIC", None))
        self.rbtn_INTER_AREA_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_AREA", None))
        self.rbtn_INTER_LANCZOS4_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_LANCZOS4", None))
        self.rbtn_INTER_LINEAR_EXACT_ofImage.setText(QCoreApplication.translate("MainWindow", u"INTER_LINEAR_EXACT", None))
        self.toolBox_process_image.setItemText(self.toolBox_process_image.indexOf(self.tbpg_resize_image), QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u5927\u5c0f", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u62d3\u5c55\u586b\u5145\u65b9\u5f0f\uff1a", None))
        self.rbtn_BORDER_CONSTANT_image.setText(QCoreApplication.translate("MainWindow", u"BORDER_CONSTANT", None))
        self.rbtn_BORDER_REFLECT_image.setText(QCoreApplication.translate("MainWindow", u"BORDER_REFLECT", None))
        self.rbtn_BORDER_REPLICATE_image.setText(QCoreApplication.translate("MainWindow", u"BORDER_REPLICATE", None))
        self.rbtn_BORDER_WRAP_image.setText(QCoreApplication.translate("MainWindow", u"BORDER_WRAP", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u586b\u5145\u989c\u8272\uff1a", None))
        self.squre_showRGB_ofImage.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.toolBox_process_image.setItemText(self.toolBox_process_image.indexOf(self.tbpg_square_image), QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u65b9\u5f62\u5316", None))
        self.toolBox_function_image.setItemText(self.toolBox_function_image.indexOf(self.tbpg_processTool_image), QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406\u5de5\u5177", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_rotate_ofImage.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u89d2\u5ea6\uff1a", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f\u7f29\u653e\uff1a", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u586b\u5145\u989c\u8272\uff1a", None))
        self.rotate_showRGB_ofImage.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_rotate_image), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u65cb\u8f6c", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_HFlip_ofImage.setText("")
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_HFlip_image), QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_VFlip_ofImage.setText("")
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_VFlip_image), QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u7ffb\u8f6c", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_blur_ofImage.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6ee4\u6ce2\u65b9\u5f0f\uff1a", None))
        self.rbtn_blur_mean_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.rbtn_blur_box_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6846\u6ee4\u6ce2", None))
        self.rbtn_blur_gaussian_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.rbtn_blur_median_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6ee4\u6ce2\u6838\u5927\u5c0f\uff1a", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_blur_image), QCoreApplication.translate("MainWindow", u"\u6a21\u7cca", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_noise_ofImage.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u566a\u58f0\u5904\u7406\u64cd\u4f5c\uff1a", None))
        self.cb_noise_gaussian_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6esigma\u503c\uff1a", None))
        self.cb_noise_saltPepper_ofImage.setText(QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6erate\u503c\uff1a", None))
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_noise_image), QCoreApplication.translate("MainWindow", u"\u566a\u58f0", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_brightness_ofImage.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6\u8c03\u6574\uff1a", None))
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_brightness_image), QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_contrast_ofImage.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6\u8c03\u6574\uff1a", None))
        self.toolBox_imageAugment_image.setItemText(self.toolBox_imageAugment_image.indexOf(self.tbpg_contrast_image), QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6", None))
        self.toolBox_function_image.setItemText(self.toolBox_function_image.indexOf(self.tbpg_imageAugment_image), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u589e\u5f3a", None))
        self.lb_preTitle_image.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u524d\u56fe\u50cf\u9884\u89c8", None))
        self.lb_pre_image.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7a97\u53e3\u50cf\u7d20\uff1a360\u00d7360", None))
        self.img_pre_image.setText("")
        self.lb_afterTitle_image.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u540e\u56fe\u50cf\u9884\u89c8", None))
        self.lb_after_image.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7a97\u53e3\u50cf\u7d20\uff1a360\u00d7360", None))
        self.img_after_image.setText("")
        self.show_algorithm_ofImage.setText("")
        self.btn_importDataset.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e\u96c6", None))
        self.btn_exportResult_dataset.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5bfc\u51fa\u8def\u5f84", None))
        self.btn_preview_dataset.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.btn_run_dataset.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.btn_jpg_ofDataset.setText(QCoreApplication.translate("MainWindow", u"jpg", None))
        self.rb_jpg_ofDataset.setText("")
        self.btn_jpeg_ofDataset.setText(QCoreApplication.translate("MainWindow", u"jpeg", None))
        self.rb_jpeg_ofDataset.setText("")
        self.btn_png_ofDataset.setText(QCoreApplication.translate("MainWindow", u"png", None))
        self.rb_png_ofDataset.setText("")
        self.btn_bmp_ofDataset.setText(QCoreApplication.translate("MainWindow", u"bmp", None))
        self.rb_bmp_ofDataset.setText("")
        self.toolBox_process_dataset.setItemText(self.toolBox_process_dataset.indexOf(self.tbpg_suffix_dataset), QCoreApplication.translate("MainWindow", u"\u7edf\u4e00\u540e\u7f00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u547d\u540d\u683c\u5f0f\uff1a", None))
        self.rbtn_rename1_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b_i", None))
        self.rbtn_rename2_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7bi", None))
        self.rbtn_rename3_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b-i", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4ece0\u5f00\u59cb\u547d\u540d\uff1a", None))
        self.cb_rename0_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u4ece0\u5f00\u59cb\u547d\u540d", None))
        self.toolBox_process_dataset.setItemText(self.toolBox_process_dataset.indexOf(self.tbpg_name_dataset), QCoreApplication.translate("MainWindow", u"\u7edf\u4e00\u547d\u540d", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6e\u56fe\u50cf\u7684\u5927\u5c0f\uff1a", None))
        self.lineEdit_resizepx1_ofDataset.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1~8192", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"px \u00d7 ", None))
        self.lineEdit_resizepx2_ofDataset.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1~8192", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u63d2\u503c\u65b9\u5f0f\uff1a", None))
        self.rbtn_INTER_LINEAR_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_LINEAR", None))
        self.rbtn_INTER_NEAREST_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_NEAREST", None))
        self.rbtn_INTER_CUBIC_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_CUBIC", None))
        self.rbtn_INTER_AREA_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_AREA", None))
        self.rbtn_INTER_LANCZOS4_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_LANCZOS4", None))
        self.rbtn_INTER_LINEAR_EXACT_ofDataset.setText(QCoreApplication.translate("MainWindow", u"INTER_LINEAR_EXACT", None))
        self.toolBox_process_dataset.setItemText(self.toolBox_process_dataset.indexOf(self.tbpg_resize_dataset), QCoreApplication.translate("MainWindow", u"\u7edf\u4e00\u5927\u5c0f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u62d3\u5c55\u586b\u5145\u65b9\u5f0f\uff1a", None))
        self.rbtn_BORDER_CONSTANT_ofDataset.setText(QCoreApplication.translate("MainWindow", u"BORDER_CONSTANT", None))
        self.rbtn_BORDER_REFLECT_ofDataset.setText(QCoreApplication.translate("MainWindow", u"BORDER_REFLECT", None))
        self.rbtn_BORDER_REPLICATE_ofDataset.setText(QCoreApplication.translate("MainWindow", u"BORDER_REPLICATE", None))
        self.rbtn_BORDER_WRAP_ofDataset.setText(QCoreApplication.translate("MainWindow", u"BORDER_WRAP", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u586b\u5145\u989c\u8272\uff1a", None))
        self.squre_showRGB_ofDataset.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.toolBox_process_dataset.setItemText(self.toolBox_process_dataset.indexOf(self.tbpg_square_dataset), QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u65b9\u5f62\u5316", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6570\u636e\u96c6\u5206\u5272\u6bd4\u4f8b\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u96c6train\u6bd4\u4f8b\uff1a", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u96c6val\u6bd4\u4f8b\uff1a", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u96c6test\u6bd4\u4f8b\uff1a", None))
        self.toolBox_process_dataset.setItemText(self.toolBox_process_dataset.indexOf(self.tbpg_split_dataset), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u5206\u5272", None))
        self.toolBox_function_dataset.setItemText(self.toolBox_function_dataset.indexOf(self.tbpg_processTool), QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406\u5de5\u5177", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_rotate_ofDataset.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u5ea6\u65cb\u8f6c\u8303\u56f4\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f\u7f29\u653e\u8303\u56f4\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u586b\u5145\u989c\u8272\uff1a", None))
        self.rotate_showRGB_ofDataset.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_rotate_dataset), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u65cb\u8f6c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_HFlip_ofDataset.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_HFlip_dataset), QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_VFlip_ofDataset.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_VFlip_dataset), QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u7ffb\u8f6c", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_blur_ofDataset.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6ee4\u6ce2\u65b9\u5f0f\uff1a", None))
        self.rbtn_blur_mean_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.rbtn_blur_box_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6846\u6ee4\u6ce2", None))
        self.rbtn_blur_gaussian_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.rbtn_blur_median_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6ee4\u6ce2\u6838\u5927\u5c0f\u8303\u56f4\uff1a", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"From\uff1a", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"To\uff1a", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_blur_dataset), QCoreApplication.translate("MainWindow", u"\u6a21\u7cca", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_noise_ofDataset.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.cb_noise_gaussian_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6esigma\u8303\u56f4\uff1a", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.cb_noise_saltPepper_ofDataset.setText(QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bbe\u7f6erate\u8303\u56f4\uff1a", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_noise_dataset), QCoreApplication.translate("MainWindow", u"\u566a\u58f0", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_brightness_ofDataset.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6\u8303\u56f4\uff1a", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_brightness_dataset), QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528\uff1a", None))
        self.switchButton_contrast_ofDataset.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6570\u636e\u96c6\u4e2d\u5b9e\u73b0\u7684\u6982\u7387\uff1a", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6\u8c03\u6574\uff1a", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.toolBox_imageAugment_dataset.setItemText(self.toolBox_imageAugment_dataset.indexOf(self.tbpg_contrast_dataset), QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6", None))
        self.toolBox_function_dataset.setItemText(self.toolBox_function_dataset.indexOf(self.tbpg_imageAugment_dataset), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u589e\u5f3a", None))
        self.lb_preTitle_dataset.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u524d\u56fe\u50cf\u9884\u89c8", None))
        self.lb_pre_dataset.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7a97\u53e3\u50cf\u7d20\uff1a360\u00d7360", None))
        self.img_pre_dataset.setText("")
        self.lb_afterTitle_dataset.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u540e\u56fe\u50cf\u9884\u89c8", None))
        self.lb_after_dataset.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7a97\u53e3\u50cf\u7d20\uff1a360\u00d7360", None))
        self.img_after_dataset.setText("")
        self.show_algorithm_ofDataset.setText("")
        self.btn_import_datasetSplit.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5212\u5206\u6570\u636e\u96c6", None))
        self.btn_output.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5bfc\u51fa\u8def\u5f84", None))
        self.btn_terminate.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62", None))
        self.btn_run_trainer.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u9009\u62e9\uff1a", None))
        self.comboBox_trainer_net.setItemText(0, QCoreApplication.translate("MainWindow", u"AlexNet", None))
        self.comboBox_trainer_net.setItemText(1, QCoreApplication.translate("MainWindow", u"VGG11", None))
        self.comboBox_trainer_net.setItemText(2, QCoreApplication.translate("MainWindow", u"VGG13", None))
        self.comboBox_trainer_net.setItemText(3, QCoreApplication.translate("MainWindow", u"VGG16", None))
        self.comboBox_trainer_net.setItemText(4, QCoreApplication.translate("MainWindow", u"VGG19", None))
        self.comboBox_trainer_net.setItemText(5, QCoreApplication.translate("MainWindow", u"GoogLeNet", None))
        self.comboBox_trainer_net.setItemText(6, QCoreApplication.translate("MainWindow", u"ResNet18", None))
        self.comboBox_trainer_net.setItemText(7, QCoreApplication.translate("MainWindow", u"ResNet34", None))
        self.comboBox_trainer_net.setItemText(8, QCoreApplication.translate("MainWindow", u"ResNet50", None))
        self.comboBox_trainer_net.setItemText(9, QCoreApplication.translate("MainWindow", u"ResNet101", None))
        self.comboBox_trainer_net.setItemText(10, QCoreApplication.translate("MainWindow", u"ResNet152", None))
        self.comboBox_trainer_net.setItemText(11, QCoreApplication.translate("MainWindow", u"ResNeXt50(32x4d)", None))
        self.comboBox_trainer_net.setItemText(12, QCoreApplication.translate("MainWindow", u"ResNeXt101(32x8d)", None))
        self.comboBox_trainer_net.setItemText(13, QCoreApplication.translate("MainWindow", u"MobileNetV2", None))
        self.comboBox_trainer_net.setItemText(14, QCoreApplication.translate("MainWindow", u"MobileNetV3(large)", None))
        self.comboBox_trainer_net.setItemText(15, QCoreApplication.translate("MainWindow", u"MobileNetV3(small)", None))
        self.comboBox_trainer_net.setItemText(16, QCoreApplication.translate("MainWindow", u"ShuffleNetV2(x0.5)", None))
        self.comboBox_trainer_net.setItemText(17, QCoreApplication.translate("MainWindow", u"ShuffleNetV2(x1.0)", None))
        self.comboBox_trainer_net.setItemText(18, QCoreApplication.translate("MainWindow", u"ShuffleNetV2(x1.5)", None))
        self.comboBox_trainer_net.setItemText(19, QCoreApplication.translate("MainWindow", u"ShuffleNetV2(x2.0)", None))
        self.comboBox_trainer_net.setItemText(20, QCoreApplication.translate("MainWindow", u"EfficientNetB0", None))
        self.comboBox_trainer_net.setItemText(21, QCoreApplication.translate("MainWindow", u"EfficientNetB1", None))
        self.comboBox_trainer_net.setItemText(22, QCoreApplication.translate("MainWindow", u"EfficientNetB2", None))
        self.comboBox_trainer_net.setItemText(23, QCoreApplication.translate("MainWindow", u"EfficientNetB3", None))
        self.comboBox_trainer_net.setItemText(24, QCoreApplication.translate("MainWindow", u"EfficientNetB4", None))
        self.comboBox_trainer_net.setItemText(25, QCoreApplication.translate("MainWindow", u"EfficientNetB5", None))
        self.comboBox_trainer_net.setItemText(26, QCoreApplication.translate("MainWindow", u"EfficientNetB6", None))
        self.comboBox_trainer_net.setItemText(27, QCoreApplication.translate("MainWindow", u"EfficientNetB7", None))
        self.comboBox_trainer_net.setItemText(28, QCoreApplication.translate("MainWindow", u"EfficientNetV2-S", None))
        self.comboBox_trainer_net.setItemText(29, QCoreApplication.translate("MainWindow", u"EfficientNetV2-M", None))
        self.comboBox_trainer_net.setItemText(30, QCoreApplication.translate("MainWindow", u"EfficientNetV2-L", None))
        self.comboBox_trainer_net.setItemText(31, QCoreApplication.translate("MainWindow", u"VisionTransformer(b16)", None))
        self.comboBox_trainer_net.setItemText(32, QCoreApplication.translate("MainWindow", u"VisionTransformer(b32)", None))
        self.comboBox_trainer_net.setItemText(33, QCoreApplication.translate("MainWindow", u"SwinTransformer(t)", None))
        self.comboBox_trainer_net.setItemText(34, QCoreApplication.translate("MainWindow", u"SwinTransformer(s)", None))
        self.comboBox_trainer_net.setItemText(35, QCoreApplication.translate("MainWindow", u"SwinTransformer(b)", None))

        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u4fdd\u5b58\u95f4\u9694\uff1a", None))
        self.lineEdit_trainer_period.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"epoch", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u8fc1\u79fb\u5b66\u4e60\uff1a", None))
        self.switchButton_trainer_imageNet.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\u6743\u91cd\uff1a", None))
        self.switchButton_trainer_initWeights.setText("")
        self.toolBox_trainer.setItemText(self.toolBox_trainer.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bbe\u7f6e", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u56fe\u50cf\u6570\u636e\u5927\u5c0f\uff1a", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.lineEdit_trainer_inputSize3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u635f\u5931\u51fd\u6570\uff1a", None))
        self.comboBox_trainer_lossFunction.setItemText(0, QCoreApplication.translate("MainWindow", u"CrossEntropyLoss", None))
        self.comboBox_trainer_lossFunction.setItemText(1, QCoreApplication.translate("MainWindow", u"Softmax", None))

        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5316\u5668\uff1a", None))
        self.comboBox_trainer_optimizer.setItemText(0, QCoreApplication.translate("MainWindow", u"Adam", None))
        self.comboBox_trainer_optimizer.setItemText(1, QCoreApplication.translate("MainWindow", u"SGD", None))

        self.label_97.setText(QCoreApplication.translate("MainWindow", u"\u5f52\u4e00\u5316\u53c2\u6570", None))
        self.btn_trainer_normalize_default.setText(QCoreApplication.translate("MainWindow", u"[-1, 1]\u5206\u5e03", None))
        self.btn_trainer_normalize_pretrain.setText(QCoreApplication.translate("MainWindow", u"\u8fc1\u79fb\u5b66\u4e60\u53c2\u6570", None))
        self.btn_trainer_normalize_cal.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u96c6train", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Mean\uff1a", None))
        self.lineEdit_trainer_train_mean.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Std\uff1a", None))
        self.lineEdit_trainer_train_std.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u96c6val", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Mean\uff1a", None))
        self.lineEdit_trainer_val_mean.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Std\uff1a", None))
        self.lineEdit_trainer_val_std.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u96c6test", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Mean\uff1a", None))
        self.lineEdit_trainer_test_mean.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Std\uff1a", None))
        self.lineEdit_trainer_test_std.setText(QCoreApplication.translate("MainWindow", u"[0.5, 0.5, 0.5]", None))
        self.toolBox_trainer.setItemText(self.toolBox_trainer.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u53c2\u6570", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Batch Size\uff1a", None))
        self.lineEdit_trainer_batchSize.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Learning Rate\uff1a", None))
        self.lineEdit_trainer_learningRate.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Epoch\uff1a", None))
        self.lineEdit_trainer_epoch.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Dropout\uff1a", None))
        self.toolBox_trainer.setItemText(self.toolBox_trainer.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"\u8d85\u53c2\u6570\u8c03\u4f18", None))
        self.btn_trainer_showStep.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.btn_trainer_showEpoch.setText(QCoreApplication.translate("MainWindow", u"Epoch", None))
        self.btn_trainer_matrix.setText(QCoreApplication.translate("MainWindow", u"\u6df7\u6dc6\u77e9\u9635", None))
        self.btn_trainer_rangeReset.setText(QCoreApplication.translate("MainWindow", u"\u8303\u56f4\u91cd\u7f6e", None))
        self.lb_showAcc.setText("")
        self.img_confusionMatrix.setText("")
        self.lb_showDatasetNum.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Coriander Saint", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

