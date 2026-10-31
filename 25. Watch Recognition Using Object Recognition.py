import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()

img = cv2.imread(path)

if img is not None:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    original = cv2.resize(img, (400, 300))
    processed = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    processed = cv2.resize(processed, (400, 300))

    result = np.hstack((original, processed))

    cv2.imshow("Original Image | Object Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not selected!")
