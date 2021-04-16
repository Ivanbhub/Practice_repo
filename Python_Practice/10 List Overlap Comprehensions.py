a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	
list=[]
	
[(list.append(x)) for x in a if x in b if x not in list]
	
print(list)
#######################EXTRA:################################

import random

list1=[]
list2=[]


for i in range(12):
    x = random.randint(1,50)
    list1.append(x)
    x = random.randint(1,50)
    list2.append(x)
    
print(list1)
print(list2)

Final_List=[]
#This list will contain elements that are common between the two randomly generated lists
[Final_List.append(y) for y in list1 if y in list2 and y not in Final_List]
print(Final_List)
    
    
