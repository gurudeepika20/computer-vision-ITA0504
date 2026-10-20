
import cv2
import numpy as np

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    result = np.hstack((img, blur))
    cv2.imshow("Original | Gaussian Blur", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
