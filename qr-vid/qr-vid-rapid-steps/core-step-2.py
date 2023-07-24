import json

# Read the contents of functions.txt
with open('functions.txt', 'r') as functions_file:
    functions_contents = functions_file.read()

# Split the contents into a list of strings, using the custom separator
functions_entries = functions_contents.split('#END OF PROGRAM#\n')

# Create a dictionary to hold the key-value pairs
functions_data = {}

# Assign each code block to a unique key
for i, entry in enumerate(functions_entries, start=1):
    key = f"entry_{i}"
    functions_data[key] = entry.strip()

# Write the dictionary to function.json
with open('function.json', 'w') as json_file:
    json.dump(functions_data, json_file, indent=4)
