import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file and read its content
    with open(csv_file_path, mode='r') as csv_file:
        # Using DictReader to map the information into a dictionary format
        csv_reader = csv.DictReader(csv_file)

        # Convert the CSV rows into a list of dictionaries
        data = []
        for row in csv_reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


# Provide the paths for the CSV and JSON files
csv_file = 'input_file.csv'
json_file = 'output_file.json'

# Call the function to convert the CSV to JSON
csv_to_json(csv_file, json_file)

print(f"CSV file has been successfully converted to {json_file}")
