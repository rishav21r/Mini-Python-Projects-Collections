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
```

## Usage
1. Ensure you have Python installed on your system. 
2. Navigate to the csv_to_json directory. 
3. Install the required dependencies using the command mentioned in the Requirements section. 
4. Run the script using the following command:

```bash
python csvtojason.py
```
5. A popup window will appear, allowing you to select the input CSV file and choose where to save the output JSON file.

## How it works
1. The script uses tkinter to create a simple GUI for file selection and pop-up notifications.
2. The user selects a CSV file, and the script converts it into JSON format.
3. The resulting JSON file is saved in the location specified by the user.

## Customization
You can customize the script by modifying the following in `csvtojason.py`:
* Change the file dialog prompts or add validation for specific CSV structures.
* Adjust the default directory where the JSON file is saved.
* Extend the script to support additional file formats if needed.

## Error Handling
The script includes basic error handling:

* It shows a warning if the user does not select a CSV or JSON file.
* Unexpected errors are caught and displayed in a pop-up window.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source and available under the [MIT License](../LICENSE).