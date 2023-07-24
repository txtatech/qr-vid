import os
import math

def main():
    # PART 1 - Generate Python files
    os.makedirs('python_programs', exist_ok=True)


    # The base Python program templates
    program_templates = [
        "def math_func_{i}(n):\n    return n + {val}\n\nprint(math_func_{i}({val}))\n",  # Addition
        "def math_func_{i}(n):\n    return n - {val}\n\nprint(math_func_{i}({val}))\n",  # Subtraction
        "def math_func_{i}(n):\n    return n * {val}\n\nprint(math_func_{i}({val}))\n",  # Multiplication
        "def math_func_{i}(n):\n    return n / {val}\n\nprint(math_func_{i}({val}))\n",  # Division
        "def math_func_{i}(n):\n    return n % {val}\n\nprint(math_func_{i}({val}))\n",  # Modulus
        "def math_func_{i}(n):\n    return math.pow(n, {val})\n\nprint(math_func_{i}({val}))\n",  # Power
        "def math_func_{i}(n):\n    return math.sqrt(n)\n\nprint(math_func_{i}(n))\n",  # Square root
        "def math_func_{i}(n):\n    return math.log(n)\n\nprint(math_func_{i}(n))\n",  # Logarithm
        "def math_func_{i}(n):\n    return math.sin(n)\n\nprint(math_func_{i}(n))\n",  # Sine
        "def math_func_{i}(n):\n    return math.cos(n)\n\nprint(math_func_{i}(n))\n",  # Cosine
        "def math_func_{i}(n):\n    return math.tan(n)\n\nprint(math_func_{i}(n))\n"  # Tangent
    ]

    for i in range(1, 11):
        if i == 11:
            program = "# This is a null program"
        else:
            val = i if i < 21 else i % 20 + 1
            template = program_templates[i % len(program_templates)]
            program = template.format(i=i, val=val)

        with open(f'python_programs/math_func_{i}.py', 'w') as file:
            file.write(program.strip())

    
    # PART 2 - Combine Python files into functions.txt using custom separator
    with open('functions.txt', 'w') as outfile:
        python_files = sorted(os.listdir('python_programs'))
        for filename in python_files:  # Process each Python file individually
            if filename.endswith('.py'):
                with open(os.path.join('python_programs', filename), 'r') as infile:
                    outfile.write(infile.read())  # Write the full program
                    outfile.write('\n#END OF PROGRAM#\n')  # Custom separator on a new line

    # PART 3 - Convert functions.txt to SRT format
    def generate_srt_from_functions(functions_text, frame_delay=5):
        functions = functions_text.split('\n\n')
        srt_content = ""
        start_time = 0
        for i, function_code in enumerate(functions, start=1):
            end_time = start_time + frame_delay
            srt_entry = f"{i}\n"
            srt_entry += f"{format_time(start_time)} --> {format_time(end_time)}\n"
            srt_entry += f"{function_code}\n\n"
            srt_content += srt_entry
            start_time = end_time
        return srt_content

    def format_time(time_in_seconds):
        hours = int(time_in_seconds / 3600)
        minutes = int((time_in_seconds % 3600) / 60)
        seconds = int(time_in_seconds % 60)
        milliseconds = int((time_in_seconds - int(time_in_seconds)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    with open('functions.txt', 'r') as file:
        functions_text = file.read()

    srt_content = generate_srt_from_functions(functions_text, frame_delay=5)

    with open('functions.srt', 'w') as srt_file:
        srt_file.write(srt_content)

if __name__ == '__main__':
        main()