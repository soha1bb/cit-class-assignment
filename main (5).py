#Python program to copy the contents of a file to another file:
source_file = 'source.txt'
destination_file = 'destination.txt'

with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
        destination.write(source.read())

print(f"Contents of {source_file} copied to {destination_file}.")
