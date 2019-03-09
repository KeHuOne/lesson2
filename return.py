age = int(input("Укажите ваш возраст:"))

kindergarten = 7
school = 18
academy = 24
work = 65
retiree = 90
long_liver = 122

def classification(age):
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
        return f"Долгожителей старше {long_liver} лет не было зафиксировано,вы меня обманываете!"

p = classification(age)
print(p)