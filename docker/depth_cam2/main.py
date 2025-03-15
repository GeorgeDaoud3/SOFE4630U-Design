from PIL import Image
import depth_pro
import numpy as np
import torch

# inputs

Occluding_Image_View, _, _ = depth_pro.load_rgb("./B_001.png")
vehicles=np.array([[1311, 541, 1919, 931],
	 	[256, 540, 373, 613],
	 	[374, 542, 474, 606],
	 	[469, 544, 549, 594]],dtype=np.int32);

################################################################################################################

f_px=2500

threshold=20;
# Load model and preprocessing transform
model, transform = depth_pro.create_model_and_transforms()
model.eval()

# Load and preprocess an image.

Occluding_Image_View = transform(Occluding_Image_View)

# Run inference.
prediction = model.infer(Occluding_Image_View, f_px=torch.Tensor([f_px]))
depth = prediction["depth"]  # Depth in [m].
focallength_px = prediction["focallength_px"]  # Focal length in pixels.
# Convert depth to numpy array
depth_np = depth.squeeze().cpu().numpy()
close_objects=[]
depths=[]
for i in range(vehicles.shape[0]):
	#print("box :" + str(i))
	x1, y1, x2, y2=vehicles[i,:];
	# Extract depth value at the center of the bounding box
	depth_value = np.median(depth_np[y1:y2, x1:x2])
	#print("Depth:" + str(depth_value))
	if(depth_value<threshold):
		close_objects.append(vehicles[i,:])
		depths.append(depth_value)

depths=np.array(depths)
vehicles=np.array(close_objects).astype(np.int32);

################################################################################################################

# outputs
print("Close objects")
print(vehicles)
print("their depth")
print(depths)