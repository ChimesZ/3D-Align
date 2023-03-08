import numpy as np
import pandas as pd
import open3d as o3

color = 'red'
points_data_result = np.loadtxt(f"/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/After_Align_R/N01 2nd recall 02 {color} aligned.txt")
points_data_source = np.loadtxt(f"/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/After_Align_R/N01 TR 02 {color}.txt")
points_data_target = np.loadtxt(f"/Users/apple/YiLab/Raw_Data/System Reconsolidation/Point Cloud/After_Align_R/N01 1st recall 02 {color} aligned.txt")
result = o3.geometry.PointCloud()
source = o3.geometry.PointCloud()
target = o3.geometry.PointCloud()
result.points = o3.utility.Vector3dVector(points_data_result)
source.points = o3.utility.Vector3dVector(points_data_source)
target.points = o3.utility.Vector3dVector(points_data_target)
source.paint_uniform_color([1, 0, 0])
target.paint_uniform_color([0, 1, 0])
result.paint_uniform_color([0, 0, 1])
o3.visualization.draw_geometries([source,target])
