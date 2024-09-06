# WiFi QR Code Generator

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that generates QR codes for WiFi networks using a simple graphical user interface.

## Project Structure

```
Mini-Python-Projects-Collections/
|
|──wifi_qrcode_generator/
    |──wifi_qrcode.py
    |──README.md
    |──requirements.txt
    |──.gitignore
    |──LICENSE
```

- `wifi_qrcode.py`: The main Python script that generates WiFi QR codes.
- `README.md`: This file, containing project information and usage instructions.
- `requirements.txt`: A file listing the project's dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `LICENSE`: The MIT license file for this project.

## Functionality

The `wifi_qrcode.py` script does the following:

1. Provides a graphical user interface for inputting WiFi network details.
2. Allows the user to input the SSID, security type, and password.
3. Generates a QR code image based on the input.
4. Saves the generated QR code image in the same directory as the script.

## Requirements

This project requires the `qrcode` library with PIL support for image handling. To install the requirements, use:

```
pip install -r requirements.txt
```

## How it works

1. The script uses `tkinter` to create a simple graphical user interface for input.
2. The user enters the WiFi network details.
3. When the "Generate QR Code" button is clicked, the script creates a WiFi configuration string.
4. This string is then used to generate a QR code using the `qrcode` library.
5. The QR code is saved as an image file named after the SSID.
