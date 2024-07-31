import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import RectangleSelector


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=96, facecolor="none"):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor=facecolor)
        self.axes = fig.add_subplot(111, facecolor=facecolor)
        # 设置 x 轴的刻度定位器为只显示整数
        self.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        super(MplCanvas, self).__init__(fig)
        # 创建矩形选择器
        self.rectangle_selector = RectangleSelector(self.axes, self.onselect, useblit=True,
                                                    button=[1],  # 只对鼠标左键作出反应
                                                    minspanx=5, minspany=5,
                                                    spancoords='pixels',
                                                    interactive=True,
                                                    props=dict(facecolor='#3CB37133', edgecolor='#3CB371', linestyle='--', linewidth=1))

    def onselect(self, eclick, erelease):
        # 当用户选择一个区域时调用
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        self.rectangle_selector.clear()

        # 放大选定的区域
        if (x2 - x1 < 0.01)  or (y2 - y1 < 0.01):
            self.axes.set_xlim(x1 - 0.01, x2 + 0.01)
            self.axes.set_ylim(y1 - 0.01, y2 + 0.01)
        else:
            self.axes.set_xlim(x1, x2)
            self.axes.set_ylim(y1, y2)
        self.draw()

    def save_view_limits(self):
        # 保存当前的视图限制
        self.original_xlim = self.axes.get_xlim()
        self.original_ylim = self.axes.get_ylim()
    def restore_view_limits(self):
        # 恢复原始的视图限制
        self.axes.set_xlim(self.original_xlim)
        self.axes.set_ylim(self.original_ylim)
        self.draw()

    def showData(self, title, x, y, z=None):
        try:
            if z is not None:
                len_y = len(y)
                len_z = len(z)

                _y = [y[-1]] * len_y
                _z = [z[-1]] * len_z

                # 横线
                line_xy, = self.axes.plot(x, _y, linestyle=':', color="#1E90FF")
                line_xz, = self.axes.plot(x, _z, linestyle=':', color="#FF6347")
                # 竖线
                line_y = self.axes.axvline(x=len(x), linestyle='--', color="#3CB371")

                self.axes.set_title(title)

                text_y = self.axes.text(len_y - 1, y[-1], str(y[-1]))
                text_z = self.axes.text(len_z - 1, z[-1], str(z[-1]))
            else:
                len_y = len(y)
                _y = [y[-1]] * len_y

                # 横线
                line_x, = self.axes.plot(x, _y, linestyle=':', color="#1E90FF")
                # 竖线
                line_y = self.axes.axvline(x=len(x), linestyle='--', color="#3CB371")

                text_y = self.axes.text(len_y - 1, y[-1], str(y[-1]))

            self.axes.set_title(title)


            def scroll(event):
                """ 鼠标滚轮滚动事件 """
                if event.inaxes == self.axes:
                    x_min, x_max = self.axes.get_xlim()
                    range_x = (x_max - x_min) / 10
                    if event.button == 'up':
                        self.axes.set_xlim(x_min + range_x, x_max - range_x)
                    elif event.button == 'down':
                        self.axes.set_xlim(x_min - range_x, x_max + range_x)
                    self.draw_idle()

            def motion(event):
                """ 鼠标移动事件 """
                if event.inaxes == self.axes:
                    if z is not None:
                        tempx = int(np.round(event.xdata))
                        if (0 <= tempx - 1 < len_y) and (0 <= tempx - 1 < len_z):
                            tempy = y[tempx - 1]
                            tempz = z[tempx - 1]

                            for i in range(len_y):
                                _y[i] = tempy
                            for i in range(len_z):
                                _z[i] = tempz

                            line_xy.set_ydata(_y)
                            line_xz.set_ydata(_z)

                            line_y.set_xdata([event.xdata])

                            text_y.set_position((event.xdata, tempy))
                            text_z.set_position((event.xdata, tempz))

                            textx = str(tempx)
                            texty = str(tempy)
                            textz = str(tempz)

                            text_y.set_text(f"({textx}, {texty})")
                            text_z.set_text(f"({textx}, {textz})")
                            self.draw_idle()
                    else:
                        tempx = int(np.round(event.xdata))
                        if 0 <= tempx - 1 < len_y:
                            tempy = y[tempx - 1]
                            for i in range(len_y):
                                _y[i] = tempy
                            line_x.set_ydata(_y)
                            line_y.set_xdata([event.xdata])
                            text_y.set_position((event.xdata, tempy))
                            textx = str(tempx)
                            texty = str(tempy)
                            text_y.set_text(f"({textx}, {texty})")
                            self.draw_idle()

            self.mpl_connect('scroll_event', scroll)
            self.mpl_connect('motion_notify_event', motion)
        except:
            pass