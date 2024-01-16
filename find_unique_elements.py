list_example = [100, 75, 100, 20, 75, 12, 75, 25, "ola", "tudo", "bem", "ola"] 

def find_unique_elements(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
print(find_unique_elements(list_example))