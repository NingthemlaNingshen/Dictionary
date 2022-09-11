# How to find length of dictionary values

d={"name":["Sana","Tina","mina"],"Age":["12","32","45","21"],"sex":["Female","Female","Female"],"z":["1"]}
print(len(d.values()))        ##value length
a=[]
c=0
for i in d:
    a.append(d[i])
print(a)
j=0
while j<len(a):
    c=c+len(a[j])
    j=j+1
print(c)                     ##value count








