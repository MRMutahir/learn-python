getValue = int(input("Enter a Number: "))

if getValue == "":
    print("Number dose not exits.")

for i in range(5,11):
    table = getValue * i
    print(f"{getValue} * {i} = {table}")