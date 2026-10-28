def My_Inventory_Scanner():
    valid_code = ("A101", "B202", "C303", "D404")

    running = True

    
    print("--- Warehouse Scanner Terminal ---")
    print("Type 'quit' to exit the scanner.\n")

    while running:
        user_input = input("Scan item code: ")
        if user_input in valid_code:
            print("acceptrd item")
        elif user_input == "quit":
            return "Quit"
        else:
            print("Invalid item!.")


def main():
    My_Inventory_Scanner()

if __name__ == "__main__":
    main()

