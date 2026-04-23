input_file = open("Input/numbers.txt", "r")
data = input_file.read()

output_file = open("output/output01.txt", "w")
output_file.write(data)