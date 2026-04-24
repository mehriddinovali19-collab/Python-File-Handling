input_file = open("input/numbers.txt", "r")
data = input_file.read()

odd = data.split()
numbers =[int(x) for x in odd]
odd_numbers = [num for num in numbers if num % 2 == 1] 


output_file = open("Output/output06.txt", "w")
output_file.write(str(odd_numbers))