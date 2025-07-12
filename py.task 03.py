import os

f = input("Enter the file: ")
if os.path.exists(f):
    print(open(f).read())
else:
    print("File not found. Exiting.")
