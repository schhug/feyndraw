import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import use, rc
from feyndraw import *

use('agg')
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'serif','serif':['Times']})
rc('text',usetex=True)

info()

i=0

# e- gamma to gamma' e- t-channel
i+=1
fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)

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

arrow_momentum(ax,(0,1),(0,-1),b1=0.2,b2=0.2,hp=0.15)
ax.text(0.2, 0, r"$p_1-p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,hp=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,hp=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)




# e- gamma to gamma' e- s-channel

i+=1

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

arrow_momentum(ax,(-1,0),(1,0),b1=0.2,b2=0.2,hp=0.15)
ax.text(0, 0.2, r"$p_1+p_2$",color='k',fontsize=20,va='bottom',ha='center')

arrow_momentum(ax,(-2,1+d),(-1,0),b1=0.2,b2=0.2,hp=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(-1,0),b1=0.2,b2=0.2,hp=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(1,0),(2,1+d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(1,0),(2,-1-d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(1.2, 0, r"$\mu$",color='k',fontsize=15,va='center',ha='left')
ax.text(-1.2, 0, r"$\nu$",color='k',fontsize=15,va='center',ha='right')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# e+ gamma to gamma' e+ t-channel
i+=1
fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


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

arrow_momentum(ax,(0,-1),(0,1),b1=0.2,b2=0.2,hp=-0.15)
ax.text(0.2, 0, r"$-p_1+p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,hp=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,hp=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)




# e+ gamma to gamma' e+ s-channel
i+=1

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


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

arrow_momentum(ax,(1,0),(-1,0),b1=0.2,b2=0.2,hp=-0.15)
ax.text(0, 0.2, r"$-p_1-p_2$",color='k',fontsize=20,va='bottom',ha='center')

arrow_momentum(ax,(-2,1+d),(-1,0),b1=0.2,b2=0.2,hp=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(-1,0),b1=0.2,b2=0.2,hp=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(1,0),(2,1+d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(1,0),(2,-1-d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(1.2, 0, r"$\mu$",color='k',fontsize=15,va='center',ha='left')
ax.text(-1.2, 0, r"$\nu$",color='k',fontsize=15,va='center',ha='right')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# e+e- to gamma gamma' t-channel

i+=1

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


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

arrow_momentum(ax,(0,1),(0,-1),b1=0.2,b2=0.2,hp=0.15)
ax.text(0.2, 0, r"$p_1-p_3$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,1),b1=0.2,b2=0.2,hp=-0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='right')

arrow_momentum(ax,(-2,-1-d),(0,-1),b1=0.2,b2=0.2,hp=0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='right')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# e+e- to gamma gamma' u-channel
i+=1

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


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

arrow_momentum(ax,(0,-1),(0,1),b1=0.2,b2=0.2,hp=0.15)
ax.text(0.2, 0, r"$p_1-p_4$",color='k',fontsize=20,va='center',ha='left')

arrow_momentum(ax,(-2,1+d),(0,-1),b1=0.15,b2=0.6,hp=0.15)
ax.text(-1, (1+d)/2, r"$p_1$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(-2,-1-d),(0,1),b1=0.15,b2=0.6,hp=-0.15)
ax.text(-1, -(1+d)/2, r"$p_2$",color='k',fontsize=20,va='top',ha='left')

arrow_momentum(ax,(0,1),(2,1+d),b1=0.2,b2=0.2,hp=-0.15)
ax.text(1, (1+d)/2, r"$p_3$",color='k',fontsize=20,va='bottom',ha='left')

arrow_momentum(ax,(0,-1),(2,-1-d),b1=0.2,b2=0.2,hp=0.15)
ax.text(1, -(1+d)/2, r"$p_4$",color='k',fontsize=20,va='top',ha='left')

ax.text(0, 1.2, r"$\mu$",color='k',fontsize=15,va='bottom',ha='center')
ax.text(0, -1.2, r"$\nu$",color='k',fontsize=15,va='top',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)




# fermion self-energy
i+=1

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


fermion_propagator(ax,(-1.5,0),(-0.5,0))
fermion_propagator(ax,(-0.5,0),(0.5,0))
fermion_propagator(ax,(0.5,0),(1.5,0))
photon_arc(ax,(-0.5,0),(0.5,0))

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)


# fermion self-energy re-summed
i+=1

fig,ax = init_fig_ax(figsize=(8,3.5), dpi=600)


fermion_propagator(ax,(-1.5,0),(-0.5,0),double=True)
fermion_propagator(ax,(-0.5,0),(0.5,0),double=True)
fermion_propagator(ax,(0.5,0),(1.5,0),double=True)
photon_arc(ax,(-0.5,0),(0.5,0),double=True,clockwise=True)

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)


# initial-final to dark photon
i+=1

fig,ax = init_fig_ax(figsize=(6,3.5), dpi=600)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.03)
ax.text(1.5, -0.4, r"$k$",color='k',fontsize=20,va='top',ha='center')

ax.text(-0.7, -0.8, r"$i$",color='k',fontsize=20,va='top',ha='left')
ax.text(-0.7, 0.8, r"$f$",color='k',fontsize=20,va='bottom',ha='left')
ax.text(0.75, 0.2, r"$A^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(2.25, 0.2, r"$V^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(1.5, 0.2, r"$\kappa$",color='k',fontsize=20,va='bottom',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)




# initial-final to dark photon
i+=1

fig,ax = init_fig_ax(figsize=(6,3.5), dpi=600)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.06)
ax.text(1.5, -0.4, r"$\omega,k$",color='k',fontsize=20,va='top',ha='center')

ax.text(-0.7, -0.8, r"initial",color='k',fontsize=20,va='top',ha='left')
ax.text(-0.7, 0.8, r"final",color='k',fontsize=20,va='bottom',ha='left')
ax.text(0.75, 0.3, r"$A^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(0.75, 0.2, r"(virtual photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(2.25, 0.3, r"$V^\mu$",color='k',fontsize=20,va='bottom',ha='center')
ax.text(2.25, 0.2, r"(dark photon)",color='k',fontsize=10,va='bottom',ha='center')
ax.text(1.5, 0.2, r"$\kappa$",color='k',fontsize=20,va='bottom',ha='center')

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# initial-final to dark photon for CRAQ 2 (circled)
i+=1
fig,ax = init_fig_ax(figsize=(6,3.5), dpi=600)


photon_propagator(ax,(0,0),(3,0))
fermion_propagator(ax,(-1,-1),(0,0))
fermion_propagator(ax,(0,0),(-1,1))
oscillation_x(ax,(1.5,0))
blob(ax,(0,0))

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.06)
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

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)


# Self-energy photon
i+=1
fig,ax = init_fig_ax(figsize=(6,3.5), dpi=600)


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

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# Self-energy photon BIS
i+=1
fig,ax = init_fig_ax(figsize=(2,1), dpi=600)


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

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)



# Self-energy scalar
i+=1
fig,ax = init_fig_ax(figsize=(6,3.5), dpi=600)


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

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)

# 2 to 2 with grid
i+=1
def plot_small_fermions(process, p = ['f','s','f','f','b']):
    def my_photon_propagator(ax, pt1, pt2, **kwargs):
        photon_propagator(ax, pt1, pt2,h=0.09,w=8, **kwargs)
    propagator = { 'f': fermion_propagator, 'fb': antifermion_propagator, 's': scalar_propagator, 'b': my_photon_propagator }

    fig,ax = init_fig_ax(figsize=(0.7,0.7), dpi=500)

    if process == '2to2s' or process == '2to2t':
        mandel = process[-1]
        dx,dy = 1,1
        pt1,pt2,pt3,pt4 = [-dx,dy],[-dx,-dy],[dx,dy],[dx,-dy]

        if mandel == 's':
            ds = 0.5
            pp1,pp2 = [-ds,0],[ds,0]
            pt1a,pt2a,pt3a,pt4a = pp1,pp1,pp2,pp2

        elif mandel == 't':
            dt = 0.5
            pp1,pp2 = [0,dt],[0,-dt]
            pt1a,pt2a,pt3a,pt4a = pp1,pp2,pp1,pp2

    elif process == '1to3' or process == '3to1' or process == '3to1f':
        dx1 = 1
        dx,dy = 0.7,0.7

        pt1,pt2,pt3,pt4 = [-dx1,0],[2*dx,2*dy],[2*dx,0],[2*dx,-2*dy]
        pp1,pp2 = [0,0],[dx,dy]
        pt1a,pt2a,pt3a,pt4a = pp1,pp2,pp2,pp1

        if process == '3to1':
            pt1,pt2,pt3,pt4     = pt2 ,pt3 ,pt4 ,pt1
            pt1a,pt2a,pt3a,pt4a = pt2a,pt3a,pt4a,pt1a
            for pt in [pp1,pp2,pt1,pt2,pt3,pt4,pt1a,pt2a,pt3a,pt4a]:
                pt[0] = -pt[0]

        if process == '3to1f':
            pt1,pt2,pt3,pt4     = pt4 ,pt3 ,pt2 ,pt1
            pt1a,pt2a,pt3a,pt4a = pt4a,pt3a,pt2a,pt1a
            for pt in [pp1,pp2,pt1,pt2,pt3,pt4,pt1a,pt2a,pt3a,pt4a]:
                pt[0],pt[1] = -pt[0],-pt[1]

    elif process == '4to0':
        dx,dy = 1.1,0.2
        dt = 0.4

        pt1,pt2,pt3,pt4 = [-dx,dt+dy],[-dx,dt-dy],[-dx,-dt+dy],[-dx,-dt-dy]
        pp1,pp2 = [0,dt],[0,-dt]
        pt1a,pt2a,pt3a,pt4a = pp1,pp1,pp2,pp2

    show_grid(ax)

    propagator[p[0]](ax,pp1,pp2) # prop
    propagator[p[1]](ax,pt1,pt1a) # particle 1
    propagator[p[2]](ax,pt2,pt2a) # particle 2
    propagator[p[3]](ax,pt3a,pt3) # particle 3
    propagator[p[4]](ax,pt4a,pt4) # particle 4

    fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
    plt.close(fig)

plot_small_fermions('2to2t', p = ['fb','s','b','f','fb'])


# Interference diagrams
def plot_small_intf_term(ax,spec,cx=0):
    color_asym = "#FB9E3A"
    r=0.35
    theta_cut = 0
    text_fs = 12
    text_fs2 = 9
    lw = 1.3

    cut_r,d = 0.5,0.1
    cut_ls,cut_lw = '--',1.5
    color_spec = 'orange'
    color_spec = color_asym

    if spec == 'fermion':
        spec_propagator = fermion_propagator
        anti_spec_propagator = photon_propagator
        spec_text = r"$f$"
    elif spec == 'photon':
        spec_propagator = photon_propagator
        anti_spec_propagator = fermion_propagator
        spec_text = r"$\gamma$"

    # o-cross
    r = 0.07
    fermion_loop(ax,(cx,0),r=2*r,nF=0,phase=0,color='k',lw=1) #abuse of fermion_loop to draw a circle
    oscillation_x(ax,(cx,0),b=1.1*r,lw=1.5) #abuse of oscillation_x to draw ax


    b = 0.45 #spacing between the two sides
    a = 0.8 #vertical spacing
    dy = 0.65
    dx = 0.65
    dL = 0.55

    # Left side
    pt1L = np.array([-dx-dL-b+cx,-a+dL])
    pt2L = pt1L + [dx,0]
    pt3L = pt2L + [dL,+dL]
    pt4L = pt2L + [dL,-dL]
    ptS1L = pt1L + [0,2*a-dL]
    ptS2L = ptS1L + [dx+dL-0.1,0]

    photon_propagator(ax,pt2L,pt1L,lw=lw)
    fermion_propagator(ax,pt2L,pt3L,lw=lw)
    fermion_propagator(ax,pt4L,pt2L,lw=lw)

    ax.text(pt1L[0]+0.3, pt1L[1]+0.1, r"$A'$",color='k',fontsize=text_fs,va='bottom',ha='center')
    ax.text(pt4L[0]+0.05, pt4L[1], r"$f$",color='k',fontsize=text_fs,va='center',ha='left')
    ax.text(pt3L[0]+0.05, pt3L[1], r"$f$",color='k',fontsize=text_fs,va='center',ha='left')

    spec_propagator(ax,ptS1L,ptS2L,lw=lw,color=color_spec)
    ax.text((ptS1L[0]+ptS2L[0])/2, (ptS1L[1]+ptS2L[1])/2+0.15, spec_text, color=color_spec,fontsize=text_fs,va='bottom',ha='center')


    # Right side
    pt1R  = np.array([b+cx,-dy])
    pt2R  = pt1R  + [dx,0]
    pt4R  = pt2R  + [dx,0]
    pt2aR = pt2R  + [0,dy]
    pt2bR = pt2aR + [0,dy]
    pt3R  = pt2bR + [dx,0]
    ptS1R = pt2bR + [-dx,0]
    ptS2R = pt2aR + [dx,0]

    photon_propagator(ax,pt1R,pt2R,lw=lw)
    fermion_propagator(ax,pt4R,pt2R,lw=lw)
    fermion_propagator(ax,pt2R,pt2aR,lw=lw)
    fermion_propagator(ax,pt2bR,pt3R,lw=lw)

    ax.text(pt1R[0], pt1R[1]+0.1, r"$A'$",color='k',fontsize=text_fs,va='bottom',ha='center')
    ax.text(pt4R[0]+0.05, pt4R[1], r"$f$",color='k',fontsize=text_fs,va='center',ha='left')
    ax.text(pt3R[0]+0.05, pt3R[1], r"$f$",color='k',fontsize=text_fs,va='center',ha='left')

    anti_spec_propagator(ax,pt2aR,pt2bR,lw=lw)
    spec_propagator(ax,ptS1R,pt2bR,lw=lw,color=color_spec)
    spec_propagator(ax,pt2aR,ptS2R,lw=lw,color=color_spec)
    ax.text(ptS1R[0], ptS1R[1]+0.1, spec_text, color=color_spec,fontsize=text_fs,va='bottom',ha='right')
    ax.text(ptS2R[0]+0.05, ptS2R[1], spec_text, color=color_spec,fontsize=text_fs,va='center',ha='left')

for spec in ['fermion','photon']:
    fig,ax = init_fig_ax(figsize=(2.5,3), dpi=300)
    plot_small_intf_term(ax,spec,cx=0)
    i+=1
    fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
    plt.close(fig)



# tests
i+=1
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
gluon_arc(ax,(-1.5,1),(-2.5,1),dr=0.0443)
arrow_momentum_arc(ax,(-2.5,1),(-1.5,1),0,clockwise=True)

photon_propagator(ax,(0,0),(3,0))
scalar_arc(ax,(2,0),(1,0),0.1)
oscillation_x(ax,(1.5,0),b=0.1)
blob(ax,(0,0),0.2)

fermion_loop(ax,(3.5,0),0.5,nF=3,phase=np.pi/2)
gluon_propagator(ax,rotate((3.5,0),np.pi/3,3.5+0.5,0),rotate((3.5,0),np.pi/3,3.5+1.35,0))
scalar_propagator(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0))
arrow_momentum(ax,rotate((3.5,0),-np.pi/3,3.5+0.5,0),rotate((3.5,0),-np.pi/3,3.5+2,0),hp=0.2)

arrow(ax,(0.3,-0.3),(2.6,-0.3),ba=0.03)

gluon_loop(ax,rotate((3.5,0),np.pi/3,3.5+1.35+0.6,0),r=0.5,w=14)

fig.savefig(f"examples/example_{i:0=2d}".format(i=i), bbox_inches='tight')
plt.close(fig)




