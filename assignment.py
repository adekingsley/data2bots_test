import json
import os


# checking the data_types
def determine_type(value):
    if isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, list):
        if all(isinstance(item, str) for item in value):
            return "enum"
        elif all(isinstance(item, dict) for item in value):
            return "array"
    elif isinstance(value, dict):
        return "object"
    return "unknown"


# check for key_value
def process_dict(dictionary):
    output = {}
    for key, value in dictionary.items():
        entry = {
            "type": determine_type(value),
            "tag": "",
            "description": "",
            "required": False
        }
        if entry["type"] == "object":
            entry["properties"] = process_dict(value)
        elif entry["type"] == "array":
            if determine_type(value[0]) == "object":
                entry["items"] = process_dict(value[0])
        output[key] = entry
    return output


# setting up input and output directory
input_folder = 'work/data'
output_folder = 'work/schema'

# List all JSON files in the input folder
json_files = [filename for filename in os.listdir(input_folder) if filename.endswith('.json')]

# Initialize a counter to match output files
counter = 1

# Loop through each JSON file
for json_file in json_files:
    input_file_path = os.path.join(input_folder, json_file)

    with open(input_file_path) as data_file:
        input_data = json.load(data_file)

    message_data = input_data.get('message', {})
    output_schema = process_dict(message_data)

    # Generate the output schema file name with the counter
    output_file_path = os.path.join(output_folder, f'schema_{counter}.json')

    # Increment the counter for the next iteration
    counter += 1

    # Generating the Output JSON Schema
    output_schema_json = json.dumps(output_schema, indent=4)

    # Saving the Output JSON Schema
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_schema_json)
