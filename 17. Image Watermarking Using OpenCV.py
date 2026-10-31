import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    watermark = img.copy()

    cv2.putText(watermark, 'WATERMARK',
                (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                2, (0, 255, 0), 3)

    output = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

    img = cv2.resize(img, (400, 300))
    output = cv2.resize(output, (400, 300))

    result = np.hstack((img, output))
    cv2.imshow('Original | Watermarked Image', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected!")
