import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is not None:
    text = input("Enter text: ")

    cv2.putText(img, text, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    cv2.imshow("Text Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
