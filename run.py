import torch
from torchvision import transforms
from PIL import Image
from model import net

# Load test image
img = Image.open('good_output_0.png').convert('RGB')

img = img.resize((256, 128), Image.BILINEAR)

net.load_state_dict(torch.load("./model.pth"))

# Convert image to tensor
img = transforms.ToTensor()(img)
img = img.unsqueeze(0)

print("Image shape:",img.shape)

# Make prediction
output = net(img)

print("Output shape:",output.shape)

#o = output.item()
o = torch.sigmoid(output).item()
print("Output:",o)
