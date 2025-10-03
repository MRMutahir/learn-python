# # import platform

# # x = platform.system()
# # print(x)

# # text = "Hello"
# # print(dir(text))


# # num = 10 
# # print(dir(num))

# # print(dir())

# import math
# print(dir(math))

# from mymodule import person1 as hi


# print(hi)


# import datetime 

# x = datetime.datetime.now()

# # print(x.year)
# print(x.strftime("%A")) # %A se full day ka name ajyga.
# print(x.strftime("%a"))

# f = open("demofile.txt","r")
# # with open("demofile.txt") as f:
# #     print(f.read())

# print(f.readline())
# f.close()


# with open("demofile.txt", "a") as f:
#     f.write("SALAM Bro Kiya Hal hen jani. \n")


# with open("demofile.txt","a") as f:
#     f.write("ax arha hon \n")

# with open("demofile.txt") as f:
#    x = f.read()
# print(x)
 
 
# f = open("index.html","x") 

# import os
# os.rmdir("html")
# os.remove("demofile.txt")

# print(len("Hello")) # string ki length nikalega -> 5

# print(len([1, 2, 3, 4])) # list ke elements count karega -> 4

# print(len({1: "a", 2: "b"})) # dictionary ke keys count karega -> 2


# class Bird:
#     def speak(self):
#         return "Barking"


# class Dog:
#     def speak(self):
#         return "Chirping"


# for animal in (Bird(),Dog()):
#     print(animal.speak())



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(len(thisdict))



def myFun():
    x =300

    def myinnerfunc():
        print(x)
    myinnerfunc()
    # print(x)
myFun()