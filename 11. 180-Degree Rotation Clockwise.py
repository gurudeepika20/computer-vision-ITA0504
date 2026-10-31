import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Images", "*.png *.jpg *.jpeg")]
)

img = cv2.imread(path)

if img is None:
    print("Image not selected!")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    img = cv2.resize(img, (400, 300))
    rotated = cv2.resize(rotated, (400, 300))

    result = np.hstack((img, rotated))

    cv2.imshow("Original | Rotated Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
