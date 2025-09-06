import cv2
import os

# Use existing directory to save captured faces
save_dir = "data"

# Initialize webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
max_images = 50  # Number of face images to capture

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(save_dir, f"face_{count}.jpg"), face_img)
        count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if count >= max_images:
            break

    cv2.imshow('Face Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= max_images:
        break

cap.release()
cv2.destroyAllWindows()
print(f"Captured {count} face images in '{save_dir}' directory.")
