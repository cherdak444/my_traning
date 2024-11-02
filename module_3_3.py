def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(b = 25)
#print_params(c=[1, 2, 3])

values_list = (1, True, [1, 2, 3])
values_dict = {"a":123, "b":True, "c":"string"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = (123, True)
print_params(*values_list_2)

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)


