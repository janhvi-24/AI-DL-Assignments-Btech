import cv2

# Load the face cascade classifier using OpenCV's built-in path
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture
video_cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, video_data = video_cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display video
    cv2.imshow("video_live", video_data)

    # Press 'a' key to exit
    if cv2.waitKey(10) == ord("a"):
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()