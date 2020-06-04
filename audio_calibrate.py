# This program lets you know what your audio threshold should be


import sounddevice as sd
import numpy as np
import time

final_vol = 0

def audio_callback(indata, frames, time, status):
    global final_vol
    volume_norm = np.linalg.norm(indata) * 10
    if int(volume_norm) > final_vol:
        final_vol = int(volume_norm)


def audio_test():
    global final_vol
    duration = 1000  # 10 seconds
    volumes = []
    three_swing_avg = []
    stream = sd.InputStream(callback=audio_callback)
    with stream:
        for run in range(3):
            if run == 0:
                print('Starting In:')
                time.sleep(1)
                print('5')
                time.sleep(1)
                print('4')
                time.sleep(1)
                print('3')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('1')
            print('[TEN Seconds for Swing '+str(run+1)+']:')
            for a in range(11): # Ten Seconds per Swing
                sd.sleep(duration * 1)
                print(str(10-a))
            three_swing_avg.append(final_vol)
            final_vol = 0
    print("Three Audio Values:")
    print(three_swing_avg)
    print("Average:")
    print(np.mean(three_swing_avg))
    print("Standard Deviation: ")
    print(np.std(three_swing_avg))
    print('')
    print('If all three values are similar and were realistic swings, err slightly below the lowest reading')


input('Press Enter To Begin Test: ')
audio_test()


