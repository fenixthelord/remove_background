import os
import logging
from rembg import remove
from PIL import Image
from tqdm import tqdm  # For progress bar

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def ask_yes_no(question):
    """Ask a yes/no question and return True or False."""
    while True:
        response = input(question + " (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def ask_dimensions():
    """Ask the user for custom dimensions."""
    width = input("Enter width (leave blank to keep aspect ratio): ").strip()
    height = input("Enter height (leave blank to keep aspect ratio): ").strip()
    return (
        int(width) if width else None,
        int(height) if height else None
    )

def ask_compression_quality():
    """Ask the user for compression quality."""
    while True:
        quality = input("Enter compression quality (1-100, default is 85): ").strip()
        if not quality:
            return 85
        try:
            quality = int(quality)
            if 1 <= quality <= 100:
                return quality
            else:
                print("Quality must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def ask_background_color():
    """Ask the user for a custom background color."""
    while True:
        color = input("Enter background color as RGB (e.g., 255 255 255 for white): ").strip()
        if not color:
            return (255, 255, 255)  # Default to white
        try:
            r, g, b = map(int, color.split())
            if all(0 <= x <= 255 for x in (r, g, b)):
                return (r, g, b)
            else:
                print("RGB values must be between 0 and 255.")
        except ValueError:
            print("Please enter three numbers separated by spaces.")

def ask_output_format():
    """Ask the user for the output image format."""
    while True:
        format = input("Enter output format (png, jpg, webp, default is png): ").strip().lower()
        if not format:
            return "png"
        if format in ["png", "jpg", "jpeg", "webp"]:
            return format
        else:
            print("Invalid format. Choose from png, jpg, or webp.")

def process_images(input_folder, output_folder, size, background_color, quality, output_format):
    """Process all images in the input folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Created output folder: {output_folder}")

    images = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp"))]
    if not images:
        logging.warning(f"No images found in the input folder: {input_folder}")
        return

    for filename in tqdm(images, desc="Processing images", unit="image"):
        try:
            input_path = os.path.join(input_folder, filename)
            output_filename = f"processed_{os.path.splitext(filename)[0]}.{output_format}"
            output_path = os.path.join(output_folder, output_filename)

            with Image.open(input_path) as input_image:
                # Remove background
                output_image = remove(input_image)

                # Resize if dimensions are provided
                if size[0] or size[1]:
                    original_width, original_height = output_image.size
                    new_width = size[0] if size[0] else int(original_width * (size[1] / original_height))
                    new_height = size[1] if size[1] else int(original_height * (size[0] / original_width))
                    output_image = output_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Create background
                background = Image.new("RGB", (new_width, new_height), background_color)
                background.paste(output_image, (0, 0), output_image)

                # Save with compression
                background.save(output_path, quality=quality)
                logging.info(f"Processed and saved: {output_path}")

        except Exception as e:
            logging.error(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Ask user for options
    input_folder = input("Enter the input folder path (default is 'images'): ").strip() or "images"
    output_folder = input("Enter the output folder path (default is 'output_images'): ").strip() or "output_images"

    if ask_yes_no("Do you want to customize dimensions?"):
        width, height = ask_dimensions()
    else:
        width, height = None, None

    if ask_yes_no("Do you want to compress the images?"):
        quality = ask_compression_quality()
    else:
        quality = 100  # No compression

    if ask_yes_no("Do you want to change the background color?"):
        background_color = ask_background_color()
    else:
        background_color = (255, 255, 255)  # Default white

    output_format = ask_output_format()

    # Process images
    process_images(
        input_folder=input_folder,
        output_folder=output_folder,
        size=(width, height),
        background_color=background_color,
        quality=quality,
        output_format=output_format
    )