# adding common keys

d1={"a":100,"b":200,"c":300}
d2={"a":200,"b":21,"d":20}
for i in d1:
    for j in d2:
        if i==j:
            d2[i]=d1[i]+d2[j]
    else:
        d2[i]=d1[i]
        # d1[i]=d2[j]
print(d2)