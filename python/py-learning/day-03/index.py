# text = "hello world"
# text = "banana"
# print(text.find("heat")) # error not thorw if value not found
# print(text.index("heat")) # thow an error if value not found
# print("SALAM Bro")

# print(text.rfind("e"))
# print(text.rindex("e"))
# text = "banana"

# print(text.count("e"))

# filename = "report.pdf"
# # print(filename.startswith("heat"))
# print(filename.endswith("pdf"))

# Ek string me vowels (a, e, i, o, u) ki ginti count karo.
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiou"
# my_list  = []

# for alphabet in alphabets:
#     for vowel in vowels:
#         if vowel == alphabet:
#          my_list.append(alphabet)
# print(len(my_list))

# Optimized Version for GPT:
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiou"
# my_list = []

# Direct check if character is vowel
# for alphabet in alphabets:
#     if alphabet in vowels:  # Check directly if alphabet is in vowels
#         my_list.append(alphabet)
# print(len(my_list))

# Check karo ke diya gaya string palindrome hai ya nahi.
# def is_palindrome(char):
#    string = char[::-1]
#    return string == char

# print(is_palindrome("madam"))



# Ek number input lo aur check karo ke prime hai ya nahi.

# get_num = int(input("Enter a Number: "))

# def divide_By(get_number):
#     if get_number <= 1:
#         print("This is not a prime number")  # 1 or smaller numbers are not prime
#         return
    
#     for number in range(2, get_number):
#         divide_By_number = get_number % number
#         if divide_By_number == 0:
#             print("This is not a prime number")
#             return  # Break the loop if divisible
    
#     print("This is a prime number")  # Print this only if no divisor is found

# divide_By(get_num)


# number_of_sum = "4,5,6,7"
# number_of_sum_num = []

# number_of_sum_join = number_of_sum.split(",")
# print(number_of_sum_join)
# for num_list in number_of_sum_join:
#     new_num = int(num_list)
#     number_of_sum_num.append(new_num)
#     print(type(num_list))

# print(sum(number_of_sum_num))
# print(type(number_of_sum_num))


# new_list = [12, 3, 45, 7, 19]

# def check_max_and_min(get_list):
#     for list_item in get_list:
#       print(list_item)

# check_max_and_min(new_list)


# new_list = [80, 20, 300, 40, 2]

# def check_max_and_min(get_list):
#     # Initialize the first element as both max and min
#     max_value = get_list[0]
#     min_value = get_list[0]

#     print(max_value)
#     print(min_value)
    
#     # Loop through the list to find max and min
#     for list_item in get_list:
#         if list_item > max_value:
#             max_value = list_item
#         if list_item < min_value:
#             min_value = list_item
    
#     print("Maximum:", max_value)
#     print("Minimum:", min_value)

# check_max_and_min(new_list)


input_list = [10, 20, 30, 20, 40, 50, 10, 60]
print(input_list)
my_sets = set(input_list)
input_list =list(my_sets)
print(my_sets)
print(input_list)
