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

smile = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

smiles = smile.detectMultiScale(gray, 1.8, 20)

for x,y,w,h in smiles:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

print("Smiles detected:", len(smiles))

cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
