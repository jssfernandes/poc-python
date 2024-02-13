import numpy as np
import PIL
from PIL import Image

list_im = ['example0.jpg', 'example1.jpg', 'example2.jpg']
imgs    = [ Image.open(i) for i in list_im ]

# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])

# save that beautiful picture
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'merged_horizontally.jpg' )    

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( 'vertically_merged.jpg' )