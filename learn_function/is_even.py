 # Write a function is_even that takes a number and returns "Even" if the number is even, otherwise "Odd".
def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(is_even(8))
print(is_even(7))