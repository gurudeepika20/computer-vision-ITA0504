import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix = cv2.getAffineTransform(pts1, pts2)
    output = cv2.warpAffine(img, matrix, (cols, rows))

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | Affine Transformation', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
