import cv2

class ImageProcess:
    def __init__(self, image_path):
        """
        实例化
        :param image_path: 一张图片的路径
        """
        self.image_path = image_path
        self.image0 = cv2.imread(self.image_path)

    def square(self, borderType, fillColor=None):
        """
        方形化图片
        :param borderType: 边界类型
        :param fillColor: 填充颜色，三元列表RGB
        :return: 返回方形化后的图片
        """
        type = None
        if borderType == "BORDER_CONSTANT":
            type = cv2.BORDER_CONSTANT
        elif borderType == "BORDER_REFLECT":
            type = cv2.BORDER_REFLECT
        elif borderType == "BORDER_REPLICATE":
            type = cv2.BORDER_REPLICATE
        elif borderType == "BORDER_WRAP":
            type = cv2.BORDER_WRAP
        image_size = self.image0.shape[:2]
        h, w = image_size
        if h != w:
            max_side = max(h, w)
            x = (max_side - w) // 2
            y = (max_side - h) // 2
            if type == cv2.BORDER_CONSTANT:
                fillColor = fillColor[::-1]     # RGB -> BGR
                image_square =  cv2.copyMakeBorder(self.image0, y, y, x, x, borderType=type, value=fillColor)
            else:
                image_square =  cv2.copyMakeBorder(self.image0, y, y, x, x, borderType=type)
            return image_square
        else:
            return self.image0

    def resize(self, dsize, interpolation):
        """
        图像缩放
        :param dsize: 输出图像大小 (宽, 高)
        :param interpolation: 插值方式
        :return: 返回缩放后的图像
        """
        interpolationType = None
        if interpolation == "INTER_LINEAR":
            interpolationType = cv2.INTER_LINEAR
        elif interpolation == "INTER_NEAREST":
            interpolationType = cv2.INTER_NEAREST
        elif interpolation == "INTER_CUBIC":
            interpolationType = cv2.INTER_CUBIC
        elif interpolation == "INTER_AREA":
            interpolationType = cv2.INTER_AREA
        elif interpolation == "INTER_LANCZOS4":
            interpolationType = cv2.INTER_LANCZOS4
        elif interpolation == "INTER_LINEAR_EXACT":
            interpolationType = cv2.INTER_LINEAR_EXACT

        image_resize = cv2.resize(self.image0, dsize=dsize, interpolation=interpolationType)
        return image_resize
