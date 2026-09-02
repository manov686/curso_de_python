#Problema de parameros mutáveis

# def add_clients(client, list=[]):
#     list.append(client)
#     return list

# list1 = []
# client1 = add_clients("Maria",list1)
# add_clients("João",list1)

# list2 = []
# client2 = add_clients("Pedro",list2)
# add_clients("Ana",list2)

# print(client1)
# print(client2)


def add_clients(client, list=None):
    if list is None:
        list = []
    list.append(client)
    return list

list1 = []
client1 = add_clients("Maria",list1)
add_clients("João",list1)

client2 = add_clients("Pedro")
add_clients("Ana", client2)

print(client1)
print(client2)