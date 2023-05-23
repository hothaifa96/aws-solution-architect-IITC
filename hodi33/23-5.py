# Homework 1

# for i in range/list:
#     loop block
# numbers = [4, 2, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in range(10):
#     print(number ** 2)

# while condition:
#     loop

# 3.

# numbers = [100, 8, 7, 5, 1]
#
# for number in numbers[: len(numbers)//2]:
#     print(number)
# for index in range(len(numbers)//2):
#     print(numbers[index])
# range(2) -> [0,1]

# print('hothaifa', end='')
# print('zoubi')

# 4.

# words = ['coding of world', 'pen', 'python', 'hello']
#
# for word in words:
#     print(word.upper())

# 5
# words = ['coding of world', 'pen', 'python', 'hello']
#
# for word in words:
#     if len(word) < 4:
#         break
#     print(word.upper())

# 6
#
# fullname = 'gandi fewkhotsetoma'
# #
# # print(fullname[-5:])
# # print(fullname[: len(fullname)//3])
# # print(f'a appeared {fullname.count("a")} times');
# # print(fullname.count('b') != 0)
# # print( 'b' in fullname )
# print(fullname.split())
# name_list = fullname.split()
# print(name_list)
# name_list = (list(reversed(name_list)))
# print(name_list)
#
# name_list[0] = name_list[0].upper()
# print(name_list)
#
# middle_index = len(name_list[1]) // 2
# name_list[1] = (name_list[1][:middle_index] + name_list[1][middle_index + 1:])
#
# print(name_list)
#
#
# fullname = ' '.join(name_list)
#
# print(fullname)


# for lt in name :
#     if name.index(lt) == len(name)//2:
#         continue
#     print(lt,end='')



# # 8.
# צור רשימה של חמישה מספרים: [5 2, -3, 1000, 8,]
# הדפס את סכום הרשימה
# הדפס את האיבר הגדול ביותר
# הדפס את האיבר הקטן ביותר
# הדפס את ממוצע הרשימה )סכום הרשימה חלקי אורך הרשימה(
# הסר את האיבר האמצעי ברשימה
# מיין את הרשימה
# הדפס את הרשימה משוכפלת 5 פעמים
# הסר מהרשימה את האיבר הראשון
# צור תת רשימה המכילה את כל האיברים הקטנים מהממוצע

numbers = [5,2, -3, 1000, 8 ]
print(numbers)
print('the sum is ',sum(numbers))
print('max value ',max(numbers))
print('min value ',min(numbers))
print('avg ',sum(numbers)/len(numbers))
numbers.pop(len(numbers)//2)
print(numbers)
numbers.sort()

print(f'{numbers}'*5)
numbers.pop(0)

small_values=[]
for n in numbers:
    if n < sum(numbers)/len(numbers):
        small_values.append(n)

print(small_values)