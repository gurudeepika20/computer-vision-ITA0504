import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    pts1 = np.float32([[50, 50], [300, 50],
                       [50, 300], [300, 300]])

    pts2 = np.float32([[0, 0], [300, 0],
                       [0, 300], [300, 300]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img, matrix, (300, 300))

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | Perspective Transformation', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
