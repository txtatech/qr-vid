def generate_srt_from_functions(functions_text, frame_delay=5):
    # Split the text into individual code blocks based on non-empty lines
    code_blocks = [block.strip() for block in functions_text.splitlines() if block.strip()]

    # Calculate the timecodes and create SRT subtitles for each code block
    srt_content = ""
    start_time = 0
    for i, code_block in enumerate(code_blocks, start=1):
        # Calculate end time based on frame delay
        end_time = start_time + frame_delay

        # Create the SRT subtitle entry for the code block
        srt_entry = f"{i}\n"
        srt_entry += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_entry += f"{code_block}\n\n"

        # Append the entry to the SRT content
        srt_content += srt_entry

        # Update start time for the next code block
        start_time = end_time

    return srt_content

def format_time(time_in_seconds):
    # Format time in seconds to SRT time format (hh:mm:ss,mmm)
    hours = int(time_in_seconds / 3600)
    minutes = int((time_in_seconds % 3600) / 60)
    seconds = int(time_in_seconds % 60)
    milliseconds = int((time_in_seconds - int(time_in_seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def main():
    # Read the plain text file containing the functions
    with open('functions.txt', 'r') as file:
        functions_text = file.read()

    # Generate SRT content from the functions text with a frame delay of 5 seconds
    srt_content = generate_srt_from_functions(functions_text, frame_delay=5)

    # Save the SRT content to a file
    with open('functions.srt', 'w') as srt_file:
        srt_file.write(srt_content)

if __name__ == "__main__":
    main()

