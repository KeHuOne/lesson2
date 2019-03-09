#Оценки
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

list_of_ratings = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [2,4,3,2,5]},
    {'school_class': '4c', 'scores': [5,4,3,4,3]},
    {'school_class': '5a', 'scores': [5,4,5,3,2]},
    {'school_class': '5b', 'scores': [2,3,5,2,5]},
    {'school_class': '5c', 'scores': [5,4,3,4,5]}
]

scores_total = 0

for score_class in list_of_ratings:
    result = sum(score_class['scores']) / len(score_class['scores'])
    
    print(f"Средний балл по классу {score_class['school_class']} : {result}")
    scores_total += result

scores_total /= len(list_of_ratings)
print(f"Средний балл по всей школе: {scores_total} ")

