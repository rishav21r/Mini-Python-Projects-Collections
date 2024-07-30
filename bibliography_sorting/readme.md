# Bibliography Sorting Project

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that sorts a bibliography alphabetically and removes duplicate entries.

## Project Structure

```
Mini-Python-Projects-Collections/
|
|──bibliography_sorting/
    |──sort_bibliography.py
    |──readme.md
    |──input.txt
    |──sorted_output.txt
    |──requirements.txt
```

- `sort_bibliography.py`: The main Python script that performs the sorting and duplicate removal.
- `readme.md`: This file, containing project information and usage instructions.
- `input.txt`: The input file containing the unsorted bibliography.
- `sorted_output.txt`: The output file where the sorted bibliography will be written.
- `requirements.txt`: A file listing the project's dependencies (currently empty as the project uses only the Python standard library).

## Functionality

The `sort_bibliography.py` script does the following:

1. Reads the bibliography from the input file.
2. Separates the "Bibliography" heading from the references.
3. Identifies and reports any duplicate entries.
4. Removes duplicate entries.
5. Sorts the remaining references alphabetically (case-insensitive).
6. Writes the sorted bibliography to the output file.

## Requirements

This project currently uses only Python's standard library, so there are no external dependencies. However, we've included a `requirements.txt` file for future use. To view the requirements, you can cat the file:

```
cat requirements.txt
```

If any dependencies are added in the future, you can install them using:

```
pip install -r requirements.txt
```

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the `bibliography_sorting` directory.
3. (Optional) If there are any dependencies in the future, install them using the command mentioned in the Requirements section.
4. Prepare your input file (default name: `input.txt`) with the bibliography. The first line should be the "Bibliography" heading, followed by the references.
5. Run the script using the following command:

   ```
   python sort_bibliography.py
   ```

6. The script will process the input file and create a sorted output file (default name: `sorted_output.txt`).

## Customization

If you want to use different file names, you can modify the function call at the bottom of the `sort_bibliography.py` file:

```python
sort_bibliography('your_input_file.txt', 'your_output_file.txt')
```

Replace `'your_input_file.txt'` and `'your_output_file.txt'` with your desired input and output file names, respectively.

## Error Handling

The script includes error handling for common issues:

- If the input file is not found, it will display an appropriate error message.
- If the input file is empty or contains no references, it will raise a `ValueError`.
- Other unexpected errors will be caught and displayed.

## Output

The script will print messages to the console indicating:

- Whether duplicate entries were found (and list them if any).
- Confirmation that the sorted bibliography has been written to the output file.

## Contributing

Feel free to fork this project and submit pull requests with any improvements or additional features you'd like to see!

## License

[Include your chosen license information here]
