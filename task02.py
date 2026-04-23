input_file = open("Input/numbers.txt", "r")
data = input_file.read()

nums = data.split()
total = 0
for num in nums:
    total += int(num)
output_file = open("Output/output02.txt", "w")
output_file.write(str(total))





