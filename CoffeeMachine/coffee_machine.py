MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources['money'] = 0

def check_ingredients(coffee, resource_remaining):
    '''Checks if the ingredients in the coffee machine is sufficient to make the coffee.'''
    
    ingredients = MENU[coffee]['ingredients']
    
    for ingredient in ingredients:
        if resource_remaining[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False            
    return True


def check_money(coffee):
    '''Checks if money is sufficient to buy the drink.
    If more money is entered, it is returned as change and the remaining is added to the resources'''
    
    print("Please insert money.")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    total_money_inserted = quarter * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    cost_of_drink = MENU[coffee]['cost']
    
    if total_money_inserted < cost_of_drink:
        
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    else:
        
        if total_money_inserted > cost_of_drink:
            change = round(total_money_inserted - cost_of_drink, 2)
            print(f"Here is ${change} in change")
        resources['money'] += cost_of_drink
        return True

def use_ingredients(coffee, resource_remaining):
    '''Decreases ingredients from resources accordinng to requirement.'''
    ingredients = MENU[coffee]['ingredients']
    for ingredient in ingredients:
        resource_remaining[ingredient] -= ingredients[ingredient]

chooses_to_continue = True

while chooses_to_continue:

    choice = input("""What would you like? (espresso/ latte/ cappuccino):
Type 'report' to get a report of remaining contents
Type 'off' to turn it off.\n""")

    if choice == 'off':
        chooses_to_continue = False # Exits

    elif choice == 'report':
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    else:
        if check_ingredients(choice, resources):
            if check_money(choice):
                use_ingredients(choice, resources)
                print(f"Here is your {choice}. Enjoy!")
