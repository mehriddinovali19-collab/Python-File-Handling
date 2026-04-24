input_file = open("Input/students.txt", "r")
data = input_file.read().split()
output_file = open("Output/output16.txt", "w")
for name in data:
    if len(name) > 5:
        output_file.write(name + " ")