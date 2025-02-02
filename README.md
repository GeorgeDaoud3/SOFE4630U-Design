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

The Producer:
* Read the CSV file.
* Iterate over the records in the CSV file:
  * Convert each record (row from the CSV file) into a dictionary.
  * Serialize the dictionary into a message.
  * Publish the message to your topic.
The Consumer:
* Receive messages from the topic.
* Process each message:
* Deserialize the message into a dictionary.
* Print the values of the dictionary.

## Milestone 2

## Milestone 3

## Milestone 4
