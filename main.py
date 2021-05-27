import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io
import normalization, histograms, region_growing, filters, shapes, noise, region_growing, morphological, interpolation, rigid

image = color.rgb2gray(io.imread("image.jpg"))

#image = shapes.make_rectangle(200,200,50,50,50,50)
#
#image = rigid.rigid_transform(image,10,10,45)

plt.figure()
plt.imshow(image, cmap='gray')
plt.show()
