import cv2
import numpy as np

class ImageAugment:
    def __init__(self, image):
        """
        实例化
        :param image: 一张用 cv2.imread() 读入的图片
        """
        self.image = image


    def rotate(self, angle, scale, fillColor):
        """
        图像旋转
        :param angle: 旋转角度，正数表示逆时针旋转，负数表示顺时针旋转
        :param scale: 变换尺度（缩放大小）
        :param fillColor: 填充颜色三元组RGB
        :return: 返回旋转后的图像
        """
        image_size = self.image.shape[:2]
        h, w = image_size
        center = int(h / 2), int(w / 2)
        fillColor = fillColor[::-1]  # RGB -> BGR

        rotatation_matrix = cv2.getRotationMatrix2D(center, angle, scale)  # 转换矩阵
        image_rotate = cv2.warpAffine(self.image, rotatation_matrix, image_size, borderValue=fillColor)

        return image_rotate


    def flip(self, flipCode):
        """
        水平翻转（绕y轴翻转）、垂直翻转（绕x轴翻转）
        :param flipCode: flipCode=0时为垂直翻转，flipCode>0时为水平翻转，flipCode<0时为同时翻转
        :return: 返回翻转后的图像
        """
        image_flip = cv2.flip(self.image, flipCode)
        return image_flip


    def blur(self, kszie):
        """
        均值滤波
        :param kszie: 滤波核大小，二元元组
        :return: 均值滤波后的图像
        """
        image_blur = cv2.blur(self.image, kszie)
        return image_blur
    def boxBlur(self, kszie):
        """
        方框滤波
        :param kszie: 滤波核大小，二元元组
        :return: 方框滤波后的图像
        """
        image_boxBlur = cv2.boxFilter(self.image, ddepth=-1, ksize=kszie)
        return image_boxBlur
    def gaussianBlur(self, ksize):
        """
        高斯滤波
        :param ksize: 滤波核大小，二元元组【必须为奇数！】
        :return: 高斯滤波后的图像
        """
        image_GaussianBlur = cv2.GaussianBlur(self.image, ksize, 0)
        return image_GaussianBlur
    def medianBlur(self, ksize):
        """
        中值滤波
        :param ksize: 滤波核大小，整数【必须为大于1的奇数！】
        :return: 中值滤波后的图像
        """
        image_medianBlur = cv2.medianBlur(self.image, ksize)
        return image_medianBlur


    def gaussianNoise(self, sigma):
        """
        高斯噪声
        :param sigma: 过调节标准差sigma, 来控制噪声的程度。
        :return: 高斯噪声后的图像
        """
        mean = 0
        # 获取图片的高度和宽度
        h, w, c = self.image.shape[:3]
        gauss = np.random.normal(mean, sigma, (h, w, c))
        image_GNoise = np.uint8(self.image + gauss)
        return image_GNoise
    def saltPepperNoise(self, rate):
        """
        椒盐噪声
        :param rate: 通过控制噪声的比例，设置图像损坏的程度
        :return: 椒盐噪声后的图像
        """
        image_saltPepperNoise = self.image.copy()
        h, w = image_saltPepperNoise.shape[:2]
        noiseCount = int(rate * h * w / 2)
        # 白噪点
        X = np.random.randint(w, size=(noiseCount,))
        Y = np.random.randint(h, size=(noiseCount,))
        image_saltPepperNoise[Y, X] = 255
        # 黑噪点
        X = np.random.randint(w, size=(noiseCount,))
        Y = np.random.randint(h, size=(noiseCount,))
        image_saltPepperNoise[Y, X] = 0
        return image_saltPepperNoise


    def brightness(self, beta):
        """
        亮度
        :param beta: 调节亮度值，默认为0
        :return: 调节亮度后的图像
        """
        image_brightness = cv2.convertScaleAbs(self.image, alpha=1, beta=beta)
        return image_brightness


    def contrast(self, alpha):
        """
        对比度
        :param alpha: 对比度调节系数，默认为1。当α<1，图像对比度下降；当α>1图像对比度上升。
        :return: 调整对比度后的图片
        """
        image_contrast = cv2.convertScaleAbs(self.image, alpha=alpha, beta=0)
        return image_contrast
