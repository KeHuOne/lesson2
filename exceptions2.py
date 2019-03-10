#Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало

num_one = input('Введите первое число: ')
num_two = input('Введите второе число: ')

def get_summ(num_one, num_two): 
    try:
        return (int(num_one) + int(num_two))
    except ValueError:
        return 'Введите целые числа!'
print(get_summ(num_one,num_two))