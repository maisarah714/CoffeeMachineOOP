from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menuItem = MenuItem()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True
while is_on is True:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == 'off':
        is_on = False
    else:
        coffee = menu.find_drink(choice)
        if coffee is not None:
            if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(coffee.cost):
                coffeeMaker.make_coffee(coffee)
