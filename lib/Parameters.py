class Param:
    # 模型设置=============================
    # 网络选择
    # AlexNet / VGG11 / VGG13 / VGG16 / VGG19 / GoogLeNet /
    # ResNet18 / ResNet34 / ResNet50 / ResNet101 / ResNet152 / ResNeXt50(32x4d) / ResNeXt101(32x8d) /
    # MobileNetV2 / MobileNetV3(large) / MobileNetV3(small) /
    # ShuffleNetV2(x0.5) / ShuffleNetV2(x1.0) / ShuffleNetV2(x1.5) / ShuffleNetV2(x2.0) /
    # EfficientNetB0 / EfficientNetB1 / EfficientNetB2 / EfficientNetB3 /
    # EfficientNetB4 / EfficientNetB5 / EfficientNetB6 / EfficientNetB7 /
    # EfficientNetV2-S / EfficientNetV2-M / EfficientNetV2-L /
    # VisionTransformer(b16) / VisionTransformer(b32) /
    # SwinTransformer(t) / SwinTransformer(s) / SwinTransformer(b)
    net_name = ""

    # 模型保存间隔
    save_period = 10

    # 是否启用迁移学习
    isTransferLearning = False

    # 初始化权重
    init_weights = True

    # 模型参数=============================
    # 分类数
    num_classes: int = 15

    # 输入大小
    input_size = 224

    # 损失函数
    # CrossEntropyLoss / Softmax
    loss_function = "CrossEntropyLoss"

    # 优化器
    # Adam / SGD
    optimizer = "Adam"

    # 归一化参数
    train_mean = [0.5, 0.5, 0.5]
    train_std = [0.5, 0.5, 0.5]
    val_mean = [0.5, 0.5, 0.5]
    val_std = [0.5, 0.5, 0.5]
    test_mean = [0.5, 0.5, 0.5]
    test_std = [0.5, 0.5, 0.5]


    # 超参数=============================
    batch_size = 32
    learning_rate = 0.01
    epochs = 10
    dropout = 0.5

    # color=============================
    color_map = {
        'blue': '#1E90FF',       # 道奇蓝
        'orange': '#FFA500',     # 橙色
        'violet': '#9400D3',     # 深紫罗兰色
        'green': '#3CB371',      # 春天的绿色
        'pink': '#FF69B4',       # 热情的粉红
        'grey': '#696969',       # 暗淡的灰色
        'red': '#FF6347'         # 番茄
    }

