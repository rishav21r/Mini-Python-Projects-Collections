# CSV to JSON Converter

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that converts CSV files into JSON format using a simple GUI-based interface.

## Project Structure
```
Mini-Python-Projects-Collections/ 
| 
|──csv_to_json/ 
    |──csvtojason.py 
    |──README.md 
    |──requirements.txt 
    |──.gitignore 
    |──LICENSE
```

- `csvtojason.py`: The main Python script that converts CSV files to JSON.
- `README.md`: This file, containing project information and usage instructions.
- `requirements.txt`: A file listing the project's dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `LICENSE`: License information for this project.

## Functionality

The `csvtojason.py` script does the following:

1. Prompts the user to load a CSV file via a file dialog.
2. Converts the CSV file into JSON format.
3. Saves the JSON file at a specified location chosen by the user.
4. Displays a pop-up message when the conversion is complete.

## Requirements

This project requires the `tkinter` library, which is part of the Python standard library. Additionally, make sure you have the following dependencies installed:

```bash
pip install -r requirements.txt

