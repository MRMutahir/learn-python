1. Basic Arithmetic Operations

Operator	Description	Example	Result

+	Addition	5 + 3	8

-	Subtraction	5 - 3	2

*	Multiplication	5 * 3	15

/	Division	5 / 3	1.666...

//	Floor Division	5 // 3	1

%	Modulus (Remainder)	5 % 3	2

**	Exponentiation	5 ** 3	125


2. Comparison Operations

Operator	Description	Example	Result

==	Equal to	5 == 3	False

!=	Not equal to	5 != 3	True

>	Greater than	5 > 3	True

<	Less than	5 < 3	False

>=	Greater than or equal to	5 >= 3	True

<=	Less than or equal to	5 <= 3	False


1. Complex Numbers
- A complex number has two parts: a real part and an imaginary part.
- In Python, complex numbers are written as real + imagj.

z = 3 + 4j
print(type(z))  # <class 'complex'>
print(z.real)   # 3.0
print(z.imag)   # 4.0

2. Octal Numbers
- Octal numbers use base 8 and are represented with a prefix 0o.

num = 0o10  # Octal for 8 in decimal
print(num)  # 8

ayota number


4. Bitwise Operations
- Bitwise operations work directly on binary representations of numbers.
- Shift Left (<<): Multiplies a number by 2^n.

Example:
result = 1 << 2  # Equivalent to 1 * 2^2
print(result)


5. Random Numbers
- The random module in Python is used to generate random numbers.

random.random()
Generates a random floating-point number between 0 and 1.
Example:

import random
print(random.random())  # 0.3672147020812294 (output will vary)
random.randint(a, b)
Generates a random integer between a and b.
Example:

print(random.randint(1, 20))  # 16 (output will vary)
random.choice(sequence)
Picks a random element from a sequence (like a list).
Example:

l1 = ['a', 'b', 'c']
print(random.choice(l1))  # 'a' (output will vary)
random.shuffle(sequence)
Shuffles the elements of a sequence in place.
Example:

random.shuffle(l1)
print(l1)  # ['b', 'a', 'c'] (output will vary)

6. Floating-Point Precision Issue
- Floating-point numbers in Python can lead to small precision errors.
Example:

print((0.1 + 0.1 + 0.1) - 0.3)  # 5.551115123125783e-17

To handle precision issues, use the Decimal module:

from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(result)  # Decimal('0.0')

7. Fractions
Use the fractions module to handle fractions in Python.
Example:
from fractions import Fraction
fraction = Fraction(1, 3)
print(fraction)  # 1/3



8. Math with Sets
Set Operations: Perform operations like union, intersection, and difference.
Example:

setone = {1, 2, 3, 4}
print(setone - {1, 2})  # {3, 4} (difference)
print(setone | {5})     # {1, 2, 3, 4, 5} (union)


Check Data Type
Use the type() function to check the data type of a variable.
Example:

print(type({}))  # <class 'dict'>
print(type([]))  # <class 'list'>



Examples:
Octal Conversion

oct(64)
# Output: '0o100'
Hexadecimal Conversion

hex(64)
# Output: '0x40'
Binary Conversion

bin(78)
# Output: '0b1001110'
Integer Conversion from Binary String

int('10000', 2)
# Output: 16