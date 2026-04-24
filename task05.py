input_file = open("input/numbers.txt", "r")
data = input_file.read()

av = data.split()
numbers = [int(x) for x in av]
total = sum(numbers)
count = len(numbers)
average = total / count
print(str(average))

