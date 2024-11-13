# Write your solution here
times_in_week = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money_in_week = float(input("How much money do you spend on groceries in a week? "))

price_daily = (times_in_week * price + money_in_week) / 7
exp_total_weekly = times_in_week + price_daily + money_in_week

print("Average food expenditure: ")

print(f'Daily: {price_daily}')
print(f'Weekly: {exp_total_weekly}')