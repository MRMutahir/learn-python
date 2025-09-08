
# getFirstValue = input("Enter Number: ")
# getExpressionValue = input("Enter Expression: ")
# getSecValue = input("Enter Number: ")

# num1 = int(getFirstValue)
# exp = str(getExpressionValue)
# num3 = int(getSecValue)

# def calculator(one,expr,tow):
#     # sumValue = one + expr + tow
#     print("one",one)
#     print("one",type(one))
#     print("expr",expr)
#     print("two",tow)
#     # print("sumValue",sumValue)

# calculator(num1,exp,num3)


# one = 120
# exp = input("Enter Exp: ")
# two = 5

# calculat = 0
# if exp == "+":
#    calculat= one + two
# else:
#    calculat= one - two

# print(calculat)
    


getFirValue = int(input("Enter first value: "))
getSecExperesion = input("Enter an Expression (+, -, *, /): ")
getSecValue = int(input("Enter second value: "))

def my_calculator(val_one, val_two, val_exp):
    match val_exp:
        case "+":
            total_value = val_one + val_two
            print("+ kardo =", total_value)
        case "-":
            total_value = val_one - val_two
            print("- kardo =", total_value)
        case "*":
            total_value = val_one * val_two
            print("* kardo =", total_value)
        case "/":
            if val_two != 0:
                total_value = val_one / val_two
                print("/ kardo =", total_value)
            else:
                print("Division by zero not allowed!")
        case _:
            print("Invalid expression!")

if getFirValue and getSecValue and getSecExperesion:
    my_calculator(getFirValue, getSecValue, getSecExperesion)


