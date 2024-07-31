from PySide6.QtWidgets import QMessageBox

# 确认提示框
def confirmBox(widget, title, msg):
    """
    确认提示框
    :param widget: 父窗口对象
    :param title: 对话框标题
    :param msg: 提示内容
    :return:
    """
    choice = QMessageBox.question(widget, title, msg)
    if choice == QMessageBox.StandardButton.Yes :
        return "Yes"
    else:
        return "No"

# 警告提示框
def warningBox(widget, title, msg):
    """
    警告提示框
    :param widget: 父窗口对象
    :param title: 对话框标题
    :param msg: 提示内容
    :return:
    """
    QMessageBox.warning(widget, title, msg)

# 信息提示框
def infoBox(widget, title, msg):
    """
    信息提示框
    :param widget: 父窗口对象
    :param title: 对话框标题
    :param msg: 提示内容
    :return:
    """
    QMessageBox.information(widget, title, msg)

# 错误提示框
def errorBox(widget, title, msg):
    """
    错误提示框
    :param widget: 父窗口对象
    :param title: 对话框标题
    :param msg: 提示内容
    :return:
    """
    QMessageBox.critical(widget, title, msg)