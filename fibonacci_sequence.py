
number = int(input("Type the first n numbers of the Fibonacci sequence: "))
def generate_fibonacci(number):
    sequence = [0, 1]
    i = 2
    while i < number:
        i += 1
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(generate_fibonacci(number))
