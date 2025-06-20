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
# Example 1
# e- gamma to gamma' e- t-channel

fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(-2,1+d),(0,1))
fermion_propagator(ax,(0,1),(0,-1))
fermion_propagator(ax,(0,-1),(2,-1-d))
photon_propagator(ax,(0,1),(2,1+d))
photon_propagator(ax,(0,-1),(-2,-1-d))

ax.text(-2, 1+d, r"$e^-$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(2, -1-d, r"$e^-$",color='k',fontsize=30,va='top',ha='left')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(-2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='right')

arrow_momentum(ax,(0,1),(0,-1),b1=0.2,b2=0.2,h=0.15)
ax.text(0.2, 0, r"$p_1-p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,h=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,h=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_01", bbox_inches='tight')
plt.close(fig)



# Example 2
# e- gamma to gamma' e- s-channel

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)

d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(-2,1+d),(-1,0))
fermion_propagator(ax,(-1,0),(1,0))
fermion_propagator(ax,(1,0),(2,-1-d))
photon_propagator(ax,(1,0),(2,1+d))
photon_propagator(ax,(-1,0),(-2,-1-d))

ax.text(-2, 1+d, r"$e^-$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(2, -1-d, r"$e^-$",color='k',fontsize=30,va='top',ha='left')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(-2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='right')

arrow_momentum(ax,(-1,0),(1,0),b1=0.2,b2=0.2,h=0.15)
ax.text(0, 0.2, r"$p_1+p_2$",color='k',fontsize=20,va='bottom',ha='center')

arrow_momentum(ax,(-2,1+d),(-1,0),b1=0.2,b2=0.2,h=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(-1,0),b1=0.2,b2=0.2,h=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(1,0),(2,1+d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(1,0),(2,-1-d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(1.2, 0, r"$\mu$",color='k',fontsize=15,va='center',ha='left')
ax.text(-1.2, 0, r"$\nu$",color='k',fontsize=15,va='center',ha='right')

fig.savefig("examples/example_02", bbox_inches='tight')
plt.close(fig)


# Example 3
# e+ gamma to gamma' e+ t-channel

fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(2,-1-d),(0,-1))
fermion_propagator(ax,(0,-1),(0,1))
fermion_propagator(ax,(0,1),(-2,1+d))
photon_propagator(ax,(0,1),(2,1+d))
photon_propagator(ax,(0,-1),(-2,-1-d))

ax.text(-2, 1+d, r"$e^+$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(2, -1-d, r"$e^+$",color='k',fontsize=30,va='top',ha='left')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(-2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='right')

arrow_momentum(ax,(0,-1),(0,1),b1=0.2,b2=0.2,h=-0.15)
ax.text(0.2, 0, r"$-p_1+p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,h=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,h=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_03", bbox_inches='tight')
plt.close(fig)



# Example 4
# e+ gamma to gamma' e+ s-channel

fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(2,-1-d),(1,0))
fermion_propagator(ax,(1,0),(-1,0))
fermion_propagator(ax,(-1,0),(-2,1+d))
photon_propagator(ax,(1,0),(2,1+d))
photon_propagator(ax,(-1,0),(-2,-1-d))

ax.text(-2, 1+d, r"$e^+$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(2, -1-d, r"$e^+$",color='k',fontsize=30,va='top',ha='left')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(-2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='right')

arrow_momentum(ax,(1,0),(-1,0),b1=0.2,b2=0.2,h=-0.15)
ax.text(0, 0.2, r"$-p_1-p_2$",color='k',fontsize=20,va='bottom',ha='center')

arrow_momentum(ax,(-2,1+d),(-1,0),b1=0.2,b2=0.2,h=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(-1,0),b1=0.2,b2=0.2,h=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(1,0),(2,1+d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(1,0),(2,-1-d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(1.2, 0, r"$\mu$",color='k',fontsize=15,va='center',ha='left')
ax.text(-1.2, 0, r"$\nu$",color='k',fontsize=15,va='center',ha='right')

fig.savefig("examples/example_04", bbox_inches='tight')
plt.close(fig)


# Example 5
# e+e- to gamma gamma' t-channel

fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(-2,1+d),(0,1))
fermion_propagator(ax,(0,1),(0,-1))
fermion_propagator(ax,(0,-1),(-2,-1-d))
photon_propagator(ax,(0,1),(2,1+d))
photon_propagator(ax,(0,-1),(2,-1-d))

ax.text(-2, 1+d, r"$e^-$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(-2, -1-d, r"$e^+$",color='k',fontsize=30,va='top',ha='right')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='left')

arrow_momentum(ax,(0,1),(0,-1),b1=0.2,b2=0.2,h=0.15)
ax.text(0.2, 0, r"$p_1-p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,h=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,h=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_05", bbox_inches='tight')
plt.close(fig)


# Example 6
# e+e- to gamma gamma' u-channel

fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


d=0.5
h=0.2
c=0.3

fermion_propagator(ax,(-2,1+d),(0,-1))
fermion_propagator(ax,(0,-1),(0,1))
fermion_propagator(ax,(0,1),(-2,-1-d))
photon_propagator(ax,(0,1),(2,1+d))
photon_propagator(ax,(0,-1),(2,-1-d))

ax.text(-2, 1+d, r"$e^-$",color='k',fontsize=30,va='bottom',ha='right')
ax.text(-2, -1-d, r"$e^+$",color='k',fontsize=30,va='top',ha='right')
ax.text(2, 1+d, r"$\gamma \ '$",color='k',fontsize=30,va='bottom',ha='left')
ax.text(2, -1-d, r"$\gamma$",color='k',fontsize=30,va='top',ha='left')

arrow_momentum(ax,(0,-1),(0,1),b1=0.2,b2=0.2,h=0.15)
ax.text(0.2, 0, r"$p_1-p_4$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,-1),b1=0.15,b2=0.6,h=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(-2,-1-d),(0,1),b1=0.15,b2=0.6,h=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='left')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,h=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,h=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_06", bbox_inches='tight')
plt.close(fig)



# Example 7
# fermion self-energy
fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


fermion_propagator(ax,(-1.5,0),(-0.5,0))
fermion_propagator(ax,(-0.5,0),(0.5,0))
fermion_propagator(ax,(0.5,0),(1.5,0))
photon_arc(ax,(-0.5,0),(0.5,0))

fig.savefig("examples/example_07", bbox_inches='tight')
plt.close(fig)


# Example 8
# initial-final to dark photon
fig = plt.figure(figsize=(6,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),b=0.03)
ax.text(1.5, -0.4, r"$k$",color='k',fontsize=20,va='top',ha='center')

ax.text(-0.7, -0.8, r"$i$",color='k',fontsize=20,va='top',ha='left')
ax.text(-0.7, 0.8, r"$f$",color='k',fontsize=20,va='bottom',ha='left')
ax.text(0.75, 0.2, r"$A^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(2.25, 0.2, r"$V^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(1.5, 0.2, r"$\kappa$",color='k',fontsize=20,va='bottom',ha='center')

fig.savefig("examples/example_08", bbox_inches='tight')
plt.close(fig)



# Example 9
# initial-final to dark photon

fig = plt.figure(figsize=(6,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),b=0.03)
ax.text(1.5, -0.4, r"$\omega,k$",color='k',fontsize=20,va='top',ha='center')

ax.text(-0.7, -0.8, r"initial",color='k',fontsize=20,va='top',ha='left')
ax.text(-0.7, 0.8, r"final",color='k',fontsize=20,va='bottom',ha='left')
ax.text(0.75, 0.3, r"$A^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0.75, 0.2, r"(virtual photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(2.25, 0.3, r"$V^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(2.25, 0.2, r"(dark photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(1.5, 0.2, r"$\kappa$",color='k',fontsize=20,va='bottom',ha='center')

fig.savefig("examples/example_09", bbox_inches='tight')
plt.close(fig)


# Example 10
# initial-final to dark photon for CRAQ 2 (circled)
fig = plt.figure(figsize=(6,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),b=0.03)
ax.text(1.5, -0.4, r"$\omega,k$",color='k',fontsize=20,va='top',ha='center')

ax.text(-0.7, -0.8, r"initial",color='k',fontsize=20,va='top',ha='left')
ax.text(-0.7, 0.8, r"final",color='k',fontsize=20,va='bottom',ha='left')
ax.text(0.75, 0.3, r"$A^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0.75, 0.2, r"(virtual photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(2.25, 0.3, r"$V^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(2.25, 0.2, r"(dark photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(1.5, 0.2, r"$\kappa$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(1.75, 0.6, r"$\kappa_\mathrm{eff}$",color='purple',fontsize=20,va='bottom',ha='center')
ax.add_patch(mpatches.Circle((0.95,0.2),0.75,fill=False,ls='--',ec='purple'))

fig.savefig("examples/example_10", bbox_inches='tight')
plt.close(fig)


# Example 11
# Self-energy photon
fig = plt.figure(figsize=(6,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


r=0.7
photon_propagator(ax,(-r-1.5,0),(-r,0))
photon_propagator(ax,(r,0),(r+1.5,0))
fermion_loop(ax,(0,0),r)

ax.text(-r-0.7, 0.15, r"$k$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(r+0.7, 0.15, r"$k$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0, r+0.15, r"$p$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0, -r-0.15, r"$p+k$",color='k',fontsize=20,va='top',ha='center')
ax.text(-r-1.6, -0.1, r"$\mu$",color='k',fontsize=15,va='top',ha='center')
ax.text(r+1.6, -0.1, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_11", bbox_inches='tight')
plt.close(fig)


# Example 12
# Self-energy photon BIS
fig = plt.figure(figsize=(2,1), dpi=600)
ax = fig.subplots()
init_ax(ax)


r=0.7
photon_propagator(ax,(-r-1.5,0),(-r,0))
photon_propagator(ax,(r,0),(r+1.5,0))
fermion_loop(ax,(0,0),r)

fs,fs2 = 10,7
ax.text(-r-0.7, 0.15, r"$K$",color='k',fontsize=fs,va='bottom',ha='center')
ax.text(r+0.7, 0.15, r"$K$",color='k',fontsize=fs,va='bottom',ha='center')
ax.text(0, r+0.15, r"$P$",color='k',fontsize=fs,va='bottom',ha='center')
ax.text(0, -r-0.15, r"$P+K$",color='k',fontsize=fs,va='top',ha='center')
ax.text(-r-1.6, -0.1, r"$\mu$",color='k',fontsize=fs2,va='top',ha='center')
ax.text(r+1.6, -0.1, r"$\nu$",color='k',fontsize=fs2,va='top',ha='center')

fig.savefig("examples/example_12", bbox_inches='tight')
plt.close(fig)


# Example 13
# Self-energy scalar
fig = plt.figure(figsize=(6,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)


r=0.7
scalar_propagator(ax,[-r-1.5,0], [-r,0], color='k', lw=1)
scalar_propagator(ax,[r,0], [r+1.5,0], color='k', lw=1)
fermion_loop(ax,(0,0),r,phase=np.pi)

ax.text(-r-0.7, 0.15, r"$\Phi$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(r+0.7, 0.15, r"$\Phi$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0, r+0.15, r"$\phi_1$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0, -r+0.15, r"$\phi_2$",color='k',fontsize=20,va='bottom',ha='center')

ax.text(-r-0.7, -0.15, r"$i\omega_\ell, \vec{k}$",color='k',fontsize=15,va='top',ha='center')
ax.text(r+0.7, -0.15, r"$i\omega_\ell, \vec{k}$",color='k',fontsize=15,va='top',ha='center')
ax.text(0, r-0.15, r"$i\omega_n, \vec{p}$",color='k',fontsize=15,va='top',ha='center')
ax.text(0, -r-0.15, r"$i\omega_n-i\omega_\ell, \vec{p} - \vec{k}$",color='k',fontsize=15,va='top',ha='center')

fig.savefig("examples/example_13", bbox_inches='tight')
plt.close(fig)

"""
# Example 14
# tests
fig = plt.figure(figsize=(8,3.5), dpi=600)
ax = fig.subplots()
init_ax(ax)



fermion_propagator(ax,(-5,-1),(-4,-1))
fermion_arc(ax,(-4,-1),(-3,-1),clockwise=True)
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
oscillation_x(ax,(1.5,0),0.1,5)
blob(ax,(0,0),0.2)

fermion_loop(ax,(3.5,0),0.5,nF=3,phase=np.pi/2)
gluon_propagator(ax,rotate((3.5,0),np.pi/3,3.5+0.5,0),rotate((3.5,0),np.pi/3,3.5+1.35,0))
scalar_propagator(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0))
arrow_momentum(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0),h=0.2)

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.03)

gluon_loop(ax,rotate((3.5,0),np.pi/3,3.5+1.35+0.6,0),0.5,w=14)

fig.savefig("examples/example_14", bbox_inches='tight')
plt.close(fig)

