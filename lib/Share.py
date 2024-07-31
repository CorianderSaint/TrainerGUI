class SI:
    # 功能互斥标志：True表示正在运行，False表示不在运行
    functionMutex = False
    # 线程互斥标志：True表示正在运行，False表示不在运行
    threadMutex = False

    # 窗口最大化标志
    isMaximized = False

    # 当前项目绝对路径
    appPath = ""

    # 当前页面
    # process_image / process_dataset /trainer / info
    current_page = ""

    # 预览的temp图像 的相对路径
    review_temp_image_path = ""

    # ==============================================    单张图片预处理    ==============================================
    # 路径
    image_path = ""
    export_path_ofImage = ""

    # 同步信号
    syncFlag_blur_ofImage = False      # 模糊操作的滑块同步标志

    # 当前预处理功能（最外侧ToolBox）
    # 预处理工具 / 图像增强
    current_process_function_ofImage = ""

    # 当前预处理工具功能（内侧ToolBox1）
    # 更改后缀 / 图片方形化 / 更改大小
    current_processTool_ofImage = ""

    # 当前已开启的图像增强功能（内侧ToolBox2-SwitchButton）
    # 图像旋转 + 水平翻转 + 垂直翻转 + 模糊 + 噪声 + 亮度 + 对比度
    current_imageAugment_ofImage = []



    # 记录当前的预处理工具算法
    # modifySuffix_jpg / modifySuffix_jpeg / modifySuffix_png / modifySuffix_bmp /
    # square_BORDER_CONSTANT / square_BORDER_REFLECT / square_BORDER_REPLICATE / square_BORDER_WRAP /
    # resize_INTER_LINEAR / resize_INTER_NEAREST / resize_INTER_CUBIC /
    # resize_INTER_AREA / resize_INTER_LANCZOS4 / resize_INTER_LINEAR_EXACT
    processToolAlgorithm_ofImage = ""

    # 记录当前的图像增强算法
    # rotate + HFlip + VFlip +
    # blur_mean + blur_box + blur_gaussian + blur_median +
    # noise_gaussian + noise_saltPepper +
    # brightness + contrast
    imageAugmentAlgorithm_ofImage = []



    # ==============================================    数据集预处理    ==============================================
    # 路径
    dataset_path = ""
    export_path_ofDataset = ""
    # 数据集中所有图片路径
    dataset_images_path = []
    # 记录错误的图片
    error_images_path = []

    # 统一命名操作是否从0开始
    flag_rename0 = False

    # 同步信号
    syncFlag_blur_ofDataset = False      # 模糊操作的滑块同步标志

    # 当前预处理功能（最外侧ToolBox）
    # 预处理工具 / 图像增强
    current_process_function_ofDataset = ""

    # 预处理工具（内侧ToolBox 1）
    # 统一后缀 / 统一命名 / 图片方形化 / 统一大小 / 数据集分割
    current_processTool_ofDataset = ""

    # 当前已开启的图像增强功能（内侧ToolBox2-SwitchButton）
    # 图像旋转 + 水平翻转 + 垂直翻转 + 模糊 + 噪声 + 亮度 + 对比度
    current_imageAugment_ofDataset = []


    # 记录当前的预处理工具算法
    # modifySuffix_jpg / modifySuffix_jpeg / modifySuffix_png / modifySuffix_bmp /
    # uniformName_i / uniformNamei / uniformName-i /
    # square_BORDER_CONSTANT / square_BORDER_REFLECT / square_BORDER_REPLICATE / square_BORDER_WRAP /
    # resize_INTER_LINEAR / resize_INTER_NEAREST / resize_INTER_CUBIC /
    # resize_INTER_AREA / resize_INTER_LANCZOS4 / resize_INTER_LINEAR_EXACT
    processToolAlgorithm_ofDataset = ""

    # 记录当前的图像增强算法
    # rotate + HFlip + VFlip +
    # blur_mean + blur_box + blur_gaussian + blur_median +
    # noise_gaussian + noise_saltPepper +
    # brightness + contrast
    imageAugmentAlgorithm_ofDataset = []


    # 参数记录--------------------
    # 图片方形化-----
    # BORDER_CONSTANT / BORDER_REFLECT / BORDER_REPLICATE / BORDER_WRAP
    param_square_ofDataset_borderType = ""
    param_square_ofDataset_fillColor = None
    # 统一大小-----
    param_resize_ofDataset_dsize = None
    # INTER_LINEAR / INTER_NEAREST / INTER_CUBIC / INTER_AREA / INTER_LANCZOS4 / INTER_LINEAR_EXACT
    param_resize_ofDataset_interpolation = ""
    # 数据集分割-----
    param_split_ofDataset_train = None
    param_split_ofDataset_val = None
    param_split_ofDataset_test = None
    train_path_ofDataset = None
    val_path_ofDataset = None
    test_path_ofDataset = None
    # 图像旋转-----
    param_rotate_ofDataset_probability = None
    param_rotate_ofDataset_degree1 = None
    param_rotate_ofDataset_degree2 = None
    param_rotate_ofDataset_scale1 = None
    param_rotate_ofDataset_scale2 = None
    param_rotate_ofDataset_fillColor = None
    # 水平翻转-----
    param_HFlip_ofDataset_probability = None
    # 垂直翻转-----
    param_VFlip_ofDataset_probability = None
    # 模糊-----
    param_blur_ofDataset_probability = None
    param_blur_ofDataset_filter = None
    param_blur_ofDataset_ksizeFrom= None
    param_blur_ofDataset_ksizeTo = None
    # 噪声-----
    param_noise_ofDataset_probability = None
    param_noise_ofDataset_sigma1 = None
    param_noise_ofDataset_sigma2 = None
    param_noise_ofDataset_rate1 = None
    param_noise_ofDataset_rate2 = None
    # 亮度-----
    param_brightness_ofDataset_probability = None
    param_brightness_ofDataset_beta1 = None
    param_brightness_ofDataset_beta2 = None
    # 对比度-----
    param_contrast_ofDataset_probability = None
    param_contrast_ofDataset_alpha1 = None
    param_contrast_ofDataset_alpha2 = None


    # ==============================================    可视化训练器    ==============================================
    # 数据集划分路径
    dataset_split_path = ""
    dataset_train_path = ""
    dataset_val_path = ""
    dataset_test_path = ""

    # 输出路径
    outputDir_path = ""

    # 模型保存路径
    model_save_path = ""

    # 混淆矩阵图片保存路径
    matrix_save_path = ""

    # log路径：
    # outputDir_path/log
    log_dir_path = ""
    # outputDir_path/log/log.txt
    log_text_path = ""

    # 分类json文件路径：outputDir_path/class_indices.json
    class_indices_path = ""

    # 记录可视化的页面
    # step / epoch / matrix
    current_canvas = "step"

    # 混淆矩阵展示
    matrixAcc = None
