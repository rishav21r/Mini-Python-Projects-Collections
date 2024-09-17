# Password Generator

This project is part of the Mini-Python-Projects-Collections repository. It contains a Python script that generates strong, random passwords using a graphical user interface (GUI) built with CustomTkinter.

## Project Structure

```
Mini-Python-Projects-Collections/
|
|──password_generator/
    |──password_generator.py
    |──readme.md
    |──requirements.txt
    |──.gitignore
```

- `password_generator.py`: The main Python script that generates strong passwords.
- `readme.md`: This file, containing project information and usage instructions.
- `requirements.txt`: A file listing the project's dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Functionality

The `password_generator.py` script does the following:

1. Generates strong passwords of 16 characters.
2. Includes lowercase letters, uppercase letters, digits, and special characters.
3. Provides a user-friendly GUI for easy password generation.
4. Offers an option to clear the generated password.

## Requirements

This project requires the CustomTkinter library. To install the requirements, use:

```
pip install -r requirements.txt
```

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the `password_generator` directory.
3. Install the required dependencies using the command mentioned in the Requirements section.
4. Run the script using the following command:
   ```
   python password_generator.py
   ```
5. The GUI will appear, allowing you to generate and clear passwords.

## How it works

1. Click the "Generate Password" button to create a new password.
2. The generated password will appear below the buttons.
3. Click the "Clear Password" button to remove the displayed password.

## Customization

You can customize the password generation by modifying the following in `password_generator.py`:

- Change the `length` parameter in `generate_strong_password()` to adjust password length.
- Modify the character sets used for password generation.
- Adjust the GUI layout or styling using CustomTkinter options.

## Error Handling

The script includes basic error handling:

- It raises a `ValueError` if the requested password length is less than 12 characters.
- Other unexpected errors will be caught and displayed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](../LICENSE).
