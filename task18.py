search_name = input("Qidirmoqchi bulgan ismingizni kiriting: ")

input_file = open("Input/students.txt", "r")
data = input_file.read().split()


output_file = open("Output/output18.txt", "w")

if search_name in data:
    output_file.write("FOUND")
else:
    output_file.write("NOT FOUND")