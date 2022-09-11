{1: 10, 2: 60, 3: 30, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={1:30,2:40}
dic3={5:50,6:60} 
for i in dic1 :
    for j in dic2:
        if i==j:
            dic3[i]=dic1[i]+dic2[j]
        else:
            dic3[i]=dic1[i]
            dic3[i]=dic2[j]
print(dic3)
print((len(dic3)))



# Sum list of dictionaries with the same key?

dic = [{'a':5, 'b':10, 'c':90},{'a':45, 'b':78}, {'a':90, 'c':10}]
d={}
for i in dic:
    for j in i.keys():
        d[j]=d.get(j,0)+i[j]
print(d)



### making two dic into one dic


dic1={1:10, 2:20}
dic2={3:30,2:40}
for i in dic1:
    for j in dic2:
        if i==j:
            dic2[i]+=dic1[i]
d={**dic1,**dic2}
print(d)


## adding the value of same key and tuening into one dic

d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
for i in d1:
    if i in d2:
        d1[i]=d1[i]+d2[i]
d2.update(d1)
print(d2)
 