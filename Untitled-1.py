def pizza_order():
    while True:
        pizza_cost = float(input("Enter the cost of the pizza: "))
        add = {
            "orange_juice": 2.5,
            "lemonade": 3.5,
            "soda": 1.5,
            "water": 1.0,
            "coca_cola": 2.0,
            "apple_juice": 2.0,
            "ice_tea": 2.5,
            "olive_oil": 3.0,
            "vinegar": 1.5,
            "salt": 0.5,
            "pepper": 0.5,
            "ketchup": 0.5,
            "mustard": 0.5,
            "mayonnaise": 0.5,
            "olive": 0.5,
            "cheese": 0.5,
            "mushroom": 0.5,
            "pepperoni": 0.5,
            "sausage": 0.5,
            "bacon": 0.5,
            "onion": 0.5,
            "bell_pepper": 0.5,
            "pineapple": 0.5,
            "anchovies": 0.5,
            "jalapenos": 0.5
        }
        lucky_day = input(
            "Do you have a lucky day  or sombody of your group have a lucky day (yes/no)? ")
        if lucky_day == "yes":
            print("Great! Happy lucky day!")
            discounts = {
                "birthday": 0.9,
                "anniversary": 0.95,
                "graduation": 0.85,
                "new year": 0.9,
                "christmas": 0.8,
                "recovery": 0.8,
                "blessing": 0.7,
                "a new baby was born": 0.85,
                "a new pet was adopted": 0.97,
                "a new house was bought": 0.9,
                "a new car was bought": 0.95,
                "A new job was started": 0.9,
                "A new friend was made": 0.95,
                "A new skill was learned": 0.9,
                "A new hobby was started": 0.95,
                "A new journey was started": 0.9,
                "Friendly aliens arrived": 0.8,
                "A new planet was discovered": 0.7,
                "A new star was born": 0.6,
                "A new successful company was made": 0.55,
                "A new successful product was launched": 0.70
            }
            special_days = {
                "Woman Day": 0.9,
                "Father's Day": 0.95,
                "Mother's Day": 0.85,
                "Valentine's Day": 0.8,
                "Halloween": 0.75,
                "Thanksgiving": 0.8,
                "Easter": 0.85,
                "Independence Day": 0.9,
            }

            options = ', '.join(discounts.keys())
            special_days_keys = ', '.join(special_days.keys())
            why_lucky = input(
                f"Why is it a lucky day? \n You can choose between ({options} or maybe you have special discount coupon, or there is some of these day  {special_days_keys}) else you need to talk to your group or to the manager: ")
            if why_lucky in discounts:
                pizza_cost *= discounts[why_lucky]
                print(f"The cost of the pizza is now: {pizza_cost}")
            elif why_lucky in special_days:
                pizza_cost *= special_days[why_lucky]
                print(f"The cost of the pizza is now: {pizza_cost}")
            elif why_lucky == "have a special discount coupon":
                discount = float(
                    input("Enter the discount percentage (e.g., 10 for 10%): "))
                pizza_cost *= (1 - discount / 100)
                print(f"The cost of the pizza is now: {pizza_cost}")
            else:
                print("Unknown reason for discount")

        elif lucky_day == "no":
            problem = input("Oh no! What problem may happen? ")
            problem_prices = {
                "very very very small for exmaple  bacteria": 0.999,
                "very very small animal for example ladybug, ant": 0.99,
                "very small animal for exmaple rabbit, rat,hamster": 0.92,
                "small animal for example cat, dog": 0.85,
                "medium animal for example cow, goat": 0.75,
                "big animal for example elephant, horse": 0.5,
                "very big animal for example whale": 0.25,
                "very very big animal for example dinosaur": 0.1,
                "very very very big animal for example dragon": 0.01,
                "very very very very big animal for example monster": 0.001,
                "delay": 0.8,
                "wrong order": 0.5,
                "wrong address": 0.7,
                "too small": 0.6,
                "over cooked": 0.5,
                "wrong type of pizza": 0.6,
            }
            if problem in problem_prices:
                pizza_cost *= problem_prices[problem]
                print(f"The cost of the pizza is now: {pizza_cost}")
            else:
                print(
                    "Invalid problem! Please enter a valid problem.Talk to your group and manager to solve it.")
                continue
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
            continue

        num_people = int(input("How many people are in your group? "))
        pizza_percentage = 100
        total_percentage = 0
        percentages = []
        names = []
        each_person_percent = []

        for i in range(num_people):
            name = input(f"Enter the name of person {i + 1}: ")
            names.append(name)

            while True:
                try:
                    percent = float(
                        input(f"How much of the pizza does {name} want to eat (in %)? "))
                    each_person_percent.append(percent)
                    if percent < 0 or percent > pizza_percentage:
                        print(
                            "Invalid input! Please enter a percentage between 0 and 100.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a number.")
                print(f"{name}, select your toppings:")
                for i, topping in enumerate(add.keys()):
                    print(f"{i+1}. {topping.title()}")
                    toppings = input(
                        "Enter the numbers of the toppings you want to add (separated by commas): ")
                    toppings = [add.keys()[int(i)-1]
                                for i in toppings.split(",")]
                    return toppings

                def calculate_price(toppings, percent):
                    price = sum(add[topping] for topping in toppings)
                    return price * (percent / 100)

            total_percentage += percent
            percentages.append(percent)

            if total_percentage > pizza_percentage:
                print(
                    f"Total percentage exceeds 100%! Currently, it is {total_percentage}%.")
                print(
                    "Please discuss with the group to adjust the percentages or order a new pizza.")
                break
        else:
            print(f"Total pizza percentage: {total_percentage}%")
            if total_percentage == pizza_percentage:
                print("Perfect! The pizza has been split evenly.")
            elif total_percentage < pizza_percentage:
                print(
                    f"Great! There is still {pizza_percentage - total_percentage}% of the pizza left.")
            else:
                print(
                    f"Oops! You have ordered too much pizza. Please adjust your order.")

            for name, percent in zip(names, each_person_percent):
                print(
                    f"{name} wants to eat {percent}% of the pizza. \n so they have to pay  {(percent/100) * pizza_cost} $")
            break


# Run the pizza order function
pizza_order()
