input_file = open("Input/students.txt", "r")
data = input_file.read().split()
output_file = open("Output/output15.txt", "w")
for name in data:
    length = len(name)
    output_file.write(f"Ism: {name} | Ismning o'zinligi: {length} ")





