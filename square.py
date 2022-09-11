# Below is a program in which the keys are between 1 to 15 and the values ​​are the squares of 
# the keys.

# The output should be something like this:-
# <br>{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,<br>9: 81, 10: 100, 11: 121, 12: 144, 
# 13: 169, 14: 196, 15: 225}

# Now, you have to debug this :-


# x = dict(name = "John", age = 36, country = "Norway")

c=dict()
for i in range(1,16):
    a=i
    b=i*i
    c.update({a:b})
print(c)

#or

c={}
for i in range(1,16):
    c[i]=i*i
print(c)


##or

c=dict()
# print(c)
for i in range(1,16):
    c[i]=i*i
print(c)

##or

i=1
dic={}
while i<=15:
    dic[i]=i*i
    i=i+1
print(dic)
