import numpy as np
import scipy.signal as signal

def numpy_gradient(image):
    #returns gradient_y, gradient_x
    return np.gradient(image)


def my_gradient(image):
  gradient_y = np.zeros(image.shape)
  gradient_x = np.zeros(image.shape)

  gradient_y[1:-1, :] = (image[2:, :] - image[0:-2, :]) / 2
  gradient_x[:, 1:-1] = (image[:, 2:] - image[:, 0:-2]) / 2

  return gradient_y, gradient_x


def my_window_gradient(image):
    window_x = np.array([
            [0,0,0],
            [-1,0,1],
            [0,0,0]
            ])
    window_y = window_x.T
    
    gradient_x = signal.correlate2d(image, window_x) / 2
    gradient_y = signal.correlate2d(image, window_y) / 2
    
    return gradient_y, gradient_x


def sobel_gradient(image):
    window_x = np.array([
            [-1,0,1],
            [-2,0,2],
            [-1,0,1]
            ])
    window_y = window_x.T
    
    gradient_x = signal.correlate2d(image, window_x) / 2
    gradient_y = signal.correlate2d(image, window_y) / 2
    
    return gradient_y, gradient_x
    

def prewitt_gradient(image):
    window_x = np.array([
            [-1,0,1],
            [-1,0,1],
            [-1,0,1]
            ])
    window_y = window_x.T
    
    gradient_x = signal.correlate2d(image, window_x) / 2
    gradient_y = signal.correlate2d(image, window_y) / 2
    
    return gradient_y, gradient_x