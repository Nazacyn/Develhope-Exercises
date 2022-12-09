list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

# 1. print the lengths of list1, tuple1, set1, dict1
print(len(list1))  
print(len(tuple1)) 
print(len(set1))  
print(len(dict1)) 

# 2. print the first element of list1 and tuple1
print(list1[0]) 
print(tuple1[0])  

# 3. print the value of lion key of dict1
print(dict1["lion"])

# 4. change the 2nd position element of list1 to "rabbit"
list1[1] = "rabbit"
print(list1)  

# 5. try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
#tuple1[1] = "rabbit"
#error, tuple objects are immutable and cannot be modified.

# 6. add "monkey" to list1
list1.append("monkey")
print(list1) 

# 7. remove "rabbit" from list1
list1.remove("rabbit")
print(list1)  

# 8. in dict1 the number of feet is written as value to each animal the fish has wrong value just fix it.
dict1["fish"] = 0
print(dict1)