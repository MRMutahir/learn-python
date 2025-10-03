# get_num = int(input("Enter your number: "))
# print(get_num)

# get_num = get_num % 2
# print(get_num)

# if get_num == 0:
#     print("this is even number")
# else:
#     print("this is odd number")



num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
num3 = int(input("Enter Number: "))

# print(num1)
# print(num2)
# print(num3)

if num1 > num2:
    print("num1 is big")
elif num2 > num1:
    print("num2 is big")
elif num3 > num1 or num3 > num2:
    print("num3 is big")

