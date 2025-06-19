    # example_script.py
import os

BASE_PATH = '\Bhanu'

# Print the path of the current script
print(f"The current script is located at: {__file__}")
#print(f"{__file__ }" + BASE_PATH )

print('File name :    ', os.path.basename(__file__))
print('Directory Name:     ', os.path.dirname(__file__))

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
print(f"The script directory is: {script_dir}")
print("The script directory is: " + script_dir)

# Construct a path to a file in the same directory
file_path = os.path.join(script_dir, 'example_file.txt')
print(f"The path to the example file is: {file_path}")
