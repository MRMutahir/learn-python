# thislist = ["apple", "banana", "cherry"]
# mylist = ["apple", "banana", "cherry","banana"]
# print("mylist >>>>>>>>>>>>>>>",mylist)
# print(type(mylist))
# print(len(mylist))
# print(thislist[0])
# print(thislist[1])
# print(thislist[2])
# print(thislist[-1])
# print(thislist[-2])

# 🔥 List Slicing Practice Questions
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Q1: First 3 fruits print karo.
# 👉 Output: ['apple', 'banana', 'cherry']
print(fruits[0],fruits[1],fruits[2])
print(fruits[0:3])
print(fruits[:3])
# done

# Q2: Last 2 fruits print karo.
# 👉 Output: ['melon', 'mango']
print(fruits[5])
print(fruits[6])
print(fruits[5:7])
# Done

# Q3: Middle 3 fruits (3rd, 4th, 5th) print karo.
# 👉 Output: ['cherry', 'orange', 'kiwi']
print(fruits[2:5])
# done

# Q4: Har doosra fruit print karo.
# 👉 Output: ['apple', 'cherry', 'kiwi', 'mango']
print(fruits[0:7:2])


# Q5: List ko reverse order me print karo (without using reverse method).
# 👉 Output: ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
fruits.reverse()
print(fruits)


# Q6: First 5 fruits lo aur unme se last 2 print karo.
# 👉 Output: ['orange', 'kiwi']
new_fruits = fruits[:5]
print(new_fruits[-2:])
# done


# ⚡ Bonus Tricky Question
nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[-5:-2]) 