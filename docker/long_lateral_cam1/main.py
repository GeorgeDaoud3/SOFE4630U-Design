import torch
from torch import nn
import numpy as np

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.x_max=np.array([1920,1080,1920,1080,20])
        self.y_max=torch.Tensor([10,10])
        self.mlp = nn.Sequential(
            nn.Linear(5, 10),
            nn.ReLU(),
            nn.Linear(10, 10),
            nn.ReLU(),
            nn.Linear(10, 2),
            nn.Tanh()
        )

    def forward(self, x):
        inputs=torch.Tensor(x/self.x_max).float();
        with torch.no_grad():
	        logits = self.mlp(inputs)*self.y_max;
        return logits

box=[1010,  654, 1132, 1080];
depth=4.669038;

x=np.array([*box,depth])

mlp = NeuralNetwork()
mlp.load_state_dict(torch.load("mlp_camA.pkl", weights_only=True))
mlp.eval()
outputs = np.array(mlp(torch.Tensor(x)))
print(outputs)
