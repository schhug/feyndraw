import numpy as np
import matplotlib.patches as mpatches
from .geometry import find_angle, find_length, rotate
from .basicdraw import arrow,arrow_triangle,line

########################
# Scalars and Fermions #
########################

# Straignt line propagator from point p1 to p2
# Use this one for full customization
def line_propagator(ax,p1,p2,arrw=False,color='k',lw=1,ls='-'):
	line(ax,p1,p2,color,lw,ls)
	if arrw:
		x1,y1 = p1
		x2,y2 = p2
		theta = find_angle(p1,p2)
		cx,cy = (x1+x2)/2,(y1+y2)/2
		arrow_triangle(ax,(cx,cy),theta,color=color)

# Dashed line, no arrow
def scalar_propagator(ax,p1,p2,arrw=False,color='k',lw=1,ls='--'):
	line_propagator(ax,p1,p2,arrw,color,lw,ls=ls)

# Full line, with arrow
def fermion_propagator(ax,p1,p2,arrw=True,color='k',lw=1,ls='-'):
	line_propagator(ax,p1,p2,arrw,color,lw,ls=ls)

def antifermion_propagator(ax,p1,p2,arrw=True,color='k',lw=1,ls='-'):
	line_propagator(ax,p2,p1,arrw,color,lw,ls=ls)

######################
# Photons and Gluons #
######################

def parametric_propagator(ax,p1,p2,h,w,color,lw,ts_fs):
	ts_init = np.linspace(0,find_length(p1,p2),1000)
	ts, fs = ts_fs(ts_init,h,w)
	p1x,p1y = p1
	xs, ys = rotate(p1,find_angle(p1,p2),p1x+ts_init+ts,p1y+fs)
	ax.plot(xs, ys, color=color, lw=lw)


def ts_fs_scalar(ts_init,h,w):
	return np.zeros(len(ts_init)),np.zeros(len(ts_init))

def ts_fs_photon(ts_init,h,w):
	return np.zeros(len(ts_init)),h*np.sin(np.sin(np.sin(ts_init*w*np.pi)))

def ts_fs_gluon(ts_init,h,w):
	return h*np.sin(ts_init*w*np.pi),h*np.cos(ts_init*w*np.pi)

# Photon (wavy-line) propagator from point p1 to p2
def photon_propagator(ax,p1,p2,h=0.07,w=12,color='k',lw=1,ls='-'):
	parametric_propagator(ax,p1,p2,h,w,color,lw,ts_fs_photon)

# Gluon (helix) propagator from point p1 to p2
def gluon_propagator(ax,p1,p2,h=0.07,w=12,color='k',lw=1,ls='-'):
	parametric_propagator(ax,p1,p2,h,w,color,lw,ts_fs_gluon)

