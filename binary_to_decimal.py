def binary_to_decimal(binary_str):
    """Convert binary string to decimal."""
    try:
        return int(binary_str, 2)  # Convert binary to decimal
    except ValueError:  # Handle invalid binary input
        return "Invalid binary input"

def array_to_string(array):
    """Convert an array to a string representation."""
    result = ""
    for i in range(len(array)):  # Loop through array elements
        result += str(array[i])  # Convert each element to string
        if i < len(array) - 1:  # Check if it's not the last element
            result += ", "  # Add a comma for separation
    return result  # Return the formatted string

def translate_assembly(assembly_instruction):
    """Translate assembly language instruction."""
    translation_dict = {  # Dictionary of translations
        'MOV': 'Move data from one location to another',
        'ADD': 'Add two values',
        'SUB': 'Subtract one value from another',
        'JMP': 'Jump to a specific memory address',
        'CMP': 'Compare two values',  # Add more instructions if needed
        'JNE': 'Jump if not equal', 
        'JE': 'Jump if equal',
        'CALL': 'Call a subroutine',
        'RET': 'Return from a subroutine'
    }
    return translation_dict.get(assembly_instruction, 'Unknown instruction')  # Return translation

def calculator():
    """Main calculator function."""
    print("Welcome to the Translator Calculator!")  # Greeting
    while True:
        print("\nSelect an option:")  # Menu options
        print("1. Binary to Decimal")
        print("2. Array Representation")
        print("3. Assembly Language Translation")
        print("4. Exit")
        
        choice = input("Enter your choice: ")  # User input for choice
        
        if choice == '1':  # Binary to Decimal option
            binary_input = input("Enter a binary number: ")  # Input binary number
            decimal_output = binary_to_decimal(binary_input)  # Call conversion function
            print(f"Decimal: {decimal_output}")  # Output result
        
        elif choice == '2':  # Array Representation option
            array_input = input("Enter an array (comma separated): ")  # Input array
            try:
                array = list(map(int, array_input.split(',')))  # Convert input to array
                print(f"Array: {array_to_string(array)}")  # Output formatted array
            except ValueError:  # Handle invalid array input
                print("Invalid array input")
        
        elif choice == '3':  # Assembly Language Translation option
            assembly_input = input("Enter an assembly instruction: ")  # Input instruction
            translation = translate_assembly(assembly_input)  # Call translation function
            print(f"Translation: {translation}")  # Output translation
        
        elif choice == '4':  # Exit option
            print("Exiting...")  # Exit message
            break  # Exit the loop
        
        else:  # Invalid choice handling
            print("Invalid choice, please try again.")  # Prompt user to try again

if __name__ == "__main__":  # Main execution point
    calculator()  # Call the calculator function
