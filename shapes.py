import numpy as np

def make_rectangle(img_height, img_width, y_corner, x_corner, width, height):
    image = np.zeros((img_height,img_width))
    image[y_corner:y_corner+height, x_corner:x_corner + width] = 1
    return image


def make_circle(img_height, img_width, center_y, center_x, radius):
    image = np.zeros((img_height,img_width))
    for y in range(len(image)):
        for x in range(len(image[0])):
            if (x-center_x)**2 + (y-center_y)**2 <= radius**2:
                image[y][x] = 1
    return image


def make_ellipsis(img_height, img_width, center_y, center_x, a, b):
    image = np.zeros((img_height, img_width))
    for y in range(len(image)):
        for x in range(len(image[0])):
            if ((((x-center_x)**2)/(a**2)) + (((y-center_y)**2)/(b**2))) <= 1:
                image[y][x] = 1
    return image
    

def make_multiple_circles(img_height, img_width, center_y_s, center_x_s, radiuses):
    images = []
    
    for center_y, center_x, radius in zip( center_y_s, center_x_s, radiuses):
        images.append(make_circle(img_height, img_width, center_y, center_x, radius))
        
    out_image = np.zeros((img_height, img_width))
    
    for partial_image in images:
        out_image = np.logical_or(out_image, partial_image)
        
    return out_image