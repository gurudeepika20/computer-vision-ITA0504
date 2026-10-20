
import cv2
import numpy as np

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    original = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    processed = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    result = np.hstack((original, processed))
    cv2.imshow("Original | Equalized", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

