import os

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

import matplotlib

from lib.Share import SI

matplotlib.use('agg')  # 使用 agg 非交互式后端


class ConfusionMatrix(object):
    def __init__(self, num_classes: int, labels: list, matrix_save_path: str=None, log_text_path: str=None):
        self.matrix = np.zeros((num_classes, num_classes))
        self.num_classes = num_classes
        self.labels = labels
        self.matrix_save_path = matrix_save_path
        self.log_text_path = log_text_path


    # def update(self, preds, labels):
    #     for p, t in zip(preds, labels):
    #         self.matrix[p, t] += 1

    def update(self, preds, labels):
        for p, t in zip(preds, labels):
            if p < self.num_classes and t < self.num_classes:
                self.matrix[p, t] += 1

    def summary(self):
        # calculate accuracy
        sum_TP = 0
        for i in range(self.num_classes):
            sum_TP += self.matrix[i, i]
        acc = sum_TP / np.sum(self.matrix)
        SI.matrixAcc = acc
        print("The model accuracy is ", acc)

        # precision, recall, specificity
        table = PrettyTable()
        table.field_names = ["Classes", "Precision", "Recall", "F1-Score"]
        for i in range(self.num_classes):
            TP = self.matrix[i, i]
            FP = np.sum(self.matrix[i, :]) - TP
            FN = np.sum(self.matrix[:, i]) - TP
            TN = np.sum(self.matrix) - TP - FP - FN
            Precision = round(TP / (TP + FP), 3) if TP + FP != 0 else 0.
            Recall = round(TP / (TP + FN), 3) if TP + FN != 0 else 0.
            F1 = round((2 * Precision * Recall) / (Precision + Recall), 3) if Precision + Recall != 0 else 0.
            table.add_row([self.labels[i], Precision, Recall, F1])
        print(table)
        if self.log_text_path is not None:
            with open(self.log_text_path, 'a', encoding='utf-8') as file:
                file.write(f"The model accuracy is {acc}\n")
                # 将 table 的内容转换为字符串
                table_string = table.get_string()
                # 将字符串写入文件
                file.write(table_string)

    def plot(self):
        matrix = self.matrix
        # print(matrix)
        plt.imshow(matrix, cmap=plt.cm.Blues)

        # 设置x轴坐标label
        plt.xticks(range(self.num_classes), self.labels, rotation=45)
        # 设置y轴坐标label
        plt.yticks(range(self.num_classes), self.labels)
        # 显示colorbar
        plt.colorbar()
        plt.xlabel('True Labels')
        plt.ylabel('Predicted Labels')
        plt.title('Confusion matrix')

        # 在图中标注数量/概率信息
        thresh = matrix.max() / 2
        for x in range(self.num_classes):
            for y in range(self.num_classes):
                # 注意这里的matrix[y, x]不是matrix[x, y]
                info = int(matrix[y, x])
                plt.text(x, y, info,
                         verticalalignment='center',
                         horizontalalignment='center',
                         color="white" if info > thresh else "black")
        plt.tight_layout()
        # 保存图片
        if self.matrix_save_path is not None:
            plt.savefig(self.matrix_save_path, facecolor='none', edgecolor='none', transparent=True, dpi=300)
        plt.clf()

