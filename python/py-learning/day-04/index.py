class Students:
    scl_name = "The Karachi ites School"
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self._scl_name = self.scl_name

    def print_name(self):
        print("this is python method")


# Multiple students ka data
students_list = [
    Students("Muhammad", "mutahir@devxtech.com", "!Abc@321"),
    Students("Ayesha", "ayesha@gmail.com", "Ayesha@123"),
    Students("Ali", "ali.khan@yahoo.com", "Ali@456"),
    Students("Sara", "sara123@hotmail.com", "Sara@789"),
    Students("Usman", "usman.devxtech@gmail.com", "Usman@101")
]

# Har student ka data print karna
for student in students_list:
    print(f"Name: {student.name}, Email: {student.email}, Password: {student.password} , School Name : {student.scl_name}")


s1 = Students("Usama", "usama.devxtech@gmail.com", "Uasma@101")
s1.print_name()
# print()
