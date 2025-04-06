print("Hello!")

# chce aby każda osoba była zapytana ile chce zjeść procent pizzy , xcały procent to jest 100 % od użytkownika zapytammy się ile jest osob , i chce jeżeli ktoś chce zjeśc procent pizzy więcej niż porcent pozosrał np. 1 osoba chce zjeśc 25% zatem zanstępna osoba nie moze zjesc 80%  w tedy chce aby wyswieltilo ise po ang że pogadj z reszta grupy , lub order new pizza


def pizza_order():
    num_people = int(input("How many people are in your group? "))
    pizza_percentage = 100
    total_percentage = 0
    percentages = []

    for i in range(num_people):
        while True:
            try:
                percent = float(
                    input(f"How much of the pizza does person {i + 1} want to eat (in %)? "))
                if percent < 0 or percent > pizza_percentage:
                    print("Invalid input! Please enter a percentage between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

        total_percentage += percent
        percentages.append(percent)

        if total_percentage > pizza_percentage:
            print(
                f"Total percentage exceeds 100%! Currently, it is {total_percentage}%.")
            print(
                "Please discuss with the group to adjust the percentages or order a new pizza.")
            # Ends the function, allowing the user to try again or change the plan.
            return

    print(f"Total pizza percentage: {total_percentage}%")
    if total_percentage == pizza_percentage:
        print("Perfect! The pizza has been split evenly.")
    else:
        print(
            f"The total percentage of pizza requested is {total_percentage}%. Consider adjusting to share it more equally.")


# Run the pizza order function
pizza_order()
