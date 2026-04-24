input_file = open("Input/students.txt", "r")
data = input_file.read().split()
output_file = open("Output/output17.txt", "w")
for name in data:
    if name.startswith("A"):
        output_file.write(name + " " )