from classes import *

def view_superstars():
    print("Viewing all superstars...")
    example = Superstar("John Cena", 98)
    print(example)

def hire_superstar():
    print("Hiring a new superstar...")
    
def fire_superstar():
    print("Firing a superstar...")

def book_match():
    print("Booking a match...")

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
                view_superstars()
            case 2:
                hire_superstar()
            case 3:
                fire_superstar()
            case 4:
                book_match()
            case 5:
                print("Exiting the simulator. Goodbye!")
            case _:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()