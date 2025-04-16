def read_file(file_name):
    """Attempts to read content from the specified file and handles errors."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content read successfully:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: The file '{file_name}' could not be read due to an I/O error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Prompt the user for a filename
    file_name = input("Enter the name of the file to read: ")
    
    # Attempt to read the file
    read_file(file_name)

if __name__ == "__main__":
    main()
