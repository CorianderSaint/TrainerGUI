import os

from lib.Share import SI


def toJpg(path, dirFlag):
    """
    将图片的后缀转换为jpg
    :param path: 图片/数据集 路径
    :param dirFlag: 是单张图片还是数据集
    :return: 数据集返回"OK"，单张图片返回修改后的图片完整路径，失败则返回空串
    """
    new_suffix = ".jpg"

    try:
        # 数据集
        if dirFlag:
            classificationNameList = os.listdir(path)
            for classificationName in classificationNameList:
                classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 获取得到文件后缀
                    split_image_name = os.path.splitext(img)
                    new_image_suffix = split_image_name[0] + new_suffix            # 修改后的文件完整名称
                    # 实现重命名操作
                    os.rename(
                        os.path.join(classificationNamePath, img),                 # 文件路径不变
                        os.path.join(classificationNamePath, new_image_suffix))    # 文件后缀变为 new_suffix 值
            return "OK"

        # 单张图片
        else:
            # 获取得到文件后缀
            split_image_name = os.path.splitext(path)
            new_image_suffix = split_image_name[0] + new_suffix  # 修改后的文件完整名称
            os.rename(  # 实现重命名操作
                os.path.join(path, path),  # 文件路径不变
                os.path.join(path, new_image_suffix))  # 文件后缀变为 new_suffix 值
            SI.image_path = new_image_suffix
            return new_image_suffix
    except Exception as e:
        print("《toJpg》时错误：", e)
        return ""


def toJpeg(path, dirFlag):
    """
        将图片的后缀转换为jpeg
        :param path: 图片/数据集 路径
        :param dirFlag: 是单张图片还是数据集
        :return: 数据集返回"OK"，单张图片返回修改后的图片完整路径，失败则返回空串
        """
    new_suffix = ".jpeg"

    try:
        # 数据集
        if dirFlag == True:
            classificationNameList = os.listdir(path)
            for classificationName in classificationNameList:
                classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 获取得到文件后缀
                    split_image_name = os.path.splitext(img)
                    new_image_suffix = split_image_name[0]+ new_suffix             # 修改后的文件完整名称
                    os.rename(                              # 实现重命名操作
                        os.path.join(classificationNamePath, img),                 # 文件路径不变
                        os.path.join(classificationNamePath, new_image_suffix))    # 文件后缀变为 new_suffix 值
            return "OK"
        # 单张图片
        else:
            # 获取得到文件后缀
            split_image_name = os.path.splitext(path)
            new_image_suffix = split_image_name[0] + new_suffix  # 修改后的文件完整名称
            os.rename(  # 实现重命名操作
                os.path.join(path, path),  # 文件路径不变
                os.path.join(path, new_image_suffix))  # 文件后缀变为 new_suffix 值
            SI.image_path = new_image_suffix
            return new_image_suffix
    except Exception as e:
        print("《toJpeg》时错误：", e)
        return ""


def toPng(path, dirFlag):
    """
    将图片的后缀转换为png
    :param path: 图片/数据集 路径
    :param dirFlag: 是单张图片还是数据集
    :return: 数据集返回"OK"，单张图片返回修改后的图片完整路径，失败则返回空串
    """
    new_suffix = ".png"

    try:
        # 数据集
        if dirFlag == True:
            classificationNameList = os.listdir(path)
            for classificationName in classificationNameList:
                classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 获取得到文件后缀
                    split_image_name = os.path.splitext(img)
                    new_image_suffix = split_image_name[0]+ new_suffix             # 修改后的文件完整名称
                    os.rename(                              # 实现重命名操作
                        os.path.join(classificationNamePath, img),                 # 文件路径不变
                        os.path.join(classificationNamePath, new_image_suffix))    # 文件后缀变为 new_suffix 值
            return "OK"
        # 单张图片
        else:
            # 获取得到文件后缀
            split_image_name = os.path.splitext(path)
            new_image_suffix = split_image_name[0] + new_suffix  # 修改后的文件完整名称
            os.rename(  # 实现重命名操作
                os.path.join(path, path),  # 文件路径不变
                os.path.join(path, new_image_suffix))  # 文件后缀变为 new_suffix 值
            SI.image_path = new_image_suffix
            return new_image_suffix
    except Exception as e:
        print("《toPng》时错误：", e)
        return ""



def toBmp(path, dirFlag):
    """
        将图片的后缀转换为bmp
        :param path: 图片/数据集 路径
        :param dirFlag: 是单张图片还是数据集
        :return: 数据集返回"OK"，单张图片返回修改后的图片完整路径，失败则返回空串
        """
    new_suffix = ".bmp"

    try:
        # 数据集
        if dirFlag == True:
            classificationNameList = os.listdir(path)
            for classificationName in classificationNameList:
                classificationNamePath = os.path.join(os.path.abspath(path), classificationName)
                for img in os.listdir(classificationNamePath):
                    # 获取得到文件后缀
                    split_image_name = os.path.splitext(img)
                    new_image_suffix = split_image_name[0]+ new_suffix             # 修改后的文件完整名称
                    os.rename(                              # 实现重命名操作
                        os.path.join(classificationNamePath, img),                 # 文件路径不变
                        os.path.join(classificationNamePath, new_image_suffix))    # 文件后缀变为 new_suffix 值
            return "OK"
        # 单张图片
        else:
            # 获取得到文件后缀
            split_image_name = os.path.splitext(path)
            new_image_suffix = split_image_name[0] + new_suffix  # 修改后的文件完整名称
            os.rename(  # 实现重命名操作
                os.path.join(path, path),  # 文件路径不变
                os.path.join(path, new_image_suffix))  # 文件后缀变为 new_suffix 值
            SI.image_path = new_image_suffix
            return new_image_suffix
    except Exception as e:
        print("《toBmp》时错误：", e)
        return ""