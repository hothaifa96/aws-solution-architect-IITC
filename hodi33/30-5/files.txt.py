# w - override the file if exist else create it  >
# r - you may read the file not to write in it
# a - add to exist file ir else create it >>

# w+ - write and read  cursor at index 0
# r+
# a+

# file = open('names.txt',mode='a+')
# names=['name1','name2','gadi','eran','avi']
# print(file.tell())
# file.seek(5)
# print(file.read(199))
# file.close()

# file = open('names.txt','r')
# file.close()

# with open('names.txt','r') as file:
#     lines=file.readlines()
#     print(lines)
#     if 'gadi\n' in lines:
#         print('gadi is here')

with open('names.txt', 'a+') as file:
    last_index = file.tell()
    index = 0
    file.seek(0)
    while index < last_index:
        if file.read(1) == 'g':
            if file.read(3) == 'adi':
                print(file.tell() - 4)
        index = file.tell()
