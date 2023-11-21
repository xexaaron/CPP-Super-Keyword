#!/usr/bin python
import os
import json
import datetime

# Create a log file to record changes

if os.path.exists('change_log.txt'):
    os.remove('change_log.txt')

log_file_path = 'change_log.txt'
log = open(log_file_path, 'a')  # Open the log file in append mode

# Read JSON data
with open('Super.json') as json_file:
    data = json.load(json_file)

# Iterate through each entry in the JSON data
for file_path, details in data.items():
    # Check if the file exists
    if os.path.exists(file_path):
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Replace 'Super' with the parent value
        replaced_content = file_content.replace('Super', details['parent'])

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(replaced_content)

        # Log the changes made to the file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: Replaced 'Super' with '{details['parent']}' in {file_path}\n"
        log.write(log_entry)
        log.write("-------------------------------------------------------------------------------------------\n")
# Close the log file
log.close()

