import os

from PySide6.QtCore import Qt, Property, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from modules.switch_button.Indicator import Indicator


class SwitchButton(QWidget):

    checkedChanged = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__spacing = 15
        self.hBox = QHBoxLayout(self)
        self.indicator = Indicator(self)
        self.label = QLabel()
        self.__initWidget()


    def __initWidget(self):
        """ 初始化小部件 """
        # 设置布局
        self.hBox.addWidget(self.label)         # 标签在左边
        self.hBox.addWidget(self.indicator)     # 滑块在右边
        self.hBox.setSpacing(self.__spacing)
        self.hBox.setAlignment(Qt.AlignLeft)
        self.setAttribute(Qt.WA_StyledBackground)
        self.hBox.setContentsMargins(0, 0, 0, 0)

        # 设置默认样式
        current_dir = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(current_dir, 'switch_button.qss')
        with open(qss_path, encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        # 信号连接到槽
        self.indicator.checkedChanged.connect(self.checkedChanged)

    def isChecked(self):
        return self.indicator.isChecked()

    def setChecked(self, isChecked: bool):
        """ 设置选中状态 """
        self.indicator.setChecked(isChecked)

    def toggleChecked(self):
        """ 切换选中状态 """
        self.indicator.setChecked(not self.indicator.isChecked())

    def setText(self, text: str):
        self.text = text
        self.label.setText(text)
        self.adjustSize()

    def getSpacing(self):
        return self.__spacing

    def setSpacing(self, spacing: int):
        self.__spacing = spacing
        self.hBox.setSpacing(spacing)
        self.update()

    spacing = Property(int, getSpacing, setSpacing)

    def setMouseReleaseEventTime(self, mouseReleaseEventTime: int):
        """ 设置鼠标点击更新选中状态的时间 """
        self.indicator.mouseReleaseEventTime = mouseReleaseEventTime

    def setPosition(self, position):
        """ 设置 indicator 和 label 的相对位置 """
        if position == "left":
            # 设置布局
            self.hBox.addWidget(self.label)
            self.hBox.addWidget(self.indicator)
            self.hBox.setSpacing(self.__spacing)
            self.hBox.setAlignment(Qt.AlignLeft)
            self.setAttribute(Qt.WA_StyledBackground)
            self.hBox.setContentsMargins(0, 0, 0, 0)
            self.hBox.update()
        elif position == "right":
            # 设置布局
            self.hBox.addWidget(self.indicator)
            self.hBox.addWidget(self.label)
            self.hBox.setSpacing(self.__spacing)
            self.hBox.setAlignment(Qt.AlignLeft)
            self.setAttribute(Qt.WA_StyledBackground)
            self.hBox.setContentsMargins(0, 0, 0, 0)
            self.hBox.update()
        else:
            return

    def setEnabled(self, enabled: bool):
        """ 禁用或启用内部的 Indicator """
        self.indicator.setEnabled(enabled)

