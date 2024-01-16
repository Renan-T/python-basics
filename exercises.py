string = input("Insert any word: ")

def reverse_string(string):
    reverse = (string[::-1])
    return reverse

def is_palindrome(string):
    string = string.lower()
    reverse = reverse_string(string)
    if reverse == string:
        return("Is Palindrome!!!")
    else:
        return("Is not Palindrome")

def sum_of_digits(number):
        sum = 0
        for digit in str(number):
             sum += int(digit)
        return sum

print(is_palindrome(string))
print(reverse_string(string))

number = input("Insert any positive number: ")
