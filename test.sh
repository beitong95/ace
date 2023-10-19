# with vis
#renderings_dir="output/renderings/own"

# python test_ace.py datasets/office output/own/office.pt --render_visualization True --render_target_path "$renderings_dir" --render_flipped_portrait True
# python test_ace.py datasets/stairs output/own/stairs_50.pt --render_visualization True --render_target_path "$renderings_dir" --render_flipped_portrait True
#python3 test_ace.py datasets/office2 output/own/office2.pt --image_resolution 720 2>&1 | tee output/own/log_office2.txt
python3 test_ace.py datasets/office2 output/own/office2_240p.pt --image_resolution 240 2>&1 | tee output/own/log_office2.txt 
# python3 test_ace.py datasets/office2 output/own/office2_120p.pt --image_resolution 120 2>&1 | tee output/own/log_office2.txt 
# python3 test_ace.py datasets/office2 output/own/office2_160p.pt --image_resolution 160 2>&1 | tee output/own/log_office2.txt 
#python3 test_ace.py datasets/office2 output/own/office2_90p.pt --image_resolution 90 2>&1 | tee output/own/log_office2.txt 
# python3 test_ace.py datasets/office2 output/own/office2_60p.pt --image_resolution 60 2>&1 | tee output/own/log_office2.txt 
