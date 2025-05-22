"""
feyndraw
Author: Hugo Schérer
Version 1.0
2024-06-01
"""

import matplotlib.pyplot as plt
from .geometry import find_angle, find_length, find_center, rotate
from .basicdraw import arrow_triangle,arrow,arrow_momentum,arrow_momentum_arc
from .propagators import line_propagator,scalar_propagator,fermion_propagator,photon_propagator,gluon_propagator
from .loops import scalar_loop,fermion_loop,gluon_loop,scalar_arc,fermion_arc,photon_arc,gluon_arc
from .vertices import blob,oscillation_x

def init_ax(ax):
	ax.axis("off")
	ax.set_aspect('equal', adjustable='box')

def init_fig_ax(figsize,dpi):
	fig = plt.figure(figsize=figsize, dpi=dpi)
	ax = fig.subplots()
	init_ax(ax)
	return fig,ax

__all__ = [
			"init_ax",
			"init_fig_ax",
			"find_angle",
			"find_length",
			"find_center",
			"rotate",
			"arrow_triangle",
			"arrow",
			"arrow_momentum",
			"arrow_momentum_arc",
			"line_propagator",
			"scalar_propagator",
			"fermion_propagator",
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