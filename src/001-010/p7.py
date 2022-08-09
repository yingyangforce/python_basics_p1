#------------------------------------------------------------
# | p7 - | take a filename from user and print its extension
#------------------------------------------------------------

import sys

if len(sys.argv) > 1:
    filename = sys.argv[-1]
else:
    filename = input(
    "Please enter a filename with its extension: ")

if len(filename.split('.')) != 2:
    print("Err, please enter valid filename + extension.")
else: # grab text after last '.'
    print(f"File extension is .{filename.split('.')[-1]}")

