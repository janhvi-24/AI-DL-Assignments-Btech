from ultralytics import YOLO
import cv2
import cvzone
import math
import time

# Attempt to initialize the webcam with different indices
cap_index = 0 # Start with index 0
cap = cv2.VideoCapture(cap_index)

# Loop to try different camera indices if the initial one fails
while not cap.isOpened():
    print(f"Failed to open camera with index {cap_index}. Trying next index...")
    cap_index += 1
    if cap_index > 5: # Limit the number of attempts to avoid infinite loop
        print("Could not open any camera. Please check your camera connection and drivers.")
        exit() # Exit the program if no camera is found
    cap = cv2.VideoCapture(cap_index)

# If a camera is successfully opened, set its properties
cap.set(3, 1280) # Set width
cap.set(4, 720) # Set height

# For video file (uncomment and modify path if you want to use a video)
# cap = cv2.VideoCapture("../Videos/motorbikes.mp4")

model = YOLO("../Yolo-Weights/yolov8l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

prev_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read() # Read a frame from the capture object

    if not success: # Check if the frame was read successfully
        print("Failed to read frame from camera/video. Exiting.")
        break # Exit the loop if unable to read frame

    results = model(img, stream=True) # Perform object detection on the frame

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Class Name
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    # Calculate and display FPS
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    # You can also use cvzone.putTextRect to display FPS on the image
    cvzone.putTextRect(img, f'FPS: {int(fps)}', (20, 70), scale=2, thickness=2, colorR=(0, 255, 0)) # Example of displaying FPS on image

    cv2.imshow("Image", img) # Display the processed image

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
