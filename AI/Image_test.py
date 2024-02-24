from ultralytics import YOLO
from PIL import Image
model = YOLO("runs/detect/train2/weights/best.pt")
classNames = ["defog"]
im1 = Image.open(" ")#image path
results = model.predict(source=im1, save=True)
