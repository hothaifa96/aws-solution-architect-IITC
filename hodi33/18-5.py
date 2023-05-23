#
s = 'i love python'

print(s[7:])
print(s[7:14:-1])
print(s[-6:])
print(s[-6:14])
print(s[ s.index('p') : ])
print(s[ s.index('python') : ])
print(s[ s.rindex('python') : ])

#
# s= 'azzip evol i'
# print(s[::-1])
# print(s[14::-1])

# -------------------if ------------------
#
# print(type(False))
# # < > >= <= != ==
# numb1 = 4
# numb2 = 55
#
# print(f'{numb1} == {numb2} -> {numb1 == numb2}')
# print(f'{numb1} > {numb2} -> {numb1 > numb2}')
# print(f'{numb1} < {numb2} -> {numb1 < numb2}')
# print(f'{numb1} != {numb2} -> {numb1 != numb2}')
# print(f'{numb1} >= {numb2} -> {numb1 >= numb2}')
# print(f'{numb1} <= {numb2} -> {numb1 <= numb2}')

# print(0 < -6 and 1==1)


# if logical exp :
#     #True block
# else:
#     # FalseBlock

# age = 97
#
# if age >= 68:
#     print('you may drink 500 ml ')
# elif age > 18:
#     print('i challenge you to drink 3 l')
# else:
#     print('go home or drink almond milk')
# print('hangover')
#
a = 5555
b = 1
c = 19

# using if and condition print the greater number

# if a > b >= c:
#     print(f'max is : {a}')
# elif b > c:
#     print(f'max is : {b}')
# else:
#     print(f'max is : {c}')
#
print(f'max is : {a if b < a > c else b if b >= c else c}')
#
# print(max(a,b,c))

# x = int(input('enter a number : '))
# print(type(x))
# print(x//14)
#

# name = input('enter your name')

# print(name.isalpha())
# print(name.isspace())
# print(name.istitle())
# print('a' in name)
# print('love' not in name)
# print(name.isupper())


# print(len(name) )


# valid PIN is a 4 digit str that contains only digits
# write a code to receive from the user a pin
# print success if the password valid

pin = input('enter the pin')
if len(pin) == 4 and pin.isdigit() :
    print('success')
else:
    print('invalid')

print('success' if len(pin) == 4 and pin.isdigit() else 'invalid' )