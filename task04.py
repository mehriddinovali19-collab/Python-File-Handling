input_file = open("Input/numbers.txt", "r")
data = input_file.read()

even = data.split()
numbers = [int(x) for x in even]
even_num = [num for num in numbers if num % 2 == 0]

output_file = open("Output/output04.txt", "w")
output_file.write(str(even_num))


     