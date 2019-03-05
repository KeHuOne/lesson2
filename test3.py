#a = 1
#d = {}

#d = dict(number = int(a))
#print(d)
a = [1,2,3]
b = [4,5,6]

c = list(map(lambda x,y: x + y, a,b))
print(c)