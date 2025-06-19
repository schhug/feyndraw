import numpy as np
import matplotlib.patches as mpatches
from .geometry import rotate

### Blob ###

# Blow at center c and radius r
def blob(ax,c,r=0.2,lw=1):
	ax.add_patch(mpatches.Circle(c,r,fill=True,hatch='\\\\\\\\',fc='0.8',ec='0',zorder=6,lw=lw))

### Oscillation ###

# X for oscillation at center c, width/height b, linewidth lw
def oscillation_x(ax,c,b=0.1,lw=5,color='k',theta=0):
	cx, cy = c
	pt1 = rotate(c,theta,cx-b,cy-b)
	pt2 = rotate(c,theta,cx+b,cy+b)
	pt3 = rotate(c,theta,cx-b,cy+b)
	pt4 = rotate(c,theta,cx+b,cy-b)

	ax.plot([pt1[0],pt2[0]], [pt1[1],pt2[1]], color=color, lw=lw ,zorder=60)
	ax.plot([pt3[0],pt4[0]], [pt3[1],pt4[1]], color=color, lw=lw ,zorder=60)
	#ax.plot([cx-b,cx+b], [cy-b,cy+b], color=color, lw=lw)
	#ax.plot([cx-b,cx+b], [cy+b,cy-b], color=color, lw=lw)