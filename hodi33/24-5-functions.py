# def my_max(a, b):
#     return (a if a > b else b)
#
#
# #      => |function| =>
#
# print(my_max(5, 7))
# # max = my_max(5, 111)


# def greet():
#     print('hello')
#
#
# def greet_with_name(name, age, salary):
#     print(age)
#     print(name)
#     print(salary)

#
# greet_with_name('moshe', 9, 99000)
# greet_with_name(age=16, name='yael', salary=1000)
#
# st1 = ['eran', 25, 120000]
# greet_with_name(st1[0], st1[1], st1[2])
# name = 'maxim'
# age = '27'
# salary = 88999
# greet_with_name(name,age,salary)
#
# def foo(name):
#     print(name)

#
# x = 5
#
#
# def foo():
#     x=12
#     print(x)
#
#
# foo()

# Write a Python function to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


# def rev_word():
#     word = input('enter str')
#     # word = word[::-1]
#     # return word
#     print(word[::-1])


# Write a Python function to check whether a
# number falls within a given range.
# the function must receive 3 args
# value  max min        3   5 9    5   -9   11

# x = int(input('please enter the value : '))
# un = int(input('please enter under limit : '))
# up = int(input('please enter upper limit : '))
#
#
# def check_in_range(x, start, end):
#     return start <= x <= end
#
#
# print(check_in_range(x, un, up))

# Write a Python program to detect
# the number of local variables declared in a function.

g = 77
x = 77


def foo():
    a = 'hodi'
    b = 'love pizza'
    g = 66

    print(a, b, x, g)
    print(foo.__code__.co_nlocals)


foo()
