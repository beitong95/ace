# with vis
#renderings_dir="output/renderings/own"

# python test_ace.py datasets/office output/own/office.pt --render_visualization True --render_target_path "$renderings_dir" --render_flipped_portrait True
#python test_ace.py datasets/stairs output/own/stairs_50.pt --render_visualization True --render_target_path "$renderings_dir" --render_flipped_portrait True
python3 test_ace.py datasets/office2 output/own/office2.pt 2>&1 | tee output/own/log_office2.txt
