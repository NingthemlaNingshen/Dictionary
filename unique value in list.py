# take a list having dictionary elements as shown below (Sample Data) and then store all the
#  unique values into a list and print.

# Example :-
# Input :-
# [
#   {"first":"1"}, 
#   {"second": "2"}, 
#   {"third": "1"}
#   {"four": "5"}, 
#   {"five":"5"}, 
#   {"six":"9"},
#   {"seven":"7"}
# ]
# Visualize
# Output :-
# ['2', '7', '9', '5', '1']


a=[
{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
b=[]
for i in a:
    for j in i.values():
        b.append(j)
print(set(b))              ## output in Dictionary


a=[
{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
b=[]
for i in a:
    for j in i.values():
        if j not in b:
            b.append(j)       
print(b)                      ##output in list
