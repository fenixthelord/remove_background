# Remove Background

A Python tool to **remove backgrounds from images**, **resize them**, and **add customizable backgrounds**. Perfect for batch processing images with ease!

---

## Features

- **Background Removal**: Remove backgrounds using the `rembg` library.
- **Resizing**: Resize images to custom dimensions (width, height, or both).
- **Custom Backgrounds**: Add a solid background color (e.g., white, red, or any RGB color).
- **Image Compression**: Compress images while maintaining quality.
- **Batch Processing**: Process all images in a folder automatically.
- **Multiple Formats**: Supports `.jpg`, `.jpeg`, `.png`, `.webp`, and `.bmp`.
- **Interactive Menu**: Customize settings via an easy-to-use interactive menu.

---

## Prerequisites

- **Python 3.8 or higher**: Download and install from [python.org](https://www.python.org/).
- **Required Libraries**: Install the required Python packages.

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
   pip install rembg pillow onnxruntime tqdm
   ```

---

## Usage

### Interactive Options

When you run the script, it will ask you:
1. **Input Folder**: Path to the folder containing images (default: `images`).
2. **Output Folder**: Path to save processed images (default: `output_images`).
3. **Custom Dimensions**: Set width, height, or both (leave blank to keep aspect ratio).
4. **Compression**: Choose compression quality (1-100, default: 85).
5. **Background Color**: Set a custom background color (e.g., `255 255 255` for white).
6. **Output Format**: Choose between `.png`, `.jpg`, or `.webp` (default: `.png`).

### Example Run

1. Place your images in the `images` folder (or specify a custom folder).
2. Run the script:
   ```bash
   python remove_bg.py
   ```
3. Follow the prompts to customize the process.

---

## Folder Structure

```
remove_background/
├── images/                  # Folder containing input images
├── output_images/           # Folder containing processed images
├── remove_bg.py             # Python script for processing images
├── README.md                # This README file
└── requirements.txt         # List of dependencies
```

---

## Customization

### Change Default Settings

You can modify the script to change default settings:
- **Image Size**: Edit the `new_size` variable in the script.
- **Background Color**: Edit the `background_color` variable.
- **Compression Quality**: Edit the `quality` variable.

### Command-Line Arguments

You can also run the script with command-line arguments for automation:
```bash
python remove_bg.py --input path/to/input --output path/to/output --size 800 600 --bg-color 255 0 0 --quality 90 --format jpg
```

---

## Troubleshooting

### Common Issues

1. **Error: `ModuleNotFoundError: No module named 'onnxruntime'`**:
   - Ensure all dependencies are installed:
     ```bash
     pip install rembg pillow onnxruntime tqdm
     ```

2. **Error: `FileNotFoundError: [WinError 3] The system cannot find the path specified`**:
   - Ensure the `images` folder exists and contains images.

3. **Error: `Unsupported image format`**:
   - Ensure the input images are in a supported format (`.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`).

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please:
1. Open an issue on GitHub.
2. Submit a pull request.

---

## Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) for the background removal library.
- [Pillow](https://pillow.readthedocs.io/) for image processing.
- [tqdm](https://tqdm.github.io/) for the progress bar.

---

## Author

[Muhammad khalaf]  