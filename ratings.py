#Оценки
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

class_list = ['4a','4b','5a','5b']
score = [3, 4, 4, 5, 2],[2, 3, 5, 5, 4],[4, 3, 2, 5, 3],[5, 2, 3, 2, 4]

list_of_ratings = dict(zip(class_list, score))

print(list_of_ratings)

#all_class = (class_list)
#all_score = (score)

#print(all_class)
#print(all_score)

#list_of_ratings = (all_class, all_score)
#print(list_of_ratings)




#list_of_ratings = [
#    {'school_class': '4a', 'scores': [3,4,4,5,2],},
#    {'school_class': '4b', 'scores': [2,4,3,2,5],},
#    {'school_class': '4c', 'scores': [5,4,3,4,3],},
#    {'school_class': '5a', 'scores': [5,4,5,3,2],},
#    {'school_class': '5b', 'scores': [2,3,5,2,5],},
#    {'school_class': '5c', 'scores': [5,4,3,4,5],}
#]


#for score in list_of_ratings:
#    ave_sum = sum(score['scores'])
#    ave_len = len(score['scores'])
#    
#    print(ave_sum)
#    print(ave_len)

#ave_all = ave_sum / ave_len
#print(ave_all)



