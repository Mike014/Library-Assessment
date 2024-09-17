# -*- coding: utf-8 -*-
import json
import sys

def extract_subset(file_path, output_path, num_items):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Split the data into individual JSON objects
            objects = data.split('}\n{')
            objects = [obj + '}' if not obj.endswith('}') else obj for obj in objects]
            objects = ['{' + obj if not obj.startswith('{') else obj for obj in objects]
            corrected_objects = []
            for i, obj in enumerate(objects[:num_items]):
                try:
                    json_data = json.loads(obj)
                    corrected_objects.append(json_data)
                except json.JSONDecodeError as e:
                    print(f"Object {i+1}: Invalid JSON - {e}")
                    print(f"Content: {obj}")
                    return
            # Write the subset JSON array to the output file
            root_data = {"root": corrected_objects}
            with open(output_path, 'w') as file:
                json.dump(root_data, file, indent=4)
            print(f"The subset JSON file has been created with {num_items} items.")
    except Exception as e:
        print(f"Error while reading the JSON file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_subset.py <input_file_path> <output_file_path> <num_items>")
    else:
        extract_subset(sys.argv[1], sys.argv[2], int(sys.argv[3]))









