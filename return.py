age = int(input("Укажите ваш возраст:"))

def classification(age):
    if age <= 6:
        print("Вы ещё ходите в садик.")
    elif 7 <= age <= 17:
        print("Вы учитесь в школе.")
    elif 18 <= age <= 23:
        print("Вы учитесь в ВУЗе.")
    elif 90 <= age <= 122:
        print("Поздравляю! Вы долгожитель.")
    elif age >= 123:
        print("Долгожителей старше 122 лет не было зафиксировано,вы меня обманываете!")
    else:
        print("Вы ходите на работу.")

classification(age)
