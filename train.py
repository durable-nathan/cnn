from dataset import dataloader
from model import net
import torch.optim as optim
import torch.nn as nn
import torch
import tqdm

criterion = nn.BCELoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in tqdm.tqdm(enumerate(dataloader, 0)):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        print("Input shape", inputs.shape)
        print("labels", labels)
        outputs = net(inputs)

        outputs = outputs.squeeze(1)
        # Apply sigmoid to outputs to ensure values are between 0 and 1
        outputs = torch.sigmoid(outputs)

        loss = criterion(outputs, labels.float())
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

torch.save(net.state_dict(), "./model.pth")

print('Finished Training')

