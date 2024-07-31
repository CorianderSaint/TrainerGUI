import os
import re
from lib.Share import SI
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


def getDatasetImage(path):
    """
    获取数据集中所有图片的路径
    :param path: 数据集路径
    :return: 返回一个存储所有图片路径的列表
    """
    imageList = []
    classificationNameList = os.listdir(path)
    for classificationName in classificationNameList:
        classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
        for img in os.listdir(classificationNamePath):
            imgPath = os.path.join(os.path.abspath(classificationNamePath), img)
            if getSuffix(imgPath) in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', ".BMP"]:
                imageList.append(imgPath)
    return imageList


def isChinesePath(path):
    """
    判断是否含有中文路径
    :param path: 路径
    :return: True路径含有中文，False路径不含有中文
    """
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    match = pattern.search(path)
    if match:
        return True
    else:
        return False


def getSuffix(image_path):
    """
    获取图片后缀
    :param image_path: 图片路径
    :return: 图片的后缀
    """
    return os.path.splitext(image_path)[1]


def mkClassificationDir(datasetPath, exportPath):
    """
    在导出路径下创建分类文件夹
    :param datasetPath: 原数据集路径
    :param exportPath: 导出路径
    :return: 是否创建成功
    """
    try:
        classificationNameList = getClassification(datasetPath)[1]
        for classificationName in classificationNameList:
            classificationNamePath = os.path.join(os.path.abspath(exportPath), classificationName)
            if not (os.path.exists(classificationNamePath)):
                os.makedirs(classificationNamePath)
        return True
    except:
        return False


def mkTempReviewImage(origin_path):
    """
    创建预览图象的路径
    :param origin_path: 原图像路径
    :return: 返回预览图象路径
    """
    # 原图像后缀
    suffix = getSuffix(origin_path)
    # 创建temp文件夹
    if not (os.path.exists("temp")):
        os.mkdir("temp")
    # 预览图像路径
    review_image_path = "temp/reviewTemp" + suffix
    return review_image_path

def checkImages(dataset_path):
    """
    检查数据集中图片是否损坏
    :param dataset_path: 数据集
    :return: 损坏的图片路径列表
    """
    import keras
    errorImages = []
    classificationNameList = getClassification(dataset_path)[1]
    for classificationName in classificationNameList:
        classificationNamePath = os.path.join(dataset_path, classificationName)
        for img in os.listdir(classificationNamePath):
            imgPath = os.path.join(os.path.abspath(classificationNamePath), img)
            try:
                keras.preprocessing.image.load_img(imgPath)
            except:
                errorImages.append(imgPath)
    return errorImages

def getFileNum(dataset_path):
    """
    获取文件夹下文件的数量
    :param dataset_path: 数据集根路径
    :return: 文件数量
    """
    file_count = 0
    classificationNameList = getClassification(dataset_path)[1]
    for classificationName in classificationNameList:
        classificationNamePath = os.path.join(os.path.abspath(dataset_path), classificationName)
        for img in os.listdir(classificationNamePath):
            file_count += 1
    return file_count

def getClassification(dataset_path):
    """
    获取分类数量和分类名称
    :param dataset_path: 数据集路径
    :return: 分类的数量 和 所有分类名称
    """
    folders = os.listdir(dataset_path)
    classificationNameList = [classificationName for classificationName in folders
                              if os.path.isdir(os.path.join(os.path.abspath(dataset_path), classificationName))]
    num = len(classificationNameList)
    return (num, classificationNameList)


def locate_to_outputDir(appPath):
    """
    定位到output文件夹
    :param appPath: 当前项目的绝对路径
    :return: output文件夹路径
    """
    outputDir_path = os.path.join(os.path.abspath(appPath), "output")
    if not (os.path.exists(outputDir_path)):
        os.mkdir(outputDir_path)
    return outputDir_path


def getSaveName(netName, epoch, loss, acc):
    """ 保存模型命名 """
    save_name = "%s-Epoch%d-Loss%.3f-Acc%.3f.pth" % (netName, epoch, loss, acc)
    return save_name


def calOutputSize(input_size, kernel_size, padding, stride):
    """
    计算神经网络输出参数
    """
    output_size = (input_size - kernel_size + 2 * padding) // stride + 1
    return output_size


def get_save_path(model_name):
    """ 模型保存路径 """
    return os.path.join(os.path.abspath(SI.outputDir_path), model_name)

def get_checkpoints_path():
    """ 中间模型保存路径 """
    checkpoints_path = os.path.join(os.path.abspath(SI.outputDir_path), "checkpoints")
    if not (os.path.exists(checkpoints_path)):
        os.makedirs(checkpoints_path)
    return checkpoints_path

def calculate_normalize(dataset_path):
    """
    计算数据集归一化的均值mean和方差std
    :param dataset_path: 数据集
    :return: mean和std列表
    """
    import numpy as np
    from torchvision.datasets import ImageFolder
    from torchvision.transforms import ToTensor

    means = [0, 0, 0]
    std = [0, 0, 0]  # 初始化均值和方差
    transform = ToTensor()  # 可将图片类型转化为张量，并把0~255的像素值缩小到0~1之间
    dataset = ImageFolder(dataset_path, transform=transform)  # 导入数据集的图片，并且转化为张量
    num_imgs = len(dataset)  # 获取数据集的图片数量

    for img, a in dataset:  # 遍历数据集的张量和标签
        for i in range(3):  # 遍历图片的RGB三通道
            # 计算每一个通道的均值和标准差
            means[i] += img[i, :, :].mean()
            std[i] += img[i, :, :].std()
    mean = np.array(means) / num_imgs
    std = np.array(std) / num_imgs  # 要使数据集归一化，均值和方差需除以总图片数量
    # np.array --> list
    mean_list = list(mean)
    std_list = list(std)
    # 保留三位小数
    mean_list = [round(x, 3) for x in mean_list]
    std_list = [round(x, 3) for x in std_list]

    return mean_list, std_list
