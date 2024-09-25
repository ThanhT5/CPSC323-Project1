def is_special_char(char):
    """Check if the character is a special character."""
    return char in "+-*/=;()>,"

def clean_file(input_file, output_file):
    """Clean the input file by removing unnecessary whitespace and comments, 
    and write the cleaned content to the output file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove leading and trailing whitespace
            line = line.strip()
            
            # Skip empty lines and comment lines
            if not line or line.startswith('//'):
                continue

            # Remove comments
            line = line.split('//')[0]
            
            cleaned_line = ""
            i = 0
            while i < len(line):
                # Handle 'cin>>' as a special case
                if i < len(line) - 3 and line[i:i+5] == "cin>>":
                    cleaned_line += " cin>> "
                    i += 5
                # Check for special characters
                elif is_special_char(line[i]):
                    cleaned_line += f" {line[i]} "
                    i += 1
                # Collect entire word or number
                elif line[i].isalnum() or line[i] == '_':
                    word_start = i
                    while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                        i += 1
                    cleaned_line += f" {line[word_start:i]} "
                else:
                    # Skip other characters (extra spaces, etc.)
                    i += 1
            
            # Remove extra spaces from the cleaned line
            cleaned_line = ' '.join(cleaned_line.split())
            
            # Write the cleaned line to the output file
            outfile.write(cleaned_line + '\n')

def main():
    """Main function to clean the specified input file and write to output file."""
    input_file = "file.txt"
    output_file = "clean.txt"
    clean_file(input_file, output_file)
    print(f"File cleaned successfully. Output written to {output_file}")

if __name__ == "__main__":
    main()