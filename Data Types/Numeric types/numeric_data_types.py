"""
Python Documentation
Desc: Numeric data types in python
All right reserved Akintola Technologies Mar 2021 updt Aug 24
"""
# numeric datatypes(int, float, complex)
integer = 1
# numbers in other bases
bin_test = 0b100
oct_test = 0o100
hex_test = 0x100

# floating point numeric types
_float = 1.0

#complex number literal
_complex = 4 + 3j

# using the complex function
complex2 = complex(3, 4)
print(complex2)

# commutative property
com_complex = 4 + 3j == 3j + 4
# print(com_complex)

#addition of complex numbers
add = 6 + 2j + 4 + 3j
print(f"Complex number addition: {add}")

# .Accessing real and imaginary parts of a complex number
real = _complex.real
imaginary = _complex.imag
