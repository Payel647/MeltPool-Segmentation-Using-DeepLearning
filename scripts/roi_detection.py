import cv2
import os

input_folder = "../frames"
output_folder = "../roi_frames"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):

    img = cv2.imread(f"{input_folder}/{file}")

    h, w = img.shape[:2]

    x1 = int(w*0.3)
    y1 = int(h*0.3)

    x2 = int(w*0.7)
    y2 = int(h*0.7)

    roi = img[y1:y2, x1:x2]

    cv2.imwrite(f"{output_folder}/{file}", roi)

print("ROI extraction done")