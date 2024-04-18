"""10-1: Learning Python"""

# Read entire file

filename = 'learning_python.txt'

with open(filename) as file_object:
    read_file = file_object.read()
    print(read_file)

# Print once by looping over the file object

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())



# Store the lines in a list and then work with them outside of
# the with block

filename = 'learning_python.txt'

with open(filename) as file_object:
    line_list = file_object.readlines()

file_line_list = ''
for line in line_list:
    file_line_list += line

print(file_line_list)


"""10-2: Learning C"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    line_list = file_object.readlines()

file_line_list = ''
for line in line_list:
    file_line_list += line

print(file_line_list.replace('Python','C'))

