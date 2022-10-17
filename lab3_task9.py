salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = spend

for month in range(10, 1, -1):
    spend = spend * (increase + 1)
    need_money = need_money + spend

need_money = need_money - 10 * salary

print(round(need_money))
