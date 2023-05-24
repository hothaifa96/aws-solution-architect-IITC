# etgar 1
# number_matrix = [
#     [12, 87, 5],
#     [-1, 3000, 4],
#     [200, 8, 4]]
#
# # print(number_matrix[1][1])
# min = number_matrix[0][0]
#
# for list in number_matrix:
#     for number in list:
#         if number < min:
#             min = number
#
# print(min)
#
# # print(number_matrix[1][1])
# avg = []
# for list in number_matrix:
#     avg.append(  sum(list) / len(list)    )
#
# print(avg)
#
#
#
#
#

# ask the user to insert his ip address
# valid ip address is str with 3 dots
# each number is a byte - 0 255 inc
# the user must insert the subnet mask and we need to print his
# network name  using str only if the ip is valid
# what is the broadcast ip and the default getaway address
ip = '22.224.55.55/16'
valid = True
ip_list=[]
if '/' in ip:
    naked_ip=ip[:ip.index('/')]
    if naked_ip.count('.')==3:
        for byte in range(3):
            if byte==3:
                sec = int(naked_ip)
            else:
                sec = int(naked_ip[:naked_ip.index('.')])
            if not 0<= sec <=255:
                valid = False
            ip_list.append(str(sec))
            naked_ip = naked_ip[naked_ip.index('.')+1:]
        print('valid ip')
        subnet_mast= int(ip[ip.index('/')+1:])
        network_name= ip_list[: (subnet_mast//8)]
        print(network_name)
        network_name = '.'.join(network_name)
        print(f'default getaway {network_name+".0.1"}')
        print(f'broadcast {network_name+".255.255"}')










