import os
import numpy as np
from PIL import Image
from torchvision import transforms, datasets, models
import torch
import torch.nn as nn
import torch.optim as optim

def load_dataset(path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    dataset = datasets.ImageFolder(path, transform=transform)
    return dataset

def train_model(data_path, epochs=5, lr=0.001):
    dataset = load_dataset(data_path)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

    model = models.resnet18(pretrained=True)
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 3)  # authentic / fake / frankenstein

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.4f}")

    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), "models/authenticator_model.pth")

    print("Model training complete and saved to models/")
