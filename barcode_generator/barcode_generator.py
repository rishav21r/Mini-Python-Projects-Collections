import barcode
from barcode.writer import ImageWriter
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to prompt the user to choose a barcode format and input data
def get_user_input():
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to choose a barcode type
    barcode_type = simpledialog.askstring(
        title="Barcode Type",
        prompt=f"Enter the barcode type (e.g., {', '.join(barcode.PROVIDED_BARCODES)}):"
    )

    # Validate the barcode type
    if barcode_type not in barcode.PROVIDED_BARCODES:
        messagebox.showerror("Error", "Invalid barcode type!")
        return None, None

    # Ask the user to input the barcode data
    barcode_data = simpledialog.askstring(
        title="Barcode Data",
        prompt="Enter the data for the barcode:"
    )

    return barcode_type, barcode_data

# Function to generate the barcode
def generate_barcode(barcode_type, barcode_data):
    # Define the output directory
    output_dir = 'barcode_images'

    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Create the barcode object
        barcode_obj = barcode.get(barcode_type, barcode_data, writer=ImageWriter())

        # Check if barcode_obj is None
        if barcode_obj is None:
            raise ValueError(f"Failed to create barcode for type '{barcode_type}' with data '{barcode_data}'.")

        # Define the full output file path
        output_file = os.path.join(output_dir, 'barcode_image')

        # Save the barcode as an image file
        barcode_obj.save(output_file)

        messagebox.showinfo("Success", f"Barcode saved as {output_file}.png")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main function to run the barcode generator
def main():
    barcode_type, barcode_data = get_user_input()

    if barcode_type and barcode_data:
        generate_barcode(barcode_type, barcode_data)

if __name__ == "__main__":
    main()
