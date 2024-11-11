def analyze_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        
        with open(output_file, 'w') as result_file:
            result_file.write(f"Lines: {num_lines}\n")
            result_file.write(f"Words: {num_words}\n")
            result_file.write(f"Characters: {num_chars}\n")
        
        print(f"Analysis written to {output_file}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example
analyze_text_file("input.txt", "output.txt")
