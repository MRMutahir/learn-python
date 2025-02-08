# try:
#    num1:int = int(input("Enter first number"))
#    num2:int = int(input("Enter sec number"))
#    sum = num1 + num2
#    print(sum)

# except ValueError:
#    print("❌ Error: Please enter a valid integer number!")





# try:
#     evenOddNum = int(input("Enter a number: "))  
    
#     if (evenOddNum % 2) == 0:
#         # print(evenOddNum, " is Even number")
#         print(f"{evenOddNum} is an Even number")  # Extra space diya
       
#     else:
#         print(str(evenOddNum) + "is Odd number")

# except ValueError:
#     print("❌ Invalid input! Please enter a valid integer number.")

    

numInt = 2 #integer 
numFloat = 2.3 #decimal 




import math

try:
    giveNum = float(input("Enter Number: "))  
    print(f"Ceil value: {math.ceil(giveNum)}")  
    print(f"Floor value: {math.floor(giveNum)}")  

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")


import math

try:
    num = int(input("Enter Number"))
    print(f"{num} factorial {math.factorial(num)}")
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")

