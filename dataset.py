import torch
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os

import matplotlib.pyplot as plt
import numpy as np

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        # Define your classes based on directory names
        self.classes = ['bad', 'good']
        
        # Define your class-to-label mapping
        self.class_to_label = {
            'bad': 0,
            'good': 1
        }

        self.data = self.load_data()

    def load_data(self):       
        data = []              
        for cls in self.classes:
            class_dir = os.path.join(self.root_dir, cls)
            for file in os.listdir(class_dir):
                data.append((os.path.join(class_dir, file), self.class_to_label[cls]))
        return data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, label = self.data[idx]
        img = Image.open(img_path).convert('RGB')
        # Resize the image to a smaller size, e.g., 256x128
        img = img.resize((256, 128), Image.BILINEAR)

        if self.transform:
            img = self.transform(img)

        return img, label

# Example usage
root_dir = './dataset'  # Assuming dataset structure: ./dataset/bad and ./dataset/good

transform = transforms.Compose([
    transforms.ToTensor(),  # Convert PIL image to tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
])

dataset = CustomDataset(root_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Now you can iterate over dataloader for training
"""
for batch in dataloader:
    images, labels = batch

    print(images.shape)
    print(labels)
"""

    # Your training code here

