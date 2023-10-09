from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov8n.pt")

# Train the model using the 'mscoco.yaml' dataset for 2 epochs
results = model.train(data='mscoco.yaml', epochs=50, imgsz=640)

# Evaluate the model's performance on the validation set
#results = model.predict(r"C:\Users\m.ozair\CodingAssessment\mscoco\test")