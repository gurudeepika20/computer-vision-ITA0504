
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is not None:
    rotated = cv2.rotate(
        img, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    cv2.imshow("Original", img)
    cv2.imshow("270 Clockwise", rotated)

    cv2.imwrite("rotated_270.jpg", rotated)

    print("Image rotated and saved successfully")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected")
