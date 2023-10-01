def display_menu():
    print("Menu:")
    print("1. FOOD")
    print("2. COMPLAINTS")
    print("3. EMERGENCY")
    print("4. FEEDBACK")


def option1():
    print("You selected Option 1.")
    # Add your code for Option 1


def option2():
    print("You selected Option 2.")
    # Add your code for Option 2


def option3():
    print("You selected Option 3.")
    # Add your code for Option 3


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
