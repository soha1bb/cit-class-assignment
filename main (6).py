#Python program to create a file with English alphabet letters listed:
def create_alphabet_file(filename, letters_per_line):
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  with open(filename, 'w') as file:
      for i in range(0, len(alphabet), letters_per_line):
          line = alphabet[i:i+letters_per_line]
          file.write(line + '\n')

# Example usage:
output_file = 'alphabet_file.txt'
letters_per_line = 5
create_alphabet_file(output_file, letters_per_line)
print(f"File '{output_file}' created with the English alphabet listed.")
