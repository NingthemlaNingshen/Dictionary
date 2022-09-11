# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the 
# elements of the 2nd list are the corresponding values.

# Example :-
# Input :-
# list1=[“one”,”two”,”three”,”four”,”five”]

# list2=[1,2,3,4,5,]
# Visualize
# Output :-
# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
x = {}
for i in list1:
    for j in list2:
        x[i] = j
        list2.remove(j)
        break  
print(x)



# Write a program to create a dictionary with all numbers from 1 to 15 as the keys and 
# their squares as the corresponding values.

# Output :-
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 
# 13: 169, 14: 196, 15: 225}
x={}
for i in range(1,16):
    x[i]=i**2
print(x)
