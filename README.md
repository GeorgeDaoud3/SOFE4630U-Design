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
  * The **grey vehicle** is the vehicle occluding a pedestrian by blocking the a part of the field view of the ego vehicle.
  * **Region 2** is the part of the field view of the ego vehicle blocked by the other vehicle.
  * The **pedestrian** get occluded from the ego vehicle by the other vehicle.

![](/images/problem.jpg)

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

You can use images from the [/Dataset_Occluded_Pedestrian/](Dataset_Occluded_Pedestrian) folder with a name starts with **A** or **B** to test the algorithm

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
 
