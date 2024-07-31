import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
import torchvision.models as models

from algorithms.trainer.nets.alexnet import AlexNet
from algorithms.trainer.nets.efficientnet import efficientnet_b0, efficientnet_b1, efficientnet_b2, efficientnet_b3
from algorithms.trainer.nets.efficientnet import efficientnet_b4, efficientnet_b5, efficientnet_b6, efficientnet_b7
from algorithms.trainer.nets.efficientnet_v2 import efficientnet_v2_s, efficientnet_v2_m, efficientnet_v2_l
from algorithms.trainer.nets.googlenet import GoogLeNet
from algorithms.trainer.nets.mobilenet_v2 import MobileNetV2
from algorithms.trainer.nets.mobilenet_v3 import mobilenet_v3_large, mobilenet_v3_small
from algorithms.trainer.nets.resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from algorithms.trainer.nets.resnet import resnext50_32x4d, resnext101_32x8d
from algorithms.trainer.nets.shufflenet_v2 import shufflenet_v2_x0_5, shufflenet_v2_x1_0
from algorithms.trainer.nets.shufflenet_v2 import shufflenet_v2_x1_5, shufflenet_v2_x2_0
from algorithms.trainer.nets.swin_transformer import swin_tiny_patch4_window7_224, swin_small_patch4_window7_224
from algorithms.trainer.nets.swin_transformer import swin_base_patch4_window7_224
from algorithms.trainer.nets.vggnet import vgg
from algorithms.trainer.nets.vision_transformer import vit_base_patch16, vit_base_patch32

from lib.Parameters import Param

def choose_loss_function():
    """ 损失函数 """
    if Param.loss_function == "CrossEntropyLoss":
        return nn.CrossEntropyLoss()
    if Param.loss_function == "Softmax":
        return nn.Softmax()

def choose_optimizer(net):
    """ 优化器 """
    if Param.optimizer == "Adam":
        return optim.Adam(net.parameters(), lr=Param.learning_rate)
    if Param.optimizer == "SGD":
        return optim.SGD(net.parameters(), lr=Param.learning_rate)

def get_transform():
    """ transform """
    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(Param.input_size),
                                     transforms.ToTensor(),
                                     transforms.Normalize(Param.train_mean, Param.train_std)]),
        "val": transforms.Compose([transforms.Resize((Param.input_size, Param.input_size)),
                                   transforms.ToTensor(),
                                   transforms.Normalize(Param.val_mean, Param.val_std)])
    }
    return data_transform

