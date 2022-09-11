# Write a Python program to print the dictionary in a table format?
d={"Name":["Sana","Tina","mina"],"Age":[12,32,21],"Sex":["Female","Female","Female"]}
for j in zip(*([x]+(y) for x,y in (d.items()))):
        print(*j)

# for j in zip(*([x]+(y)for x,y in (d.items()))):  ##out put will be in tuple
#         print(j)

# for j in zip(([x]+(y)for x,y in (d.items()))):  ##out put will be in tuple and list
#         print(j)
