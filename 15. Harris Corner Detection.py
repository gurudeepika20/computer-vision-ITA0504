import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    output = img.copy()
    output[corners > 0.01 * corners.max()] = [0, 0, 255]

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | Harris Corner Detection', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
