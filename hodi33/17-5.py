# # # # first_name1 = 'yael'
# # # # first_name1 = 'ohad'
# # # # first_name1 = 'yuval'
# # # # first_name1 = first_name1.upper()
# # # # print(first_name1.upper())
# # # # print(first_name1)
# # #
# # # sen = 'joey doesnt share food'
# # #
# # # # print(sen[15])  # to print 1 lt we use  sen[index]
# # # # print(sen[5: 11])  # to print field ue user [start : end ]
# # # # print(sen[: 4]) # print(sen[0: 4])
# # # # print(sen[18: ]) # print(sen[18: 22])
# # # # print( sen[:] )
# # # # print( sen )
# # # # --------------------------------
# # # # print(sen[::-1])
# # # # print(sen[0:-4])
# # # # print(sen[7:])
# # #
# # #
# # #
# # # #------1-------------------------
# # # # print the domain of the email
# # # email = 'hothafafsaifa@yahooooooo.com'
# # # # print(email[9:-4])
# # # print(email[email.index('@') + 1:email.index('.')])
# # # # print(email.index('@'))
# # # # print(email.index('.'))
# # # #- ------2-------------------------
# # # # print the prefix of the phone number -- Prefix is the first 3 digits
# # # phone_number = '0526618010'
# # # print(phone_number[:3])
# # # #- -------3------------------------
# # # # print the subnet mask of the ip
# # # ip1 = ' 110.210.133/16'
# # # print(ip1[ ip1.index('/')+1:])
# # # print( ip1[13:])
# # #
# # # # what is the website1 extension -- validate extension length is 3
# # # website1 = 'https://website.net'
# # # print(website1[-3:])
# # #
# # # # etgar::
# # # bash_command = 'echo "hello from this bash code"'
# # # # build a python code to execute this bash script
# # #
# # # print(bash_command[6:-1])
# # # print(bash_command[  bash_command.index('"')+1 : bash_command.rindex('"') ])
# # # --------------------------------------------------------------------------------------------
# #
# # food = 'rice'
# # #
# # # print(food + ' ktestsot')
# # # print(f'{food} {17 + 16}')
# # # print(f'my fav food is {food}')
# #
# # print(r'c:\users\new\tomi\Desktop' * 5)
# #
# # print(fr'code /n // /t  {food}')
#
#
#
#
#
#
#
#
# declare 2 variables key and value
# the key contains the word car
# and the value containes your dream car
#
# for examole
# key = 'car'
# value = 'nissan gtr'
#
# print the code as a json in one line:
#
# {
# 		"car" : "nissan gtr"
# }

key = 'car'
value = 'nissan gtr'

print('{\n' + f'\t"{key}" : "{value}"\n' + '}')
