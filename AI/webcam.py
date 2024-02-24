from ultralytics import YOLO
import cv2
import math
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
model = YOLO("runs/detect/train2/weights/best.pt")
classNames = "deforrestration"
while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)
            if confidence>0.45:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 255, 255)
                    thickness = 2
                    cv2.putText(img, classNames, org, font, fontScale, color, thickness)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
