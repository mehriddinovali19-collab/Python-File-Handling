input_file = open("Input/grades.csv", "r")
data = input_file.read().split("\n")

output_file = open("Output/output19.txt", "w")

for line in data: 
    if line:
        name, grade = line.strip().split(",")
        output_file.write(f"Name: {name}, Grade: {grade}\n")
