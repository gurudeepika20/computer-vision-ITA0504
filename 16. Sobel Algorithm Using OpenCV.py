import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path, 0)

if img is not None:
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    x = cv2.convertScaleAbs(sobelx)
    y = cv2.convertScaleAbs(sobely)

    output = cv2.addWeighted(x, 0.5, y, 0.5, 0)

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | Sobel Filter', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
