money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
delta = salary - spend

while True:
    spend = spend * (1 + 0.05)
    money_capital_1 = money_capital - delta
    if money_capital > spend:
        delta = salary - spend
        spend = spend * (1 + 0.05)
        month += 1
    else:
        break
print(month)
