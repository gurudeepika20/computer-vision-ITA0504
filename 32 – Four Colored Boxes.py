import cv2
import numpy as np

size = int(input("Enter image size: "))

img = np.ones((size, size, 3), dtype=np.uint8) * 255

b = size // 10

img[0:b, 0:b] = (0,0,0)
img[0:b, size-b:size] = (255,0,0)
img[size-b:size, 0:b] = (0,255,0)
img[size-b:size, size-b:size] = (0,0,255)

cv2.imshow("Four Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
