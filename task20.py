input_file = open("Input/grades.csv", "r")
data = input_file.read().splitlines()

grades = []

for line in data:
    parts = line.split(",")   # Ali,4 -> ["Ali", "4"]
    grades.append(int(parts[1]))

average = sum(grades) / len(grades)

output_f = open("Output/output20.txt", "w")
output_f.write(str(average))