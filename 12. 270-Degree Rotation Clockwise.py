import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    img = cv2.resize(img, (400, 300))
    rotated = cv2.resize(rotated, (400, 300))

    result = np.hstack((img, rotated))
    cv2.imshow('Original | 270 Degree Rotation', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
