import os.path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

from algorithms.trainer.confusion_matrix.confusion_matrix_run import ConfusionMatrixRun
from algorithms.trainer.model_train import WorkerThread_ModelTrain
from lib.Share import SI
from modules.circular_progress_bar.CircularProgressBarWindow import CircularProgressBarWindow
from modules.workerThread_calculate_normalize import WorkerThreadCalculateNormalize
from modules.workerThread_trainer_plot import *
from themes.widgets_style import EnabledStyle, DisabledStyle
from util.DisableWidgets import enable_widgets
from util.MessageBox import *
from util.Util import getFileNum


class FuncTrainer:
    def __init__(self, window, widgets):
        self.window = window
        self.widgets = widgets

    # ================================================================================================================
    # =================================================    线程操作    ================================================
    # ================================================================================================================

    # *************************************************    Trainer    *************************************************
    def runningThread(self, threadClass):
        SI.threadMutex = True
        print(f"正在运行：{Param.net_name}")
        try:
            # 训练线程
            self.window.workerThread_trainerRun = threadClass()
            self.window.workerThread_trainerRun.finished_signal.connect(lambda: self.thread_trainer_finished())
            self.window.workerThread_trainerRun.terminated_signal.connect(lambda: self.thread_trainer_terminated())
            # step画布
            self.window.workerThread_trainerRun.update_step_loss_signal.connect(
                lambda step_data, stepLoss_data, train_steps:
                self.update_plot_step_loss(step_data, stepLoss_data, train_steps)
            )
            # epoch画布
            self.window.workerThread_trainerRun.update_epoch_lossAndAcc_signal.connect(
                lambda epoch_data, loss_data, acc_data:
                self.update_plot_epoch_lossAndAcc(epoch_data, loss_data, acc_data)
            )
            # 开启线程
            self.window.workerThread_trainerRun.start()

        except Exception as e:
            print(f"《{Param.net_name}-run》时错误：", e)

    def thread_trainer_finished(self):
        """ 网络线程运行完成后 """
        print("Thread draw finished.")
        # 启用混淆矩阵按钮
        self.widgets.btn_trainer_matrix.setEnabled(True)
        self.widgets.btn_trainer_matrix.setStyleSheet(EnabledStyle.pushbutton)
        # 开启混淆矩阵线程 =================================================================================
        self.window.workerThread_matrix = ConfusionMatrixRun()
        self.window.workerThread_matrix.finished_signal.connect(lambda: self.thread_matrix_finished())
        self.window.workerThread_matrix.terminated_signal.connect(lambda: self.thread_matrix_terminated())
        self.window.workerThread_matrix.start()

    def thread_trainer_terminated(self):
        """ 网络线程中断后 """
        SI.threadMutex = False
        print("Thread draw terminated.")
        # 禁用混淆矩阵按钮
        self.widgets.btn_trainer_matrix.setEnabled(False)
        self.widgets.btn_trainer_matrix.setStyleSheet(DisabledStyle.pushbutton)
        # 启用控件
        enable_widgets(self.widgets)

    def thread_matrix_finished(self):
        """ 混淆矩阵运行完成后 """
        SI.threadMutex = False
        # 展示混淆矩阵
        self.widgets.img_confusionMatrix.setPixmap(QPixmap(SI.matrix_save_path))
        self.widgets.img_confusionMatrix.setScaledContents(True)
        # 展示模型准确率
        self.widgets.lb_showAcc.setText("The model accuracy is %.3f" % SI.matrixAcc)
        # 启用控件
        enable_widgets(self.widgets)

    def thread_matrix_terminated(self):
        """ 混淆矩阵运行中断后 """
        SI.threadMutex = False
        # 禁用混淆矩阵按钮
        self.widgets.btn_trainer_matrix.setEnabled(False)
        self.widgets.btn_trainer_matrix.setStyleSheet(DisabledStyle.pushbutton)
        # 启用控件
        enable_widgets(self.widgets)




    # ************************************************    step    ******************************************************
    def update_plot_step_loss(self, step_data, stepLoss_data, train_steps):
        """ step-loss画布画点 """
        # 标题
        title = "Step Loss"

        # 清除之前的绘图
        self.widgets.canvas_step_loss.axes.clear()
        # Step Loss
        self.widgets.canvas_step_loss.axes.plot(step_data, stepLoss_data,
                                                color=Param.color_map["blue"],
                                                label='Step Loss')
        # 每个Epoch画一条分隔线
        for i in range(1, len(step_data)):
            if i % train_steps == 0:
                self.widgets.canvas_step_loss.axes.axvline(x=step_data[i], linestyle='-', color=Param.color_map["grey"], alpha=0.2)

        self.widgets.canvas_step_loss.save_view_limits()                               # 保存原始视图限制
        self.widgets.canvas_step_loss.axes.set_xlabel('Steps')                         # 设置x轴坐标名称
        self.widgets.canvas_step_loss.axes.set_title(title)                            # 设置标题
        self.widgets.canvas_step_loss.axes.legend()                                    # 显示图例
        self.widgets.canvas_step_loss.draw()                                           # 更新图形显示
        # 保存画布
        try:
            self.widgets.canvas_step_loss.figure.savefig(os.path.join(os.path.abspath(SI.log_dir_path), f"{Param.net_name}-steps.png"))
        except:
            pass
        # Show Data
        self.widgets.canvas_step_loss.showData(title, step_data, stepLoss_data)

    # *************************************************    epoch    ****************************************************
    def update_plot_epoch_lossAndAcc(self, epoch_data, loss_data, acc_data):
        """ epoch-loss-acc画布画点 """
        # 标题
        title = "Train Loss and Validation Accuracy"

        # 清除之前的绘图
        self.widgets.canvas_epoch_loss_acc.axes.clear()
        # Train Loss
        self.widgets.canvas_epoch_loss_acc.axes.plot(epoch_data, loss_data, ".-",
                                                     color=Param.color_map["blue"],
                                                     label='Train Loss')
        # Validation Accuracy
        self.widgets.canvas_epoch_loss_acc.axes.plot(epoch_data, acc_data, ".-",
                                                     color=Param.color_map["red"],
                                                     label='Validation Accuracy')

        self.widgets.canvas_epoch_loss_acc.save_view_limits()                                   # 保存原始视图限制
        self.widgets.canvas_epoch_loss_acc.axes.set_xlabel('Epochs')                            # 设置x轴坐标名称
        self.widgets.canvas_epoch_loss_acc.axes.set_title(title)                                # 设置标题
        self.widgets.canvas_epoch_loss_acc.axes.legend()                                        # 显示图例
        self.widgets.canvas_epoch_loss_acc.draw()                                               # 更新图形显示
        # 保存画布
        try:
            self.widgets.canvas_epoch_loss_acc.figure.savefig(os.path.join(os.path.abspath(SI.log_dir_path), f"{Param.net_name}-epochs.png"))
        except:
            pass
        # Show Data
        self.widgets.canvas_epoch_loss_acc.showData(title, epoch_data, loss_data, acc_data)

    # ================================================================================================================
    # =================================================    归一化计算    ===============================================
    # ================================================================================================================
    def cal_normalize_run(self):
        SI.threadMutex = True
        print(f"正在运行：归一化计算")
        try:
            # 获取图片总量
            total = getFileNum(SI.dataset_train_path)
            total += getFileNum(SI.dataset_val_path)
            total += getFileNum(SI.dataset_test_path)
            # 执行多线程
            self.window.workerThread_calNormalize = WorkerThreadCalculateNormalize()
            self.window.progress_window = CircularProgressBarWindow(self.window.workerThread_calNormalize, f"正在运行：归一化计算")
            self.window.progress_window.show()
            self.window.workerThread_calNormalize.update_signal.connect(
                lambda i: self.window.progress_window.update_progress(int(round(i / total, 2) * 100)))
            self.window.workerThread_calNormalize.update_signal.connect(
                lambda i: self.window.progress_window.progress_bar.Loading(f"{i}/{total}"))
            self.window.workerThread_calNormalize.finished_signal.connect(self.window.progress_window.task_finished)
            self.window.workerThread_calNormalize.finished_signal.connect(lambda: self.cal_normalize_run_finished("归一化计算"))
            self.window.workerThread_calNormalize.terminate_signal.connect(lambda: self.cal_normalize_run_terminate("归一化计算"))
            self.window.workerThread_calNormalize.start()

        except Exception as e:
            print(f"《归一化计算-run》时错误：", e)

    def cal_normalize_run_finished(self, runningFunction):
        """ 子线程运行完成后 """
        SI.threadMutex = False
        # ui控件展示
        self.widgets.lineEdit_trainer_train_mean.setText(str(Param.train_mean))
        self.widgets.lineEdit_trainer_train_std.setText(str(Param.train_std))
        self.widgets.lineEdit_trainer_val_mean.setText(str(Param.val_mean))
        self.widgets.lineEdit_trainer_val_std.setText(str(Param.val_std))
        self.widgets.lineEdit_trainer_test_mean.setText(str(Param.test_mean))
        self.widgets.lineEdit_trainer_test_std.setText(str(Param.test_std))
        # 完成
        self.window.workerThread_calNormalize.deleteLater()
        self.window.workerThread_calNormalize = None
        infoBox(self.window, "成功", f"{runningFunction}完成")
        # 3秒后释放进度条窗口
        timer = QTimer(self.window.progress_window)
        timer.timeout.connect(self.window.progress_window.deleteLater)
        timer.start(3000)

    def cal_normalize_run_terminate(self, runningFunction):
        """ 子线程中断 """
        SI.threadMutex = False
        # ui控件展示
        self.widgets.lineEdit_trainer_train_mean.setText("")
        self.widgets.lineEdit_trainer_train_std.setText("")
        self.widgets.lineEdit_trainer_val_mean.setText("")
        self.widgets.lineEdit_trainer_val_std.setText("")
        self.widgets.lineEdit_trainer_test_mean.setText("")
        self.widgets.lineEdit_trainer_test_std.setText("")
        errorBox(self.window, "错误", f"{runningFunction}运行中断")
        self.window.progress_window.deleteLater()


    # ================================================================================================================
    # =================================================    网络选择    ================================================
    # ================================================================================================================
    def run_net(self):
        SI.matrix_save_path = os.path.join(os.path.abspath(SI.log_dir_path), f"{Param.net_name}-ConfusionMatrix.png")
        print("matrix_save_path=", SI.matrix_save_path)
        self.runningThread(WorkerThread_ModelTrain)



