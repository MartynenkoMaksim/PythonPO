salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month = 0
capital_salary = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(0, months):
    capital_salary += spend - salary
    spend *= (1 + increase)
    month += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(capital_salary))
