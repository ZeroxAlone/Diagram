# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:43:32 2019

@author: lisa_
"""

import mido


mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

s = 320
Count = 0
SubCount = 0
#Note = [0,61,63,65,66,68,70,71]
Note = [0,73,75,77,78,80,82,83]
SubNote = 66
HisTheme = [1,5,4,1,3,3,4,1,4,1,3,3,4,1,5,4,1,3,3,4,1,4,6,5,4,5]

for i in HisTheme:
    if 5 <= Count <= 6 or 11 <= Count <= 12:
        track.append(mido.Message('note_on', note=Note[i], velocity=96, time=int(s/2*3), channel=1))
        track.append(mido.Message('note_on', note=Note[i]-12, velocity=70, time=0, channel=2))
    else:
        track.append(mido.Message('note_on', note=Note[i], velocity=96, time=1*s, channel=1))
        track.append(mido.Message('note_on', note=Note[i]-12, velocity=70, time=0*s, channel=2))
    Count += 1
    SubCount += 1
    if Count == 7:
        track.append(mido.Message('note_off', note=Note[i], velocity=96, time=1*s, channel=1))
        track.append(mido.Message('note_on', note=SubNote, velocity=70, time=0*s, channel=2))        
    elif Count == 13:
        if SubCount == 13:
            SubNote = 68
        Count = 0
    
    if SubCount % 14 == 0:
        track.append(mido.Message('note_on', note=SubNote, velocity=70, time=0*s, channel=2))
        SubNote = 71
    elif SubCount == 26:
        SubNote = 66
        track.append(mido.Message('note_on', note=SubNote, velocity=70, time=0*s, channel=2))

track.extend(track)

mid.save('HisTheme.mid')

