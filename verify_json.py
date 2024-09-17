# -*- coding: utf-8 -*-
import json
import sys

def verify_and_correct_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Try to load the content as an array of JSON objects
            try:
                json_data = json.loads(data)
                if isinstance(json_data, list):
                    print("The JSON file is already correctly formatted.")
                    return
            except json.JSONDecodeError as e:
                print(f"Initial JSON load error: {e}")

            # If the content is not an array, try to correct it
            corrected_data = "[" + data.replace("}{", "},{") + "]"
            try:
                json_data = json.loads(corrected_data)
                with open(file_path, 'w') as file:
                    json.dump(json_data, file, indent=4)
                print("The JSON file has been corrected and formatted correctly.")
            except json.JSONDecodeError as e:
                print(f"Error after attempting to correct JSON: {e}")
                # Attempt a more robust correction by splitting and rejoining
                try:
                    objects = data.split('}{')
                    objects = [obj + '}' if not obj.endswith('}') else obj for obj in objects]
                    objects = ['{' + obj if not obj.startswith('{') else obj for obj in objects]
                    json_data = [json.loads(obj) for obj in objects]
                    with open(file_path, 'w') as file:
                        json.dump(json_data, file, indent=4)
                    print("The JSON file has been corrected and formatted correctly with robust method.")
                except Exception as e:
                    print(f"Robust correction failed: {e}")
    except Exception as e:
        print(f"Error while verifying or correcting the JSON file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_json.py <file_path>")
    else:
        verify_and_correct_json(sys.argv[1])






