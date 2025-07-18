import numpy as np
import matplotlib.pyplot as plt
from .geometry import find_angle, find_length, find_center, rotate
from .basicdraw import arrow_triangle,arrow,arrow_momentum,arrow_momentum_arc,line
from .propagators import line_propagator,scalar_propagator,fermion_propagator,antifermion_propagator,photon_propagator,gluon_propagator
from .loops import scalar_loop,fermion_loop,gluon_loop,scalar_arc,fermion_arc,photon_arc,gluon_arc
from .vertices import blob,oscillation_x

def info():
	title = "feyndraw"
	version = "1.1"
	author = "Hugo Schérer"
	date = "2025-07-18"
	doi = "https://doi.org/10.5281/zenodo.16100536"
	print(f"Package: {title} v{version} (released {date})\nAuthor: {author}\nTo cite this work: {doi}")

def init_ax(ax):
	ax.axis("off")
	ax.set_aspect('equal', adjustable='box')
	ax.plot(0,0,'ro',alpha=0)  # Add a dummy point to avoid bugs from no data in the plot

def init_fig_ax(*args, **kwargs):
	fig = plt.figure(*args, **kwargs)
	ax = fig.subplots()
	init_ax(ax)
	return fig,ax

def show_grid(ax, color='0.8', lw=0.5, ls='-', zorder=-100):
    ax.axis("on")
    ax.grid(which='major', color=color, ls=ls, lw=lw)
    for axis in [ax.xaxis, ax.yaxis]: axis.set_zorder(zorder)
    ax.tick_params(axis='both', colors=color, width=lw, zorder=zorder, bottom=True, top=True, left=True, right=True, labelbottom=True, labeltop=True, labelleft=True, labelright=True)
    ax.set_frame_on(False)

__all__ = [
			"info",
			"init_ax",
			"init_fig_ax",
			"show_grid",
			"find_angle",
			"find_length",
			"find_center",
			"rotate",
			"arrow_triangle",
			"arrow",
			"arrow_momentum",
			"arrow_momentum_arc",
			"line",
			"line_propagator",
			"scalar_propagator",
			"fermion_propagator",
			"antifermion_propagator",
			"photon_propagator",
			"gluon_propagator",
			"scalar_loop",
			"fermion_loop",
			"gluon_loop",
			"scalar_arc",
			"fermion_arc",
			"photon_arc",
			"gluon_arc",
			"blob",
			"oscillation_x"
		]
