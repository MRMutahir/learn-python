# text_revers = "Lordgy"
# new_text = " ".join(reversed(text_revers))
# # new_text = " ".join(reversed(text_revers))
# print(new_text)
# print(type(new_text))


# def reverse_string_loop(s):
#     reversed_s = "p"
#     print(reversed_s)
#     for char in s:
#         print(char)
#         reversed_s = char + reversed_s
#     return reversed_s

# my_string = "python"
# print(reverse_string_loop(my_string))  # Output: nohtyp


alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet in "b")
conunt = 0
new_word = alphabet.find("a")
if new_word != -1:
    conunt = conunt + 1

# print(new_word)