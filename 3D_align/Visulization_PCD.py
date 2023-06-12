import numpy as np
import open3d as o3
import pandas as pd
import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib as mpl

def pcd_3d_loader(path, color = [1, 0, 0],round=False):
    data = np.loadtxt(path)
    if round:
        data = np.round(data)
    pcd = o3.geometry.PointCloud()
    pcd.points = o3.utility.Vector3dVector(data)
    pcd.source.paint_uniform_color(color)
    return pcd

def downsample(pcd:np.array, rate = 0.7): 
    select = np.random.uniform(low=0,high=1,size=pcd.shape[0])
    

def pcd_3d_plt(pcds,colors,size=2,alpha=0.5):
    '''Plot `pcd` with pyplot
    ---
    param:
        pcds(list):
        colors(list):
        size(int):
        alpha(float):
    ---
    Returen:
        ax: 
    '''
    assert len(pcds) == len(colors)
    ax = plt.axes(projection='3d')
    for pcd,color in zip(pcds,colors): 
        ax.scatter(pcd[:,0],pcd[:,1],-pcd[:,2], 
                s=size,
                c = color)
    ax.set_zlim3d(-150,50)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_xlabel('X(µm)')
    ax.set_ylabel('Y(µm)')
    ax.set_zlabel('Z(µm)')
    return ax

if __name__ == '__main__':
    path1 = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/68 1st TR 0004 green.txt'
    path2 = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/68 2nd TR 0004 green registered.txt'
    path3 = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/68 2nd TR 0004 green.txt'
    # path3 = '/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/N01 1st recall 02 red.txt'
    # path4 = '/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/N01 2nd recall 02 red.txt'
    pcd1 = np.loadtxt(path1)
    pcd2 = np.loadtxt(path2)
    pcd3 = np.loadtxt(path3)
    # pcd4 = np.loadtxt(path4)
    fig = plt.figure(figsize=(20,20))
    ax1 = pcd_3d_plt([pcd1,pcd3],colors=['red','blue'],size=10,alpha=0.1)
    # plt.savefig('/Users/apple/YiLab/Resoursces/3D Align/sample/'+'after align red.svg',format='svg')
    plt.grid(True)
    plt.show()
    # pcd1 = pcd_3d_loader(path1,color=[1,0,0])
    # pcd2 = pcd_3d_loader(path2,color=[0,1,0])
    # o3.visualization.draw_geometries([pcd1,pcd2])
