# Introduction
A lot of sensors are mounted on modern vehicles. Software is needed to process the data generated from the sensors. The software can run locally, over the cloud, or in a hybrid way. Modern vehicles are able to perform a lot of tasks:
* localization: to accurate localize itselvies on the map.
* Perception: determines and gather informations about other road agents as other vehicles and pedistrains. Also, it detects the traffic sign, lights, and other road marks like the lane borders.
* Prediction: predicts the paths that surrounding road agents may take.
* Planning: plans the best route the vehicle should follow to reach its destination. Also, it can increase the safety by performing short-term planning to prevent accidents and collision.
* Control: depends on the autonomy level of the vehicle, this can be varying from warning the user to take the full control of the vehicle.

The efficiency of those tasks has been improved significantly in normal situation. However, the performance gradually decreases in a crowded situation due to occlusion.

# The Problem Statement
The problem is to detect pedestrians occluded by other vehicles. As shown in the following figure,
  * The **red vehicle** is the vehicle that executes the software or request the cloud service. Thus, it's called **ego vehicle**.
  * The **regions 1 and 2** are the field view of the camera of the ego vehicle.
  * The **grey vehicle** is the vehicle occluding a pedestrian by blocking the a part of the field view of the ego vehicle. We will refer to it as the **other vehicle**.
  * **Region 2** is the part of the field view of the ego vehicle blocked by the other vehicle.
  * The **pedestrian** get occluded from the ego vehicle by the other vehicle.

![](/images/problem.jpg)

# The Dataset Description

The dataset contains a file named **labels.csv**. It includes the following information:
* **Timestamp**: The scene time in nanoseconds.
* **Car1_Location_X** and	**Car1_Location_Y**: the locations of the center of the **other vehicle** that is occluding the pedestrian in real-world coordinates.
* **Car1_Length**,	**Car1_Width**,	and **Car1_Height**: the dimensions of the **other vehicle** in meters.
* **Car2_Location_X** and	**Car2_Location_Y**: the locations of the center of the **ego vehicle** in real-world coordinates.
* **Car2_Length**,	**Car2_Width**,	and **Car2_Height**: the dimensions of the **ego vehicle** in meters.
* **pedestrian_Location_X** and	**pedestrian_Location_X**: the locations of the center pedestrian in real-world coordinates.
* **pedestrian_Length**,	**pedestrian_Width**,	and **pedestrian_Height**: the dimensions of the pedestrian in meters.
* **cam1_pedestrian_x1**,	**cam1_pedestrian_y1**,	**cam1_pedestrian_x2**, and	**cam1_pedestrian_y2**: the bounding box coordinates that surrounding the pedestrian in the image captured by Camera1. This camera is mounted on the **other vehicle**.
* **cam2_car_x1**,	**cam2_car_y1**,	**cam2_car_x2**, and	**cam2_car_y2**: the coordinates of the bounding box surrounding the nearest vehicle in the image captured by Camera2. This camera is mounted on the **other vehicle**.
* **cam3_pedestrian_x1**,	**cam3_pedestrian_y1**,	**cam3_pedestrian_x2**, and	**cam3_pedestrian_y2**: the coordinates of the bounding box that should surround the pedestrian in the image captured by the camera mounted on the **other vehicle** if there was no occlusion. This information may be needed for validation.
* **Occluded_Image_View**: images captured by the camera mounted on the **other vehicle**. It shows the occluded view by the **other vehicle**.
* **Occluded_Image_Lidar**: (**optional**) The Lidar row data captured by the Lidar mounted on the **other vehicle**.
* **Occluding_Image_View**: images captured by the camera mounted on the **ego vehicle**. It shows the occluding view by the **other vehicle**.
* **Occluding_Image_Lidar**: (**optional**) The Lidar row data captured by the Lidar mounted on the **ego vehicle**.
* **Ground_Truth_View**: images that should be captured by Camera2 (mounted on the **ego vehicle**) if there is no occlusion by the **other vehicle**.

