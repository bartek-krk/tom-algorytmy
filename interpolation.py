import numpy as np
import math

def bilinear_interpolation(image, new_height, new_width):
    orginal_height, orginal_width = image.shape
    image = np.pad(image, ((0,1),(0,1)), 'constant')
    out_img = np.zeros((new_height,new_width), dtype=np.float64)
    for i in range(new_height):
        for j in range(new_width):
            orginal_x = (i+1)*(orginal_height/new_height)-1
            orginal_y = (j+1)*(orginal_width/new_width)-1
            x = math.floor(orginal_x)
            y = math.floor(orginal_y)
            u = orginal_x - x
            v = orginal_y - y
            out_img[i,j] = (1-u)*(1-v)*image[x,y]+u*(1-v)*image[x+1,y]+(1-u)*v*image[x,y+1]+u*v*image[x+1,y+1]
    return out_img