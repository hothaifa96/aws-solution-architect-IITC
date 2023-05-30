# int - 22
# float -444.2
# bool - True False
# str -  '' ""
# list - []
# tuple - ()
# set - {}

# r1 = list(range(1,101,1))
# print(r1)

# numbers = []
# for number in range(1,1001):
#     if number % 7 == 0 and number % 3 ==0:
#         numbers.append(number)
#
# print(numbers)

# l1 = [x for x in range(1001) if x % 7 == 0 and x % 3 == 0]
#
# print(l1)

# new_food=[]
# foods=['pizza','shawarma','burger','knafeh','wings']
# for food in foods:
#     if len(food) >= 6:
#         new_food.append(food)
#
# new_food=[x for x in foods if len(x) >=6]

# use the list comp to print a list with all the negative
# values in this list [5,-22,-9,0,55,-88.8,-15]


# list1 = [5,-22,-9,0,55,-88.8,-15]
#
# print([x for x in list1 if x<0])
# print(list1)

# my_list = [1, 2, 3]
# my_list.append(4)
# my_list.pop(2)  # remove index 2
# print(my_list)

# my_tuple = (1,2,3,"hodi")
# l1 = list(my_tuple)
# print(my_tuple)
# print(l1)

# l4 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 2, 2, 2, 2, 5, 5]
# my_set = {1, 1, 2,99, 3, 4, 5, 6, 7, 8, 2, 2, 2, 2, 2, 2, 5, 5}
#
# print(my_set)
# set1={1, 2, 3, 3, 3, 3,3}
# print(set1)
# set1.add(2)
# print(set1)


car1 = {'make': 'chevrolet',
        'model': 'cruze',
        'price': [10000,20000],
        'fixes': {
            '21-5': 'weels',
            '28-5': 'window'
        }
        }

# print(type(car1))
# print(car1.get('del'))
# car1['year'] = 2020
# print(car1['fixes']['21-5'])
# print(list(car1.keys()))
# for key in car1.keys():
#     print(key +':',car1[key])
for val in car1.values():
    if type(val)is list :
        print(val)