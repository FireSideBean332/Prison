import random

def start_menu():
    print("=== PRISON ESCAPE ===")
    print("Welcome to PRISON ESCAPE!")
    print("Choose difficulty:")
    print("1. Normal")
    print("2. Hard")

    difficulty = input("> ")
    if difficulty == "1":
        difficulty = "normal"
        health = 2  # 2 lives in normal mode
    elif difficulty == "2":
        difficulty = "hard"
        health = 1  # Just a placeholder; no second chances in hard
    else:
        print("Invalid choice. Try again.\n")
        return start_menu()

    print("\nDo you want to start the game? (yes/no)")
    start = input("> ").lower()

    if start == "yes":
        prison_cell(difficulty, health)
    else:
        print("Game exited.")

def game_over():
    print("\nYOU LOST!")
    print("Would you like to return to the main menu? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        start_menu()
    else:
        print("Thanks for playing. Goodbye!")

def prison_cell(difficulty, health):
    print("\nYou wake up in your prison cell.")
    print("You see a guard's key on the floor near the bars.")
    print("Do you want to take the key? (yes/no)")

    choice = input("> ").lower()
    if choice == "yes":
        lunch_room(difficulty, health)
    else:
        print("You didn't take the key. You're trapped forever.")
        game_over()

def lunch_room(difficulty, health):
    print("\nYou sneak out and enter the lunch room.")
    print("Do you want to go left or right?")

    choice = input("> ").lower()
    if choice == "right":
        print("A guard sees you and catches you.")
        game_over()
    elif choice == "left":
        multiplication_question(difficulty, health)
    else:
        print("Invalid choice. Try again.")
        lunch_room(difficulty, health)

def multiplication_question(difficulty, health):
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 10)
    correct = num1 * num2

    print(f"\nQuestion: What is {num1} * {num2}?")
    try:
        answer = int(input("> "))
    except ValueError:
        print("You must type a number!")
        return multiplication_question(difficulty, health)

    if answer == correct:
        wc(difficulty, health)
    else:
        if difficulty == "hard":
            print("Wrong answer. No second chance on hard mode.")
            game_over()
        else:
            health -= 1
            if health == 0:
                print("Wrong again. You have no lives left.")
                game_over()
            else:
                print(f"Wrong answer. You have {health} lives left.")
                multiplication_question(difficulty, health)

def wc(difficulty, health):
    print("\nYou enter the bathroom.")
    print("You see a window and a ventilation shaft.")
    print("Do you take the window or the ventilation?")

    choice = input("> ").lower()
    if choice == "window":
        print("You climb out the window and escape!")
        print("YOU WON! 🏆\n")
    elif choice == "ventilation":
        if difficulty == "hard":
            print("The guards hear you in the vent and catch you.")
            game_over()
        else:
            print("You almost get stuck but manage to crawl back to the lunch room.")
            multiplication_question(difficulty, health)
    else:
        print("Invalid choice. Try again.")
        wc(difficulty, health)

# Start the game
start_menu()
