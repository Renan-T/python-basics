number = int(input("Insert any natural number greater than 1: "))

def is_prime(number):
    num = int(number)
    divisors = []
    for i in range(number):
            i = i + 1
            if number % i == 0:
                divisors.append(i)
    divisors_length = len(divisors)
    if divisors_length == 2:
         return True
    else:
         return False
    
print(is_prime(number))
    