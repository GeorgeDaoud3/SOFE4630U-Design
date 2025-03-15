import numpy as np
import cv2
import matplotlib.pyplot as plt

# inputs
Car2_location=np.array([-61.0599594116211,140]);
Car1_dimensions=np.array([4.79177951812744,2.16345000267029]);
Car2_dimensions=np.array([4.79177951812744,2.16345000267029]);
Pedestrians=np.array([[1009.6,653.66,1131.7,1080]], dtype=np.int32)
Pedestrians_longitudinal=np.array([4.935154])
Pedestrians_lateral=np.array([0.28780216])
vehicles_longitudinal=np.array([9.5173])
vehicles_lateral=np.array([2.9744525])

################################################################################################################

def length2pixel(length): #length in meters
    return np.array([28.682*length[1],28.682*length[0]]);
def coordinate2pixel(point): #coordinate in meters
    return np.array([28.682*point[1]-3659.026,-28.682*point[0]-1278.32]);

try:
    
    car2_car1_distance=np.array([vehicles_longitudinal[0],vehicles_lateral[0]])
    car1_ped_distance=np.array([Pedestrians_longitudinal[0],Pedestrians_lateral[0]])

    Car1_location=Car2_location+car2_car1_distance
    Ped_location=Car1_location+car1_ped_distance

    ped_box=Pedestrians[0,:]

    x1,y1,x2,y2=ped_box
    center_ped_camB=(1920-x1-x2)/2;
    ped_width_camB=(x2-x1);
    ped_width_meter=car1_ped_distance[1]/center_ped_camB*ped_width_camB



    car1_location_px=coordinate2pixel(Car1_location)
    car2_location_px=coordinate2pixel(Car2_location)
    ped_location_px=coordinate2pixel(Ped_location)
    car1_dimensions_px=length2pixel(Car1_dimensions)
    car2_dimensions_px=length2pixel(Car2_dimensions)
    ped_dimensions_px=length2pixel(np.array([ped_width_meter,ped_width_meter]))

    img=cv2.imread("aerialView.png")

    start_point = car2_location_px-car2_dimensions_px/2
    end_point = car2_location_px+car2_dimensions_px/2
    start_point=start_point.astype(int)
    end_point=end_point.astype(int)
    color = (255, 0, 0)
    thickness = -1   # to fill
    print("car 1, from "+str(start_point)+" to "+str(end_point))
    img = cv2.rectangle(img, start_point, end_point, color, thickness)

    start_point = car1_location_px-car1_dimensions_px/2
    end_point = car1_location_px+car1_dimensions_px/2
    start_point=start_point.astype(int)
    end_point=end_point.astype(int)
    color = (255, 255, 0)
    thickness = -1   # to fill
    print("car 2, from "+str(start_point)+" to "+str(end_point))
    img = cv2.rectangle(img, start_point, end_point, color, thickness)

    start_point = ped_location_px-ped_dimensions_px/2
    end_point = ped_location_px+ped_dimensions_px/2
    start_point=start_point.astype(int)
    end_point=end_point.astype(int)
    color = (255, 0, 255)
    thickness = -1   # to fill
    print("pedestrian, from "+str(start_point)+" to "+str(end_point))
    img = cv2.rectangle(img, start_point, end_point, color, thickness)
except:
    img=cv2.imread("aerialView.png")

################################################################################################################

# the shape of the output image 
print("output shape : "+str(img.shape))