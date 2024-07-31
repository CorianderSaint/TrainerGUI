import os
import shutil
import random


def splitDataset(classificationNamePath, train_path, val_path, test_path, train_rate, val_rate, test_rate):
    """
    按照一个分类文件夹划分数据集
    :param classificationNamePath: 分类之一的路径
    :param train_path: 训练集根路径
    :param val_path: 验证集根路径
    :param test_path: 测试集根路径
    :param train_rate: 训练集比例
    :param val_rate: 验证集比例
    :param test_rate: 测试集比例
    """

    classificationName = os.path.basename(classificationNamePath)
    train_class_path = os.path.join(train_path, classificationName)  # 训练集根路径下该分类的路径
    val_class_path = os.path.join(val_path, classificationName)  # 验证集根路径下该分类的路径
    test_class_path = os.path.join(test_path, classificationName)  # 测试集根路径下该分类的路径

    # 定义源文件夹和目标文件夹
    folders = [train_class_path, val_class_path, test_class_path]
    ratios = [train_rate, val_rate, test_rate]

    # 获取源文件夹中所有的图片文件
    images = [image for image in os.listdir(classificationNamePath)
              if os.path.isfile(os.path.join(classificationNamePath, image))]

    # 随机打乱文件顺序
    random.shuffle(images)

    # 计算每个文件夹应分配的文件数量
    all = len(images)
    split_sizes = [int(all * r) for r in ratios]
    # 确保数量匹配：test = all - train - val
    split_sizes[-1] = all - sum(split_sizes[:-1])

    # 分配文件到对应文件夹
    start_idx = 0
    for folder, size in zip(folders, split_sizes):
        # 创建目标文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)

        # 分配文件
        for i in range(start_idx, start_idx + size):
            # 源文件路径和目标文件路径
            src_file_path = os.path.join(classificationNamePath, images[i])
            dst_file_path = os.path.join(folder, images[i])

            shutil.copy(src_file_path, dst_file_path)

        start_idx += size

