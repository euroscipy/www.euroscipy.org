Title:Deep Learning for Human Pose Estimation
URL:2018/descriptions/Deep Learning for Human Pose Estimation.html
save_as: 2018/descriptions/Deep Learning for Human Pose Estimation.html



# Deep Learning for Human Pose Estimation
Robots are coming. Whether they come as humanoids, home assistants or self-driving cars, but they're coming. They're coming out from the orderly, synthetic and isolated manufacturing plants to the chaotic, evolutionary and interactive real world. And it's this interaction what will separate these machines between lifeless appliance and sociable robots. Understanding both verbal and non-verbal communication is the last layer of robotic development, though it may be one of the more challengings.

Fortunately, deep learning emerged a few years ago with astonishing results. It has led to huge advances in verbal human-machine communication and it's starting to see great outcomes in non-verbal. Detecting the 3D position and orientation of the people around you with no more than an RGB camera is increasingly becoming a reality.

Throughout the talk, we'll cover the process from receiving an RGB image to make a real robot detect a person position and orientation to finally approach her. And everything with Python.
* The magic: design of the neural network architecture (OpenPose) to detect body keypoints (such as eyes, neck, shoulders or knees), discussing methods to make it faster though losing accuracy.
* Postprocessing: If there are a bunch of people, which part belongs to which person? 
* From 2D to 3D: heuristics to extract position and orientation of a human from its skeleton.
* Application: integration of the model into a real assistant robot, using the position and orientation information to approach the person face-to-face.