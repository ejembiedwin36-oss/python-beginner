# Write a function calculate_score that takes score and bonus, adds them together, and returns "Pass" if the total is at least 50; otherwise return "Fail".
def calculate_score(score, bunus):
    total = score + bunus
    if total == 50:
        return "Pass"
    else:
        return "Fail"
result = calculate_score(25, 25)
print(result)
   
