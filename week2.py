#1 
my_list = []
#2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)  
print(my_list)
#3
my_list.insert(1, 15)
print(my_list)
#4
list = [50, 60, 70]
my_list.extend(list)
print(my_list)
#5
del my_list[-1]
print(my_list)
#6
my_list.sort()
print(my_list)
#7
index = my_list.index(30)
print(index)
#finally the output of my_list
print(my_list)