import cv2
import numpy as np

size = int(input("Enter image size: "))

img = np.ones((size,size,3), dtype=np.uint8)*255

cv2.circle(img,(size//2,size//2),
           size//4,(0,255,0),3)

cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
