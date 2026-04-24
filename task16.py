# input faylni ochamiz
input_file = open("Input/students.txt", "r")
data = input_file.read()

# ismlarni ajratamiz
names = data.split()

# output faylni ochamiz
output_file = open("Output/task16.txt", "w")

# filter qilamiz va yozamiz
for name in names:
    if len(name) > 5:
        output_file.write(name + " ")

# fayllarni yopamiz
input_file.close()
output_file.close()