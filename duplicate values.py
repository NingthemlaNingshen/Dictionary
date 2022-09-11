# Find keys with duplicate values in the dictionary
# dic={1: 10, 2: 60, 3: 5, 5: 50, 6: 60}
dic={1: 10, 2: 60, 3: 50, 5: 50, 6: 60}
d={}
for i,j in  dic.items():
    if j not in d:
        d[j] = [i]
    else:
        d[j].append(i)
print("final_dictionary", d)