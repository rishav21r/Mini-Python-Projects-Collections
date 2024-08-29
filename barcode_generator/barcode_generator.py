import barcode
from barcode.writer import ImageWriter

# Specify the type of barcode you want to generate (e.g., 'ean13', 'code39', 'code128')
barcode_type = 'code128'

# Specify the data for the barcode (for EAN-13, it must be 12 digits)
barcode_data = '123456789012'

# Create the barcode
barcode_obj = barcode.get(barcode_type, barcode_data, writer=ImageWriter())

# Save the barcode as an image file
output_file = 'barcode_image'
barcode_obj.save(output_file)

print(f"Barcode saved as {output_file}.png")
