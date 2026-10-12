# Write a function called check_priority that takes urgency and affected_users. If urgency == "high" and affected_users >= 10, return "critical". Otherwise return "normal"

def check_priority(urgency, affected_users):
    
    if urgency == "high" and affected_users >= 10:
        return "chritical"
    else:
        return "normal"

urgency = "high"
affected_users = 10

output = check_priority(urgency, affected_users)
print(output)