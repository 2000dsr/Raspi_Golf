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
  - Used in Appendix B, this is not required but a nice touch and saves disk space down the line
- USB or Bluetooth Keyboard
  - Not necessary if you intend to only use SSH for the initialization, but convinient for ironing out bugs and making quick changes without the constraints of VNC

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
There are a number of python packages that you will need in order to run the program. Each one has a slightly different set of steps to install it so pay attention to the syntax






  




### Support or Contact

Having trouble with your project? Reach out to me by emailing 2000dsr@gmail.com and I will see if I can help.