All images mentioned in the **labels.csv** table are in the **Dataset_Occluded_Pedestrian** folder.

All Lidar data mentioned in the **labels.csv** table are in the **Lidar** folder (**optional**). Note that the lidar data can be visualized using this [online tool](https://imagetostl.com/view-ply-online). It can be processed with many open-source pre-trained neural networks such as [PointRCNN](https://github.com/sshaoshuai/PointRCNN).

The images representing the aerial View of the scenes are in the **AerialView** folder (**optional**).

The **aerialView.png** file gives an empty aerial View of the scene.

## Milestone 1

Download the Labels.csv file from the repository. Write two Python scripts to produce and consume the records read from the CSV file. Create a new topic and assign it a name that suits the purpose of the tasks below.

**The Producer**:
1. Read the CSV file.
2. Iterate over the records in the CSV file:
  * Convert each record (row from the CSV file) into a dictionary.
  * Serialize the dictionary into a message.
  * Publish the message to your topic.

**The Consumer**:
1. Receive messages from the topic.
2. Process each message:
  * Deserialize the message into a dictionary.
  * Print the values of the dictionary.

## Milestone 2
We will contine using the same dataset used in the first milestone. However, we will use the Whole dataset, not only the CSV file. The dataset:

* can be accessed from https://github.com/GeorgeDaoud3/SOFE4630U-Design
* contains a folder, Dataset_Occluded_Pedestrian, of images
* contains the Labels.csv file, you used in the first milestone.

You needed to

* create two topics one for the records of the CSV file and the other for the images.
* Deploy a MySQL server and create an empty table within it to accomidate the records of the CSV file.
* Create an application integration to automatically store the records published in the topic into the MySQL database.
* Use the same script, we written in the first milestone to publish the messages into the topic.
* Deploy a Redis server to store the images.
* Create an application integration to automatically store the images published in the other topic into the Redis datastorage.
* Write a python script that will publish the images to the topic. The script should
  * Read search for all the images in the folder.
  * For each image
    * Read the image.
    * Serialize it.
    * Publish the message into the topic using the image name as the message key and the serialized image as the message value.

## Milestone 3
To solve the pedestrian occlusion problem, the person captured by the vehicle's camera needs to be detected and the distance between the person and the camera (camera's focal point) needs to be estimated. Many ML models can be used for object detection like

* The family of R-CNN, Fast R-CNN, Faster R-CNN, ...
* The different versions of You Only Look Once (YOLO).
* Single-shot detector (SSD)

The models are already pre-trained on real-life datasets, so no more training is needed. The pre-trained models are capable of detecting pedestrians, other road agents, and other objects. The model generates the following information for each object:

1. the class of the object.
2. The confidence (probability) of the detection.
3. The bounding box surrounding the object.
   
The following figure illustrates how this information can be visualized. The figure at left is the input to the model while the figure at right is the input image annotated by the information generated by the model.

![](/images/yolo.jpg)

Then, we need to estimate the distance between the camera and the detected pedestrian. This can be done with many tools and methods. One of them is using <a href='https://github.com/apple/ml-depth-pro'>Depth Pro</a>. This is only a suggestion. You can use any other tool. Depth Pro uses a trained ML model to generate the depth image of the standard RGB image. The depth image is a numerical image in which the value of each pixel is the distance from the camera. For visualization purposes, the depth image is shown in the following figure, with the more blueish color meaning less depth while the more yellowish color means far objects.

![](/images/depth.jpg)

By averaging the depth of the area detected with the object detection model, the depth of the pedestrian can be estimated.

![](/images/ped_depth.jpg)

You can use images from the [/Dataset_Occluded_Pedestrian/](Dataset_Occluded_Pedestrian) folder with a name starts with **A** or **C** to test the algorithm

