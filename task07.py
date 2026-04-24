input_file = open("input/numbers.txt", "r")
data = input_file.read()

kv = data.split()
numbers = [int(x) for x in kv]

output_file = open("Output/output07.txt", "w") 

for num in numbers:
    result = pow(num, 2)
    output_file.write(str(result) + "\n") 


    


