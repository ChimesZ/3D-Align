import numpy as np
import open3d as o3

def pcd_3d_visulize(path, color = [1, 0, 0],round=False):
    data = np.loadtxt(path)
    if round:
        data = np.round(data)
    pcd = o3.geometry.PointCloud()
    pcd.points = o3.utility.Vector3dVector(data)
    pcd.source.paint_uniform_color(color)
    return pcd
