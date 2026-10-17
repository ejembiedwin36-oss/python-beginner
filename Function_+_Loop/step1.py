# Write a function called print_numbers() that uses a loop to print 1 to 10.

"""def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()


# Write a function called print_even() that uses a loop to print the even numbers from 1 to 20.

def print_even():
    for i in range(1, 21):
        if i % 2 == 0:

            print(i, "even")

print_even()


# Write a function called count_to(number) that takes one parameter and prints from 1 up to that number. Example: count_to(5) prints 1 2 3 4 5.

def count_to(number):
    #return num1 + num1
    for s in range(1, number + 1):
        print(s)

count_to(5)


# Write a function called show_names(names) that takes a list of names and uses a loop to print every name.

def show_names(names):

    for names in list_name:
        print(names)


list_name = ['matthew', 'loveth', 'mercy', 'joshua', 'mary']


show_names(list_name)


# Write a function called show_even(numbers) that takes a list of numbers and prints only the even numbers.


def show_even(numbers):

    for num in numbers:
        if num % 2 == 0:

            print(num, "even")

# Test the function with a list of numbers
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
show_even(list_numbers)


def show_odd(numbers):
    for num1 in numbers:
        if num1 % 2 == 1:
            print(num1, "odd")

list_of_odd_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
show_odd(list_of_odd_numbers)"""


#Write a function called sum_numbers(numbers) that loops through a list, adds all the numbers together, and returns the total.
def sum_numbers(numbers):
    total = 0
    for num2 in numbers:
        total += num2
    return total

your_list_here = [10, 20, 30, 40, 50]
        
print(sum_numbers(your_list_here))


# Write a function called count_even(numbers) that returns how many even numbers are in a list.

def count_even(numbers):
    count = 0 
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

count__number = [1, 2, 3, 4, 5, 6, 7]
print(f"The number of even numbers is :{count__number}")