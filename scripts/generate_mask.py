import os
import json
import labelme
import numpy as np
from PIL import Image

json_folder = "../roi_frames"
output_folder = "../dataset/masks"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(json_folder):

    if file.endswith(".json"):

        path = os.path.join(json_folder, file)

        data = json.load(open(path))

        img = np.array(Image.open(os.path.join(json_folder, data['imagePath'])))

        mask = labelme.utils.shapes_to_label(
            img.shape,
            data['shapes'],
            {'_background_': 0, 'meltpool': 1}
        )[0]

        mask = (mask * 255).astype(np.uint8)

        save_name = file.replace(".json", ".png")

        Image.fromarray(mask).save(
            os.path.join(output_folder, save_name)
        )

print("Masks generated")