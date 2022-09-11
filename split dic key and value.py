# Split dictionary keys and values into separate lists
d={"my":"I'm","name":"ningthemla","Is":"ningshen"}
key=d.keys()
value=d.values()
print(*key)
print(*value)             ##whithout * output comes in ([.....])




dic= {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
keys, values = zip(*dic.items())
print ("keys : ", keys)
print ("values : ",values)


dict = {'name' : 'akshara', 'place' : 'Bangalore', 'animal': 'Lion'}
keys = []
values = []
items = dict.items()
for i in items:
    keys.append(i[0]), values.append(i[1])
print ("keys : ", keys)
print ("values : ", values)