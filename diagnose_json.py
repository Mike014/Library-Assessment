# -*- coding: utf-8 -*-
import json
import sys

def diagnose_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            objects = data.split('}{')
            objects = [obj + '}' if not obj.endswith('}') else obj for obj in objects]
            objects = ['{' + obj if not obj.startswith('{') else obj for obj in objects]
            for i, obj in enumerate(objects):
                try:
                    json_data = json.loads(obj)
                    print(f"Object {i+1}: Valid JSON")
                except json.JSONDecodeError as e:
                    print(f"Object {i+1}: Invalid JSON - {e}")
                    print(f"Content: {obj}")
    except Exception as e:
        print(f"Error while reading the JSON file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python diagnose_json.py <file_path>")
    else:
        diagnose_json(sys.argv[1])





