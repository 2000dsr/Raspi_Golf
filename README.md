# Pi Golf Replay

## THIS PROJECT IN CURRENTLY IN PROGRESS. CHECK BACK LATER FOR UPDATES! (June 4, 2020)
## Introduction
This project aims to create a program and hardware setup that listens for a golf swing, then replays the swing in its entirety in full speed and slow motion with no user input. The videos are saved locally and to the cloud if the user desires. All coding is in python.

## **What To Buy**
### Required Materials
- [Raspberry Pi 4 (4gb)](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_4?dchild=1&keywords=raspberry+pi&qid=1590900503&sr=8-4)
  - Untested on other versions/configurations of the Pi, but should work on any reasonably recent iteration
- [Raspberry Pi Camera Module](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?dchild=1&keywords=raspberry+pi+camera&qid=1590900526&sr=8-1)
  - New High-Quality Camera works as well (perhaps better), but probably warrants the new 8gb Pi for processing
- [USB Microphone](https://www.amazon.com/AIYIBEN-Super-Micr%C3%B3fono-Laptop-Desktop/dp/B01MQ2AA0X/ref=sr_1_1_sspa?dchild=1&keywords=usb+microphone+raspberry+pi&qid=1590903075&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUzFWMzNHTjBPN1c3JmVuY3J5cHRlZElkPUEwMzQxMjkyMkJaRUY4MEwwODNMNiZlbmNyeXB0ZWRBZElkPUEwMzY1NTk2MVVIVDhPWE80TzVDSCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
- Any monitor that accepts HDMI input
- Micro-HDMI to HDMI Cable
- USB Mouse
- [USB-C Power Cable](https://www.raspberrypi.org/products/type-c-power-supply/)
  - While any USB-C cable will connect, it  might be either too much or too little power so I reccomend buying one designed for the Pi
- Micro SD Card for the Operating System
  - 16GB should be regarded as the bare minimum. Many are sold with Pi OS preinstalled
  
### Optional Materials
- Raspberry Pi Starter  Kit
  - There are a variety of these on the internet, and they often come bundled with a case and the required hdmi and power cables
- [Two Step Pedal System](https://www.amazon.com/gp/product/B07QDRPDS2/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
  - Used in Appendix C, this is not required but a nice touch and increases functionality
- USB or Bluetooth Keyboard
  - Not necessary if you intend to only use SSH for the initialization, but convinient for ironing out bugs and making quick changes without the constraints of VNC or SSH (See Appendix A)

## **Step 0: Set up the Raspberry Pi**
You can skip this step if you have already set up your Pi.

There are countless guides online to set up your Raspberry Pi. I inlcuded some below for your convinience. This guide assumes that Raspbian Buster is installed. All you need to do is get the OS installed to proceed to Step 1. To verify that you have, simply plug the Pi into a monitor and verify that you are guided to a Desktop.

### Guides for basic setup (You just need to pick one)
- [Official Raspberry Pi Guide](https://www.raspberrypi.org/help/noobs-setup/2/)
- [HowToForge Guide](https://www.howtoforge.com/tutorial/howto-install-raspbian-on-raspberry-pi/)
- [ThePi.io Guide](https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/)


## Appendix A: Remote vs. Local
The commands in this guide can either come through SSH (from another computer remotely) or be typed into a keyboard connected to the Raspberry Pi. The instructions will assume they are typed directly (because a monitor is required anyway), so if you plan to use SSH simply follow the instructions below. These instructions are for Mac users, but they should work on any platform. 

[How to set up SSH the first time](https://www.raspberrypi.org/documentation/remote-access/ssh/)

Each time you want to use SSH to interface, you will need to follow these instructions:

[How to connect to SSH each time](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)

Given that these instructions are followed, any command line instruction can be typed into the Terminal on your computer or to the Pi Terminal.

## **Step 1: Download Everything You Will Need**
There are a number of python packages that you will need in order to run the program. Each one has a slightly different set of steps to install it so pay attention to the syntax. For convinience, they are first listed altogether and then the command to download is below.

Occasionally, the command line will ask if you wish to continue given the amount of memory it requires. It needs an input of Y to continue, so simply type Y and then press enter when this occurs. Depending on the version of Raspbian you install, you might already have some of these, but run each command to be sure. 

### Required Packages
- picamera
- cv2
- sounddevice
- numpy
- libportaudio

### Download Instructions (Type these commands into Terminal)
##### **System Packages needed for OpenCV (Thanks to [pyimagesearch](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/) for these)**
```
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
```
##### Make sure your system is up to date
```sudo apt-get update```

##### **NOTE: I reccomend installing these in a [virtual environment](https://docs.python.org/3/library/venv.html)**
##### picamera
```sudo apt-get install python-picamera python3-picamera```
##### libportaudio
```sudo apt-get install -y libportaudio-dev```
##### sounddevice
  ```python3 -m pip install sounddevice```
##### numpy
  ```pip install numpy```
##### OpenCV
  ```pip install opencv-contrib-python```

## **Step 2: Install The Camera Module**
Consult [this guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2) to install the camera module. Ensure that it is in the correct orientation (blue tape towards the ethernet port) and that you enable the camera module either in the local settings or by typing ```sudo raspi-config``` into terminal. 

**USE CAUTION WHEN HANDLING THE CAMERA. IT IS VERY SENSITIVE TO STATIC ELECTRICITY SO BE SURE TO GROUND YOURSELF**

## Appendix B: Making a case for the camera
Due to the camera's sensitivity to static electricity, it might be smart to create a case for the camera. You could buy one online, or it is very easy to make your own using a SD Card Case. Simply cut a square into the plastic for the lens to go through and clear out one side of it for the ribbon cable. 

PICTURE HERE

## **Step 3: Check that the camera and mic are functional**
To check that the camera is working, type ```raspistill -o Desktop/test.jpg``` into the terminal. This will take a still image and allows you to ensure the camera is connected and functioning properly. 

To verify that the microphone is working, plug it into one of the USB Ports and then right click the audio icon in the menu bar. Click input devices and turn its volume all the way up. This step will vary slightly depending on which mic you used, but it was the procedure for the two types of mics I tested (USB Lapel Mic and the USB Mic linked in the materials section).

## **Step 4: Download the main program**
The main program ([linked here](swing_replay.py)) is what will run while you are hitting. There are a variety of lines that are commented out, so if you run it as it comes, it has only the basic functionality (listens for shot, replays it full speed, replays it half speed) and doesn't include pedal support or cloud functionality. Step 7 will discuss how to enable these portions of it and other steps you will need to take. 

Download [the file](swing_replay.py) to your desktop and save it to any name you want (obviously ensuring it ends with .py).

## **Step 5: Set up the required folders and subprograms**
You can name the folders anything you want, but if you choose a different name be sure to update it in the code wherever referenced. For simplicity, the names in the instructions align with the ones in the python program. 

- **Create a folder named Swing Replays**
On the desktop, right click and make a folder called "Swing Replays" for the video files

- **Create a file named golf_video_replay**
On the desktop, right click and make a file named "golf_video_replay". This will be the icon for the desktop for you to actually run the program. 

- **OPTIONAL: Download the audio calibration program**
This isn't required (I did it manually with trial and error), but each setup will have a slightly different audio level threshold for the microphone based on mic brand and proximity to the swing. To figure out your specific threshold I made a simple program to identify your level. 

## **Step 6: Find your Audio Threshold and write it into your program**
ONCE AUDIO PROGRAM IS MADE PUT INSTRUCTIONS HERE

## **Step 7: Add additional functionality**
In order to have any additional functionality, you will need to have the [Two Step Pedal System](https://www.amazon.com/gp/product/B07QDRPDS2/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1). All it is, though, is a big keyboard where the left pedal presses 'a' and the right presses 'b'. With this in mind, you can enable this functionality by using a usb keyboard or some other implementation.

### Extra Features:
There are three primary extra features included with the program. Because the pedal system has two pedals, you need to pick two. I assume most people will elect to include "replay again" and "cloud upload" but if your system is offline or there is some other reason you do not want to have one of these two it also has the capability to have a button to simply skip the swing. 

##### 1. Upload to cloud
This will upload the last swing to the cloud. 

##### 2. Replay last swing again
This will show the most recent swing in full speed and then slow motion

##### 3. Skip the replay and begin listening
This will close out the replay and begin listening again (useful if the mic is accidentally set off or you want to quickly hit again without viewing)

CONTINUE HERE WITH INSTRUCTIONS FOR ENABLING THE DESIRED FEATURES


### Thanks To
The following resources were used to make this project:


### Support or Contact

Having trouble with your project? Reach out to me by emailing 2000dsr@gmail.com and I will see if I can help.
