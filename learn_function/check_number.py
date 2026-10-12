# Write a function called check_number that takes one number. 
#Return "Positive" if the number is greater than 0;
# otherwise return "Zero or Negative".
def check_number():
    number = 1
    if number > 0:
        return "Positive"
    else:
        return "Zero or Negative"
result = check_number()
print(result)
