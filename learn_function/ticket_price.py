# Write a function ticket_price that takes age. Return:
#- "Free" if age is less than 5
#- "Child" if age is from 5 to 17
#- "Adult" if age is 18 or above

def ticket_price(age):
    #age = 18
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "Child"
    else: 
        return "Adult"

print(ticket_price(3))
print(ticket_price(12))
print(ticket_price(19))


