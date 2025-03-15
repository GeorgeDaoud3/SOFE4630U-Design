from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("./yolo11n.pt")  # load an official detection model

# predict and locate object
im2 = cv2.imread("./A_001.png")
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# print results
# Process results list
person_boxes = []
for result in results:
    print(result)
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
	    print("\t cls : "+str(cls))
	    print("\t conf : "+str(conf))
