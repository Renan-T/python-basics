def count_characteres(word):
    characteres = [*word]
    counts = []
    for i in range(len(characteres)):
        counts.append(characteres.count(characteres[i]))
        for i in characteres:
            x = characteres.index(i)
        count_char = {}
    for i in range(len(characteres)):
        count_char[characteres[i]] = counts[i]
    return count_char

print(count_characteres("ahsudhaushduashduahsduhasudh80912983****"))


