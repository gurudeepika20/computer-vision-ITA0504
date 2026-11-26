import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray, 1.1, 5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)

    print("Total faces:", len(faces))

    cv2.imshow("Face Count", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
