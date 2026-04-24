input_file = open("Input/numbers.txt", "r")
data = input_file.read()

numbers = [int(x) for x in data.split()]
numbers.sort()

output_file = open("Output/output10.txt", "w")

for num in numbers:
    output_file.write(str(num) + " ")