import numpy as np
import pandas as pd
# import open3d as o3
import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib as mpl
import time


def scatter_3d(trial_1, trial_2, orgnizer,size = 100,edgecolor = 'black',save = False):
    fig = plt.figure(figsize=(30,10))
    ax1 = fig.add_subplot(131,projection='3d')
    ax1.scatter(orgnizer[orgnizer[trial_1]==1]['x'],
               orgnizer[orgnizer[trial_1]==1]['y'],
               -orgnizer[orgnizer[trial_1]==1]['z'],
               c='red',
               s=size,
               edgecolors=edgecolor) # source
    plt.title('1st image cells')
    ax2 = fig.add_subplot(132,projection='3d')
    ax2.scatter(orgnizer[orgnizer[trial_2]==1]['x'],
               orgnizer[orgnizer[trial_2]==1]['y'],
               -orgnizer[orgnizer[trial_2]==1]['z'],
               c='green',
               s=size,
               edgecolors=edgecolor) # source
    plt.title('2nd image cells')
    ax3 = fig.add_subplot(133,projection='3d')
    ax3.scatter(orgnizer[(orgnizer[trial_2]==0)&(orgnizer[trial_1]==1)]['x'],
               orgnizer[(orgnizer[trial_2]==0)&(orgnizer[trial_1]==1)]['y'],
               -orgnizer[(orgnizer[trial_2]==0)&(orgnizer[trial_1]==1)]['z'],
               c='red',
               s=size,
               edgecolors=edgecolor)
    ax3.scatter(orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==0)]['x'],
               orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==0)]['y'],
               -orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==0)]['z'],
               c='green',
               s=size,
               edgecolors=edgecolor)
    ax3.scatter(orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==1)]['x'],
               orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==1)]['y'],
               -orgnizer[(orgnizer[trial_2]==1)&(orgnizer[trial_1]==1)]['z'],
               c='yellow',
               s=size,
               edgecolors=edgecolor) # source
    y_unique = [0,1,2]
    color = ['red','green','yellow']
    label = [trial_1 + " cells",trial_2 + " cells",'Co-expressed cells']
    legend_lines = [mpl.lines.Line2D([0], [0], linestyle="none", marker='o', c=color[y]) for y in y_unique]
    legend_labels = [label[y] for y in y_unique]
    ax3.legend(legend_lines, legend_labels, numpoints=1, title='Method',loc='upper right')
    
    plt.title('merged')
    ax1.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.set_xlabel('X(µm)')
    ax1.set_ylabel('Y(µm)')
    ax1.set_zlabel('Z(µm)')
    ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.set_xlabel('X(µm)')
    ax2.set_ylabel('Y(µm)')
    ax2.set_zlabel('Z(µm)')
    ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax3.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax3.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax3.set_xlabel('X(µm)')
    ax3.set_ylabel('Y(µm)')
    ax3.set_zlabel('Z(µm)')
    plt.grid(True)
    plt.show()
    if save:
        fig.savefig('/Users/apple/YiLab/Raw_Data/System Reconsolidation/Figure/'+f'{trial_1 + " and " + trial_2}.svg',format='svg',dpi=150)


if __name__ == '__main__':
    orgnizer = pd.read_csv('/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/After_Align_R/green/data_organize.csv')
    scatter_3d('1st TR','1st recall',orgnizer,save = True)