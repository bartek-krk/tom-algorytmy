import numpy as np
import random

def salt_and_pepper(image, noise_proportion=0.1):
    image_copy = np.array(image, copy=True)
    img_height, img_width = image_copy.shape
    
    for _ in range(int((img_height*img_width)*noise_proportion)):
        current_y = random.randint(0,img_height-1)
        current_x = random.randint(0,img_width-1)
        image_copy[current_y][current_x] = random.randint(0,1)
        
    return image_copy