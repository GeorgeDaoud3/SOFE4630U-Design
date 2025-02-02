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

To solve the pestrain occlusion problem, the images from the both vehicles has to be stitching together. The following Figure show how this can be done.

## Milestone 4
