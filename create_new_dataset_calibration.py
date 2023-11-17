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

    parser.add_argument('--dest_path', type=Path, default='datasets/office3_rpi',
                        help='source dataset path, e.g. "datasets/office3_rpi"')
    parser.add_argument('--focal_length', type=float, default=500,
                            help='focal_length of the camera')    
    parser.add_argument('--offset_x', type=float, default=320,
                            help='camera x-axis center offset') 
    parser.add_argument('--offset_y', type=float, default=240,
                        help ='camera x-axis center offset')   
    
    opt = parser.parse_args()

    dest_path = opt.dest_path
    focal_length = opt.focal_length
    offset_x = opt.offset_x
    offset_y = opt.offset_y

    intrinsic = np.zeros((3,3))
    intrinsic[0,0] = focal_length
    intrinsic[1,1] = focal_length
    intrinsic[2,0] = offset_x
    intrinsic[2,1] = offset_y
    intrinsic[2,2] = 1.0
    print(intrinsic)

    total_captured_rgb_count = len(os.listdir(os.path.join(dest_path, 'rgb')))
    print(f"Total captured RGB Count:{total_captured_rgb_count}")

    for i in range(total_captured_rgb_count):
        new_filepath = os.path.join(dest_path, 'calibration', f"{i:05d}.txt")
        np.savetxt(new_filepath, intrinsic, fmt='%f', delimiter=' ')
 