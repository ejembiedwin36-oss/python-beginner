# while loop cointinues as long as the condition remains True. 
# to stop it the condition has to0 be False 
john_is_a_boy = True

while john_is_a_boy:
    print("John is a BOY")

    result = input("Do you want to still be a boy: \n1. no\n2. yes: ")
    if result == "NO" or result == "1":
        print("John is not a boy!.")
        john_is_a_boy = False

    else:
        continue