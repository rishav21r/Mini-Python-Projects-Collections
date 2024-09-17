# Captcha Generator Project

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that generates CAPTCHA images with distorted text.

## Project Structure

```
Mini-Python-Projects-Collections/
|
|──captcha_generator/
    |──captcha_generator.py
    |──readme.md
    |──requirements.txt
```

- `captcha_generator.py`: The main Python script that generates the CAPTCHA images.
- `readme.md`: This file, containing project information and usage instructions.
- `requirements.txt`: A file listing the project's dependencies.

## Functionality

The `captcha_generator.py` script does the following:

1. Generates random text for the CAPTCHA.
2. Creates an image with the CAPTCHA text.
3. Applies distortion effects to the text (rotation, noise, lines).
4. Saves the generated CAPTCHA image.

## Requirements

This project requires the Pillow library. To install the requirements, use:

```
pip install -r requirements.txt
```

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the `captcha_generator` directory.
3. Install the required dependencies using the command mentioned in the Requirements section.
4. Run the script using the following command:
   ```
   python captcha_generator.py
   ```
5. The script will generate a CAPTCHA image and save it in the current directory.

## Customization

You can customize the CAPTCHA generation by modifying the following in `captcha_generator.py`:

- Change the `length` parameter in `generate_random_text()` to adjust CAPTCHA length.
- Modify `width` and `height` in `generate_captcha()` to change image dimensions.
- Adjust font size and type in the `generate_captcha()` function.
- Change the number of noise points and lines for different levels of distortion.

## Error Handling

The script includes basic error handling:
- If the specified font file is not found, it falls back to the default font.
- Other unexpected errors will be caught and displayed.

## Output

The script will:
- Generate a CAPTCHA image.
- Save the image with a filename like `captcha_ABC123.png`, where `ABC123` is the generated CAPTCHA text.
- Display the image.
- Print a confirmation message with the saved image filename.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](../LICENSE).