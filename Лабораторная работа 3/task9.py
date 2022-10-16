salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0

mounth = 10
summ = spend
for i in range(2, mounth + 1):
    spend = spend * 1.03
    summ = summ + spend
need_money = (summ - salary * mounth)
print(round(need_money))