def choose_net(isTrain=True):
    """
    选择神经网络
    :param isTrain: 是训练模式还是验证模式
    :return: 神经网络
    """
    net = None
    # AlexNet
    if Param.net_name == "AlexNet":
        if Param.isTransferLearning:
            if isTrain:
                net = models.alexnet(weights=None)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/alexnet.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                net.classifier[-1].out_features = Param.num_classes
            else:
                net = models.alexnet(weights=None)
                net.classifier[-1].out_features = Param.num_classes
        else:
            net = AlexNet(num_classes=Param.num_classes, init_weights=Param.init_weights)
    # VGG11
    elif Param.net_name == "VGG11":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vgg11(weights=None)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vgg11.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                net.classifier[-1].out_features = Param.num_classes
            else:
                net = models.vgg11(weights=None)
                net.classifier[-1].out_features = Param.num_classes
        else:
            net = vgg(model_name="vgg11", num_classes=Param.num_classes, init_weights=Param.init_weights)
    # VGG13
    elif Param.net_name == "VGG13":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vgg13(weights=None)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vgg13.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                net.classifier[-1].out_features = Param.num_classes
            else:
                net = models.vgg13(weights=None)
                net.classifier[-1].out_features = Param.num_classes
        else:
            net = vgg(model_name="vgg13", num_classes=Param.num_classes, init_weights=Param.init_weights)
    # VGG16
    elif Param.net_name == "VGG16":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vgg16(weights=None)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vgg16.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                net.classifier[-1].out_features = Param.num_classes
            else:
                net = models.vgg16(weights=None)
                net.classifier[-1].out_features = Param.num_classes
        else:
            net = vgg(model_name="vgg16", num_classes=Param.num_classes, init_weights=Param.init_weights)
    # VGG19
    elif Param.net_name == "VGG19":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vgg19(weights=None)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vgg19.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                net.classifier[-1].out_features = Param.num_classes
            else:
                net = models.vgg19(weights=None)
                net.classifier[-1].out_features = Param.num_classes
        else:
            net = vgg(model_name="vgg19", num_classes=Param.num_classes, init_weights=Param.init_weights)
    # GoogLeNet
    elif Param.net_name == "GoogLeNet":
        if Param.isTransferLearning:
            if isTrain:
                net = models.googlenet(init_weights=False)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/googlenet.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.googlenet(init_weights=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
        else:
            if isTrain:
                net = GoogLeNet(num_classes=Param.num_classes, aux_logits=True, init_weights=Param.init_weights)
            else:
                net = GoogLeNet(num_classes=Param.num_classes, aux_logits=False, init_weights=Param.init_weights)
    # ResNet18
    elif Param.net_name == "ResNet18":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnet18()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnet18.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnet18(num_classes=Param.num_classes)
        else:
            net = resnet18(num_classes=Param.num_classes)
    # ResNet34
    elif Param.net_name == "ResNet34":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnet34()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnet34.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnet34(num_classes=Param.num_classes)
        else:
            net = resnet34(num_classes=Param.num_classes)
    # ResNet50
    elif Param.net_name == "ResNet50":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnet50()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnet50.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnet50(num_classes=Param.num_classes)
        else:
            net = resnet50(num_classes=Param.num_classes)
    # ResNet101
    elif Param.net_name == "ResNet101":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnet101()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnet101.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnet101(num_classes=Param.num_classes)
        else:
            net = resnet101(num_classes=Param.num_classes)
    # ResNet152
    elif Param.net_name == "ResNet152":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnet152()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnet152.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnet152(num_classes=Param.num_classes)
        else:
            net = resnet152(num_classes=Param.num_classes)
    # ResNeXt50(32x4d)
    elif Param.net_name == "ResNeXt50(32x4d)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnext50_32x4d()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnext50_32x4d.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnext50_32x4d(num_classes=Param.num_classes)
        else:
            net = resnext50_32x4d(num_classes=Param.num_classes)
    # ResNeXt101(32x8d)
    elif Param.net_name == "ResNeXt101(32x8d)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.resnext101_32x8d()
                pretrained_weights = torch.load("algorithms/trainer/imagenet/resnext101_32x8d.pth")
                net.load_state_dict(pretrained_weights, strict=False)
                in_channel = net.fc.in_features
                net.fc = nn.Linear(in_channel, Param.num_classes)
            else:
                net = models.resnext101_32x8d(num_classes=Param.num_classes)
        else:
            net = resnext101_32x8d(num_classes=Param.num_classes)
    # MobileNetV2
    elif Param.net_name == "MobileNetV2":
        if Param.isTransferLearning:
            if isTrain:
                net = models.mobilenet_v2(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/mobilenet_v2.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.mobilenet_v2(num_classes=Param.num_classes)
        else:
            net = MobileNetV2(num_classes=Param.num_classes)
    # MobileNetV3(large)
    elif Param.net_name == "MobileNetV3(large)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.mobilenet_v3_large(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/mobilenet_v3_large.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.mobilenet_v3_large(num_classes=Param.num_classes)
        else:
            net = mobilenet_v3_large(num_classes=Param.num_classes)
    # MobileNetV3(small)
    elif Param.net_name == "MobileNetV3(small)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.mobilenet_v3_small(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/mobilenet_v3_small.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.mobilenet_v3_small(num_classes=Param.num_classes)
        else:
            net = mobilenet_v3_small(num_classes=Param.num_classes)
    # ShuffleNetV2(x0.5)
    elif Param.net_name == "ShuffleNetV2(x0.5)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.shufflenet_v2_x0_5(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/shufflenetv2_x0_5.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.shufflenet_v2_x0_5(num_classes=Param.num_classes)
        else:
            net = shufflenet_v2_x0_5(num_classes=Param.num_classes)
    # ShuffleNetV2(x1.0)
    elif Param.net_name == "ShuffleNetV2(x1.0)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.shufflenet_v2_x1_0(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/shufflenetv2_x1_0.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.shufflenet_v2_x1_0(num_classes=Param.num_classes)
        else:
            net = shufflenet_v2_x1_0(num_classes=Param.num_classes)
    # ShuffleNetV2(x1.5)
    elif Param.net_name == "ShuffleNetV2(x1.5)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.shufflenet_v2_x1_5(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/shufflenetv2_x1_5.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.shufflenet_v2_x1_5(num_classes=Param.num_classes)
        else:
            net = shufflenet_v2_x1_5(num_classes=Param.num_classes)
    # ShuffleNetV2(x2.0)
    elif Param.net_name == "ShuffleNetV2(x2.0)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.shufflenet_v2_x2_0(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/shufflenetv2_x2_0.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.shufflenet_v2_x2_0(num_classes=Param.num_classes)
        else:
            net = shufflenet_v2_x2_0(num_classes=Param.num_classes)
    # EfficientNetB0
    elif Param.net_name == "EfficientNetB0":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b0(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b0.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b0(num_classes=Param.num_classes)
        else:
            net = efficientnet_b0(num_classes=Param.num_classes)
    # EfficientNetB1
    elif Param.net_name == "EfficientNetB1":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b1(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b1.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b1(num_classes=Param.num_classes)
        else:
            net = efficientnet_b1(num_classes=Param.num_classes)
    # EfficientNetB2
    elif Param.net_name == "EfficientNetB2":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b2(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b2.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b2(num_classes=Param.num_classes)
        else:
            net = efficientnet_b2(num_classes=Param.num_classes)
    # EfficientNetB3
    elif Param.net_name == "EfficientNetB3":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b3(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b3.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b3(num_classes=Param.num_classes)
        else:
            net = efficientnet_b3(num_classes=Param.num_classes)
    # EfficientNetB4
    elif Param.net_name == "EfficientNetB4":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b4(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b4.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b4(num_classes=Param.num_classes)
        else:
            net = efficientnet_b4(num_classes=Param.num_classes)
    # EfficientNetB5
    elif Param.net_name == "EfficientNetB5":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b5(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b5.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b5(num_classes=Param.num_classes)
        else:
            net = efficientnet_b5(num_classes=Param.num_classes)
    # EfficientNetB6
    elif Param.net_name == "EfficientNetB6":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b6(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b6.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b6(num_classes=Param.num_classes)
        else:
            net = efficientnet_b6(num_classes=Param.num_classes)
    # EfficientNetB7
    elif Param.net_name == "EfficientNetB7":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_b7(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_b7.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_b7(num_classes=Param.num_classes)
        else:
            net = efficientnet_b7(num_classes=Param.num_classes)
    # EfficientNetV2-S
    elif Param.net_name == "EfficientNetV2-S":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_v2_s(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_v2_s.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_v2_s(num_classes=Param.num_classes)
        else:
            net = efficientnet_v2_s(num_classes=Param.num_classes)
    # EfficientNetV2-M
    elif Param.net_name == "EfficientNetV2-M":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_v2_m(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_v2_m.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_v2_m(num_classes=Param.num_classes)
        else:
            net = efficientnet_v2_m(num_classes=Param.num_classes)
    # EfficientNetV2-L
    elif Param.net_name == "EfficientNetV2-L":
        if Param.isTransferLearning:
            if isTrain:
                net = models.efficientnet_v2_l(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/efficientnet_v2_l.pth")
                pre_dict = {k: v for k, v in pretrained_weights.items() if net.state_dict()[k].numel() == v.numel()}
                net.load_state_dict(pre_dict, strict=False)
            else:
                net = models.efficientnet_v2_l(num_classes=Param.num_classes)
        else:
            net = efficientnet_v2_l(num_classes=Param.num_classes)
    # VisionTransformer(b16)
    elif Param.net_name == "VisionTransformer(b16)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vit_b_16(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vit_b_16.pth")
                del_keys = ['heads.head.weight', 'heads.head.bias']
                for k in del_keys: del pretrained_weights[k]
                net.load_state_dict(pretrained_weights, strict=False)
            else:
                net = models.vit_b_16(num_classes=Param.num_classes)
        else:
            net = vit_base_patch16(num_classes=Param.num_classes, img_size=Param.input_size)
    # VisionTransformer(b32)
    elif Param.net_name == "VisionTransformer(b32)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.vit_b_32(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/vit_b_32.pth")
                del_keys = ['heads.head.weight', 'heads.head.bias']
                for k in del_keys: del pretrained_weights[k]
                net.load_state_dict(pretrained_weights, strict=False)
            else:
                net = models.vit_b_32(num_classes=Param.num_classes)
        else:
            net = vit_base_patch32(num_classes=Param.num_classes, img_size=Param.input_size)
    # SwinTransformer(t)
    elif Param.net_name == "SwinTransformer(t)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.swin_t(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/swin_t.pth")
                for k in list(pretrained_weights.keys()):
                    if "head" in k:
                        del pretrained_weights[k]
                net.load_state_dict(pretrained_weights, strict=False)
            else:
                net = models.swin_t(num_classes=Param.num_classes)
        else:
            net = swin_tiny_patch4_window7_224(num_classes=Param.num_classes, img_size=Param.input_size)
    # SwinTransformer(s)
    elif Param.net_name == "SwinTransformer(s)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.swin_s(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/swin_s.pth")
                for k in list(pretrained_weights.keys()):
                    if "head" in k:
                        del pretrained_weights[k]
                net.load_state_dict(pretrained_weights, strict=False)
            else:
                net = models.swin_s(num_classes=Param.num_classes)
        else:
            net = swin_small_patch4_window7_224(num_classes=Param.num_classes, img_size=Param.input_size)
    # SwinTransformer(b)
    elif Param.net_name == "SwinTransformer(b)":
        if Param.isTransferLearning:
            if isTrain:
                net = models.swin_b(num_classes=Param.num_classes)
                pretrained_weights = torch.load("algorithms/trainer/imagenet/swin_b.pth")
                for k in list(pretrained_weights.keys()):
                    if "head" in k:
                        del pretrained_weights[k]
                net.load_state_dict(pretrained_weights, strict=False)
            else:
                net = models.swin_b(num_classes=Param.num_classes)
        else:
            net = swin_base_patch4_window7_224(num_classes=Param.num_classes, img_size=Param.input_size)

    # RETURN
    return net
