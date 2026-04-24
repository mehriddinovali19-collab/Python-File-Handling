input_file = open("Input/numbers.txt", "r")
data = input_file.read()

five = data.split()
numbers =[int(x) for x in five]

five_multi = [num for num in numbers if num % 5 == 0]
count = len(five_multi)

Output_file = open("Output/output08.txt", "w")
Output_file.write(f"Sonlar: {five_multi}\nSoni: {count}")




