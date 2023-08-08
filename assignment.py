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


