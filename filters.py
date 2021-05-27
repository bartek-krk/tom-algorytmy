import numpy as np
import scipy.signal as signal
import scipy.ndimage as nd

def uniform_filter(image, filter_size):
    return nd.uniform_filter(image, filter_size)

def gaussian_filter(image, sigma):
    return nd.gaussian_filter(image, sigma)

def median_filter(image, filter_size):
    return nd.median_filter(image, filter_size)

def laplacian(image):
    window = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
    ])
    laplacian_image = signal.correlate2d(image, window)
    return laplacian_image

def image_treshold(image, lower_treshold, upper_treshold):
    bool_img_lower = image > lower_treshold
    bool_img_upper = image < upper_treshold
    bool_img = np.bitwise_and(bool_img_lower,bool_img_upper)
    return bool_img.astype('int')