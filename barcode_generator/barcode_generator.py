import barcode
from barcode.writer import ImageWriter
import random
import string

# Specify the type of barcode you want to generate (e.g., 'code128', 'ean13')
barcode_type = 'code128'  # You can change this to test other types

# Generate random data based on the barcode type
def generate_random_data(barcode_type):
    if barcode_type == 'ean13':
        # EAN-13 requires exactly 12 digits
        return ''.join(random.choices(string.digits, k=12))
    elif barcode_type == 'code128':
        # Code128 can include letters, digits, and some special characters
        length = random.randint(8, 16)  # You can specify a range for the length
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    else:
        raise ValueError(f"Barcode type '{barcode_type}' is not supported for random generation.")

# Generate the random barcode data
barcode_data = generate_random_data(barcode_type)

try:
    # Print available barcode types
    print("Available barcode types:", barcode.PROVIDED_BARCODES)

    # Create the barcode object
    barcode_obj = barcode.get(barcode_type, barcode_data, writer=ImageWriter())

    # Check if barcode_obj is None
    if barcode_obj is None:
        raise ValueError(f"Failed to create barcode for type '{barcode_type}' with data '{barcode_data}'.")

    # Save the barcode as an image file
    output_file = 'barcode_image'
    barcode_obj.save(output_file)

    print(f"Barcode saved as {output_file}.png with data '{barcode_data}'")

except Exception as e:
    print(f"An error occurred: {e}")
