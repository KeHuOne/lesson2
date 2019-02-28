#Практика: Сравнение строк
#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты

def string_comparison(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    elif str1 == str2 :
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
        


print(string_comparison(1, 100))
print(string_comparison(1, 'привет'))
print(string_comparison('программист', 'привет'))
print(string_comparison('мир', 'мир'))
print(string_comparison('Привет', 'learn'))
