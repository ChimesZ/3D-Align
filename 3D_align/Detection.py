import numpy as np
import pandas as pd
import open3d as o3
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

def pcd_init(path, min_points, Vis=False):
    '''Initialize the pointcloud from given path and hyperparameter
    ------
    param:
    path: Path of point cloud .txt file
    min_points: Min number of points demand to be recognized as a cell
    -----
    Return:
    pcd: o3.geometry.PointCloud class
    labels: np.array
    ------
    '''
    pcd = o3.geometry.PointCloud()
    raw_data = np.loadtxt(path)
    pcd.points = o3.utility.Vector3dVector(raw_data)
    labels = np.array(pcd.cluster_dbscan(eps=2.5, min_points=min_points))
    max_label = labels.max()
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3.utility.Vector3dVector(colors[:, :3])
    if Vis:
        o3.visualization.draw_geometries([pcd])
    return pcd,labels
def parameter_choice(path):
    """Choice proper parameter for `pcd_init`
    ---
    param: 
    path -> path to `.txt` point cloud file
    ---
    Show:
    pyplot figure between min_point and the number of detected cell
    }
    """   
    numbers = []
    for i in tqdm(range(0,100)):
        _, label = pcd_init(path, i)
        numbers.append(label.max())
    plt.scatter(range(0,100),numbers)
    plt.show()
def stat(path,Vis=True):
    """
    ---
    param: 
    path -> path to `.txt` point cloud file
    ---
    Return:
    cells -> numpy.array([cell...])
    cell -> dict: {'locs':'label':'center':}
    """
    data, labels = pcd_init(path,20,Vis=Vis)
    points = pd.DataFrame(data.points)
    points.columns = ['x','y','z']
    points['labels'] = labels
    cells = []
    for i in tqdm(range(0,max(points['labels'])+1)):
        index = points.index[points['labels'] == i].tolist()
        loc = np.asarray(points.loc[index, ['x','y','z']])
        cell = {}
        cell['locs'] = loc
        cell['label'] = i
        cell['center'] = np.mean(loc,axis=0)
        cells.append(cell)
    return np.asarray(cells)

if __name__ == '__main__':
    path = '/Users/apple/YiLab/Resoursces/3D Align/Bad data test/'
    path = path + '68 NC 0004 green registered'
    np.save(path + '.npy',stat(path + '.txt'))
    # names = os.listdir(path)
    # for name in tqdm(names):
    #     np.save(path + name + '.npy',stat(path + name))
    



    
