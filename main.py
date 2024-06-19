def load_morse_code(filename):
    # An empty dictionary to hold Mose Code mappings
    morse_dict = {}

    # Open the morse code file
    with open(filename, 'r') as file:
        # Read the file line by line
        for line in file:
            # Split each line into character and its corresponding Morse code
            char, morse = line.strip().split('\t')
            # Add the character and Morse code to the dictionary
            morse_dict[char] = morse

        # Return the completed Morse code dictionary
        return morse_dict


def text_to_morse(text, morse_filename='morse_code.txt'):   # Create function to take text and morse code file
    # Load the Morse code dictionary from the given file
    morse_dict = load_morse_code(morse_filename)
    # Initialize an empty string to build the Morse code conversion
    morse_conversion = ''

    # Iterate over each character in the input text, converted to uppercase
    for char in text.upper():
        # Check if the character is in the Morse code dictionary
        if char in morse_dict:
            # Append the corresponding Morse code and a space to the result
            morse_conversion += morse_dict[char] + " "
        elif char == " ":
            # If the character is a space, add two spaces for word separation
            morse_conversion += "  "
        else:
            # For any unknown characters, add a placeholder
            morse_conversion += "<unknown> "

    # Return the final Morse code conversion, removing any trailing spaces
    return morse_conversion.strip()


# Define the input text to be converted to Morse code
input_text = "Text to morse code 123'?/"
# Convert the input text to Morse code using the text_to_morse function
morse_code = text_to_morse(input_text)
# Print the original text
print(f"Text: {input_text}")
# Print the converted Morse code
print(f"Morse Code: {morse_code}")
