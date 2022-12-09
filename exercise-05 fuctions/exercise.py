import random
mylist = []
values = random.randint(-100,100)
def random_list_summer():
    for i in range(values):
        mylist.append(i)
random_list_summer()  
print(mylist)
print(sum(mylist))
