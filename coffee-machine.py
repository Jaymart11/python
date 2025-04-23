coffee = \
    [
        {"flavor":"espresso", "coffee": 18, "water": 50, "price": 1.50},
        {"flavor":"latte", "coffee": 24, "water": 200, "milk": 150, "price": 2.50},
        {"flavor":"cappucino", "coffee": 24, "water": 250, "milk": 100, "price": 3.50}
    ]

report = \
    {
    "water" : 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
    }

def main():

    while True:
        user_input = input("What would you like? (espresso/latte/cappucino) or report: ")

        if user_input == "report":
            reports()
        else:
            user_choice = next(filter(lambda x: x["flavor"] == user_input.lower(), coffee), None)
            if user_choice: 
                print("Please insert coins")
                quarter = int(input("How many quarters?: ") or 0) 
                dime = int(input("How many dimes?: ") or 0) 
                nickel = int(input("How many nickels?: ") or 0) 
                penny = int(input("How many pennies?: ") or 0)
                coin_sum = coin_conversion("quarter", quarter) + coin_conversion("dime", dime) + coin_conversion("nickel", nickel) + coin_conversion("penny", penny)
                order(user_choice, coin_sum)
            else:
                print("You inputted an invalid choice")
        
def order(choice, coin_sum):
    if(not check_quantities(choice)):
        if(coin_sum > choice["price"] or coin_sum == choice["price"]):
            print(f"You paid ${coin_sum:.2f}")
            if coin_sum > choice["price"]:
                print(f"Here is ${coin_sum - choice["price"]:.2f} in change")
            print(f"Here is your {choice["flavor"]} Enjoy!")
            update_reports(choice, coin_sum)
        else:
            print("Your inserted coin/s is insufficient")
    else:
        check_quantities(choice)

def reports():
    print(f"""Water: {report["water"]}ml
Milk: {report["milk"]}ml
Coffee: {report["coffee"]}g
Money: ${report["money"]}""")

def coin_conversion(coin, num):
    if(coin == "quarter"):
        return 0.25 * num
    elif(coin == "dime"):
        return 0.1 * num
    elif(coin == "nickel"):
        return 0.05 * num
    else:
        return 0.01 * num

def update_reports(choice, money):
    report["water"] -= choice["water"]
    if "milk" in choice:
        report["milk"] -=  choice["milk"] 
    report["coffee"] -= choice["coffee"]
    report["money"] += money

def check_quantities(order):
    if(report["water"] < order["water"]):
        return "Insufficient water. Please try again later"
    elif(report["coffee"] < order["coffee"]):
        return "Insufficient coffee. Please try again later"
    elif("milk" in order and report["milk"] < order["milk"]):
        return "Insufficient milk. Please try again later"

if __name__ == "__main__":
    main()

