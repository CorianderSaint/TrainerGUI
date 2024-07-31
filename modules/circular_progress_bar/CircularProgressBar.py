from PySide6.QtCore import QPoint, QRect, QSize, Qt
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import *


class CircularProgressBarOption(object):
    def __init__(self, position: QPoint = QPoint(10, 10), progressbarWidth: int = 320,
                 progressbarColor: QColor = QColor(85, 170, 255, 255),
                 progressbarBgColor: QColor = QColor(77, 77, 127)) -> None:
        self.__position: QPoint = position
        self.__width: int = progressbarWidth
        self.__color: QColor = progressbarColor
        self.__bgColor: QColor = progressbarBgColor

    @property
    def Position(self):
        return self.__position

    @property
    def Width(self):
        return self.__width

    @property
    def Color(self):
        return self.__color

    @property
    def BackgroundColor(self):
        return self.__bgColor


class CircularProgressBar(object):
    def __init__(self, parent, option: CircularProgressBarOption) -> None:
        self.__opt = option

        # 进度条的基础
        circularProgressBarBase = QFrame(parent)
        circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        circularProgressBarBase.setGeometry(QRect(option.Position.x(), option.Position.y(), option.Width, option.Width))
        circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.__base = circularProgressBarBase

        # 进度条
        circularProgress = QFrame(circularProgressBarBase)
        circularProgress.setObjectName(u"circularProgress")
        circularProgress.setGeometry(
            QRect(option.Position.x(), option.Position.x(), option.Width - 20, option.Width - 20))
        # QFrame 不能省略.  stop:0.99999 , 1.00 外观显示为： 没有进度
        styleSheet = "QFrame{{border-radius: {0}px;background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.99999 rgba(255, 0, 127, 0), stop:1.0 {1});}}".format(
            (option.Width - 20) / 2, option.Color.name())
        circularProgress.setStyleSheet(styleSheet)
        circularProgress.setFrameShape(QFrame.NoFrame)
        circularProgress.setFrameShadow(QFrame.Raised)
        self.__progressbar = circularProgress

        # 进度条背景
        circularBg = QFrame(circularProgressBarBase)
        circularBg.setObjectName(u"circularBg")
        circularBg.setGeometry(QRect(10, 10, 300, 300))
        bgColor = option.BackgroundColor
        bgColor.setAlpha(120)

        styleSheet1 = "QFrame{{border-radius: {0}px;background-color: {1};}}".format((option.Width - 20) / 2,
                                                                                     bgColor.name(
                                                                                         QColor.NameFormat.HexArgb))
        circularBg.setStyleSheet(styleSheet1)
        circularBg.setFrameShape(QFrame.NoFrame)
        circularBg.setFrameShadow(QFrame.Raised)

        # 中心大圆
        container = QFrame(circularProgressBarBase)
        container.setObjectName(u"container")
        container.setGeometry(QRect(25, 25, 270, 270))
        container.setStyleSheet(
            "QFrame{{border-radius: {}px;background-color: {};}}".format((option.Width - 20) / 2 - 15, bgColor.name()))
        container.setFrameShape(QFrame.NoFrame)
        container.setFrameShadow(QFrame.Raised)

        # 布局
        widget = QWidget(container)
        widget.setObjectName(u"widget")
        widget.setGeometry(QRect(40, 50, 193, 191))
        gridLayout = QGridLayout(widget)
        gridLayout.setObjectName(u"gridLayout")
        gridLayout.setContentsMargins(0, 0, 0, 0)

        # 标题
        labelTitle = QLabel(widget)
        labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        labelTitle.setFont(font)
        labelTitle.setStyleSheet(u"background-color: none;color: #FFFFFF")
        labelTitle.setAlignment(Qt.AlignCenter)
        labelTitle.setText('')
        self.__title = labelTitle

        gridLayout.addWidget(labelTitle, 0, 0, 1, 6)

        # %
        labelPercent = QLabel(widget)
        labelPercent.setObjectName(u"labelPercent")
        # labelPercent.setStyleSheet(u"QLabel{margin-left: 40px;}")
        labelPercent.setText('<span style=\"font-size:40pt;vertical-align:sub; color: white;\">%</span>')
        gridLayout.addWidget(labelPercent, 1, 5, 1, 1)

        '''
             后创建 进度， 使得 进度控件在 % 控件上面
        '''
        # 进度
        labelPercentage = QLabel(widget)
        labelPercentage.setObjectName(u"labelPercentage")
        labelPercentage.setStyleSheet(u"background-color: none;color: #FFFFFF")
        labelPercentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelPercentage.setText('<span style=\"font-size:80px;color: white;\">0</span>')
        self.__percentage = labelPercentage
        gridLayout.addWidget(labelPercentage, 1, 0, 1, 6)

        # 信息
        labelLoadingInfo = QLabel(widget)
        labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        labelLoadingInfo.setMinimumSize(QSize(0, 20))
        labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        labelLoadingInfo.setFont(font2)
        labelLoadingInfo.setStyleSheet(
            u"QLabel{border-radius: 10px;background-color: rgb(93, 93, 154);color: #FFFFFF;margin-left: 20px;margin-right: 20px;}")
        labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        labelLoadingInfo.setAlignment(Qt.AlignCenter)
        labelLoadingInfo.setText("......")
        self.__loading = labelLoadingInfo

        gridLayout.addWidget(labelLoadingInfo, 2, 0, 1, 6)

        self.labelCredits = QLabel(widget)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"background-color: none; color: rgb(93, 93, 154);")
        self.labelCredits.setAlignment(Qt.AlignCenter)
        self.labelCredits.setText("正在处理中...")

        gridLayout.addWidget(self.labelCredits, 3, 0, 1, 6)

        circularBg.raise_()
        circularProgress.raise_()
        container.raise_()


    def __setProgressbarValue(self, value=0):
        stop1 = 0.99999
        stop2 = 1.0

        if value > 0:
            progress = (100 - value) / 100.0
            stop1 = progress - 0.001
            stop2 = progress

        if value == 100:
            stop1 = 1.000
            stop2 = 1.000

        styleSheet = "QFrame{{border-radius: {0}px;background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{1} rgba(255, 0, 127, 0), stop:{2} {3});}}".format(
            (self.__opt.Width - 20) / 2, stop1, stop2, self.__opt.Color.name())
        self.__progressbar.setStyleSheet(styleSheet)


    def MoveTo(self, x: int, y: int):
        self.__base.setGeometry(QRect(x, y, self.__opt.Width, self.__opt.Width))

    def setTitle(self, title):
        return self.__title.setText(title)

    def Loading(self, text):
        self.__loading.setText(text)

    def Update(self, percent):
        self.__percentage.setText('<span style=\"font-size:80px;color: white;\">{} </span>'.format(percent))
        self.__setProgressbarValue(percent)
    def setProcessing(self, text):
        self.labelCredits.setText(text)