# remove_background
Image Background Remove


# Background Removal and Image Resizing Tool

This Python script removes the background from images, resizes them to 1000x1000 pixels, and adds a white background. It processes all images in a specified folder and saves the results in an output folder.

---

## Features
- Removes the background from images using the `rembg` library.
- Resizes images to 1000x1000 pixels while maintaining aspect ratio (you can change it).
- Adds a white background to the processed images.
- Processes all images in a folder automatically.

---

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.8 or higher**:
   - Download and install Python from [python.org](https://www.python.org/).
   - During installation, make sure to check the box that says **"Add Python to PATH"**.

2. **Required Python Packages**:
   - Install the required packages using `pip`.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fenixthelord/remove_background.git
   cd remove_background
   ```

2. **Install Dependencies**:
   Run the following command to install the required Python packages:
   ```bash
   pip install rembg pillow onnxruntime
   ```

---

## Usage

1. **Prepare Your Images**:
   - Create a folder named `images` in the project directory.
   - Place all the images you want to process inside the `images` folder.

2. **Run the Script**:
   - Open a terminal or command prompt in the project directory.
   - Run the script:
     ```bash
     python remove_bg.py
     ```

3. **Check the Output**:
   - The processed images will be saved in a folder named `output_images`.
   - Each processed image will have a filename like `processed_<original_name>.png`.

---

## Folder Structure

```
your-repo-name/
├── images/                  # Folder containing input images
├── output_images/           # Folder containing processed images
├── remove_bg.py        # Python script for processing images
└── README.md                # This README file
```

---

## Customization

- **Change Image Size**:
  To resize images to a different size, modify the `new_size` variable in the script:
  ```python
  new_size = (width, height)  # Replace with your desired dimensions
  ```

- **Change Background Color**:
  To change the background color, modify the `white_bg` variable in the script:
  ```python
  white_bg = Image.new("RGB", new_size, (R, G, B))  # Replace (R, G, B) with your desired color
  ```

---

## Troubleshooting

1. **Error: `ModuleNotFoundError: No module named 'onnxruntime'`**:
   - Ensure you have installed all required packages:
     ```bash
     pip install rembg pillow onnxruntime
     ```

2. **Error: `FileNotFoundError: [WinError 3] The system cannot find the path specified`**:
   - Ensure the `images` folder exists in the project directory and contains your images.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) for the background removal library.
- [Pillow](https://pillow.readthedocs.io/) for image processing.

---

## Author

[Your Name]  
[Your GitHub Profile]  
[Your Email]

---
