#!/usr/bin python
# Script Directory :Tools/Super

import os
import fnmatch
import yaml
import json

SourceDirName="src"

script_dir = os.path.dirname(os.path.abspath(__file__))

def find_files(directory, extensions):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for extension in extensions:
            for filename in fnmatch.filter(filenames, f'*.{extension}'):
                matches.append(os.path.join(root, filename))
    return matches


parent_dir = os.path.dirname(script_dir)

# move up two directories and into the source directory into project src dir

directory_to_search = os.path.join(os.path.dirname(parent_dir), SourceDirName)

extensions_to_find = ['cpp', 'hpp']

found_files = find_files(directory_to_search, extensions_to_find)

matching_word = ""
matching_lines = {}
data = {}

for file_path in found_files:
    file_name = os.path.basename(file_path)
    class_name = os.path.splitext(os.path.basename(file_path))[0]
    
    matching_word = ""
    matching_lines = {}

    # filter through files for parent definiton and extract the parent to be
    # put into the json file. 

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if f"class {class_name} final : public" in line:
                words_after_pattern = line.split(f"class {class_name} final : public")[1].split()
                if words_after_pattern:
                    matching_word = words_after_pattern[0]
            elif f"class {class_name} : public" in line:
                words_after_pattern = line.split(f"class {class_name} : public")[1].split()
                if words_after_pattern:
                    matching_word = words_after_pattern[0]
            elif f"Super" in line:
                matching_lines[line_number] = line.lstrip() 

    # Create yaml data using the filepath of each file as the object
    # Add the parent and child information extracted from the above function
    # to its corresponding filepath object. 

    if matching_word and matching_lines:
        data[file_path] = {
            "parent": matching_word,
            "child": class_name
        }
with open("extracted_data.yaml", "w") as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

with open("extracted_data.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# convert yaml output json because yaml looked ugly

json_data = json.dumps(yaml_data, indent=2)


with open('Super.json', 'w') as json_file:
    json_file.write(json_data)
    
try:
    os.remove("extracted_data.yaml")
except FileNotFoundError:
    print("YAML file not found.")    





