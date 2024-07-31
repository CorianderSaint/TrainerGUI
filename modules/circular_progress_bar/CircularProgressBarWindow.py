from PySide6.QtWidgets import QMainWindow, QPushButton

from modules.circular_progress_bar.CircularProgressBar import CircularProgressBarOption, CircularProgressBar


class CircularProgressBarWindow(QMainWindow):
    def __init__(self, worker_thread, windowTitle="运行中..."):
        super().__init__()
        self.setWindowTitle(windowTitle)
        self.setMaximumSize(340, 400)
        self.setMinimumSize(340, 400)
        self.worker_thread = worker_thread

        # 设置进度条的配置
        options = CircularProgressBarOption()

        # 创建进度条实例
        self.progress_bar = CircularProgressBar(self, options)

        # 添加停止按钮
        self.stop_button = QPushButton("停止", self)
        self.stop_button.clicked.connect(self.close_window)
        self.stop_button.setGeometry(110, 340, 120, 30)
        self.stop_button.setStyleSheet("""
        QPushButton {
        	border: 2px solid #6272a4;
        	border-radius: 5px;	
        	background-color: #6272A4;
            color: #f8f8f2;
        }
        QPushButton:hover {
        	background-color: #7082b6;
        	border: 2px solid #7082b6;
        }
        QPushButton:pressed {	
        	background-color: #546391;
        	border: 2px solid #ff79c6;
        }""")

    def update_progress(self, value):
        self.progress_bar.Update(value)

    def close_window(self):
        self.worker_thread.stop()   # 停止线程
        self.close()                # 关闭窗口

    def task_finished(self):
        self.stop_button.setText("完成")  # 更新按钮文本
        self.stop_button.clicked.disconnect(self.close_window)  # 更新槽函数
        self.stop_button.clicked.connect(self.close)  # 连接到关闭窗口的槽函数