import random
def random_list_summer(n=15):
    values = [random.randint(-100,100) for i in range(n)]
    print(values)
    print(sum(values))

random_list_summer() 
