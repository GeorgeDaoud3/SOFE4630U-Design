from ultralytics import YOLO
import cv2
import numpy as np

# input
Occluded_Image_View = cv2.imread("./A_001.png")

################################################################################################################

# Load a model
model = YOLO("./yolo11n.pt")  # load an official detection model

# predict and locate object
results = model.predict(source=Occluded_Image_View, save=True, save_txt=True)  # save predictions as labels

# print results
# Process results list
person_boxes = []
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy() # Get bounding boxes
    classes = result.boxes.cls.cpu().numpy() # Get class labels
    confs = result.boxes.conf.cpu().numpy() # Get class labels
count=0;
for box, cls, conf in zip(boxes, classes,confs):
    if result.names[int(cls)] == 'person': # Filter for person class
	    print('object : '+str(count));
	    count+=1;
	    print("\t box : "+str(box[:4]))
	    x1, y1, x2, y2 = map(int, box[:4])
	    person_boxes.append(box[:4])

person_boxes=np.array(person_boxes).round().astype(np.int32)

################################################################################################################        

#ouput
print("output : "+str(person_boxes));
