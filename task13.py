input_file = open("Input/students.txt", "r")
data = input_file.read().split()
data.sort()

output_file = open("Output/output13.txt", "w")
output_file.write(str(data))