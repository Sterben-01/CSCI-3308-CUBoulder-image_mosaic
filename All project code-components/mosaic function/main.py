from skimage.io import imread
import photomosaic as pm
from skimage.io import imsave
image = imread('C:/Users/01/Desktop/generated/psb.jpg')
# Analyze the collection (the "pool") of images.
pool = pm.make_pool('C:/Users/01/Desktop/photo library/*.jpeg')
print(pool)
#mos = pm.basic_mosaic(image, pool, (5, 5))
#print(mos)
#imsave('C:/Users/01/Desktop/final/mosaic.png', mos)
print(pool[[23.25636976, -9.05370638, -7.07396279]])