import os
import fnmatch
import json

if os.path.exists('Super.json'):
    os.remove('Super.json')

def find_files(directory, extensions):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for extension in extensions:
            for filename in fnmatch.filter(filenames, f'*.{extension}'):
                matches.append(os.path.join(root, filename))
    return matches


script_dir = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.abspath(os.path.join(script_dir, '..', '..'))


src_directory = os.path.join(root_directory, 'src')
include_directory = os.path.join(root_directory, 'include')

found_impl_files = find_files(src_directory, ['cpp', 'hpp'])
found_h_files = find_files(include_directory, ['h'])

data = {}
for impl_file in found_impl_files:
    impl_file_dir, impl_filename = os.path.split(impl_file)
    impl_class_name = os.path.splitext(impl_filename)[0]
    matching_word = ""
    matching_lines = {}
    if os.path.splitext(impl_filename)[1] == ".hpp":
        with open(impl_file, 'r') as h_file:
            lines = h_file.readlines()
            for line in lines:
                # Extract parent information from the header file
                if f"class {impl_class_name} final : public" in line:
                    words_after_pattern = line.split(f"class {impl_class_name} final : public")[1].split()
                    if words_after_pattern:
                        matching_word = words_after_pattern[0]
                elif f"class {impl_class_name} : public" in line:
                    words_after_pattern = line.split(f"class {impl_class_name} : public")[1].split()
                    if words_after_pattern:
                        matching_word = words_after_pattern[0]
        # Store the data with the implementation file path and parent information from the header file
        if matching_word:
            data[impl_file] = {
                "parent": matching_word,
                "child": impl_class_name
            }
    else:
        corresponding_h_file = os.path.join(include_directory, f"{impl_class_name}.h")
        if corresponding_h_file in found_h_files:
            with open(corresponding_h_file, 'r') as h_file:
                lines = h_file.readlines()
                for line in lines:
                    # Extract parent information from the header file
                    if f"class {impl_class_name} final : public" in line:
                        words_after_pattern = line.split(f"class {impl_class_name} final : public")[1].split()
                        if words_after_pattern:
                            matching_word = words_after_pattern[0]
                    elif f"class {impl_class_name} : public" in line:
                        words_after_pattern = line.split(f"class {impl_class_name} : public")[1].split()
                        if words_after_pattern:
                            matching_word = words_after_pattern[0]
            # Store the data with the implementation file path and parent information from the header file
            if matching_word:
                data[impl_file] = {
                    "parent": matching_word,
                    "child": impl_class_name
                }
with open("Super.json", "w") as json_file:
    json.dump(data, json_file, indent=2)










