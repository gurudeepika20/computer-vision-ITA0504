import cv2
import pytesseract
from tkinter import Tk, filedialog

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Video", "*.mp4 *.avi")]
)

cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("Extracted Text:", text.strip())

    cv2.imshow("Video Text Extraction", frame)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
