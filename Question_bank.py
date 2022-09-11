# # o/p={'name': 'jaya', 'score': 60, 'school': 'pyds'}
d= [{"name":"komal","score":40,"school":"pyds"},

{"name":"koma","score":40,"school":"pyd"},

{"name":"jaya","score":60,"school":"pyds"},

{"name":"Sonam","score":60,"school":"Union"},

{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
i=0
while i<len(d):
    if d[i]["name"]=="jaya" and d[i]["score"]==60 and d[i]["school"]=="pyds":
        print(d[i]) 
    i=i+1


# ## o/p={"name":"Sonam","score":60,"school":"Union"}  changing key to value
dic={"Sonam":"name",60:"score","Union":"school"}
x={}
for i,j in dic.items():
    x[j]=i
print(x)


# ##o/p={"d":1,"i":1,"f":2,"r":1,"e":2,"n":1,"t":1}

char_list=["d","i","f","f","e","r","e","n","t"]
i=0
a=[]
while i<len(char_list):               
    j=0
    count=0
    b=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    b.append(char_list[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i=i+1
print(a)