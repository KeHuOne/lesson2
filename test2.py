#l1 = [1,2,3,4,5,6,7]

#new_list = list(map(lambda x: x*2, l1))

#print (new_list)

a = [1,2,3]

#new_a = []
#for item in a:
#    new_a.append(str(item))
#массив строк из интов
#print(new_a)

#c = list(new_a[0])
#print(c)
#из массива интов массив массивов,превращая инт в массив
#c_all = []
#for numbers in new_a:
#    c_all.append(list(numbers))
#print(c_all)

b = []
for chislo in a:
    d = dict(number = chislo)
    b.append(d)
    
print(b)