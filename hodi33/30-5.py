l1 = [55, "gandi", 'hummos and tea']
s1 = {2, 2, 2, 2, True, 2, 3, 4}
t1 = (1, 2, 3, "misgav", 4)

person1 = {'name': 'saar', 'salary': 90000}

# print(person1)
# # print(d1['skill'])
# # print(d1.get('skill'))
person1['car'] = 'cupra'
# print(person1)
#
# print( person1.keys() )
# print( person1.values() )
#
# print(person1.items())

for k,v in person1.items():
    #  [(k,v),(k,v),(k,v) ]
    print(f'{k}-> {v}')


print(person1)