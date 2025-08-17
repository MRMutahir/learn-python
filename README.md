# Python Data Types  

Python me data types basically 2 categories me aate hain:  

---

## 1. Basic Types / Primitive Types  

- **str** → String  
- **int** → Number  
- **float** → Decimal Number  
- **bool** → True / False  
- **None** → Null ka Python version  

### Example:
```python
name = "Muhammad"   # str
age = 21            # int
height = 5.0        # float
is_active = True    # bool 
nothing = None      # NoneType
2. Collection Types
Multiple values store karne ke liye use hote hain.

1. List (JS array ki tarha)
Ordered hoti hai (index hota hai)

Changeable hoti hai (add/remove/change kar sakte ho)

Duplicate values allow karti hai

python
Copy
Edit
# List Example
mylist = ["name", "email", "password"]
print(mylist[0])   # Output: name
mylist.append("age")
print(mylist)      # ['name', 'email', 'password', 'age']
2. Tuple
Ordered hota hai (index hota hai)

Changeable nahi hota (immutable)

Duplicate values allow karta hai

python
Copy
Edit
# Tuple Example
mytuple = ("apple", "banana", "cherry")
print(mytuple[1])   # Output: banana
# mytuple[0] = "orange" ❌  (Error: tuple change nahi hota)
3. Set
Unordered hota hai (koi index nahi hota)

Changeable hota hai (items add/remove ho sakte hain)

Duplicate values allow nahi karta

python
Copy
Edit
# Set Example
myset = {"apple", "banana", "cherry", "apple"}
print(myset)   # Output: {'apple', 'banana', 'cherry'}  (duplicate remove ho gaya)
myset.add("orange")
print(myset)   # {'apple', 'banana', 'cherry', 'orange'}
4. Dictionary
Key : Value pairs me data store karta hai

Keys unique hote hain

Changeable hota hai

python
Copy
Edit
# Dictionary Example
mydict = {
  "name": "Ali",
  "email": "ali@example.com",
  "age": 21
}
print(mydict["name"])   # Output: Ali
mydict["age"] = 22      # value change ho gayi
print(mydict)           # {'name': 'Ali', 'email': 'ali@example.com', 'age': 22}
🔑 Short Summary
List → Ordered, changeable, duplicates allowed

Tuple → Ordered, not changeable, duplicates allowed

Set → Unordered, changeable, no duplicates

Dictionary → Key-Value store, changeable, keys unique