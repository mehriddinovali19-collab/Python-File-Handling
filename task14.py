input_file = open("Input/students.txt", "r")
data = input_file.read().split()

reversed_data = data[::-1]

output_file = open("Output/output14.txt", "w")
output_file.write(str(reversed_data))
