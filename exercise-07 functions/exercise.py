my_list= [*range(5)] 

result = list(map(lambda x: 2 ** x, my_list))
for i in my_list:
   print("2 raised to power",i,"is",result[i])