The processing algorithm can be summarized as 
1. Use any pre-trained object detection model.
2. Filter the output to pedestrians only.
3. Estimate the depth of the pedestrian.
4. report the bounding box and the average depth.

The task is to implement this algorithm as a Dataflow Job. To do this, you may follow the following steps.
1. Implement the algorithm locally on your machine.
2. Generate a Docker image for the Dataflow worker with all the needed libraries installed.
3. Write the Python script that creates a Dataflow pipeline that
    1. Reads from a topic.
    2. Detect the pedestrian.
    3. Estimate the depth.
    4. Publish the results (at least the bounding boxes and depth) to another topic.
4. Test the pipeline locally first at the GCP console.
5. Run it as a stream process using the Docker image as a cloud-based Dataflow Job.
6. Create a publisher and subscriber to test the job
 
## Milestone 4
In this milestone, you will build a solution to the problem based on a microservices approach that communicates over a shared bus. To simplify the problem, we will assume that only a single car is close to the ego vehicle and that only a single pedestrian is occluded by that car. All the code and docker files are given in the [docker](/docker) folder. Only the communication part is missing. Although some stages can be run in parallel, we will create a straight pipeline of microservices for simplicity. The microservices (stages) are in order:

1. Pedestrian  detecting:

|   | Details |
| ------- | ------- |
| Input fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, **Occluded_Image_View**, **Occluding_Image_View**  |
| Output fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, **Occluded_Image_View**, **Occluding_Image_View**, $${\large \color{green}\textbf{Pedestrians}}$$ |   
| function  | run **Yolo v11** on the **Occluded_Image_View** image and produce a list of boxes that surround pedestrians  |   
| path to the code  | [Yolo pedestrian](/docker/Yolo_pedestrian)  | 

2. Pedestrian depth

  |   | Details |
| ------- | ------- |
| Input fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, $${\large \color{red}\textbf{Occluded} \textunderscore \textbf{Image} \textunderscore \textbf{View}}$$, **Occluding_Image_View**, **Pedestrians**  |
| Output fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, **Occluding_Image_View**, **Pedestrians**, $${\large \color{green}\textbf{Pedestrians} \textunderscore \textbf{depth}}$$ |   
| function  | runs **depth pro** on the **Occluded_Image_View** image, estimates the depth of the pedestrians, and filters out any pedestrian more than ten meters away. Also, as the **Occluded_Image_View** is no longer needed, it will be excluded from the output. Note that the **depth pro** algorithm takes less than 3 seconds on a machine with a GPU but may take up to 5 without a GPU. |   
| path to the code  | [depth_cam1](/docker/depth_cam1)  | 

3. Longitudal and lateral distance for Pedestrians

  |   | Details |
| ------- | ------- |
| Input fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, **Occluding_Image_View**, **Pedestrians** , $${\large \color{red}\textbf{Pedestrians} \textunderscore \textbf{depth}}$  |
| Output fields  | **Timestamp**, **Car2_Location_X**, **Car2_Location_Y**, **Car1_Length**,	**Car1_Width**, **Car1_Height**, **Car2_Length**, **Car2_Width**,	**Car2_Height**, **Occluding_Image_View**, **Pedestrians**, $${\large \color{green}\textbf{Pedestrians} \textunderscore \textbf{longitudinal}}$$ ,$${\large \color{green}\textbf{Pedestrians} \textunderscore \textbf{lateral}}$$ |   
| function  | runs a customized MLP to convert the depth into longitudinal and lateral distnaces. Refer to the following figure for more information about the longitudinal and lateral distances. The MLP takes the surrounding box and the depth of the pedestrian as input to generate the longitudinal and lateral distances. The MLP is already pre-trained. As the depth is no longer needed, **Pedestrians_depth** will be excluded from the output |   
| path to the code  | [long lateral_cam1](/docker/long_lateral_cam1)  | 

![image](https://github.com/user-attachments/assets/da0d7e8d-f636-4a4a-b50f-da409823218c)

