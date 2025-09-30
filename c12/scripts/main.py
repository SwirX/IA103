import os

input_file = 'data.md'

if not os.path.exists(input_file):
    print(f"File {input_file} not found.")
    input_file = input("Enter the correct file path: ")

with open(input_file, 'r') as file:
    content = file.read()
    split_content = content.split('---')
    entries = []
    for i, section in enumerate(split_content):
        section = section.strip()
        for line in section.split('\n'):
            title = None
            if line.startswith('|') and line.endswith('|'):
                if not title:
                    title = line
                else:
                    entries.append(line)
        if title and entries:
            # ask the user for description of each column name then type and length
            descriptions = []
            for entry in entries:
                description = input(f"Enter description for {entry}: ")
                col_type = input(f"Enter type for {entry}: ")
                col_length = input(f"Enter length for {entry}: ")
                descriptions.append({'description': description, 'type': col_type, 'length': col_length})
            # map descriptions to entries
            for entry, description in zip(entries, descriptions):
                entry['description'] = description['description']
                entry['type'] = description['type']
                entry['length'] = description['length']
            # write to a new file
            output_file = f'output_{i}.txt'
            with open(output_file, 'w') as out_file:
                out_file.write(f"Title: {title}\n")
                for entry in entries:
                    out_file.write(f"{entry['content']} | {entry['description']} | {entry['type']} | {entry['length']}\n")
                    out_file.write("\n")
                out_file.write("\n")
            entries = []
            title = None
            print(f"Processed section {i+1}, output written to {output_file}")
# This script processes a markdown file, extracts sections separated by '---',
