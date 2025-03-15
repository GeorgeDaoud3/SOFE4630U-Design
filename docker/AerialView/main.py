import numpy as np
import cv2
import matplotlib.pyplot as plt

def length2pixel(length): #length in meters
    return np.array([28.682*length[1],28.682*length[0]]);
def coordinate2pixel(point): #coordinate in meters
    return np.array([28.682*point[1]-3659.026,-28.682*point[0]-1278.32]);
car2_location=np.array([-61.0599594116211,140]);
car1_dimensions=np.array([4.79177951812744,2.16345000267029]);
car2_dimensions=np.array([4.79177951812744,2.16345000267029]);

car2_car1_distance=np.array([9.999999,2.94525])
car1_ped_distance=np.array([4.935154, 0.28780216])

car1_location=car2_location+car2_car1_distance
ped_location=car1_location+car1_ped_distance
ped_box=np.array([1009.6,653.66,1131.7,1080])

x1,y1,x2,y2=ped_box
center_ped_camB=(1920-x1-x2)/2;
ped_width_camB=(x2-x1);
ped_width_meter=car1_ped_distance[1]/center_ped_camB*ped_width_camB

car1_location_px=coordinate2pixel(car1_location)
car2_location_px=coordinate2pixel(car2_location)
ped_location_px=coordinate2pixel(ped_location)
car1_dimensions_px=length2pixel(car1_dimensions)
car2_dimensions_px=length2pixel(car2_dimensions)
ped_dimensions_px=length2pixel(np.array([ped_width_meter,ped_width_meter]))

img=cv2.imread("aerialView.png")

start_point = car2_location_px-car2_dimensions_px/2
end_point = car2_location_px+car2_dimensions_px/2
start_point=start_point.astype(int)
end_point=end_point.astype(int)
color = (255, 0, 0)
thickness = 1
print("car 1, from "+str(start_point)+" to "+str(end_point))
img = cv2.rectangle(img, start_point, end_point, color, thickness)

start_point = car1_location_px-car1_dimensions_px/2
end_point = car1_location_px+car1_dimensions_px/2
start_point=start_point.astype(int)
end_point=end_point.astype(int)
color = (255, 255, 0)
thickness = 1
print("car 2, from "+str(start_point)+" to "+str(end_point))
img = cv2.rectangle(img, start_point, end_point, color, thickness)

start_point = ped_location_px-ped_dimensions_px/2
end_point = ped_location_px+ped_dimensions_px/2
start_point=start_point.astype(int)
end_point=end_point.astype(int)
color = (255, 0, 255)
thickness = 1
print("pedestrian, from "+str(start_point)+" to "+str(end_point))
img = cv2.rectangle(img, start_point, end_point, color, thickness)
