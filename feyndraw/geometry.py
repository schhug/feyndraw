import numpy as np
import matplotlib.patches as mpatches

# Find the angle betwenn x axis ans the line p1 -> p2
def find_angle(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	if x1 == x2:
		if y2>y1:
			theta = np.pi/2
		else:
			theta = -np.pi/2
	else:
		theta = np.arctan((y2-y1)/(x2-x1))
		if x2<x1: theta = theta + np.pi
	return theta

# Find length between two points
def find_length(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def find_center(p1,p2,h):
	x1,y1 = p1
	x2,y2 = p2
	theta = find_angle(p1,p2)
	cx = (x1+x2)/2 + h*np.sin(theta)
	cy = (y1+y2)/2 - h*np.cos(theta)
	return cx,cy

# rotate points [t,f] by theta around c
def rotate(c,theta,ts,fs):
	cx,cy = c
	xs = cx + (ts-cx)*np.cos(theta) - (fs-cy)*np.sin(theta)
	ys = cy + (ts-cx)*np.sin(theta) + (fs-cy)*np.cos(theta)
	return xs,ys