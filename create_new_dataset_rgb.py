import os
import shutil
import cv2
import numpy as np
import pytransform3d.transformations as pytr
import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create poses.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--source_path', type=Path, default='datasets/office3_rpi/rgb_raw',
                        help='source dataset path, e.g. "datasets/office3"')
    parser.add_argument('--dest_path', type=Path, default='datasets/office3_rpi/rgb',
                        help='source dataset path, e.g. "datasets/office3_rpi"')
    parser.add_argument('--change_aspect_ratio', action='store_true',
                        help='convert aspect ratio to 16:9')

    opt = parser.parse_args()

    source_path = opt.source_path
    dest_path = opt.dest_path
    change_aspect_ratio = opt.change_aspect_ratio
    
    total_captured_rgb_count = len(os.listdir(source_path))
    print(f"Total captured RGB Count:{total_captured_rgb_count}")

    filepaths = sorted([os.path.join(source_path,filename) for filename in os.listdir(source_path)])
    for i, filepath in enumerate(filepaths):
            image = cv2.imread(filepath)
            filename = os.path.basename(filepath)
            if change_aspect_ratio:
                original_height, original_width = image.shape[:2]
                new_width = int(original_height * (9 / 16))
                crop_start = (original_width - new_width) // 2
                crop_end = original_width - crop_start
                image_cropped = image[:, crop_start:crop_end, :]
                rotated_image = cv2.rotate(image_cropped, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            if i == 0:
                print(f"image size {rotated_image.shape}")
            new_filepath = os.path.join(dest_path, filename)
            cv2.imwrite(new_filepath, rotated_image)


