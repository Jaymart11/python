# print("Welcome to tip calculator!")

total_bill = float(input("What is you total bill? ")[1:])
tip = int(input("How much tip would you like to give? 10, 12 ,15? "))
num_people = int(input("How many people to split the bill? "))
total_bill_per_person = ((total_bill * (tip / 100) ) + total_bill) / num_people
print(f"Each person should pay ${total_bill_per_person:.2f}")

