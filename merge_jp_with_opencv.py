import cv2
import numpy as np

image1 = cv2.imread('page0.jpg')
image2 = cv2.imread('page1.jpg')

width = 1653
height = 2339

image1 = cv2.resize(image1, (width, height))
image2 = cv2.resize(image2, (width, height))

combined_image = np.hstack((image1, image2))

# cv2.imshow('Combined Image', combined_image)
# cv2.waitKey(0) cv2.destroyAllWindows()

cv2.imwrite('merged_image.jpg', combined_image)

