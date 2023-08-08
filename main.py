import json
import os
from assignment import process_dict


def generate_schema(input_file_path, output_file_path):
    with open(input_file_path) as data_file:
        input_data = json.load(data_file)

    message_data = input_data.get('message', {})
    output_schema = process_dict(message_data)

    output_schema_json = json.dumps(output_schema, indent=4)

    with open(output_file_path, 'w') as output_file:
        output_file.write(output_schema_json)


def main():
    input_folder = 'work/data'
    output_folder = 'work/schema'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    json_files = [filename for filename in os.listdir(input_folder) if filename.endswith('.json')]

    for counter, json_file in enumerate(json_files, start=1):
        input_file_path = os.path.join(input_folder, json_file)
        output_file_path = os.path.join(output_folder, f'schema_{counter}.json')

        generate_schema(input_file_path, output_file_path)
        print(f'Schema generated for {json_file}')


if __name__ == "__main__":
    main()
