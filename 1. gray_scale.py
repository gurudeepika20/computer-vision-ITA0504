
import cv2
import numpy as np

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    combined = np.hstack((image, gray_image))

    cv2.imshow("Original Image        |        Grayscale Image", combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
