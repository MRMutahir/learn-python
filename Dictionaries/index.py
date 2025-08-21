# users = {
#     "name":"Muhammad Mutahir",
#     "age":21,
#     "age":21,
#     "Number":3133978318
# }
# # print("users >>>>>>>>>>",users["name"])
# # print("users >>>>>>>>>>",users["age"])
# # print("users >>>>>>>>>>",users["Number"])
# print(users)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "color":["red","white","blue"]
# }
# print(len(thisdict))
# print(thisdict)
# print(type(thisdict))


# users = dict(name="Muhammad",age = 20,)
# print(users)


# users = {
#     "name":"Muhammad Mutahir",
#     "age":21,
#     "Number":3133978318
# }
# # x = users["name"]
# # print(users["name"])
# y = users.get("name")

# getKeys = users.keys()
# print(getKeys)


# cars = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = cars.keys()
# print("x >>>>>>>>>>>>>>>",x) # before

# cars["color"] = "white"

# x = cars.values()
# y = cars.keys()

# print("x >>>>>>>>>>>>>>>",x)
# print("y >>>>>>>>>",y)

# Make a change in the original dictionary, and see that the values list gets updated as well:


# user = {
# "name":"Muhammad",
# "age":20
# }
# # print("before",user.keys())
# # print("before",user.values())


# user["name"] = "Mutahir"

# # print("after",user.keys())
# print("after",user.values())

# x = user.items()
# print(x)

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# x = car["color"]= "red"
# x = car.items()

# print(x) #before the 

# car["year"] = 

print(car) #before the 
car.update({"year":2020})
car.update({"color":"red"})
print(car) # after

# print(x) # after


if "brand" in car:
  print("Yes, 'brand' is one of the keys in the thisdict dictionary")
else:
  print("No, 'brand' is one of the keys in the thisdict dictionary")
  
