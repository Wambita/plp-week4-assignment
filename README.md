# plp-week4-assignment

## Python File Handling & Error Handling Programs

## Overview

This repository contains two Python programs that demonstrate **file handling** and **exception handling** in Python. The first program reads a file, modifies its content, and writes the modified content to a new file. The second program prompts the user for a filename, attempts to read it, and handles errors if the file doesn't exist or can't be read.

### Program 1: File Handling and Exception Handling

This program focuses on handling basic file operations (reading and writing) and includes exception handling to manage potential errors.

#### Features:
- Reads content from a specified file.
- Modifies the file content (e.g., converting it to uppercase).
- Writes the modified content to a new file.
- Implements **exception handling** for various errors:
  - `FileNotFoundError`: Raised if the file doesn't exist.
  - `IOError`: Raised if there's an issue during reading or writing.
  - General exception handling for unexpected errors.

#### How to Use:
1. Run the script.
2. Enter the filename you want to read.
3. Enter the filename for the new file to write the modified content.

#### Example:

```
Enter the name of the file you want to read: example.txt
Enter the name of the new file to write the modified content: modified_example.txt
Modified content has been written to 'modified_example.txt'.
```

---

### Program 2: Error Handling Lab

This program asks the user for a filename and handles errors if the file doesn't exist or can't be read. It demonstrates how to handle different types of exceptions during file operations.

#### Features:
- Prompts the user to enter a file name.
- Attempts to read the file.
- Handles various errors:
  - `FileNotFoundError`: Raised if the file doesn't exist.
  - `IOError`: Raised if there’s an issue reading the file.
  - General exceptions are caught to handle any other unexpected errors.

#### How to Use:
1. Run the script.
2. Enter the filename you want to read.
3. If the file exists, its content is printed; otherwise, an error message is displayed.

#### Example:

```
Enter the name of the file to read: example.txt
File content read successfully:
This is the content of the file.
```

Or

```
Enter the name of the file to read: non_existing_file.txt
Error: The file 'non_existing_file.txt' does not exist.
```

---

## File Structure

```
- file_handling_program.py       # Program 1: File Handling and Exception Handling
- error_handling_lab.py          # Program 2: Error Handling Lab
```

---


## How to Run

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the Python scripts.
4. Run either script using the command:
   ```bash
   python file_handling_program.py
   ```
   or
   ```bash
   python error_handling_lab.py
   ```
