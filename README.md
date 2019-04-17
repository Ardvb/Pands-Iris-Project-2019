# Pands-Iris-Project-2019

This repository contains my research on Fisher's Iris data set, as well as my documentation and code based on this research.

## How to download the repository

1. Go to my Github profile: https://github.com/Ardvb/
2. Click on the download button and copy/paste the link: https://github.com/Ardvb/Pands-Iris-Project-2019

## How to run the code:

1. Make sure you have python installed on your device: https://www.python.org/downloads/


## The Iris flower data set

This data set was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species.
Two of the species were collected from the same pasture, on the same day, and measured at the same time by the same person with the same apparatus.
The iris data set consists of 50 samples each, of three iris species (Iris setosa, Iris virginica and Iris versicolor). 
From every sample four features were measured: the length and width of both the sepals and petals, in centimetres.

![irises](https://user-images.githubusercontent.com/47186083/56307201-35335780-613c-11e9-8191-827eca81c80e.png)
###### Source: https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers

British statistician and biologist Ronald Fisher used this dataset to develop a linear discriminant model to distinguish the species from each other.
Ronald Fisher is one of the most celebrated statisticians of all time. 
He is described as “a genius who almost single-handedly created the foundations for modern statistical science”.
The data set has some key features that make it very useful in all sorts of data analytics, from data visualisation to machine learning.
It is small, but not trivial. It consists of real data of good quality. 
The goal of the dataset, to discriminate between three species of Iris, based on measurements is simple, yet challenging.
Also, the fact someone as famous as Ronald Fisher used the dataset makes it more interesting to a lot of statisticians.
No wonder it is one of the most used data sets in the world of statistics.

## My research

I have written Python code to try and find some interesting information about this data set.
First I wanted to get a good look at the data set by visualisizing some basic features.

![image](https://user-images.githubusercontent.com/47186083/56307904-d7077400-613d-11e9-8ab2-b6ba6d73b547.png)

![image](https://user-images.githubusercontent.com/47186083/56307945-f1415200-613d-11e9-9929-1df4cd1d4d79.png)

By reading the Iris data set Excel file into my program I am able to project in onto the screen using cmder. 

Now we can start looking into what some of the more interesting features of the data set. By using the _.describe_ command, I can see lots of useful information, such as the mean, the standard deviation, the minimum and maximum etc.

![image](https://user-images.githubusercontent.com/47186083/56308155-79bff280-613e-11e9-9fee-c7298f2e96c3.png)
![image](https://user-images.githubusercontent.com/47186083/56308155-79bff280-613e-11e9-9fee-c7298f2e96c3.png)

By using the _.median_ and _.mode_ commands, I am able to see what the median(the number that is halfway into the set) and the mode(most frequently occurring number).

![image](https://user-images.githubusercontent.com/47186083/56308302-e1763d80-613e-11e9-8d34-25080d535d7b.png)
![image](https://user-images.githubusercontent.com/47186083/56308312-eb983c00-613e-11e9-8410-928ffaf52bdd.png)

![image](https://user-images.githubusercontent.com/47186083/56308322-f357e080-613e-11e9-9032-a8f317597a0a.png)
![image](https://user-images.githubusercontent.com/47186083/56308335-f9e65800-613e-11e9-91c5-043c36688957.png)

### The differences between the species

The next step was to seperate the species by only comparing the data from each species to the others.
I wrote some simple code to only display the data of 'Iris setosa':

![image](https://user-images.githubusercontent.com/47186083/56308459-45990180-613f-11e9-9bd5-ef3284493405.png)
![image](https://user-images.githubusercontent.com/47186083/56308523-65302a00-613f-11e9-8e94-eba6afca58df.png)

![image](https://user-images.githubusercontent.com/47186083/56308618-a7596b80-613f-11e9-977e-9296df0f1fc7.png)
![image](https://user-images.githubusercontent.com/47186083/56308628-b0e2d380-613f-11e9-8286-06e8be911469.png)

And the median and mode:

![image](https://user-images.githubusercontent.com/47186083/56308675-cb1cb180-613f-11e9-8297-5184dde90a9f.png)
![image](https://user-images.githubusercontent.com/47186083/56308692-d2dc5600-613f-11e9-809a-bbf1e0199b4f.png)

![image](https://user-images.githubusercontent.com/47186083/56308713-dc65be00-613f-11e9-8356-1b4d770d22c5.png)
![image](https://user-images.githubusercontent.com/47186083/56308731-e38ccc00-613f-11e9-8c0d-2411083356a0.png)
