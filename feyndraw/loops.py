import numpy as np
import matplotlib.patches as mpatches
from .geometry import numpyfy, find_angle, find_angles, find_length, find_point, find_center, rotate, rotate_points
from .basicdraw import arrow_triangle, arc, arc_arrow_triangle, ba_def, ha_def, da_def
from .propagators import z_def_prop,ts_fs_scalar,dts_dfs_scalar,ts_fs_photon,dts_dfs_photon,ts_fs_gluon


########
# Arcs #
########

# arc propagator from point p1 to p2 going counter clockwise
# dr is the distance between the "center" of the would-be circle and the straight line joining p1 to p2, and can be negative
def parametric_arc(ax,p1,p2,dr,ts_fs,h,w,color,lw,ls,hp=0,zorder=z_def_prop,clockwise=False):
	c = find_center(p1,p2,dr)
	r = find_length(c,p1)
	theta1, theta2 = find_angles(c,p1,p2)
	ts_init = np.linspace(0,r*np.abs(theta1-theta2),1000)
	ts,fs = ts_fs(ts_init,h,w,hp=hp)
	arc(ax,p1,p2,dr=dr,ts=ts,fs=fs,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	return c,r,theta1,theta2

def scalar_arc(ax,p1,p2,dr=0,color='k',lw=1,ls='--',arrw=False,bp=0.5,ba=ba_def,ha=ha_def,da=da_def,zorder=z_def_prop,clockwise=False,double=False):
	if double:
		hp = 0.01*lw
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_scalar,h=0,w=0,hp=hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_scalar,h=0,w=0,hp=-hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	else:
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=ts_fs_scalar,h=0,w=0,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	if arrw: arc_arrow_triangle(ax,p1,p2,dr=dr,bp=bp,ba=ba,ha=ha,da=da,color=color,zorder=zorder,clockwise=clockwise)

def fermion_arc(ax,p1,p2,dr=0,color='k',lw=1,ls='-',arrw=True,bp=0.5,ba=ba_def,ha=ha_def,da=da_def,zorder=z_def_prop,clockwise=False,double=False):
	if double:
		hp = 0.01*lw
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_scalar,h=0,w=0,hp=hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_scalar,h=0,w=0,hp=-hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	else:
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=ts_fs_scalar,h=0,w=0,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	if arrw: arc_arrow_triangle(ax,p1,p2,dr=dr,bp=bp,ba=ba,ha=ha,da=da,color=color,zorder=zorder,clockwise=clockwise)

def photon_arc(ax,p1,p2,dr=0,h=0.07,w=12,color='k',lw=1,ls='-',zorder=z_def_prop,clockwise=False,double=False):
	if double:
		hp = 0.01*lw
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_photon,h=h,w=w,hp=hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=dts_dfs_photon,h=h,w=w,hp=-hp,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)
	else:
		parametric_arc(ax,p1,p2,dr=dr,ts_fs=ts_fs_photon,h=h,w=w,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)

def gluon_arc(ax,p1,p2,dr=0,h=0.07,w=12,color='k',lw=1,ls='-',zorder=z_def_prop,clockwise=False):
	parametric_arc(ax,p1,p2,dr=dr,ts_fs=ts_fs_gluon,h=0,w=0,color=color,lw=lw,ls=ls,zorder=zorder,clockwise=clockwise)


##############
# Full Loops #
##############

# loop propagator at center c and radius r
# there are nP arrows, and the phase rotates them
def line_loop(ax,c,r,nP=2,phase=0,color='k',lw=1,ls='-',ba=ba_def,ha=ha_def,da=da_def,zorder=z_def_prop,clockwise=False):
	ax.add_patch(mpatches.Circle(c,r,fill=False,ec=color,ls=ls,lw=lw,zorder=zorder))
	for i in range(nP):
		theta = phase + i*2*np.pi/nP
		pt = rotate_points(c,theta,numpyfy(c) + [0,-r])
		arrow_triangle(ax,pt,theta=theta,ba=ba,ha=ha,da=da,color=color,zorder=zorder)

def scalar_loop(ax,c,r,nS=0,ls='--',**kwargs):
	line_loop(ax,c,r,nP=nS,ls=ls,**kwargs)

def fermion_loop(ax,c,r,nF=2,ls='-',**kwargs):
	line_loop(ax,c,r,nP=nF,ls=ls,**kwargs)

def gluon_loop(ax,c,r,dr=0,h=0.07,w=12,ls='-',lw=1,color='k',zorder=z_def_prop):
	p = numpyfy(c) + [r,0]
	gluon_arc(ax,p,p,dr=dr,h=0,w=0,color=color,lw=lw,ls=ls,zorder=z_def_prop)
