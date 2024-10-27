money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

capital = money_capital + salary
month = 0

while capital >= spend:
    capital += salary
    capital -= spend
    spend += spend * increase  # Начисляем проценты
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
