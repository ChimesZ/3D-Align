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
from tqdm import tqdm

def red_channel_align_mat(source_path_red, target_path_red,method = 'Affine'):
    '''Generate affine transformation matrix
    Based on Maxium probility register to align source red channel point cloud with ref 
    ------
    Args:
        source_path_red(str): red channel `.txt` point cloud file waiting for transform
        target_path_red(str): ref red channel `.txt` point cloud file
        method(str): could be `'Affine'`, `'NonRigid'` or `'Rigid'`
    -----
    Returns:
        tf_param
    ------
    '''
    source, target = utils.prepare_source_and_target_nonrigid_3d(source_path_red, target_path_red)
    source = cp.asarray(source.points, dtype=cp.float32)
    target = cp.asarray(target.points, dtype=cp.float32)
    # Select method
    if method == 'Affine':
        acpd = cpd.AffineCPD(source, use_cuda=use_cuda)
    elif method == 'NonRigid':
        acpd = cpd.NonRigidCPD(source, use_cuda=use_cuda)
    elif method == 'Rigid':
        acpd = cpd.RigidCPD(source, use_cuda=use_cuda)
    # Calculate tf_param 
    tf_param, _, _ = acpd.registration(target)
    return tf_param

def transform(source_path, save_path, tf_param):
    '''Transform point cloud data
    ---
    Args:
        source_path(str): green channel `.txt` point cloud file waiting for transform
        save_path(str): way to save
        tf_param: generated in `red_channel_align_mat()`
    ---
    Returns:
        Save the transformed point cloud
    ---
    '''
    source = utils.prepare_source_nonrigid_3d(source_path)
    source = cp.asarray(source.points, dtype=cp.float32)
    result = copy.deepcopy(source)
    result = tf_param.transform(result)
    cp.savetxt(save_path,result)

if __name__ == '__main__':
    namelist = ['1st recall','2nd recall']
    method = 'Rigid'
    source_path = '/home/zhongzh/zhongzh_data/System_Reconsolidation/Before_Align/'
    save_path = '/home/zhongzh/zhongzh_data/System_Reconsolidation/After_Align_R/'
    for name in tqdm(namelist):
        tf_param = red_channel_align_mat(source_path + 'N01 {} 02 red.txt'.format(name), 
                                         source_path + 'N01 TR 02 red.txt',
                                         method=method)
        transform(source_path + f'N01 {name} 02 green.txt',
                  save_path +f'N01 {name} 02 green aligned.txt',
                  tf_param)
        transform(source_path + f'N01 {name} 02 red.txt',
                  save_path +f'N01 {name} 02 red aligned.txt',
                  tf_param)
        
        

