import csv
import json
import tkinter as tk
from tkinter import filedialog, messagebox


def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file and read its content
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Convert the CSV rows into a list of dictionaries
        data = [row for row in csv_reader]

    # Write the data to a JSON file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


def load_file():
    # Open a file dialog to select the CSV file
    csv_file = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])

    if csv_file:
        # Ask the user where to save the JSON file
        json_file = filedialog.asksaveasfilename(title="Save JSON File As", defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json")])

        if json_file:
            # Convert the CSV to JSON
            csv_to_json(csv_file, json_file)

            # Display a pop-up message when conversion is complete
            messagebox.showinfo("Success", f"CSV file has been successfully converted to {json_file}")
        else:
            messagebox.showwarning("Warning", "No JSON file selected.")
    else:
        messagebox.showwarning("Warning", "No CSV file selected.")


# Create the Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show file dialog and run the conversion
load_file()

# Close the Tkinter window
root.quit()
