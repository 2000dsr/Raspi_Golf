
import io
import random
import picamera
import cv2
import time

import sounddevice as sd
import numpy as np
from subprocess import call
listening = True
video_num = 0
no_slow = False
dropbox_bool = False

def upload_to_db(filename, upload):
    dbx = dropbox.Dropbox('qpOipSp-m5wAAAAAAAABfigNoquCpwZijEZgoOCqhD_oBer0PCzeWB0cqJSdCMQ0')
    with open(filename, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        try:
            dbx.files_upload(f.read(), "/"+upload, mode=WriteMode('overwrite'))
        except ApiError as err:
            pass

def audio_monitor():
    global listening
    duration = 10  # number *10 = millisseconds (1 is 10 milliseconds)
    volumes = [0]

    audio_thresh = 20 #revert to 8

    def audio_callback(indata, frames, time, status):
        global listening
        volume_norm = np.linalg.norm(indata) * 10
        if volume_norm > audio_thresh and listening:
            listening = False

    stream = sd.InputStream(callback=audio_callback)
    with stream:
        while listening:
            sd.sleep(duration * 10)

def show_video(fn, fps):
    global no_slow
    global dropbox_bool
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
stream = picamera.PiCameraCircularIO(camera, seconds=1)
camera.start_recording(stream, format='h264')  # used to be h264 if this throws an error...

while True:# Main Loop
    if listening:
        audio_monitor()  # listens for the audio to be too loud
    if not listening:# triggered when audio is too loud, this is the video replay command
        no_slow = False
        dropbox_bool = False
        #try:
        camera.wait_recording(1)
        #if not listening:  # don't think this does anything but leaving it nonetheless
            # Keep recording for 10 seconds and only then write the
            # stream to disk

        timestr = time.strftime("%Y%m%d-%H%M%S")
        fname = "/home/pi/Desktop/Swing Videos/" + timestr + '.h264'
        stream.copy_to(fname)
        show_video(fname, 10)
        #time.sleep(1)
        if not no_slow:
            show_video(fname, 30)
        if dropbox_bool:
            #upload_to_dropbox(fname, timestr + '.h264')
            pass
        listening = True
       

