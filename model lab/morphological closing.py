
import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)
    result = cv2.morphologyEx(
        gray, cv2.MORPH_CLOSE, kernel
    )

    cv2.imshow("Original", img)
    cv2.imshow("Closing", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected")
