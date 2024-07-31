import torch.nn as nn
import torch

from lib.Parameters import Param
from util.Util import calOutputSize


class AlexNet(nn.Module):
    def __init__(self, num_classes=15, init_weights=Param.init_weights):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 48, kernel_size=11, stride=4, padding=2),  # input[3, 224, 224]  output[48, 55, 55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[48, 27, 27]
            nn.Conv2d(48, 128, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 13, 13]
            nn.Conv2d(128, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),          # output[128, 13, 13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 6, 6]
        )



        self.classifier = nn.Sequential(
            nn.Dropout(p=Param.dropout),
            nn.Linear(self.output_size(), 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p=Param.dropout),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def output_size(self):
        output_size = calOutputSize(Param.input_size, 11, 2, 4)     # output[48, 55, 55]
        output_size = output_size // 2                              # output[48, 27, 27]
        output_size = calOutputSize(output_size, 5, 2, 1)           # output[128, 27, 27]
        output_size = output_size // 2                              # output[128, 13, 13]
        output_size = calOutputSize(output_size, 3, 1, 1)           # output[192, 13, 13]
        output_size = calOutputSize(output_size, 3, 1, 1)           # output[192, 13, 13]
        output_size = calOutputSize(output_size, 3, 1, 1)           # output[192, 13, 13]
        output_size = output_size // 2                              # output[128, 6, 6]
        return 128 * output_size * output_size

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, start_dim=1)
        x = self.classifier(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)