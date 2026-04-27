input_file = open("Input/grades.csv", "r")
data = input_file.read().replace(",", " ").split("")
grades = []
for item in data:
    if item.isdigit():
        grades.append(int(item))
average = sum(grades) / len(grades)

output_f = open("Output/output20.txt", "w")
output_f.write(str(average))
