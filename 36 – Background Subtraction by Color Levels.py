import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is not None:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    cv2.imshow("Background Subtraction", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
