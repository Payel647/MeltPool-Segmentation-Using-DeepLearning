import cv2
import os

video_path = "../input_video/meltpool.mp4"
output_folder = "../frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0
save_count = 0
n = 5

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % n == 0:
        filename = f"{output_folder}/frame_{save_count}.png"
        cv2.imwrite(filename, frame)
        save_count += 1

    frame_count += 1

cap.release()

print("Frames extracted successfully")