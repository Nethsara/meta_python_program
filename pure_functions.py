my_list = [1,2,3]

#Normal Function
def add_to_list(item):
    return my_list.append(item)

def add_to_list_pure(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list_pure(my_list, 4)

print(my_list)
print(new_list)