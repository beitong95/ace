#! bin/bash

#### office3 raspberry pi cam
directory="/home/bizon/beitong/ace/datasets/office3_rpi"
echo "creating dataset for $directory"
subdirectory_path="$directory/rgb_raw"
if [ -d "$subdirectory_path" ]; then
    echo "check $subdirectory_path PASS"
else
    echo "Please copy rgb images captured by your camera into $subdirectory_path"
fi
subdirectories=("poses" "rgb" "calibration")
for subdir in "${subdirectories[@]}"; do
    subdirectory_path="$directory/$subdir"
    
    if [ -d "$subdirectory_path" ]; then
        echo "Subdirectory exists: $subdirectory_path"
    else
        echo "Subdirectory does not exist: $subdirectory_path"
        mkdir $subdirectory_path
    fi
done
# rgb
echo "creating rgb"
python3 create_new_dataset_rgb.py --source_path datasets/office3_rpi/rgb_raw/ --dest_path datasets/office3_rpi/rgb --change_aspect_ratio
# poses
echo "creating poses"
python3 create_new_dataset_poses.py --source_path ./datasets/office3 --dest_path ./datasets/office3_rpi --source_start 311 --dest_start 72 --offset_path camera_config_imx219.txt 
# calibration
echo "creating calibration"
python3 create_new_dataset_calibration.py --dest_path ./datasets/office3_rpi --focal_length 532.56 --offset_x 320 --offset_y 240