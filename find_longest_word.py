import re

def find_longest_word(text):
    remove_special = re.sub("[$&+,:;=?@#|'<>.^*()%!-]", "", text).lower()
    words = remove_special.split()
    lenght = []
    for i in words:
        lenght.append(len(i))
    first_longest_index = lenght.index(max(lenght))
    return words[first_longest_index]
    
text_test = "Biden farewell to the chaos of juggling multiple tools for course tracking, project ideation, and task management. Developer's Brain transforms Notion into a, all-in-one solution for mastering your coding journey. Unlock the power of:"
print(find_longest_word(text_test))