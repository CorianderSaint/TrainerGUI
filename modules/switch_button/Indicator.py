from PySide6.QtCore import Signal, Property, QTimer
from PySide6.QtGui import QColor, QPainter, Qt
from PySide6.QtWidgets import QToolButton


class Indicator(QToolButton):
    """ 指示器 """

    checkedChanged = Signal(bool)
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setCheckable(True)
        super().setChecked(False)
        self.resize(50, 18)
        self.__sliderOnColor = QColor(Qt.white)
        self.__sliderOffColor = QColor(Qt.black)
        self.__sliderDisabledColor = QColor(QColor(155, 154, 153))
        self.timer = QTimer(self)
        self.padding = self.height() // 4
        self.sliderX = self.padding
        self.sliderRadius = (self.height() - 2 * self.padding) // 2
        self.sliderEndX = self.width() - 2 * self.sliderRadius
        self.sliderStep = self.width() / 50
        self.timer.timeout.connect(self.__updateSliderPos)
        self.mouseReleaseEventTime = 5

    def __updateSliderPos(self):
        """ 更新滑块位置 """
        if self.isChecked():
            if self.sliderX + self.sliderStep < self.sliderEndX:
                self.sliderX += self.sliderStep
            else:
                self.sliderX = self.sliderEndX
                self.timer.stop()
        else:
            if self.sliderX - self.sliderStep > self.sliderEndX:
                self.sliderX -= self.sliderStep
            else:
                self.sliderX = self.sliderEndX
                self.timer.stop()

        self.style().polish(self)

    def setChecked(self, isChecked: bool):
        """ 设置选中状态 """
        if isChecked == self.isChecked():
            return
        super().setChecked(isChecked)
        self.sliderEndX = self.width() - 2 * self.sliderRadius - \
                          self.padding if self.isChecked() else self.padding
        self.timer.start(5)
        self.checkedChanged.emit(self.isChecked())


    def mouseReleaseEvent(self, e):
        """ 鼠标点击更新选中状态 """
        super().mouseReleaseEvent(e)
        self.sliderEndX = self.width() - 2 * self.sliderRadius - \
                          self.padding if self.isChecked() else self.padding
        self.timer.start(self.mouseReleaseEventTime)
        self.checkedChanged.emit(self.isChecked())

    def resizeEvent(self, e):
        self.padding = self.height() // 4
        self.sliderRadius = (self.height() - 2 * self.padding) // 2
        self.sliderStep = self.width() / 50
        self.sliderEndX = self.width() - 2 * self.sliderRadius - self.padding if self.isChecked() else self.padding
        self.update()

    def paintEvent(self, e):
        """ 绘制指示器 """
        super().paintEvent(e)  # 背景和边框由 qss 指定
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        if self.isEnabled():
            color = self.sliderOnColor if self.isChecked() else self.sliderOffColor
        else:
            color = self.sliderDisabledColor
        painter.setBrush(color)
        painter.drawEllipse(self.sliderX, self.padding,
                            self.sliderRadius * 2, self.sliderRadius * 2)

    def getSliderOnColor(self):
        return self.__sliderOnColor

    def setSliderOnColor(self, color: QColor):
        self.__sliderOnColor = color
        self.update()

    def getSliderOffColor(self):
        return self.__sliderOffColor

    def setSliderOffColor(self, color: QColor):
        self.__sliderOffColor = color
        self.update()

    def getSliderDisabledColor(self):
        return self.__sliderDisabledColor

    def setSliderDisabledColor(self, color: QColor):
        self.__sliderDisabledColor = color
        self.update()

    sliderOnColor = Property(QColor, getSliderOnColor, setSliderOnColor)
    sliderOffColor = Property(QColor, getSliderOffColor, setSliderOffColor)
    sliderDisabledColor = Property(QColor, getSliderDisabledColor, setSliderDisabledColor)
