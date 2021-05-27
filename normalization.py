import numpy as np

def normalize(image):
    image_copy = np.array(image, copy=True)
    return (image_copy - np.min(image_copy)) / (np.max(image_copy) - np.min(image_copy))

def normalize_to_range(image, lower, upper, to_int):
    image_copy = np.array(image, copy = True)
    normalized = (upper-lower) * normalize(image_copy) + lower
    return normalized.astype(int) if to_int else normalized