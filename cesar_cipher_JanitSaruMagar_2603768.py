def welcome():
    """Display welcome message for the Caesar Cipher program."""
    print("Welcome to the Caesar Cipher")
    print("\nThis program encrypts and decrypts text with the Caesar Cipher.\n")


def enter_message():
    """Get mode (encrypt/decrypt), message, and shift value from user input.
    
    Prompts user to choose 'e' for encrypt or 'd' for decrypt.
    Accepts a message string.
    Ensures shift value is an integer between 1 and 25.
    Returns:
        tuple:(mode, message, shift)
    """
    while True:
        mode = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
        if mode in ['e', 'd']:
            break
        print("Invalid! Please enter 'e' or 'd'.")
    message = input("Enter your message: ").lower()
    while True:
        try: 
            # contains code that might be an error
            shift = int(input("Enter shift number (1-25): "))
            if 1 <= shift <= 25:
                break
            print("Please enter a number between 1 and 25.")
        except:
            # code to run if there is an error in try block
            print("Please enter a valid number.")
    return mode, message, shift


def encrypt(message, shift):
    """Encrypt a message using Caesar Cipher.
    
    Args:
        message (str): The text to encrypt.
        shift (int): The shift value (1–25).
    
    Returns:
        str: Encrypted message in uppercase.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in message:
        if letter == ' ':
            result += ' '
        elif letter in letters:
            new_index = (letters.find(letter) + shift) % 26
            result += letters[new_index]
        else:
            result += letter
    return result.upper()


def decrypt(message, shift):
    """Decrypt a message using Caesar Cipher.
    
    Args:
        message (str): The encrypted text.
        shift (int): The shift value used during encryption.
    
    Returns:
        str: Decrypted message in uppercase.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in message:
        if letter == ' ':
            result += ' '
        elif letter in letters:
            new_index = (letters.find(letter) - shift) % 26
            result += letters[new_index]
        else:
            result += letter
    return result.upper()


def process_file(filename, mode, shift):
    """Process a file containing messages for encryption or decryption.
    
    Args:
        filename (str): Path to the input file.
        mode (str): 'e' for encrypt, 'd' for decrypt.
        shift (int): Shift value for Caesar Cipher.
    
    Returns:
        list: Processed lines (encrypted or decrypted).
    """
    results = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                msg = line.strip().lower()
                if mode == 'e':
                    processed = encrypt(msg, shift)
                else:
                    processed = decrypt(msg, shift)
                results.append(processed)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        results = []
    except Exception as e:
        print(f"Error reading file: {e}")
        results = []
    return results


def write_messages(messages):
    """Write processed messages to results.txt file.
    Args:
        messages (list): List of encrypted/decrypted strings.
    """
    with open('results.txt', 'w') as f:
        for msg in messages:
            f.write(msg + '\n')


def message_or_file():
    """Prompt user to choose input method (console or file).
    
    Returns:
        tuple: (mode, message, filename, shift)
    """
    # Tuple is the immutable version of a list. It is used to store multiple items in a single variable.
    while True:
        mode_input = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode_input in ['e', 'd']:
            mode = mode_input
            break
        print("Invalid Mode")
    while True:
        choice = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if choice in ['f', 'c']:
            break
        print("Invalid choice, please enter 'f' or 'c'.")
    while True:
        try:
            shift = int(input("What is the shift number: "))
            if 1 <= shift <= 26:
                break
            print("Invalid Shift")
        except:
            print("Invalid Shift")
    if choice == 'c':
        message = input(
            f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: "
        ).lower()
        return mode, message, None, shift
    else:
        while True:
            filename = input("Enter a filename: ")
            try:
                with open(filename, 'r'):
                    return mode, None, filename, shift
            except FileNotFoundError:
                print("Invalid Filename. File not found.")
            except Exception:
                print("Invalid Filename cannot read file.")
# Returns MODE, MESSAGE, FILENAME, SHIFT.

def main():
    """Main program loop for Caesar Cipher.
    
    - Displays welcome message.
    - Prompts user for input method (console/file).
    - Encrypts or decrypts messages.
    - Writes results to file if needed.
    - Allows repeated use until user exits.
    """
    welcome()
    # This function is used to print the welcome message when the program starts. It is defined before the main() function, so it can be called within main().
    while True:
        mode, console_message, filename, shift = message_or_file()
        if console_message is not None:
            if mode == 'e':
                result = encrypt(console_message, shift)
                print(result)
            else:
                result = decrypt(console_message, shift)
                print(result)
        else:
            results = process_file(filename, mode, shift)
            if results:
                write_messages(results)
                print("Output written to results.txt")
        while True:
            again = input(
                "Would you like to encrypt or decrypt another message? (y/n): "
            ).lower()
            if again in ['y', 'n']:
                break
            print("Invalid response, please enter 'y' or 'n'.")
        if again == 'n':
            print("Thanks for using the program.")
            break
main()
