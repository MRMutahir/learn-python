print('SALAM world')  # This prints "SALAM world"

# Original list
names = ["Muhmmad", "Mutahir", "Talha",["matric","Inter","Uni"]]

# Importing the copy module
import copy 

# Creating a shallow copy of the list
listCopy = copy.copy(names)

# Printing the original list

# print(names)
# # # Printing the copied list
# print(listCopy)
# print(listCopy == names)
# print(listCopy is names)




nestedList = [["Muhmmad"], ["Mutahir", "Talha"]]
deepCopy = copy.deepcopy(nestedList)

# print(nestedList)
# print(deepCopy)
