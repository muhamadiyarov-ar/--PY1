salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for need_money in range(1, months+1):
    need_money = spend - salary
    need_money = need_money + (spend * 1.03)
    need_money += 1


print(round(need_money))
