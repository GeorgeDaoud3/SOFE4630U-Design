import torch
from torch import nn
import numpy as np

# inputs
vehicles =np.array([[1311,  541, 1919,  931]]);
vehicles_depth=np.array([8.153904]);

################################################################################################################

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

mlp = NeuralNetwork()
mlp.load_state_dict(torch.load("mlp_camB.pkl", weights_only=True))
mlp.eval()

outputs=[]

for i in range(vehicles.shape[0]):
    box=vehicles[i,:]
    depth=vehicles_depth[i]
    x=np.array([*box,depth])
    outputs.append(np.array(mlp(torch.Tensor(x))))

outputs=np.array(outputs)
################################################################################################################

#outputs

print("longitudinal : "+str(outputs[:,0]))
print("lateral : "+str(outputs[:,1]))
