# Write a function called is_adult that takes an age. 
#If the age is 18 or greater, return "Adult". 
#Otherwise, return "Not Adult".

def is_adult(age):
    #return age
    age = 18
    if age >= 18:
        return "Adult"
    else:
        return "Not Adult"

result = is_adult(18)
print(result)

