import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is None:
    print("Image not selected")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

value = int(input("Enter threshold value: "))

ret, result = cv2.threshold(
    gray, value, 255, cv2.THRESH_BINARY
)

cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
