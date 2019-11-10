# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:47:53 2019

@author: Administrator

生成正弦波形声音

plottingWaveform.py
"""

import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

# sample/every second
framerate = 44100
# bytes needed every sample
sample_width = 2

frequency = [0,1047,1175,1319,1397,1568,1760,1967]
HisTheme = [1,5,4,1,3,3,4,0,1,4,1,3,3,4,0,1,5,4,1,3,3,4,0,1,4,6,5,4,5]
Duration = [0.5,0.5,0.5,0.5,0.75,0.75,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.5]
volume = 1000
#save wav file
wf = wave.open("HisTheme.wav", 'wb')
wf.setnchannels(1)
wf.setframerate(framerate)
wf.setsampwidth(sample_width)
Count = 0
for i in HisTheme:
    x = np.linspace(0, Duration[Count], num=Duration[Count]*framerate)
    y = np.sin(2 * np.pi * frequency[i] * x) * volume
    Count+=1
    # 将波形数据转换成数组
    sine_wave = y
    for i in sine_wave:
        data = struct.pack('<h', int(i))
        wf.writeframesraw(data)

wf.close()
