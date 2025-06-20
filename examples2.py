import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import use, rc
from feyndraw import *

use('agg')
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'serif','serif':['Times']})
rc('text',usetex=True)
"""

# Example 14
# tests
fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)



fermion_propagator(ax,(-5,-1),(-4,-1))
fermion_arc(ax,(-4,-1),(-3,-1),clockwise=True,color='r')
photon_propagator(ax,(-4,-1),(-3,-1))
fermion_propagator(ax,(-3,-1),(-1,-1))
fermion_propagator(ax,(-1,-1),(0,0))
photon_arc(ax,(-1.5,-1),(-2.5,-1),0)
arrow_momentum_arc(ax,(-1.5,-1),(-2.5,-1),0)

d=0.06
fermion_propagator(ax,(-5,1),(-4,1))
fermion_arc(ax,(-3,1),(-4,1))
gluon_propagator(ax,(-4,1-d),(-3,1-d),w=12)
fermion_propagator(ax,(0,0),(-1,1))
fermion_propagator(ax,(-1,1),(-3,1))
gluon_arc(ax,(-1.5,1),(-2.5,1),0.0443)
arrow_momentum_arc(ax,(-2.5,1),(-1.5,1),0,clockwise=True)

photon_propagator(ax,(0,0),(3,0))
scalar_arc(ax,(2,0),(1,0),0.1)
oscillation_x(ax,(1.5,0),b=0.1)
blob(ax,(0,0),0.2)

fermion_loop(ax,(3.5,0),0.5,nF=3,phase=np.pi/2,color='b')
gluon_propagator(ax,rotate((3.5,0),np.pi/3,3.5+0.5,0),rotate((3.5,0),np.pi/3,3.5+1.35,0))
scalar_propagator(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0))
arrow_momentum(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0),hp=0.2)

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.03)

gluon_loop(ax,rotate((3.5,0),np.pi/3,3.5+1.35+0.6,0),0.5,w=14)

fig.savefig("examples/example_14", bbox_inches='tight')
plt.close(fig)
"""
# test
theta=0.3
b=0.1
h=0.1
d=0.02
p1=[0,1]
p2=[1,1]

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)
"""
fermion_loop(ax,(1.5,0),0.5,nF=3,phase=np.pi/2)
arrow_triangle(ax,[0,0.5],theta,b,h,d,color='k')
arrow_momentum(ax,p1,p2,b1=0.2,b2=0.2,hp=0.2)
photon_propagator(ax,p1,p2, color='r')
color='#7177BB'
#color='k'
photon_propagator(ax,[0,0],[2,0.5], color=color, double=True,lw=2)
blob(ax,(0.5,0),0.2,color=color)
oscillation_x(ax,[2,0],theta=0.3,b=0.1,color='k',lw=5,zorder=2)
scalar_propagator(ax,[0,0.5],[2,1], color=color, double=True,lw=1)

scalar_arc(ax,p1,p2,double=True,color='b')
fermion_arc(ax,p2,p1,double=True,color='g')
"""
photon_propagator(ax,[1,1],[2,0.5], color='k', double=True,lw=2)
fermion_arc(ax,[1,0],[0,0],double=False,color='r')
fermion_arc(ax,[2,0],[1,0],double=True,color='r')

fig.savefig("examples/example_15", bbox_inches='tight')
plt.close(fig)
