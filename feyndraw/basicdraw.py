import numpy as np
import matplotlib.patches as mpatches
from .geometry import find_angle, find_length, find_center, rotate

# Draw the triangle of an arrow
def arrow_triangle(ax,c,theta,b=0.05,h=0.05,color='k'):
	cx,cy = c
	ax.add_patch(mpatches.Polygon(
			[[cx+h*np.cos(theta),cy+h*np.sin(theta)],
			[cx-h*np.cos(theta)-b*np.sin(theta),cy-h*np.sin(theta)+b*np.cos(theta)],
			[cx-h*np.cos(theta)+b*np.sin(theta),cy-h*np.sin(theta)-b*np.cos(theta)]],
	   		closed=True,fill=True,fc=color,ec=color))

# Draw an arrow with pointy end
def arrow(ax,p1,p2,b=0.05,h=0.05,lw=1,color='k'):
	x1,y1 = p1
	x2,y2 = p2
	theta = find_angle(p1,p2)
	ax.plot([x1,x2], [y1,y2], color=color, lw=lw)
	arrow_triangle(ax,p2,theta,b,h,color)

def arrow_momentum(ax,p1,p2,b1=0.2,b2=0.2,h=0.1,ba=0.05,ha=0.05,lw=1,color='k'):
	theta = find_angle(p1,p2)
	L = find_length(p1,p2)
	ts = np.array([b1*L,(1-b2)*L])
	fs = np.array([h,h])
	p1x,p1y = p1
	xs,ys = rotate(p1,theta,ts+p1x,fs+p1y)
	arrow(ax,(xs[0],ys[0]),(xs[1],ys[1]),ba,ha,lw,color)


def arrow_momentum_arc(ax,p1,p2,h=0,b1=0.3,b2=0.3,H=0.2,ba=0.05,ha=0.05,lw=1,color='k',clockwise=False):
	if clockwise:
		p1,p2 = p2,p1

	c = find_center(p1,p2,h)
	cx,cy = c
	theta1 = find_angle(c,p1)
	theta2 = find_angle(c,p2)
	if theta1>theta2:
		theta2 = theta2 + 2*np.pi
	r = find_length(c,p1)

	theta = (theta2-theta1)
	theta1b = theta1+b1*theta
	theta2b = theta2-b2*theta
	thetas = np.linspace(theta1b,theta2b,1000)

	xs = cx + (r+H)*np.cos(thetas)
	ys = cy + (r+H)*np.sin(thetas)

	ax.plot(xs,ys,lw=lw,color=color)

	phase = np.pi/2
	theta_lim = theta2b
	if clockwise:
		theta_lim = theta1b
		phase = 3*np.pi/2
	p2b = (cx + (r+H)*np.cos(theta_lim),cy + (r+H)*np.sin(theta_lim))
	arrow_triangle(ax,p2b,theta_lim+phase,ba,ha)

def line(ax,p1,p2,color='k',lw=1,ls='-',**kwargs):
	x1,y1 = p1
	x2,y2 = p2
	ax.plot([x1,x2], [y1,y2],ls=ls,color=color,lw=lw,**kwargs)