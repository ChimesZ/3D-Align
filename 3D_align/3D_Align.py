import numpy as np
use_cuda = True
if use_cuda:
    import cupy as cp
    to_cpu = cp.asnumpy
    cp.cuda.set_allocator(cp.cuda.MemoryPool().malloc)
else:
    cp = np
    to_cpu = lambda x: x
import open3d as o3
from probreg import cpd
from probreg import callbacks
import utils
import copy

def red_channel_align_mat(source_path_red, target_path_red):
    '''Generate affine transformation matrix
    Based on Maxium probility register to align source red channel point cloud with ref 
    ------
    Args:
        source_path_red(str): red channel `.txt` point cloud file waiting for transform
        target_path_red(str): ref red channel `.txt` point cloud file
    -----
    Returns:
        tf_param: parameters for affine transformation
    ------
    '''
    source, target = utils.prepare_source_and_target_nonrigid_3d(source_path_red, target_path_red,voxel_size=1)
    source = cp.asarray(source.points, dtype=cp.float32)
    target = cp.asarray(target.points, dtype=cp.float32)
    acpd = cpd.AffineCPD(source, use_cuda=use_cuda)
    tf_param, _, _ = acpd.registration(target)
    return tf_param

def transform(source_path, save_path, tf_param):
    source = utils.prepare_source_nonrigid_3d(source_path)
    source = cp.asarray(source.points, dtype=cp.float32)
    result = copy.deepcopy(source)
    result = tf_param.transform(result)
    cp.savetxt(save_path,result)

