# # # users = {
# # #     "name":"Muhammad Mutahir",
# # #     "age":21,
# # #     "age":21,
# # #     "Number":3133978318
# # # }
# # # # print("users >>>>>>>>>>",users["name"])
# # # # print("users >>>>>>>>>>",users["age"])
# # # # print("users >>>>>>>>>>",users["Number"])
# # # print(users)

# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964,
# # #   "color":["red","white","blue"]
# # # }
# # # print(len(thisdict))
# # # print(thisdict)
# # # print(type(thisdict))


# # # users = dict(name="Muhammad",age = 20,)
# # # print(users)


# # # users = {
# # #     "name":"Muhammad Mutahir",
# # #     "age":21,
# # #     "Number":3133978318
# # # }
# # # # x = users["name"]
# # # # print(users["name"])
# # # y = users.get("name")

# # # getKeys = users.keys()
# # # print(getKeys)


# # # cars = {
# # # "brand": "Ford",
# # # "model": "Mustang",
# # # "year": 1964
# # # }
# # # x = cars.keys()
# # # print("x >>>>>>>>>>>>>>>",x) # before

# # # cars["color"] = "white"

# # # x = cars.values()
# # # y = cars.keys()

# # # print("x >>>>>>>>>>>>>>>",x)
# # # print("y >>>>>>>>>",y)

# # # Make a change in the original dictionary, and see that the values list gets updated as well:


# # # user = {
# # # "name":"Muhammad",
# # # "age":20
# # # }
# # # # print("before",user.keys())
# # # # print("before",user.values())


# # # user["name"] = "Mutahir"

# # # # print("after",user.keys())
# # # print("after",user.values())

# # # x = user.items()
# # # print(x)

# # # The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

# # car = {
# # "brand": "Ford",
# # "model": "Mustang",
# # "year": 1964
# # }

# # # x = car["color"]= "red"
# # # x = car.items()

# # # print(x) #before the 

# # # car["year"] = 

# # # print(car) #before the 
# # # car.update({"year":2020})
# # # car.update({"color":"red"})
# # # print(car) # after

# # # # print(x) # after


# # # if "brand" in car:
# # #   print("Yes, 'brand' is one of the keys in the thisdict dictionary")
# # # else:
# # #   print("No, 'brand' is one of the keys in the thisdict dictionary")
  



# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.pop("brand")
# # # thisdict.popitem()

# # # if "brand" in thisdict:
# # #   del thisdict["brand"]
# # # else:
# # #   thisdict["hello"] ="Mutahir"
# # # print("after >>>>>>>>",thisdict)
# # # # del thisdict
# # # thisdict.clear()
# # # print("before",thisdict)


# # users = {
# #   "name" :"Muhammad Mutahir",
# #   "age":20,
# # }
# # # print(users["name"])

# # # for y in users.keys():
# # #   print(y)
  
# # # for x in users.values():
# # #   print(x)
  
# # # for x ,y in users.items():
# # #   print(x,y)

# # # newUser = users.copy()
# # # # newUser = dict(users)


# # # print(newUser)

# # students = {
# #   "st_1" :{
# #     "name":"Ali",
# #     "age":20,
# #     "roll":12345
# #   },
# #     "st_2" :{
# #     "name":"Hamad",
# #     "age":20,
# #     "roll":85545
# #   }
# # }

# # print(students["st_1"]["name"])



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.popitem()

# print(x)
# print(car)

# 📝 Python Dictionary Practice Questions

student = {"name": "Mutahir", "age": 21, "city": "Karachi"}
# print("name",student["name"])
# print("age",student["age"])
# print("city",student['city'])
student["skills"] =["Python","Javascript"]
name = student.get("name")
# print(name)
# print("student",student)
# print("type student",type(student))


car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

car["model"] = "Yaris"

car["color"] = "white"

del car["year"]

# print("car",car)


user = {"username": "mutahir", "password": "1234"}

user["password"] = "hash"

# if "email" in user:
#   print("you are successful login")
# else:
#   print("User not found")

marks = {"math": 90, "english": 85, "science": 92}

allKeys = marks.keys()
allValue = marks.values()
allKeysAndValue = marks.items()
# print("allKeys",allKeys)
# print("allValue",allValue)
# print("allKeysAndValue",allKeysAndValue)

# for x,y in marks.items():
  # print(f"{x}:{y}")


students = {
    "student1": {"name": "Ali", "age": 20},
    "student2": {"name": "Ahmed", "age": 22}
}
# print( "Student1 ka name", students["student1"]["name"])
# print( "Student2 ka age", students["student2"]["age"])

cart = {
    "shoes": 2,
    "t-shirt": 3,
    "watch": 1
}

# totalItem = cart["shoes"] + cart["t-shirt"] + cart["watch"]
# print("totalItem",totalItem)
getValue = sum(cart.values())
# cart["cap"] =2
# print("cart",cart)
# cart.pop("cap")
# print("cart",cart)
# print("getValue",getValue)


employees = {
    "emp1": {"name": "Ali", "salary": 50000},
    "emp2": {"name": "Ahmed", "salary": 60000},
    "emp3": {"name": "Sara", "salary": 70000}
}

# employee = employees.items()
# print(employees)

for singleEm in employees.values():
  number = singleEm["salary"]
  # print(average)
  

print(number)