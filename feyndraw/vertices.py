import numpy as np
import matplotlib.patches as mpatches

### Blob ###

# Blow at center c and radius r
def blob(ax,c,r=0.2):
	ax.add_patch(mpatches.Circle(c,r,
   		fill=True,hatch='\\\\\\\\',fc='0.8',ec='0',zorder=6))

### Oscillation ###

# X for oscillation at center c, width/height b, linewidth lw
def oscillation_x(ax,c,b=0.1,lw=5):
	cx, cy = c
	ax.plot([cx-b,cx+b], [cy-b,cy+b], color='k', lw=lw)
	ax.plot([cx-b,cx+b], [cy+b,cy-b], color='k', lw=lw)