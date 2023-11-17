# mainly for adding offset in the poses (ground truth)
import os
import shutil
import cv2
import numpy as np
import pytransform3d.transformations as pytr
import argparse
from pathlib import Path
# souce_start = 311
# dest_start = 72
# offset = [-0.0378,0.01,0] # hardcoded


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create poses.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--source_path', type=Path, default='datasets/office3',
                        help='source dataset path, e.g. "datasets/office3"')
    parser.add_argument('--dest_path', type=Path, default='datasets/office3_rpi',
                        help='source dataset path, e.g. "datasets/office3_rpi"')
    parser.add_argument('--source_start', type=int, default=0,
                            help='start frame in the source dataset')    
    parser.add_argument('--dest_start', type=int, default=0,
                            help='start frame in the source dataset') 
    parser.add_argument('--offset_path', type=Path, default='./camera_config_imx219.txt',
                        help ='path of file containing offset from camera to iphone camera when using our customized rig')   
    
    opt = parser.parse_args()

    source_path = opt.source_path
    dest_path = opt.dest_path
    two_folders = ["train", "test"]
    final_folder = 'poses'
    souce_start = opt.source_start
    dest_start = opt.dest_start
    start = souce_start - (dest_start * (30/15)) # fps is 15 so we 
    offset_path = opt.offset_path
    offset = np.loadtxt(offset_path)
    print(f"Offset {offset}")
 
    total_captured_rgb_count = len(os.listdir(os.path.join(dest_path, 'rgb')))
    print(f"Total captured RGB Count:{total_captured_rgb_count}")

    count = 0
    for folder in two_folders:
        path = os.path.join(source_path, folder, 'poses')
        file_names = sorted(os.listdir(path))
        for file_name in file_names:
            file_name_int = int(file_name.split(".")[0])
            if file_name_int >= start and (file_name_int - start) % 2 == 0:
                file_path = os.path.join(source_path, folder, 'poses', file_name)
                data = np.loadtxt(file_path)
                point = pytr.vector_to_point(offset)
                res = pytr.transform(data, point)
                res_extrinsic_matrix = data.copy()
                res_extrinsic_matrix[:, 3] = res
                new_filepath = os.path.join(dest_path, 'poses', f"{count:05d}.txt")
                np.savetxt(new_filepath, res_extrinsic_matrix, fmt='%f', delimiter=' ')
                count += 1
                if count == total_captured_rgb_count:
                    break
            if count == total_captured_rgb_count:
                break

    print(f"Total generated poses files conunt:  {count}")
