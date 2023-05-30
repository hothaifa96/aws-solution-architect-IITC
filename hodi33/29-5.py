# # 1
# def find_maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# #2
# def sum_numbers(numbers):
#     total = 0
#
#     for number in numbers:
#         total += number
#
#     return total
# #3
# def mul_numbers(numbers):
#     total = 0
#
#     for number in numbers:
#         total *= number
#
#     return total
# #4
# def reverse_string(input_string):
#     reversed_string = input_string[::-1]
#     return reversed_string
#
# #5
def calculate_factorial(n):
    factorial = 1
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    for i in range(1, n + 1):
        factorial *= i
    return factorial


#
# #6
# def check_number_in_range(number, lower_bound, upper_bound):
#     if number >= lower_bound and number <= upper_bound:
#         return True
#     else:
#         return False
#
# #7
# def count_upper_lower_case(string):
#     upper_count = 0
#     lower_count = 0
#
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     return upper_count, lower_count
#
# #8
# def get_distinct_elements(input_list):
#     distinct_list = list(set(input_list))
#     return distinct_list
#
# #9
# def check_prime(number):
#     if number < 2:
#         return False
#
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#
#     return True
#


# # 12
# def check_palindrome():
#     s1 = input('please enter word')
#     s1 = s1.lower().replace(' ', '')
#
#     if s1 == s1[::-1]:
#         return 'found it'


# 13

# n = 5
# print(1, 4, 6, 4, 1)
# n = 4
# print(1, 3, 3, 1)
# n = 6
# print(1, 5,10,10,5, 1)


# pascal = n! / ((n - r)! * r!)
def pascal(n):
    for i in range(n):
        # for k in range(n-i+1):
        #     print(' ',end='')
        for x in range(i+1):
            print(calculate_factorial(i)
                  //
                  (calculate_factorial(x)*calculate_factorial(i-x)),
                  end=' ')
        print()


pascal(5)