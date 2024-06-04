import homework4, importlib
importlib.reload(homework4)

def list_to_dict(input_list):
    return {i: input_list[i] for i in range(len(input_list))}
pass

print(homework4.list_to_dict([1, 3.14, "hello", True]))
print(homework4.list_to_dict(["a", "a", "a"]))
print(homework4.list_to_dict([]))

import importlib, grade
importlib.reload(grade)




