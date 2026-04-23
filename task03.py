input_file = open("Input/numbers.txt", "r")
data = input_file.read()

nums = data.split()
max_num = int(nums[0])
for num in nums:
    raq = int(num)
    if raq > max_num:
        max_num = raq
    

output_file = open("Output/output03.txt", "w")
output_file.write(str(max_num))

