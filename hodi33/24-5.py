# write python code to print thr length of the username
# and then print 1.. 2.. 3.. 4.. 5.. 6.. 7.. 8.. 9..
# and ask the user to insert a name - print the length of the name
import datetime


def calc_name_length():
    name = input('please enter your name : ')
    print(len(name))


calc_name_length()

print('1.. 2.. 3.. 4.. 5.. 6.. 7.. 8.. 9..')

calc_name_length()

def greet():
    print('hello')
    # dont receive and dont return a values


def sum(a, b):
    print(a + b)
    # do receive and dont return a values

def get_date():
    return '24-5'
    # dont receive and do return a values


def c_to_f(c):
    return (c / 1.8 + 32)
    # do receive and do return a values
