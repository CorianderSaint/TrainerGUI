import os
import time

from util.Util import getSuffix


def uniformName(path, form):
    """
    统一命名
    :param path: 数据集路径
    :param form: 命名格式
    :return: 是否成功
    """
    try:
        classificationNameList = os.listdir(path)  # 列举文件夹
        for classificationName in classificationNameList:
            i = 1
            classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
            for img in os.listdir(classificationNamePath):
                src = os.path.join(os.path.abspath(classificationNamePath), img)
                dst = None
                suffix = getSuffix(src)
                if form == "分类_i":
                    dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + '_' + str(i) + suffix)
                elif form == "分类i":
                    dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + str(i) + suffix)
                elif form == "分类-i":
                    dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + '-' + str(i) + suffix)
                try:
                    os.rename(src, dst)
                    i += 1
                except:
                    continue
        return True
    except:
        return False

def uniformName_image(src, classificationNamePath, classificationName, suffix, index, form):
    """
    统一命名
    path = D:\\AAA\\BBB\\CCC\\classificationName\\x.jpg
    :param src: 原图片绝对路径
    :param classificationNamePath: D:\\AAA\\BBB\\CCC\\classificationName
    :param classificationName: classificationName
    :param suffix: .jpg
    :param index: i
    :param form: 命名格式
    :return: 是否成功
    """

    try:
        dst = None
        if form == "分类_i":
            dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + '_' + str(index) + suffix)
        elif form == "分类i":
            dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + str(index) + suffix)
        elif form == "分类-i":
            dst = os.path.join(os.path.abspath(classificationNamePath), str(classificationName) + '-' + str(index) + suffix)
        os.rename(src, dst)

        return True
    except:
        return False

def uniformName_temp(dirPath):
    """
    将数据集按照时间戳暂时命名
    :param dirPath: 数据集路径
    :return: 返回修改后的所有图片路径列表
    """
    try:
        images = []
        timestamp = str(round(time.time() * 100))       # 当前时间戳
        classificationNameList = os.listdir(dirPath)    # 列举文件夹
        for classificationName in classificationNameList:
            i = 1
            classificationNamePath = os.path.join(os.path.abspath(dirPath), classificationName)
            for img in os.listdir(classificationNamePath):
                src = os.path.join(os.path.abspath(classificationNamePath), img)
                suffix = getSuffix(src)
                dst = os.path.join(os.path.abspath(classificationNamePath), 'temp_' + timestamp + '_' + str(i) + suffix)
                try:
                    os.rename(src, dst)
                    i += 1
                except:
                    continue
                images.append(dst)
        return images
    except:
        return []

