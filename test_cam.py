import cv2 
import numpy as np
import argparse
screen_width, screen_height = 1920, 1080

def set_cam(image_width, image_height):
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, image_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, image_height)
    cam.set(cv2.CAP_PROP_HUE, 100) 
    cam.set(cv2.CAP_PROP_SATURATION, 50)      
    cam.set(cv2.CAP_PROP_CONTRAST, 32)  
    cam.set(cv2.CAP_PROP_BRIGHTNESS, 128) 

    fps = cam.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    return cam

def set_cv_window():
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def process_image(image, is_fit, image_width, image_height):
    black_canvas = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
    if is_fit:
        scale_factor_width = screen_width / image_width
        scale_factor_height = screen_height / image_height
        scale_factor = min(scale_factor_width, scale_factor_height)
        scaled_width = int(image_width * scale_factor)
        scaled_height = int(image_height * scale_factor)
        x_offset = (screen_width - scaled_width) // 2
        y_offset = (screen_height - scaled_height) // 2
        resized_image = cv2.resize(image, (scaled_width, scaled_height))
        black_canvas[y_offset:y_offset+scaled_height, x_offset:x_offset+scaled_width] = resized_image
    else:
        x_offset = (screen_width - image_width) // 2
        y_offset = (screen_height - image_height) // 2
        black_canvas[y_offset:y_offset+image_height, x_offset:x_offset+image_width] = image
    return black_canvas





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display an image with optional fitting to screen.')
    parser.add_argument('--fit', action='store_true', help='Fit the image within the screen.')
    parser.add_argument('--iw', type=int, default=640, help='Width of the image.')
    parser.add_argument('--ih', type=int, default=480, help='Height of the image.')
    args = parser.parse_args()
    image_width = args.iw
    image_height = args.ih
    is_fit = args.fit

    cam = set_cam(image_width, image_height)
    set_cv_window()


    while True:
        ret, image = cam.read()

        processed_image = process_image(image, is_fit, image_width, image_height)
        cv2.imshow('window',processed_image)

        k = cv2.waitKey(1)
        if k != -1:
            break

    cv2.imwrite('/home/pi/testimage.jpg', image)
    cam.release()
    cv2.destroyAllWindows()
