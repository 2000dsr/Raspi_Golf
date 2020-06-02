# Pi Golf Replay

## THIS PROJECT IN CURRENTLY IN PROGRESS. CHECK BACK LATER FOR UPDATES! (May 31, 2020)

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
##### **NOTE TO SELF: VERIFY THAT THESE WORK**
##### Make sure your system is up to date
```sudo apt-get update```
##### picamera
```sudo apt-get install python-picamera python3-picamera```
##### libportaudio
```sudo apt-get install -y libportaudio-dev```
##### sounddevice
  ```python3 -m pip install sounddevice```
##### numpy
  ```pip install numpy```
##### OpenCV
  This is by far the most time consuming step. Consult [this guide](https://pimylifeup.com/raspberry-pi-opencv/) for a very thorough walkthrough of how to do it correctly. 

## **Step 2: Install The Camera Module**
Consult [this guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2) to install the camera module. Ensure that it is in the correct orientation (blue tape towards the ethernet port) and that you enable the camera module either in the local settings or by typing ```sudo raspi-config``` into terminal. 

**USE CAUTION WHEN HANDLING THE CAMERA. IT IS VERY SENSITIVE TO STATIC ELECTRICITY SO BE SURE TO GROUND YOURSELF**

## Appendix B: Making a case for the camera
Due to the camera's sensitivity to static electricity, it might be smart to create a case for the camera. You could buy one online, or it is very easy to make your own using a SD Card Case. Simply cut a square into the plastic for the lens to go through and clear out one side of it for the ribbon cable. 

PICTURE HERE

## **Step 3: Check that the camera and mic are functional**
To check that the camera is working, type ```raspistill -o Desktop/test.jpg``` into the terminal. This will take a still image and allows you to ensure the camera is connected and functioning properly. 

To verify that the microphone is working, plug it into one of the USB Ports and then right click the audio icon in the menu bar. Click input devices and turn its volume all the way up. This step will vary slightly depending on which mic you used, but it was the procedure for the two types of mics I tested (USB Lapel Mic and the USB Mic linked in the materials section).

## **Step 4: Set up the required folders and subprograms**

## **Step 5: Select which version you want**
I have included three different versions of the main python program. You can decide which you want based on the materials you have and what functionality you want.




### Thanks To
The following resources were used to make this project:


### Support or Contact

Having trouble with your project? Reach out to me by emailing 2000dsr@gmail.com and I will see if I can help.
