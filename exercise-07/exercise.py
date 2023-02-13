# Functions - Exercise 7 🐍

Create a lambda function that returns 2nd power of given number if its even   
and run it on the given list   
then print the result to the screen 

my_list= [*range(5)] 

# use anonymous function
result = list(map(lambda x: 2 ** x, my_list))

print("The total terms are:",len(my_list))
for i in my_list:
   print("2 raised to power",i,"is",result[i])
