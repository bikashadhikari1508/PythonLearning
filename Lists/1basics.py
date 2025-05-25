"""
List:
    it is an ordered set of values
    Each value in the list identified by an index
    Values stored by the list may be an integer, string or float etc.
    enclose the elements in square brackets [ ]
    A list is a collection of different kinds of values or items
    List items are ordered, changeable(mutable), and allow duplicate values.
"""

# List Slices
list1 = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
print(list1[1:3])
print(type(list1))
# output ['b' , 'c']


raw = r'this\t\nis a cow'
print(raw)

#List are mutable
#Multiple changes at once 

# For loop in list
x = ['a', 'e' , 'i' , 'o' , 'u']
for i in x:
    print(i , end=' ')
print('\n')

for i in (x):
    if i == 'e' :
        print(f"value {i}")
    else:
        print(f"not e {i}")


# Aliasing in list
x = [1,2,3]
b = x
print(b)

# List cloning
# Cloning means making a copy. Sometimes we need to copy a list and want to modify the copied list but do not want to make changes in the original list. 

num = [2,7,4,3]
clone_values = num[:]
print(clone_values)
clone_values[2]=10
print(f"{num:} and {clone_values:}")

#Slice
x = [3,2,1]
y = x[:]
print(y)

# output
[3,2,1]

#Nested List
list2 = [3,4,5,["bikash","zoya"],9]
# Accessing nested list elements
print(list2[3][0]+","+list2[3][1])

#Split operator 
string = "Hello I Am Bikash"
print(string.split(" "))

string2 = "Cat Bat Sat Fat Pat"
print(string2.split("t"))

text = "Hello geek Welcome to GeeksforGeeks."

result = text.split('Welcome')
print(result)

string3 = "litchi\tapple\tgauva\tbanana"
res = string3.split('\t')
print(res)

number_str = "12345"
digits = list(number_str)
print(digits)