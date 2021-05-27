import numpy as np
from skimage import measure
    
def local_growing(image, seed, bottom_treshold, upper_treshold):
    seed_value = image[seed]
    bottom_treshold = seed_value - bottom_treshold
    upper_treshold = seed_value + upper_treshold
    
    lower_matches = image > bottom_treshold
    upper_matches = image < upper_treshold
    matches = np.logical_and(lower_matches,upper_matches)
        
    visited = []
    queue = [seed]
    highlighted = []
    
    while len(queue) > 0:
        current_pixel = queue.pop(0)
        current_y, current_x = current_pixel
        
        if current_pixel not in visited:
            visited.append(current_pixel)
            neighbours = [
                    (current_y+1, current_x-1),
                    (current_y+1, current_x),
                    (current_y+1, current_x+1),
                    (current_y, current_x-1),
                    (current_y, current_x+1),
                    (current_y-1, current_x-1),
                    (current_y-1, current_x),
                    (current_y-1, current_x+1)]
            
            for neighbour in neighbours:
                if matches[neighbour] == True:
                    queue.append(neighbour)
                    highlighted.append(neighbour)
                
    res_img = np.zeros(image.shape)
    
    for pixel in highlighted:
        res_img[pixel] = True
    
    return res_img
                
            
        

def global_growing(image, seed, bottom_treshold, upper_treshold):
    seed_value = image[seed]
    bottom_treshold = seed_value - bottom_treshold
    upper_treshold = seed_value + upper_treshold
    
    lower_matches = image > bottom_treshold
    upper_matches = image < upper_treshold
    matches = np.logical_and(lower_matches,upper_matches)
    
    labeled = measure.label(matches)
    
    seed_label = labeled[seed]
        
    flat_labeled_image = np.ndarray.flatten(labeled)
    flat_out_image = np.zeros(flat_labeled_image.shape)
    
    for i in range(len(flat_labeled_image)):
        if flat_labeled_image[i] == seed_label:
            flat_out_image[i] = True
    
    
    return np.reshape(flat_out_image, image.shape)