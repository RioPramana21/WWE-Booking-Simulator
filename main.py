def main():
    print("Welcome to WWE Booking Simulator!")
    menu = 0
    exit_menu = 5
    while menu != exit_menu:
        print("1. View Superstars")
        print("2. Hire Superstar")
        print("3. Fire Superstar")
        print("4. Book a Match")
        print("5. Exit")
        try:
            menu = int(input("Select a menu: "))
        except Exception as e:
            print("Invalid input, please enter a number between 1 and 5.")
            continue
        match(menu):
            case 1:
                print("Viewing Superstars...")
            case 2:
                print("Hiring Superstar...")
            case 3:
                print("Firing Superstar...")
            case 4:
                print("Booking a Match...")
            case 5:
                print("Exiting the simulator. Goodbye!")
            case _:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()