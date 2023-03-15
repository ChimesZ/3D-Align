import numpy as np
import pandas as pd
# import open3d as o3
import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib as mpl
import time

orgnizer = pd.read_csv('/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/After_Align_R/green/data_organize.csv')

size = 200
fig = plt.figure(figsize=(8,8))
ax3 = plt.axes(projection='3d')
#Type C
ax3.scatter(orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['x'],
        orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['z'],
        c='seagreen',
        s=size,
        edgecolors='black'
        )
# Type D
ax3.scatter(orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['x'],
        orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['z'],
        c='indianred',
        s=size,
        edgecolors='black',
        plotnonfinite=True
        )
#type A 
ax3.scatter(orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['x'],
        orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==1)]['z'],
        c='steelblue',
        s=size,
        edgecolors='black'
        ) # source
#Type B
ax3.scatter(orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['x'],
        orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['z'],
        c='mediumpurple',
        s=size,
        edgecolors='black'
        ) # source
ax3.scatter(orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==0)]['x'],
        orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==0)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==1)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==0)]['z'],
        c='gray',
        s=size,
        edgecolors='black',
        alpha=0.2
        ) # source
ax3.scatter(orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['x'],
        orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==1)&(orgnizer['2nd recall']==0)]['z'],
        c='gray',
        s=size,
        edgecolors='black',
        alpha=0.2
        )
ax3.scatter(orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['x'],
        orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['y'],
        -3*orgnizer[(orgnizer['1st recall']==0)&(orgnizer['1st TR']==0)&(orgnizer['2nd recall']==1)]['z'],
        c='gray',
        s=size,
        edgecolors='black',
        alpha=0.2
        )
y_unique = [0,1,2,3,4]
color = ['steelblue','mediumpurple','seagreen','indianred','gray']
label = ['Type A cells','Type B cells','Type C cells','Type D cells','Noise cells']
legend_lines = [mpl.lines.Line2D([0], [0], linestyle="none", marker='o', c=color[y]) for y in y_unique]
legend_labels = [label[y] for y in y_unique]
ax3.legend(legend_lines, legend_labels, numpoints=1, title='Method',loc='upper right')
plt.title('merged')
ax3.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.set_xlabel('X(µm)')
ax3.set_ylabel('Y(µm)')
ax3.set_zlabel('Z(µm)')
plt.grid(True)
fig.savefig('/Users/apple/YiLab/Raw_Data/System Reconsolidation/Figure/'+f'{time.time()}.svg',format='svg',dpi=150)
plt.show()
