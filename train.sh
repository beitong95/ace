#! /bin/bash

# 6000000 can use 8638 MB / 10240 MB
# batch 5120
# training buffer size 6e6
# for each epoch, there are 6e6 / 5120 = 11 iterations 
# python train_ace.py datasets/office output/own/office.pt --training_buffer_size 6000000 --epochs 30
# python train_ace.py datasets/stairs output/own/stairs_50.pt --training_buffer_size 6000000 --epochs 50 --samples_per_image 4096
# python train_ace.py datasets/stairs output/own/stairs2.pt --render_visualization True --render_target_path output/renderings/train --render_flipped_portrait True --training_buffer_size 6000000 --epochs 30 --use_aug False
# python train_ace.py datasets/wayspots_bears output/wayspots/bears.pt --render_visualization True --render_target_path output/renderings/train --render_flipped_portrait True --training_buffer_size 6000000 --epochs 30 --use_aug False
# python train_ace.py datasets/stairs output/own/stairs_50.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096
# python train_ace.py datasets/office2 output/own/office2_240p.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096 --image_resolution 240
#python train_ace.py datasets/office2 output/own/office2_120p.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096 --image_resolution 120
python train_ace.py datasets/office2 output/own/office2_60p.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096 --image_resolution 60
# python train_ace.py datasets/office2 output/own/office2_160p.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096 --image_resolution 160
# python train_ace.py datasets/office2 output/own/office2_90p.pt --training_buffer_size 6000000 --epochs 16 --samples_per_image 4096 --image_resolution 90 --device_id 0
# python train_ace.py datasets/office2 output/own/office2_240p_12M.pt --training_buffer_size 12000000 --epochs 16 --samples_per_image 9012 --image_resolution 240 --device_id 0
