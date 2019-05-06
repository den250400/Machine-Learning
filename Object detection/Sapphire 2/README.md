# Sapphire 2
 I wanted to design Sapphire as YOLO-inspired general-purpose object detection system. The key idea here is that in many applications, you don't need multi-class detection - you only need to recognize one type of objects(faces, for example). I especially wanted to give the user the ability to create his own training datasets while not spending days and weeks doing hand-labeling and struggling to convert the training set to the format required for network. 
 
 This repo contains not only the network itself, but also a utility program for hand-labeling, which takes .jpg or .png images, normalizes them and saves the whole training set as .npy file. It also does image augmentation, which can be used to increase the size of the dataset by the factor of hundreds. Thus, good performance can be achieved using only around 100 different images, which is only 20-30 minutes hand-labeling time!
 
 If you want to use pretrained weights, you may download them from here(Github doesn't allow upload files which are more than 25 Mb) and drop them to Saved models folder. Don't forget to update the model name inside the Sapphire 2 Inference file.
 Face detector: https://drive.google.com/drive/folders/1qUSGh0upudm6LpY9YW0uUG4tubfftXyi?usp=sharing
