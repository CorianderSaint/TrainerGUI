from lib.Parameters import Param
from themes.widgets_style import EnabledStyle, DisabledStyle


def disable_widgets(widgets):
    """ 禁用控件 """
    # 模型设置----------------------
    # 网络选择
    widgets.comboBox_trainer_net.setStyleSheet(DisabledStyle.combobox)
    widgets.comboBox_trainer_net.setEnabled(False)
    # 模型保存间隔
    widgets.lineEdit_trainer_period.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_period.setEnabled(False)
    # ImageNet
    widgets.switchButton_trainer_imageNet.setEnabled(False)
    # 初始化权重
    widgets.switchButton_trainer_initWeights.setEnabled(False)
    # 模型参数----------------------
    # 输入图像大小
    widgets.lineEdit_trainer_inputSize1.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_inputSize1.setEnabled(False)
    widgets.lineEdit_trainer_inputSize2.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_inputSize2.setEnabled(False)
    # 损失函数
    widgets.comboBox_trainer_lossFunction.setStyleSheet(DisabledStyle.combobox)
    widgets.comboBox_trainer_lossFunction.setEnabled(False)
    # 优化器
    widgets.comboBox_trainer_optimizer.setStyleSheet(DisabledStyle.combobox)
    widgets.comboBox_trainer_optimizer.setEnabled(False)
    # 归一化参数
    widgets.btn_trainer_normalize_default.setStyleSheet(DisabledStyle.pushbutton)
    widgets.btn_trainer_normalize_default.setEnabled(False)
    widgets.btn_trainer_normalize_pretrain.setStyleSheet(DisabledStyle.pushbutton)
    widgets.btn_trainer_normalize_pretrain.setEnabled(False)
    widgets.btn_trainer_normalize_cal.setStyleSheet(DisabledStyle.pushbutton)
    widgets.btn_trainer_normalize_cal.setEnabled(False)
    # 超参数调优----------------------
    # batch size
    widgets.lineEdit_trainer_batchSize.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_batchSize.setEnabled(False)
    # learning rate
    widgets.lineEdit_trainer_learningRate.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_learningRate.setEnabled(False)
    # epoch
    widgets.lineEdit_trainer_epoch.setStyleSheet(DisabledStyle.lineedit)
    widgets.lineEdit_trainer_epoch.setEnabled(False)
    # dropout
    widgets.dSpinBox_trainer_dropout.setStyleSheet(DisabledStyle.dspinbox)
    widgets.dSpinBox_trainer_dropout.setEnabled(False)
    widgets.slider_trainer_dropout.setStyleSheet(DisabledStyle.slider)
    widgets.slider_trainer_dropout.setEnabled(False)


def enable_widgets(widgets):
    """ 启用控件 """
    # 模型设置----------------------
    # 网络选择
    widgets.comboBox_trainer_net.setStyleSheet(EnabledStyle.combobox)
    widgets.comboBox_trainer_net.setEnabled(True)
    # 模型保存间隔
    widgets.lineEdit_trainer_period.setStyleSheet(EnabledStyle.lineedit)
    widgets.lineEdit_trainer_period.setEnabled(True)
    # ImageNet
    widgets.switchButton_trainer_imageNet.setEnabled(True)
    # 初始化权重
    widgets.switchButton_trainer_initWeights.setEnabled(True)
    # 模型参数----------------------
    # 输入图像大小
    if Param.net_name not in ["VisionTransformer(b16)", "VisionTransformer(b32)"]:
        widgets.lineEdit_trainer_inputSize1.setStyleSheet(EnabledStyle.lineedit)
        widgets.lineEdit_trainer_inputSize1.setEnabled(True)
        widgets.lineEdit_trainer_inputSize2.setStyleSheet(EnabledStyle.lineedit)
        widgets.lineEdit_trainer_inputSize2.setEnabled(True)
    # 损失函数
    widgets.comboBox_trainer_lossFunction.setStyleSheet(EnabledStyle.combobox)
    widgets.comboBox_trainer_lossFunction.setEnabled(True)
    # 优化器
    widgets.comboBox_trainer_optimizer.setStyleSheet(EnabledStyle.combobox)
    widgets.comboBox_trainer_optimizer.setEnabled(True)
    # 归一化参数
    widgets.btn_trainer_normalize_default.setStyleSheet(EnabledStyle.pushbutton)
    widgets.btn_trainer_normalize_default.setEnabled(True)
    widgets.btn_trainer_normalize_pretrain.setStyleSheet(EnabledStyle.pushbutton)
    widgets.btn_trainer_normalize_pretrain.setEnabled(True)
    widgets.btn_trainer_normalize_cal.setStyleSheet(EnabledStyle.pushbutton)
    widgets.btn_trainer_normalize_cal.setEnabled(True)
    # 超参数调优----------------------
    # batch size
    widgets.lineEdit_trainer_batchSize.setStyleSheet(EnabledStyle.lineedit)
    widgets.lineEdit_trainer_batchSize.setEnabled(True)
    # learning rate
    widgets.lineEdit_trainer_learningRate.setStyleSheet(EnabledStyle.lineedit)
    widgets.lineEdit_trainer_learningRate.setEnabled(True)
    # epoch
    widgets.lineEdit_trainer_epoch.setStyleSheet(EnabledStyle.lineedit)
    widgets.lineEdit_trainer_epoch.setEnabled(True)
    # dropout
    widgets.dSpinBox_trainer_dropout.setStyleSheet(EnabledStyle.dspinbox)
    widgets.dSpinBox_trainer_dropout.setEnabled(True)
    widgets.slider_trainer_dropout.setStyleSheet(EnabledStyle.slider)
    widgets.slider_trainer_dropout.setEnabled(True)