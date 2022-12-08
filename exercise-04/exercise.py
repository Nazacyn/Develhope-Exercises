list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for l in list1:
    print(l)

for t in tuple1:
    print(t)

for s in set1:
    print(s)

for x, y in dict1.items():
    if y == 'land':
        print(x, 'lives in',y)

