
import cv2
import numpy as np

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    edges = cv2.Canny(img, 100, 200)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    result = np.hstack((img, edges))
    cv2.imshow("Original | Canny Edges", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
