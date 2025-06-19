import numpy as np
import matplotlib.patches as mpatches
from .geometry import find_angle, find_length, find_center, rotate
from .basicdraw import arrow_triangle
from .propagators import ts_fs_scalar,ts_fs_photon,ts_fs_gluon


########
# Arcs #
########

# arc propagator from point p1 to p2 going counter clockwise
# h is the distance between the "center" of the would-be circle and the straight line joining p1 to p2, and can be negative
def parametric_arc(ax,p1,p2,h,dr,w,ls,lw,color,ts_fs):
	c = find_center(p1,p2,h)
	cx,cy = c
	theta1 = find_angle(c,p1)
	theta2 = find_angle(c,p2)
	if theta1 >= theta2:
		theta2 = theta2 + 2*np.pi
	r = find_length(c,p1)

	ts_init = np.linspace(0,r*np.abs(theta1-theta2),1000)
	ts,fs = ts_fs(ts_init,dr,w)
	thetas = np.linspace(theta1,theta2,1000)

	xs = cx + r*np.cos(thetas)+fs*np.cos(thetas)-ts*np.sin(thetas)
	ys = cy + r*np.sin(thetas)+fs*np.sin(thetas)+ts*np.cos(thetas)

	ax.plot(xs, ys, ls=ls,lw=lw,color=color)

	return c,r,theta1,theta2

def scalar_arc(ax,p1,p2,h=0,ls='--',lw=1,color='k'):
	parametric_arc(ax,p1,p2,h,0,0,ls,lw,color,ts_fs=ts_fs_scalar)

def fermion_arc(ax,p1,p2,h=0,ls='-',lw=1,color='k',clockwise=False):
	phase = np.pi/2
	if clockwise:
		p1,p2 = p2,p1
		phase = 3*np.pi/2
	c,r,theta1,theta2 = parametric_arc(ax,p1,p2,h,0,0,ls,lw,color,ts_fs=ts_fs_scalar)
	p1x,p1y = p1
	theta=(theta2-theta1)/2
	arrow_triangle(ax,rotate(c,theta,p1x,p1y),phase+theta1+theta)

def photon_arc(ax,p1,p2,h=0,dr=0.07,w=12,ls='-',lw=1,color='k'):
	parametric_arc(ax,p1,p2,h,dr,w,ls,lw,color,ts_fs=ts_fs_photon)

def gluon_arc(ax,p1,p2,h=0,dr=0.07,w=12,ls='-',lw=1,color='k'):
	parametric_arc(ax,p1,p2,h,dr,w,ls,lw,color,ts_fs=ts_fs_gluon)


##############
# Full Loops #
##############

# loop propagator at center c and radius r
# there are nP arrows, and the phase rotates them
def line_loop(ax,c,r,nP=2,phase=0,color='k',lw=1,ls='-'):
	ax.add_patch(mpatches.Circle(c,r,fill=False,ec='0',ls=ls,lw=lw,color=color))
	for i in range(nP):
		cx,cy = c
		theta = phase + i*2*np.pi/nP
		arrow_triangle(ax,rotate(c,theta,cx,cy-r),theta)

def scalar_loop(ax,c,r,nS=0,phase=0,color='k',lw=1,ls='--'):
	line_loop(ax,c,r,nS,phase,color,lw,ls=ls)

def fermion_loop(ax,c,r,nF=2,phase=0,color='k',lw=1,ls='-'):
	line_loop(ax,c,r,nF,phase,color,lw,ls=ls)

def gluon_loop(ax,c,r,h=0,dr=0.07,w=12,ls='-',lw=1,color='k'):
	cx,cy = c
	p = (cx+r,cy)
	gluon_arc(ax,p,p,r,dr,w,ls,lw,color)
