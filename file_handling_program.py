# Function to read the content of a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except IOError as e:
        print(f"Error: An IOError occurred while reading the file '{file_name}'.")
        return None

# Function to write content to a new file
def write_to_new_file(new_file_name, modified_content):
    try:
        with open(new_file_name, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content successfully written to '{new_file_name}'.")
    except IOError as e:
        print(f"Error: An IOError occurred while writing to the file '{new_file_name}'.")

# Function to modify content : changing  to uppercase
def modify_content(content):
    modified_content = content.upper()  
    return modified_content

def main():
    input_file_name = input("Enter the name of the file to read: ")
    content = read_file(input_file_name)
    
    if content is not None:
        # Modify the content
        modified_content = modify_content(content)

        # Specify the name of the new file
        output_file_name = input("Enter the name for the new file: ")

        # Write the modified content to a new file
        write_to_new_file(output_file_name, modified_content)

if __name__ == "__main__":
    main()
