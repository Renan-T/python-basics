
import re

text = input("Input a string or text to count the word frequency: ")
remove_special = re.sub("[$&+,:;=?@#|'<>.^*()%!-]", "", text).lower()
words = remove_special.split()

counts = []
for i in range(len(words)):
    counts.append(words.count(words[i]))

for i in words:
    x = words.index(i)

word_frequency = {}
for i in range(len(words)):
    word_frequency[words[i]]= counts[i]
print(word_frequency)

   


