# # avi1Grade = 99
# # avi2Grade = 100
# # gadiGrade = 56
# # daniel = 99
# # costa = 15
# #
# # daniel_Grade
#
# #         0    1    2   3   4
# grades = [99, 100, 56, 99, 15, 'hodi',True]
#
# # print( grades[0:] )
# # print(grades[::2])
# # print(grades)
# # print(grades.count(99))
# # print( len(grades) )
# grades.append(77)  # adds a new value to the list
# print(grades)
# last = grades.pop()  # remove the last value from the list
# print(grades)
#
# print(grades[::2])
#
# grades.insert(2,'first')
# grades.remove(True)
# grades.pop(2)
#
# print(grades)


# numbers =  [1,5,6,99,44,-6,-2,11,-89]
#
# print(list(reversed(sorted(numbers))))
#
# print(numbers)

# loops

# while condition :
#     # loop actions

#
# x =input('please enter a number ')
# while x != 'q':
#     print(x)
#     x =input('please enter a number ')
#
# print('bye bye')


# sum = 0
#
# while sum < 100:
#     x = int(input('please enter  anumber '))
#     sum += x
#
# print(f'the sum is {sum}')
#

# write a code to receive from the user numbers till the user insert
# negative value  then print adios and close the application

# user_input = int(input('please enter a number :'))
# while user_input>=0:
#     user_input = int(input('please enter a number :'))
# print('adios')


# declare a fruits list = ['banana','kiwi','watermelon','apple']
# using while loop iterate over the list and print the length of
# each word

# fruits = ['banana', 'kiwi', 'watermelon', 'apple']
# n = 0
#
# while n < len(fruits):
#     print(len(fruits[n]))
#     n += 1

# write a python code to calc the powers of 2 using the while loop
# for example if the user insert 4
#    you must print 2^4 = 16


# power = int(input('enter the power :'))
# temp = 1
#
# while power > 0:
#     temp *= 2
#     power -= 1  # power = power -1
#
# print(temp)

#
# r = range(1, 10, 1)
# # print(r)
# print(r)
# for i in r:
#     print(i)

# for x in range(10):
#     print('hello',x)
#
# chars = ['a','b','c','d','e','f']
#
# for x in chars:
#     if x == 'c':
#         break
#     print(x)

# write a python code to receive 4 numbers from the user
# if the number where odd stop the loop


# for i in range(4):
#     x = int(input('please enter a number'))
#     if x % 2 != 0:
#         break
#     print(x)
#



# ask the user to insert the array length that he need
# create an empty list and fill it with the user input

size = int(input('enter the length'))
l1 = []

for i in range(size):
    l1.append( input(f'enter the {i+1}/{size+1} value') )
    # l1.append( input(f'enter the {i+1} {"st" if i == 0 else"nd" if i==1 else "th"} value') )

print(l1)