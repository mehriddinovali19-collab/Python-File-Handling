input_file = open("Input/numbers.txt", "r")
data = input_file.read().split()
output_file = open("Output/output09.txt", "w")

for num in data:
    length = len(num)
    output_file.write(f"{num} soni {length} xonali\n")