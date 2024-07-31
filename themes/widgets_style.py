class EnabledStyle:
    pushbutton = """
        QPushButton {
            border: 2px solid #6272a4;
            background-color: #6272A4;
        }
        QPushButton:hover {
            background-color: #7082b6;
            border: 2px solid #7082b6;
        }
        QPushButton:pressed {	
            background-color: #546391;
            border: 2px solid #ff79c6;
        }
    """

    combobox = """
        QComboBox{
            background-color: #6272a4;
            border: 2px solid #6272a4;
        }
        QComboBox:hover{
            border: 2px solid #7284b9;
        }
        QComboBox::drop-down {
            border-left-color: #6272a4;
         }
    """

    lineedit = """
        QLineEdit {
            background-color: #6272a4;
            border-radius: 5px;
            border: 2px solid #6272a4;
            padding: 0;
            selection-color: rgb(255, 255, 255);
            selection-background-color: rgb(255, 121, 198);
        }
        QLineEdit:hover {
            border: 2px solid rgb(64, 71, 88);
        }
        QLineEdit:focus {
            border: 2px solid #ff79c6;
        }
        QLineEdit[readOnly="true"]:focus {
            border: 2px solid #6272a4;
        }
        QLineEdit[readOnly="true"]:hover {
            border: 2px solid #6272a4;
        }
    """

    spinbox = """
        QSpinBox {
            background-color: #6272A4;
        }
    """

    dspinbox = """
        QDoubleSpinBox {
            background-color: #6272A4;
        }
    """

    # horizontal slider
    slider = """
        QSlider::groove:horizontal {
            background-color: #6272a4;
        }
        QSlider::groove:horizontal:hover {
            background-color: #6272a4;
        }
    """





class DisabledStyle:
    pushbutton = """
        QPushButton {
            border: 2px solid #aaaaaa;
            background-color: #aaaaaa;
        }
        QPushButton:hover {
            background-color: #aaaaaa;
            border: 2px solid #aaaaaa;
        }
        QPushButton:pressed {	
            background-color: #aaaaaa;
            border: 2px solid #aaaaaa;
        }
    """

    combobox = """
        QComboBox{
            background-color: #aaaaaa;
            border: 2px solid #aaaaaa;
        }
        QComboBox:hover{
            border: 2px solid #aaaaaa;
        }
        QComboBox::drop-down {
            border-left-color: #aaaaaa;
         }
    """

    lineedit = """
        QLineEdit {
            background-color: #aaaaaa;
            border-radius: 5px;
            border: 2px solid #aaaaaa;
            padding: 0;
            selection-color: rgb(255, 255, 255);
            selection-background-color: rgb(255, 121, 198);
        }
        QLineEdit:hover {
            border: 2px solid #aaaaaa;
        }
        QLineEdit:focus {
            border: 2px solid #aaaaaa;
        }
        QLineEdit[readOnly="true"]:focus {
            border: 2px solid #aaaaaa;
        }
        QLineEdit[readOnly="true"]:hover {
            border: 2px solid #aaaaaa;
        }
    """

    spinbox = """
        QSpinBox {
            background-color: #aaaaaa;
        }
    """

    dspinbox = """
        QDoubleSpinBox {
            background-color: #aaaaaa;
        }
    """

    # horizontal slider
    slider = """
        QSlider::groove:horizontal {
            background-color: #aaaaaa;
        }
        QSlider::groove:horizontal:hover {
            background-color: #aaaaaa;
        }
    """
