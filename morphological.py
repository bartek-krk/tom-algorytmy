import numpy as np
import matplotlib.pyplot as plt

def dilation(image):
    #na podstawie https://www.youtube.com/watch?v=3IJ8RFtlDLY
    img_y, img_x = image.shape
    out_image = np.array(image, copy=True)
    for y in range(1,len(image)-1):
        for x in range(1,len(image[0])-1):
            upper_left = image[y+1][x-1]
            upper_center = image[y+1][x]
            upper_right = image[y+1][x+1]
            left = image[y][x-1]
            right = image[y][x+1]
            lower_left = image[y-1][x-1]
            lower_center = image[y-1][x]
            lower_right = image[y-1][x+1]
            if 1 in [upper_left,upper_center,upper_right,left,right,lower_left,lower_center,lower_right]:
                out_image[y][x] = 1

    return out_image

def erosion(image):
    img_y, img_x = image.shape
    out_image = np.array(image, copy=True)
    for y in range(1,len(image)-1):
        for x in range(1,len(image[0])-1):
            upper_left = image[y+1][x-1]
            upper_center = image[y+1][x]
            upper_right = image[y+1][x+1]
            left = image[y][x-1]
            right = image[y][x+1]
            lower_left = image[y-1][x-1]
            lower_center = image[y-1][x]
            lower_right = image[y-1][x+1]
            if 0 in [upper_left,upper_center,upper_right,left,right,lower_left,lower_center,lower_right]:
                out_image[y][x] = 0

    return out_image

def opening(image):
    after_erosion = erosion(image)
    return dilation(after_erosion)

def closing(image):
    after_dilation = dilation(image)
    return erosion(after_dilation)