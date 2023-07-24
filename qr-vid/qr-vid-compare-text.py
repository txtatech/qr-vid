import re
import math

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def strip_timecodes_and_tags(subtitles_lines):
    stripped_lines = []
    for line in subtitles_lines:
        if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line):
            continue  # Skip timecodes
        if re.match(r'^\d+$', line.strip()):
            continue  # Skip line numbers
        stripped_line = re.sub(r'<[^>]+>', '', line)
        stripped_lines.append(stripped_line.strip())
    return stripped_lines

def reformat_subtitles(subtitles_lines):
    formatted_lines = []
    for line in subtitles_lines:
        # Skip empty lines and lines with only spaces
        if not line.strip():
            continue
        # Add indentation and wrap the line with a function
        formatted_line = f"def {line.strip()}:"
        formatted_lines.append(formatted_line)
    return formatted_lines

def compare_and_generate_diff(subtitles_path, decoded_path, output_path):
    subtitles_lines = read_file(subtitles_path)
    decoded_lines = read_file(decoded_path)

    # Strip timecodes, line numbers, and tags from the subtitles lines
    subtitles_stripped = strip_timecodes_and_tags(subtitles_lines)

    # Reformat the subtitles lines to match the desired formatting
    formatted_subtitles = reformat_subtitles(subtitles_stripped)

    # Find the minimum number of lines between the two files
    min_lines = min(len(formatted_subtitles), len(decoded_lines))

    # Find differences between the files
    diff_lines = []
    for line_number in range(min_lines):
        if formatted_subtitles[line_number] != decoded_lines[line_number].strip():
            diff_lines.append((line_number + 1, formatted_subtitles[line_number], decoded_lines[line_number]))

    # Check for any remaining lines in the longer file
    if len(formatted_subtitles) > len(decoded_lines):
        for line_number in range(min_lines, len(formatted_subtitles)):
            diff_lines.append((line_number + 1, formatted_subtitles[line_number], None))
    elif len(decoded_lines) > len(formatted_subtitles):
        for line_number in range(min_lines, len(decoded_lines)):
            diff_lines.append((line_number + 1, None, decoded_lines[line_number]))

    # Generate the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for line_number, subtitle_line, decoded_line in diff_lines:
            output_file.write(f"Line {line_number}:\n")
            if subtitle_line:
                output_file.write(f"Subtitle: {subtitle_line}\n")
            if decoded_line:
                output_file.write(f"Decoded: {decoded_line}\n")
            output_file.write("----------\n")

# Paths to the files
subtitles_path = 'subtitles.srt'
decoded_path = 'qr-test-decoded.txt'
output_path = 'differences.txt'

# Compare and generate the differences file
compare_and_generate_diff(subtitles_path, decoded_path, output_path)
