from PIL import Image
import depth_pro
import numpy as np
import torch

f_px=2200
boxes=np.array([[1010,654,1132,1080]],dtype=np.int32);
threshold=10;
# Load model and preprocessing transform
model, transform = depth_pro.create_model_and_transforms()
model.eval()

# Load and preprocess an image.
image, _, _ = depth_pro.load_rgb("./A_001.png")
image = transform(image)

# Run inference.
prediction = model.infer(image, f_px=torch.Tensor([f_px]))
depth = prediction["depth"]  # Depth in [m].
focallength_px = prediction["focallength_px"]  # Focal length in pixels.
print("focallength_px : "+str(focallength_px))
# Convert depth to numpy array
depth_np = depth.squeeze().cpu().numpy()
close_objects=[]
depths=[]
for i in range(boxes.shape[0]):
	#print("box :" + str(i))
	x1, y1, x2, y2=boxes[i,:];
	# Extract depth value at the center of the bounding box
	depth_value = np.median(depth_np[y1:y2, x1:x2])
	#print("Depth:" + str(depth_value))
	if(depth_value<threshold):
		close_objects.append(boxes[i,:])
		depths.append(depth_value)
print("Close objects")
print(close_objects)
print("their depth")
print(depths)

