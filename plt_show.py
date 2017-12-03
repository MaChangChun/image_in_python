#!usr/bin/python
# coding=utf-8
"""
使用plt进行图像展示
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import time
import matplotlib.animation as animation

_figure = plt.Figure()


def display_array(a, rng=[0,1]):
	a = (a - rng[0]) / float(rng[1] - rng[0]) * 255
	a = np.uint8(np.clip(a, 0, 255))
	plt.imshow(a)
	pass


def show_items(items):
	_figure.clear()
	length = len(items)
	width = math.ceil(math.sqrt(length))
	hight = math.ceil(float(length)/width)
	for i in range(length):
		item = items[i]
		plot = plt.subplot(hight, width, i+1)
		plot.imshow(item, cmap = plt.cm.gray)
	plt.show(block=True)
	time.sleep(1)
	plt.clf()





