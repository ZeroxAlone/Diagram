# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:01:37 2019

@author: lisa_
"""

#We, 我，们，中国人

from PIL import Image
import matplotlib.pyplot as plt

'''
IMG = Image.open('build.jpg')
One = IMG.convert('1')
P = IMG.convert('P')
RGB = IMG.convert('RGB')
RGBA = IMG.convert('RGBA')
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.set_title('1bit')
ax2 = fig.add_subplot(222)
ax2.set_title('8bits')
ax3 = fig.add_subplot(223)
ax3.set_title('24bits')
ax4 = fig.add_subplot(224)
ax4.set_title('32bits')
ax1.imshow(One,cmap='gray')
ax2.imshow(P)
ax3.imshow(RGB)
ax4.imshow(RGBA)
plt.show()
plt.savefig('convert.jpg')
'''
'''
import matplotlib
matplotlib.rcParams['backend'] = 'SVG'
import matplotlib.pyplot as plt
import math

x=50
List1=[]
for i in range(500):
    List1.append(math.sin(x))
    x-=0.1
plt.plot(List1)
plt.savefig('kankan.svg',format='svg')
'''
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#Array = [[]for i in range(50)]
#for i in range(50):
#    if i % 2 == 0:
#        n = 0
#    else:
#        n = 255
#    for x in range(50):
#        Array[i].append(n)
#        if n == 0:
#            n = 255
#        else:
#            n = 0

Array = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,255,0,255,255,255,0,255,0,0,0,0,0,0,0,0,0,0],
                 [0,0,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0],
                 [0,0,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0],
                 [0,255,255,0,255,255,0,255,255,255,0,0,0,0,0,0,0,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,255,0],
                 [0,255,255,255,0,0,255,255,255,255,255,255,255,255,0,0,0,255,0],
                 [0,255,0,255,0,255,255,0,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0],
                 [0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0],
                 [0,0,255,255,0,0,255,255,0,0,0,255,255,0,0,255,255,0,0],
                 [0,0,255,255,0,0,255,255,0,0,0,255,255,0,0,255,255,0,0],
                 [0,0,255,0,0,0,255,0,0,0,0,255,0,0,0,255,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

print(Array)

plt.imshow(Array, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.savefig('bitmap.jpg')
plt.savefig('bitmap.svg')
plt.savefig('bitmap.png')
img = Image.open('bitmap.png')
img.save('bitmap.bmp')
img.save('bitmap.gif')