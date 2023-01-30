import numpy as np
import pandas as pd
import open3d as o3
import matplotlib.pyplot as plt
from tqdm import tqdm

def import_raw_data(path):
    '''Import raw point cloud data from .txt, returun point_cloud class'''
    points_data = np.loadtxt(path)
    point_cloud = o3.geometry.PointCloud()
    point_cloud.points = o3.utility.Vector3dVector(points_data)
    return point_cloud
def pcd_init(path, min_points):
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
    pcd.points = o3.utility.Vector3dVector(np.round(np.loadtxt(path)))
    labels = np.array(pcd.cluster_dbscan(eps=2.5, min_points=min_points))
    max_label = labels.max()
    colors = plt.get_cmap("tab20")(labels / (max_label 
    if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3.utility.Vector3dVector(colors[:, :3])
    # o3.visualization.draw_geometries([pcd])
    return pcd,labels
def parameter_choice(path):
    numbers = []
    for i in tqdm(range(0,100)):
        _, label = pcd_init(path, i)
        numbers.append(label.max())
    plt.scatter(range(0,100),numbers)
    plt.show()
def stat(path):
    data, labels = pcd_init(path,25)
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
    path1 = "/Users/apple/YiLab/Resoursces/3D Align/sample/MASK_DG green 1st recall_A01_G001_0001.oir - C=0.txt"
    path2 = "/Users/apple/YiLab/Resoursces/3D Align/sample/MASK_DG green 2nd recall_A01_G001_0001.oir - C=0.txt"
    data = stat(path2)
    np.save('/Users/apple/YiLab/Resoursces/3D Align/Data/2nd recall.npy',data)
    
