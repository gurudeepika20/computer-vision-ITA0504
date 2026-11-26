import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Video", "*.mp4 *.avi")]
)

cap = cv2.VideoCapture(path)
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

if frames:
    h, w = frames[0].shape[:2]

    out = cv2.VideoWriter(
        "reverse.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        25, (w, h)
    )

    for frame in reversed(frames):
        out.write(frame)

    out.release()
    print("Reverse video created successfully")
else:
    print("Video not found")
