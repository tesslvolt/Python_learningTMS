# Маша хочет накопить на телефон, который стоит N
# денег. Маша может откладывать k рублей каждый день,
# кроме воскресенья (в воскресенье она тратит эти деньги на
# поход в кино). Маша начинает копить в понедельник. За
# сколько дней она накопит нужную сумму?
money_sum = int(input("Стоимость телефона: "))
money_at_day = int(input("Сколько денег в день откладывается: "))
days_wo_sunday = int(money_sum / money_at_day)

count_sunday = int(days_wo_sunday / 7)
print(count_sunday)
days_w_sunday = days_wo_sunday + count_sunday


print(f"Денег накопиться за {days_w_sunday} дней")