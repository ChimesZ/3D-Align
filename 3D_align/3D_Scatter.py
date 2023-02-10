import numpy as np
import pandas as pd
# import open3d as o3
import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib as mpl

def eucliDist(a,b):
    return math.sqrt(math.sqrt(sum([(a - b)**2 for (a,b) in zip(a,b)])))

def get_coordinate(path):
    data = np.load(path,allow_pickle=True)
    centers = []
    for cell in data:
        center = cell['center']
        centers.append(center)
    centers = np.asarray(centers)
    type(centers)
    x,y,z = centers[:,0], centers[:,1],centers[:,2]
    return x,y,z

if __name__ == '__main__':
    path_ref = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/68 1st TR 0004 green.npy'
    path_1 = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/68 2nd TR 0004 green registered.npy'
    x,y,z = get_coordinate(path_ref)
    orgnizer = pd.DataFrame(zip(x,y,z))
    orgnizer.columns = list('xyz')
    orgnizer['1st TR'] = 1

    x,y,z = get_coordinate(path_1)

    orgnizer_len = len(orgnizer)
    orgnizer['2nd TR'] = 0
    for i in range(len(x)):
        coordinate_new = [x[i],y[i],z[i]]
        mark = 1
        for j in range(orgnizer_len):
            coordinate = list(orgnizer.iloc[j])
            coordinate = coordinate[0:3]
            if eucliDist(coordinate,coordinate_new) < 3:
                orgnizer['2nd TR'][j] = 1
                mark = 0
                break
        if mark:
            orgnizer.loc[len(orgnizer.index)] = [x[i],y[i],z[i],0,1]
    size = 100

    fig = plt.figure(figsize=(30,10))
    ax1 = fig.add_subplot(131,projection='3d')
    ax1.scatter(orgnizer[orgnizer['1st TR']==1]['x'],
            orgnizer[orgnizer['1st TR']==1]['y'],
            -3*orgnizer[orgnizer['1st TR']==1]['z'],
            c='red',
            s=size,
            edgecolors='black'
            ) # source
    ax1.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.set_xlabel('X(µm)')
    ax1.set_ylabel('Y(µm)')
    ax1.set_zlabel('Z(µm)')
    plt.title('1st image cells')

    ax2 = fig.add_subplot(132,projection='3d')
    ax2.scatter(orgnizer[orgnizer['2nd TR']==1]['x'],
            orgnizer[orgnizer['2nd TR']==1]['y'],
            -3*orgnizer[orgnizer['2nd TR']==1]['z'],
            c='green',
            s=size,
            edgecolors='black'
            ) # source
    plt.title('2nd image cells')
    ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax2.set_xlabel('X(µm)')
    ax2.set_ylabel('Y(µm)')
    ax2.set_zlabel('Z(µm)')
    ax3 = fig.add_subplot(133,projection='3d')
    ax3.scatter(orgnizer[(orgnizer['2nd TR']==0)&(orgnizer['1st TR']==1)]['x'],
            orgnizer[(orgnizer['2nd TR']==0)&(orgnizer['1st TR']==1)]['y'],
            -3*orgnizer[(orgnizer['2nd TR']==0)&(orgnizer['1st TR']==1)]['z'],
            c='red',
            s=size,
            edgecolors='black'
            )
    ax3.scatter(orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==0)]['x'],
            orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==0)]['y'],
            -3*orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==0)]['z'],
            c='green',
            s=size,
            edgecolors='black'
            )
    ax3.scatter(orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==1)]['x'],
            orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==1)]['y'],
            -3*orgnizer[(orgnizer['2nd TR']==1)&(orgnizer['1st TR']==1)]['z'],
            c='yellow',
            s=size,
            edgecolors='black'
            ) # source
    y = 3
    y_unique = [0,1,2]
    color = ['red','green','yellow']
    label = ['1st image only cells','2nd image only cells','Co-expressed cells']
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
    fig.savefig('/Users/apple/YiLab/Resoursces/3D Align/sample/'+'sample.svg',format='svg',dpi=150)
    plt.show()