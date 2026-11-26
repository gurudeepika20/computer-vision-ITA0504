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

eye = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

eyes = eye.detectMultiScale(gray, 1.1, 5)

for x,y,w,h in eyes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

print("Total Eyes:", len(eyes))

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
