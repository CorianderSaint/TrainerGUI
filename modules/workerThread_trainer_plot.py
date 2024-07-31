from PySide6.QtCore import QThread

from lib.Parameters import Param

class WorkerThread_PlotStepLoss(QThread):
    """ Step - Loss and Running Loss """
    def __init__(self, widgets, step_data, stepLoss_data, train_steps):
        super().__init__()
        self.widgets = widgets
        self.step_data = step_data
        self.stepLoss_data = stepLoss_data
        self.train_steps = train_steps
    def run(self):
        # 标题
        title = "Step Loss and Running Loss"

        # 清除之前的绘图
        self.widgets.canvas_step_loss.axes.clear()
        # Step Loss
        self.widgets.canvas_step_loss.axes.plot(self.step_data, self.stepLoss_data,
                                                     color=Param.color_map["blue"],
                                                     label='Step Loss')
        for i in range(1, len(self.step_data)):
            if i % self.train_steps == 0:
                self.widgets.canvas_step_loss.axes.axvline(x=self.step_data[i], linestyle='-', color=Param.color_map["grey"], alpha=0.2)

        self.widgets.canvas_step_loss.save_view_limits()                               # 保存原始视图限制
        self.widgets.canvas_step_loss.axes.set_xlabel('Steps')                         # 设置x轴坐标名称
        self.widgets.canvas_step_loss.axes.set_title(title)                            # 设置标题
        self.widgets.canvas_step_loss.axes.legend()                                    # 显示图例
        self.widgets.canvas_step_loss.showData(title, self.step_data, self.stepLoss_data)    # Show Data
        self.widgets.canvas_step_loss.draw()                                           # 更新图形显示

    def stop(self):
        self.requestInterruption()


class WorkerThread_PlotEpochLossAndAcc(QThread):
    """ Epoch - Train Loss and Acc """
    def __init__(self, widgets, epoch_data, loss_data, acc_data):
        super().__init__()
        self.widgets = widgets
        self.epoch_data = epoch_data
        self.loss_data = loss_data
        self.acc_data = acc_data

    def run(self):
        # 标题
        title = "Train Loss and Validation Accuracy"
        # 清除之前的绘图
        self.widgets.canvas_epoch_loss_acc.axes.clear()
        # Train Loss
        self.widgets.canvas_epoch_loss_acc.axes.plot(self.epoch_data, self.loss_data, ".-",
                                                     color=Param.color_map["blue"],
                                                     label='Train Loss')
        # Acc
        self.widgets.canvas_epoch_loss_acc.axes.plot(self.epoch_data, self.acc_data, ".-",
                                                     color=Param.color_map["red"],
                                                     label='Validation Accuracy')

        self.widgets.canvas_epoch_loss_acc.save_view_limits()                               # 保存原始视图限制
        self.widgets.canvas_epoch_loss_acc.axes.set_xlabel('Epochs')                        # 设置x轴坐标名称
        self.widgets.canvas_epoch_loss_acc.axes.set_title(title)                            # 设置标题
        self.widgets.canvas_epoch_loss_acc.axes.legend()                                    # 显示图例
        self.widgets.canvas_epoch_loss_acc.draw()                                           # 更新图形显示
        self.widgets.canvas_epoch_loss_acc.showData(title, self.epoch_data, self.loss_data, self.acc_data)    # Show Data

    def stop(self):
        self.requestInterruption()