# test
while True:
    ask = input("Как дела?")
    if ask == "Хорошо":
        print(f"Здорово, что всё {ask} !")
        break
    else:
        print("Мы похоже о разных вещах говорим, спрошу ещё раз.")

lst = [21, 2, 93]
def list_doubler(lst):
    doubled = []
    for num in lst:
        doubled.append(num*2)
    return doubled
my_doubled_list = list_doubler(lst)
print(my_doubled_list)    