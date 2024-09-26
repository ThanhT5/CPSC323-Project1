# Define the given arrays for reserved words, operators, and special symbols
RESERVED_WORDS = ["cin>>", "for", "int", "while"]
OPERATORS = ["+", "-", "*", "/", "++", "--"]
SPECIAL_SYMBOLS = [">", "=", ";", "(", ")", ">=", ","]

def is_number(lexeme):
    """Check if the lexeme is a signed or unsigned integer."""
    if lexeme.startswith(('-', '+')) and lexeme[1:].isdigit():
        return True  # Check if the entire string is a signed number
    return lexeme.isdigit()  # Check if the entire string is a digit

def is_identifier(lexeme):
    """Check if the lexeme is a valid identifier."""
    if not lexeme[0].isalpha() and lexeme[0] != '_':
        return False  # Identifiers must start with a letter or underscore
    return all(c.isalnum() or c == '_' for c in lexeme[1:])  # Check the rest of the characters

def analyze_lexeme(lexeme):
    """Analyze the lexeme and determine its type."""
    lexeme_lower = lexeme.lower()  # Case-insensitive comparison
    
    if lexeme_lower in (word.lower() for word in RESERVED_WORDS):
        return "reserved word"
    elif lexeme in OPERATORS:
        return "operator"
    elif lexeme in SPECIAL_SYMBOLS:
        return "special symbol"
    elif is_number(lexeme):
        return "number"
    elif is_identifier(lexeme):
        return "identifier"
    else:
        return "invalid"  # If none of the above, it's invalid

def split_into_lexemes(line):
    """Split a line of code into individual lexemes."""
    lexemes = []
    current_lexeme = ""
    i = 0
    while i < len(line):
        if line[i].isspace():
            if current_lexeme:
                lexemes.append(current_lexeme)
                current_lexeme = ""
            i += 1
        elif i < len(line) - 3 and line[i:i+5] == "cin>>":
            if current_lexeme:
                lexemes.append(current_lexeme)
            lexemes.append("cin>>")
            current_lexeme = ""
            i += 5
        elif i < len(line) - 1 and line[i:i+2] in ["++", "--", ">="]:
            if current_lexeme:
                lexemes.append(current_lexeme)
            lexemes.append(line[i:i+2])
            current_lexeme = ""
            i += 2
        elif line[i] in "+-*/=>(),;":
            if current_lexeme:
                lexemes.append(current_lexeme)
                current_lexeme = ""
            if i < len(line) - 1 and line[i] in "+-" and line[i+1].isdigit():
                # Handle negative or positive numbers
                current_lexeme = line[i]
            else:
                lexemes.append(line[i])
            i += 1
        else:
            current_lexeme += line[i]
            i += 1
    if current_lexeme:
        lexemes.append(current_lexeme)
    return lexemes

def main():
    """Main function to interact with the user and analyze input statements."""
    while True:
        user_input = input("Enter a statement: ")  # Prompt for user input
        if user_input.lower() == 'quit':
            break
        
        if len(user_input) > 255:
                    print("Input truncated to 255 characters.")
        # Truncate input to 255 characters
        user_input = user_input[:255]

        lexemes = split_into_lexemes(user_input)  # Split the input into lexemes
        for lexeme in lexemes:
            lexeme_type = analyze_lexeme(lexeme)  # Analyze each lexeme
            print(f"{lexeme} {lexeme_type}")  # Print the lexeme and its type
        
        print()  # Empty line for readability
        
        # Prompt to continue or exit
        continue_input = input("CONTINUE(y/n)? ")
        if continue_input.lower() != 'y':
            break

if __name__ == "__main__":
    main()  # Execute the main function