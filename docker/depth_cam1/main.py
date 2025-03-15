from PIL import Image
import depth_pro
import numpy as np
import torch

# inputs

Occluded_Image_View, _, _ = depth_pro.load_rgb("./A_001.png")
Pedestrians=np.array([[1010,654,1132,1080]],dtype=np.int32);

################################################################################################################

f_px=2200

threshold=10;
# Load model and preprocessing transform
model, transform = depth_pro.create_model_and_transforms()
model.eval()

# Load and preprocess an image.

Occluded_Image_View = transform(Occluded_Image_View)

# Run inference.
prediction = model.infer(Occluded_Image_View, f_px=torch.Tensor([f_px]))
depth = prediction["depth"]  # Depth in [m].
focallength_px = prediction["focallength_px"]  # Focal length in pixels.
# Convert depth to numpy array
depth_np = depth.squeeze().cpu().numpy()
close_objects=[]
depths=[]
for i in range(Pedestrians.shape[0]):
	#print("box :" + str(i))
	x1, y1, x2, y2=Pedestrians[i,:];
	# Extract depth value at the center of the bounding box
	depth_value = np.median(depth_np[y1:y2, x1:x2])
	#print("Depth:" + str(depth_value))
	if(depth_value<threshold):
		close_objects.append(Pedestrians[i,:])
		depths.append(depth_value)

depths=np.array(depths)
Pedestrians=np.array(close_objects).astype(np.int32);

################################################################################################################

# outputs
print("Close objects")
print(Pedestrians)
print("their depth")
print(depths)

