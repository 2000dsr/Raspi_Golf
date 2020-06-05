
import io
import random
import picamera
import cv2
import time
import shutil

import sounddevice as sd
import numpy as np
from subprocess import call
listening = True
rerun = False
video_num = 0
no_slow = False
dropbox_bool = False
fname = '/home/pi/Downloads/20200531-192136.h264'
cloud_fname = '/home/pi/Downloads/20200531-192136.h264'
import keyboard

def audio_monitor():
    global listening
    duration = 10  # number *10 = millisseconds (1 is 10 milliseconds)
    volumes = [0]

    audio_thresh = 150 #revert to 8

    def audio_callback(indata, frames, time, status):
        global listening
        global rerun
        volume_norm = np.linalg.norm(indata) * 10
        if volume_norm > audio_thresh and listening:
            listening = False
        if keyboard.is_pressed('a'):
            listening = False
            rerun = True

    stream = sd.InputStream(callback=audio_callback)
    with stream:
        while listening:
            sd.sleep(duration * 10)

def show_video(fn, fps):
    global no_slow
    global dropbox_bool
    global rerun
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(fn)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video file")
    test_img = np.zeros(shape =(640,480,3)).astype('uint8')
    cv2.imshow('Frame', test_img)
    cv2.moveWindow('Frame', 200, 200)
    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            if cv2.waitKey(int(fps)) & 0xFF == ord('b'):
                dropbox_bool = True
                no_slow = True
                break
            # Press Q on keyboard to  exit
            if cv2.waitKey(int(fps)) & 0xFF == ord('a'):
                no_slow = True
                break
                

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

camera = picamera.PiCamera()
camera.exposure_mode = 'sports'
camera.framerate = 40
stream = picamera.PiCameraCircularIO(camera, seconds=1)
camera.start_recording(stream, format='h264')  # used to be h264 if this throws an error...

while True:# Main Loop
    if listening:
        audio_monitor()  # listens for the audio to be too loud
    if not listening and not rerun:# triggered when audio is too loud, this is the video replay command
        no_slow = False
        dropbox_bool = False
        #try:
        camera.wait_recording(1)
        #if not listening:  # don't think this does anything but leaving it nonetheless
            # Keep recording for 10 seconds and only then write the
            # stream to disk

        timestr = time.strftime("%Y%m%d-%H%M%S")
        fname = "/home/pi/Desktop/Swing Videos/" + timestr + '.h264'
        cloud_fname = "/home/pi/Desktop/cloud_swings/"+ timestr + '.h264'
        stream.copy_to(fname)
        show_video(fname, 10)
        #time.sleep(1)
        if not no_slow:
            show_video(fname, 30)
        if dropbox_bool:
            stream.copy_to(cloud_fname)
        listening = True
    if rerun and not listening:
        dropbox_bool = False
        no_slow = False
        show_video(fname, 10)
        if not no_slow:
            show_video(fname, 30)
        if dropbox_bool:
            shutil.copy(fname,cloud_fname) 
        listening = True
        rerun = False
        


