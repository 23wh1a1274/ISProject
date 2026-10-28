
# File Integrity Verification System Using SHA-256

## Overview
A Python-based file integrity verification system that detects
file modifications by calculating and comparing SHA-256 hashes.

## Features
- Calculate SHA-256 hashes for files.
- Register trusted reference hashes.
- Verify file integrity against saved hashes.
- Detect modifications to file contents.
- Handle missing files and file access errors.
- Read files in chunks to support large files.

## Technologies Used
- Python 3
- hashlib
- json
- pathlib
- Git and GitHub

## How It Works
1. Select a file to register.
2. The application calculates its SHA-256 hash.
3. The hash is saved in a local JSON database.
4. Select the same file for verification.
5. The application compares the current hash with
   the stored hash.
6. Matching hashes indicate unchanged contents;
   different hashes indicate a possible modification.

## Prerequisites
- Python 3 installed
- Visual Studio Code (optional)

## Run the Project

Clone the repository and open its directory.

Run:

    python file_integrity.py

Choose option 1 to register a file.
Choose option 2 to verify a file.
Choose option 3 to exit.

## Testing
1. Register sample.txt.
2. Verify it without changing its contents.
3. Modify sample.txt and save it.
4. Verify again and observe the modification warning.

## Limitations
The reference hash database is stored locally and is not
protected against a malicious user who can modify both the
file and its saved reference hash. For stronger security,
store trusted hashes in a protected or independently
controlled location.

## Author
Tanishqa Kalidindi 
23WH1A1274 
IS Project

