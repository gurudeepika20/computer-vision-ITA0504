import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Video", "*.mp4 *.avi")]
)

cap = cv2.VideoCapture(path)
bg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mask = bg.apply(frame)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        x,y,w,h = cv2.boundingRect(c)

        if w > 60 and h > 40:
            cv2.rectangle(frame, (x,y), (x+w,y+h),
                          (0,255,0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
