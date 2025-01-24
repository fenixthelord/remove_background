from rembg import remove
from PIL import Image, ImageOps
import os

# Folder containing images
input_folder = "images"  # Replace with your folder name
output_folder = "output_images"  # Folder to save processed images

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size for resizing
new_size = (1000, 1000)  # 1000x1000 pixels

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (supports .jpg, .png, etc.)
    if filename.endswith((".jpg", ".jpeg", ".png", ".webp")):
        # Input and output file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"processed_{filename}")

        # Open the input image
        input_image = Image.open(input_path)

        # Remove the background
        output_image = remove(input_image)

        # Create a white background
        white_bg = Image.new("RGB", new_size, (255, 255, 255))

        # Resize the image to fit within 1000x1000 while maintaining aspect ratio
        output_image.thumbnail(new_size, Image.Resampling.LANCZOS)

        # Calculate position to center the image on the white background
        x = (new_size[0] - output_image.size[0]) // 2
        y = (new_size[1] - output_image.size[1]) // 2

        # Paste the resized image onto the white background
        white_bg.paste(output_image, (x, y), output_image)

        # Save the output image
        white_bg.save(output_path)

        print(f"Processed {filename} and saved as {output_path}")

print("Background removal, white background, and resizing completed for all images!")