import numpy as np
from scipy import ndimage as nd

def generate_rigid_matrix(xt, yt, rot):
    rad = rot * np.pi / 180
    return np.array([[np.cos(rad), -1*np.sin(rad), xt],
                     [np.sin(rad), np.cos(rad), yt],
                     [0,0,1]
                     ])
    

    '''
    @param shape - input image shape
    '''
def center_matrix(transform, shape):
    y,x = shape
    A = np.array([[1, 0, (x-1)/2],
                  [0,1,(y-1)/2],
                  [0,0,1]
                  ])
    
    return A @ transform @ np.linalg.inv(A)


def rigid_dot(grid_x, grid_y, transform):
    coords = np.array([np.ndarray.flatten(grid_x), np.ndarray.flatten(grid_y), np.ones(grid_x.size)])
    new_coords = transform @ coords
    transformed_grid_x = new_coords[0, :].reshape(grid_x.shape)
    transformed_grid_y = new_coords[1, :].reshape(grid_y.shape)
    return transformed_grid_x, transformed_grid_y


def rigid_transform(image, xt, yt, rot):
    transform = generate_rigid_matrix(xt, yt, rot)
    centered_transform = center_matrix(transform, image.shape)
    grid_x, grid_y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    n_grid_x, n_grid_y = rigid_dot(grid_x, grid_y, centered_transform)
    return nd.map_coordinates(image, [n_grid_y, n_grid_x])