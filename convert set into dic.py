# Q7. Convert a set into a dictionary?


x = ('nim', 'kim', 'tim')
thisdict = dict.fromkeys(x)
print(thisdict)

# ##or
d = {1, 2, 3, 4, 5}
dic=dict.fromkeys(d,"number")
print(dic)

###The fromkeys() method returns a dictionary with the specified keys and the specified value.

# #or
x = {'key1', 'key2', 'key3'}
y = "string"
thisdict = dict.fromkeys(x, y)
print(thisdict)

# Syntax
# dict.fromkeys(keys, value)

