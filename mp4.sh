  #! /bin/bash
  # /usr/bin/ffmpeg -framerate 30 -pattern_type glob -i "output/renderings/own/office/*.png" -c:v libx264 -pix_fmt yuv420p "output/renderings/own/office.mp4"
  # /usr/bin/ffmpeg -framerate 30 -pattern_type glob -i "output/renderings/own/stairs/*.png" -c:v libx264 -pix_fmt yuv420p "output/renderings/own/stairs.mp4"
    /usr/bin/ffmpeg -framerate 30 -pattern_type glob -i "output/renderings/own/stairs_50/*.png" -c:v libx264 -pix_fmt yuv420p "output/renderings/own/stairs_new_3.mp4"