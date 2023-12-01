import csv
from PIL import Image
import os

def process_images(csv_file_path, output_base_folder):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present

        for row in reader:
            image_file_name = row[1]
            image_id = row[3]
            image_class = row[4]
            center_x, center_y = int(row[5]), int(row[6])

            try:
                with Image.open('base/' + image_file_name) as img:
                    left = center_x - 50
                    top = center_y - 50
                    right = center_x + 50
                    bottom = center_y + 50

                    cropped_img = img.crop((left, top, right, bottom))
                    class_folder = os.path.join(output_base_folder, image_class)
                    print(class_folder)
                    if not os.path.exists(class_folder):
                        os.makedirs(class_folder)
                    

                    cropped_img.save(f"{class_folder}/{image_id}.png")
                    print("FUNCIONOUUU")
            except IOError:
                print(f"Error opening or processing image file: {image_file_name}")

# Example usage
process_images('classifications.csv', '/')

