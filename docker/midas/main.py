from PIL import Image
import torch
import numpy as np
import cv2

midas = torch.hub.load('intel-isl/MiDaS', 'MiDaS_small')
midas.eval()
transformss = torch.hub.load('intel-isl/MiDaS', 'transforms')
transform = transformss.small_transform
cap = cv2.imread("./A_001.png")

image = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)

image_batch = transform(image)

with torch.no_grad():
        prediction = midas(image_batch)
        prediction=torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size = image.shape[:2],
                    mode = 'bicubic',
                    align_corners=False
                    ).squeeze()

        inverse_depth_np = prediction.cpu().numpy()

box=np.array([1009.6,653.66,1131.7,1080])
x1, y1, x2, y2 = map(int, box[:4])
center_x = (x1 + x2) // 2
center_y = (y1 + y2) // 2
# Extract depth value at the center of the bounding box
inverse_depth_value = inverse_depth_np[center_y, center_x]
print("Inverse Depth:" + str(inverse_depth_value))