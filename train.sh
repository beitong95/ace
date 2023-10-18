#! /bin/bash

# 6000000 can use 8638 MB / 10240 MB
# batch 5120
# training buffer size 6e6
# for each epoch, there are 6e6 / 5120 = 11 iterations 
# python train_ace.py datasets/office output/own/office.pt --training_buffer_size 6000000 --epochs 30
python train_ace.py datasets/stairs output/own/stairs_50.pt --training_buffer_size 6000000 --epochs 50 --samples_per_image 4096
# python train_ace.py datasets/stairs output/own/stairs2.pt --render_visualization True --render_target_path output/renderings/train --render_flipped_portrait True --training_buffer_size 6000000 --epochs 30 --use_aug False
# python train_ace.py datasets/wayspots_bears output/wayspots/bears.pt --render_visualization True --render_target_path output/renderings/train --render_flipped_portrait True --training_buffer_size 6000000 --epochs 30 --use_aug False