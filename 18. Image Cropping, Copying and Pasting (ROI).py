import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    output = img.copy()

    h, w = img.shape[:2]

    roi = img[50:200, 50:200]
    roi = cv2.resize(roi, (150, 150))

    if h >= 350 and w >= 350:
        output[200:350, 200:350] = roi

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | ROI Copy and Paste', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
