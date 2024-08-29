import barcode
from barcode.writer import ImageWriter

# Specify the type of barcode you want to generate (e.g., 'code128', 'ean13')
barcode_type = 'code128'  # You can change this to test other types

# Specify the data for the barcode
barcode_data = '123456789012'  # Make sure this matches the type's requirements

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

    print(f"Barcode saved as {output_file}.png")

except Exception as e:
    print(f"An error occurred: {e}")
