

#list- follow sequence,allow duplicates, indexing
# uses square brackets
lst = [2,4,5,9,9,5,'a',"python"]
lst[3]= 18
print(lst,len(lst))
print(lst[2:])
print(lst[-4:-1])


#tuple-uses parantheses
tuple1= (2,4,5,6,5,6,'s',"srinivas")
#tuple1[3]=9   #gives error
print(tuple1,len(tuple1))

#set- collection of unique elements,doesn't follow sequence, doesn't allow duplicates, no indexing
#uses curly brackets, no order is followed
set = {4,5,"srinivas",5,5,6,6}
print(set)

#dictionaries - same like Hashmap in Java
#K,V pairs
di= {1:"srinivas", 2:"Ravi", 3:"Rahul"}
print(di)
print(di[3],",", di.get(2))

key = {1,2,3,4}
value = {"srinivas", "ramesh","suresh"}
dict1= dict(zip(key,value))
print(dict1)
