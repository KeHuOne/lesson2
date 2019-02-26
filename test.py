age = int(input("Укажите ваш возраст:"))

kindergarten = int(7)
school = int(18)
academy = int(24)
work = int(65)
retiree = int(90)
long_liver = int(122)

def classification(age):
    age = abs(int(age))
    if age <= kindergarten:
        return "Вы ещё ходите в садик."
    elif age <= school:
        return "Вы учитесь в школе."
    elif age <= academy:
        return "Вы учитесь в ВУЗе."
    elif age <= work:
         return "Вы ходите на работу."    
    elif age <= retiree:
        return "Вы пенсионер."
    elif age <= long_liver:
        return "Поздравляю! Вы долгожитель."
    else:
        return "Долгожителей старше 122 лет не было зафиксировано,вы меня обманываете!"

p = classification(age)
print(p)

