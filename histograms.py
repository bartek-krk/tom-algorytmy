import numpy as np
import matplotlib.pyplot as plt
from normalization import normalize_to_range

def histogram(image, bins_number):
    img_min = np.min(image)
    img_max = np.max(image)
    
    dx = (img_max - img_min) / bins_number
    
    bins = np.array([img_min + (i*dx) for i in range(bins_number+1)])
    
    pixels = sorted(np.ndarray.flatten(image))
    
    histogram = np.array([0 for _ in range(len(bins)-1)], dtype='int64')
    
    current_upper_treshold = 1
    i = 0
    
    while current_upper_treshold < len(bins) and i != len(pixels):
        if pixels[i] <= bins[current_upper_treshold]:
            histogram[current_upper_treshold-1] = histogram[current_upper_treshold-1] + 1
            i = i+1
        else:
            current_upper_treshold = current_upper_treshold + 1
    
    return histogram, bins

#def histogram_equalization(image, bins_number):
#    img_max = np.max(image)
#
#    hist, bins = histogram(image,bins_number)
#    
#    cumulative_histogram = [0 for _ in range(len(hist))]
#    
#    for i in range(len(hist)):
#        cumulative_histogram[i] = np.sum(cumulative_histogram[i-1]) + hist[i]
#    
#    cumulative_histogram = cumulative_histogram / cumulative_histogram[len(cumulative_histogram)-1]
#    
#    transform_map = {}
#    
#    for i in range(len(bins)-1):
#        key = (bins[i], bins[i+1])
#        value = cumulative_histogram[i] * img_max
#        transform_map[key] = value
#    
#    flat_img = np.ndarray.flatten(image)
#    flat_img_copy = np.zeros(flat_img.shape)
#    
#    for k,v in transform_map.items():
#        for pixel_n in range(len(flat_img)):
#            if flat_img[pixel_n] >= k[0] and flat_img[i] <= k[1]:
#                flat_img_copy[pixel_n] = v
#                
#    return np.reshape(flat_img_copy, image.shape)
    
def histogram_equalization(image, bins_number, return_map=False):
    img_copy = normalize_to_range(image,0,bins_number-1,True)
    
    hist, bins = histogram(img_copy, bins_number)
    
    cumulative_histogram = [0 for _ in range(len(hist))]
    
    for i in range(len(hist)):
        cumulative_histogram[i] = np.sum(cumulative_histogram[i-1]) + hist[i]
    
    cumulative_histogram = cumulative_histogram / cumulative_histogram[len(cumulative_histogram)-1]
    
    transform_map = {}
    
    for i in range(len(hist)):
        transform_map[i] = int(cumulative_histogram[i] * bins_number-1)
        
    flat_img = np.ndarray.flatten(img_copy)
    flat_img_copy = np.ones(flat_img.shape)
    
    for pixel_n in range(len(flat_img)):
        flat_img_copy[pixel_n] = transform_map[flat_img[pixel_n]]
                
    return np.reshape(flat_img_copy, image.shape), transform_map if return_map else np.reshape(flat_img_copy, image.shape)

def histogram_matching(in_image, reference_image, bins_number):
    
    in_image = normalize_to_range(in_image,0,bins_number-1,True)
    reference_image = normalize_to_range(reference_image,0,bins_number-1,True)
    
    
    _ , in_image_equalized_map = histogram_equalization(in_image, bins_number, True)
    _ , reference_image_equalized_map = histogram_equalization(reference_image, bins_number, True)
    
    
    transform_map = {}
    
    new_dict = dict([(value, key) for key, value in reference_image_equalized_map.items()])
    
    for k,v in in_image_equalized_map.items():
        transform_map[k] = new_dict[v] if v in new_dict.keys() else k
    
    flat_img = np.ndarray.flatten(in_image)
    flat_img_copy = np.ones(flat_img.shape)
    
    for pixel_n in range(len(flat_img)):
        flat_img_copy[pixel_n] = transform_map[flat_img[pixel_n]]
        
    return np.reshape(flat_img_copy, in_image.shape)
    