# Barcode Generator

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that generates barcodes using a simple command-line interface.

## Project Structure
``` 
Mini-Python-Projects-Collections/ 
| 
|──barcode_generator/ 
    |──barcode_generator.py 
    |──readme.md 
    |──requirements.txt 
    |──.gitignore
```

- `barcode_generator.py`: The main Python script that generates barcodes.
- `readme.md`: This file, containing project information and usage instructions.
- `requirements.txt`: A file listing the project's dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Functionality

The `barcode_generator.py` script does the following:

1. Prompts the user to choose a barcode format from a list of available options.
2. Allows the user to input data for the barcode generation.
3. Generates the barcode image based on the input.
4. Saves the generated barcode image in the `barcode_images/` directory.

## Requirements

This project requires the `python-barcode` library along with `Pillow` for image handling. To install the requirements, use:

```pip install -r requirements.txt```

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the `barcode_generator` directory.
3. Install the required dependencies using the command mentioned in the Requirements section.
4. Run the script using the following command:

