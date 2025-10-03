# text = "hello world"
text = "banana"
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
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
my_list  = []

# for alphabet in alphabets:
#     for vowel in vowels:
#         if vowel == alphabet:
#          my_list.append(alphabet)
# print(len(my_list))

# Optimized Version for GPT:
alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
my_list = []

# Direct check if character is vowel
# for alphabet in alphabets:
#     if alphabet in vowels:  # Check directly if alphabet is in vowels
#         my_list.append(alphabet)
# print(len(my_list))

# Check karo ke diya gaya string palindrome hai ya nahi.
def is_palindrome(char):
   string = char[::-1]
   return string == char

print(is_palindrome("madam"))