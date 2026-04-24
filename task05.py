input_file = open("input/numbers.txt", "r")
data = input_file.read()

av = data.split()
numbers = [int(x) for x in av]
total = sum(numbers)
count = len(numbers)
average = total / count



output_file = open("Output/output05.txt", "w")
output_file.write(str(average))