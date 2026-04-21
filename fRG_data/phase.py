#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
#from scipy.interpolate import spline
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties
import pylab as pl

mpl.style.use('classic')
# Data for plotting
r42data=np.loadtxt('./fitr42.dat')
Tdata=np.loadtxt('./fitT.dat')
mubdata=np.loadtxt('./FOmubfit.dat')
FOT=np.loadtxt('./FOTfit.dat')
FOT2=np.loadtxt('./FOT2fit.dat')
FOT3=np.loadtxt('./FOT3fit.dat')
expdata=np.loadtxt('./andronic-origin.dat')
stardata=np.loadtxt('./stardata.dat')
background=np.zeros([2101,3201])
# Create figure
fig=plt.figure(figsize=(4.56, 3))
#fig=plt.figure()
####################################################################################################
# Create figure
#fig=plt.figure()
ax2=fig.add_subplot(111)
im=ax2.imshow(r42data, cmap=plt.get_cmap('seismic'),interpolation='nearest',vmin=-10,vmax=10,zorder=2)#plt.cm.hot_r)
vnorm = mpl.colors.Normalize(vmin=-10, vmax=10)
plt.rcParams['font.size'] = 7
cbar=plt.colorbar(im,fraction=0.031, pad=0.04,norm=vnorm)
cbar.set_label(r'$R^B_{42}$', rotation=0,fontsize=9)
im2=ax2.imshow(background-2, cmap=plt.get_cmap('binary'),interpolation='nearest',vmin=-10,vmax=10,zorder=1)#plt.cm.hot_r)
ax2.invert_yaxis()
plt.scatter(643*4,98*10-400,color='lime',marker='*',s=40,label=r'CEP',zorder=3)
star7,=ax2.plot(mubdata,FOT2*10-400,dashes=[4,1,2,1],color='b',linewidth=1.5,alpha=0.9,label=r'freezeout: STAR Fit I',zorder=3)
star4,=ax2.plot(mubdata,FOT*10-400,dashes=[5,2],color='g',linewidth=1.5,alpha=0.9,label=r'freezeout: STAR Fit II',zorder=4)
And,=ax2.plot(mubdata,FOT3*10-400,color='r',linewidth=1.5,alpha=0.9,label=r'freezeout: Andronic et al.',zorder=3)
plt.axis([0.,3200.,0.,2100.])
plt.yticks([100,600,1100,1600,2100],[50,100,150,200,250])
plt.xticks([0,400,800,1200,1600,2000,2400,2800,3200],[0,100,200,300,400,500,600,700,800])
ax2.set_xlabel('$\mu_B\,[\mathrm{MeV}]$', fontsize=10, color='black')
ax2.set_ylabel(r'$T\,[\mathrm{MeV}]$', fontsize=10, color='black')
#ax1.set_title(r'$R^B_{42}$',loc='right')
for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(8)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(8)

ax2.legend(loc=0,fontsize=6,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

fig.subplots_adjust(top=0.85, bottom=0.15, left=-0.85, right=0.94, hspace=0.1,
                    wspace=0.1)


fig.savefig("phasediagram2.pdf",dpi=300,transparent=True)
