class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    dis_cups = 9
    money = 550

    order = ""

    while order != "exit":
        order = input("" +
                      "Write action (buy, fill, take, remaining, exit):")
        if order == "remaining":
            print("The coffee machine has:")
            print(water, " of water")
            print(milk, ' of milk')
            print(coffee, " of coffee beans")
            print(dis_cups, " of disposable cups")
            print("$%d" % money, 'of money')
        elif order == "fill":  # fill
            water_add = int(input("" +
                                  "Write how many ml of water do you want to add:"))
            water += water_add
            milk_add = int(input("" +
                                 "Write how many ml of milk do you want to add:"))
            milk += milk_add
            coffee_add = int(input("" +
                                   "Write how many grams of coffee beans do you want to add:"))
            coffee += coffee_add
            dis_cups_add = int(input("" +
                                     "Write how many disposable cups of coffee do you want to add:"))
            dis_cups += dis_cups_add
        elif order == "buy":  # buy
            type_order = input("" +
                               "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if str(type_order) == "back":  # back
                pass
            elif int(type_order) == 1:  # 1 - espresso
                if water >= 250 and coffee >= 16 and dis_cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= 250
                    coffee -= 16
                    dis_cups -= 1
                    money += 4
                else:
                    if water < 250:
                        print("Sorry, not enough water!")
                    if coffee < 6:
                        print("Sorry, not enough coffee beans!")
                    if dis_cups < 1:
                        print("Sorry, not enough disposable cups!")
            elif int(type_order) == 2:  # 2 - latte
                if water >= 350 and coffee >= 20 and dis_cups >= 1 and milk >= 75:
                    print("I have enough resources, making you a coffee!")
                    water -= 350
                    milk -= 75
                    coffee -= 20
                    dis_cups -= 1
                    money += 7
                else:
                    if water < 350:
                        print("Sorry, not enough water!")
                    if coffee < 20:
                        print("Sorry, not enough coffee beans!")
                    if dis_cups < 1:
                        print("Sorry, not enough disposable cups!")
                    if milk < 75:
                        print("Sorry, not enough milk!")

            elif int(type_order) == 3:  # 3 - cappuccino
                if water >= 200 and coffee >= 12 and dis_cups >= 1 and milk >= 100:
                    print("I have enough resources, making you a coffee!")
                    water -= 200
                    milk -= 100
                    coffee -= 12
                    dis_cups -= 1
                    money += 6
                else:
                    if water < 200:
                        print("Sorry, not enough water!")
                    if coffee < 12:
                        print("Sorry, not enough coffee beans!")
                    if dis_cups < 1:
                        print("Sorry, not enough disposable cups!")
                    if milk < 100:
                        print("Sorry, not enough milk!")

        elif order == "take":
            print("I gave you $%d" % money)
            money = 0
    if order == 'exit':  # exit
        pass


coffee = CoffeeMachine()
coffee.__init__()
