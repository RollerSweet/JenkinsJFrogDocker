import os
import zipfile
import sys

# Create an array of letters from 'a' to 'z'
letters = [chr(ord('a') + i) for i in range(26)]

# Create txt files
for letter in letters:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write("This is the content of " + filename)

        if not os.path.exists(filename):
            print(f"Failed to create {filename}")
            sys.exit(1)
        else:
            print(f"Created {filename}")

# Create zip files with version "1.2.0"
version = os.getenv('VERSION')

for letter in letters:
    txt_filename = f"{letter}.txt"
    zip_filename = f"{letter}_{version}.zip"

    with zipfile.ZipFile(zip_filename, "w") as zipf:
        zipf.write(txt_filename)

        if not os.path.exists(zip_filename):
            print(f"Failed to create {zip_filename}")
            sys.exit(1)
        else:
            print(f"Created {zip_filename} with {txt_filename}")

print("All tasks completed successfully.")