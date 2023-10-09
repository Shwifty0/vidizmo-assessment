from ultralytics import YOLO
import cv2

# Path to video:
video_path = "inference_video.mp4"
# Using the best.pt model stored in "Yolo\runs\detect\train7\weights\best.pt"
model = YOLO(r"C:\Users\m.ozair\CodingAssessment\Yolo\runs\detect\train7\weights\best.pt")

# Using cv2 to capture the video
cap = cv2.VideoCapture(video_path)

# While loop for inferencing on video and create bounding boxes if the class is detected by the model:
while True:
    ret, frame = cap.read()
    results = model(frame, stream =True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 3)


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('q'):
         break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
