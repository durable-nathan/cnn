import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # Convolutional layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        
        # Pooling layer
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        
        # Fully connected layers
        self.fc1 = nn.Linear(in_features=128 * 16 * 32, out_features=512)  # Adjusted the input features
        self.fc2 = nn.Linear(in_features=512, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=1)  # Assuming 10 output classes

    def forward(self, x):
        # Convolutional and pooling layers
        x = self.pool(F.relu(self.conv1(x)))  # Output size: (32, 32, 64, 128)
        x = self.pool(F.relu(self.conv2(x)))  # Output size: (32, 64, 32, 64)
        x = self.pool(F.relu(self.conv3(x)))  # Output size: (32, 128, 16, 32)

        # Flatten the tensor
        x = x.view(-1, 128 * 16 * 32)
        
        # Fully connected layers
        x = F.relu(self.fc1(x))
        print("fc1", x.shape)
        x = F.relu(self.fc2(x))
        print("fc2", x.shape)
        x = self.fc3(x)
        print("fc3", x.shape)
        return x

net = Net()
