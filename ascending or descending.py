# Write a program to sort a dictionary in ascending or descending according to its values .

# Input :-

# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}
# Visualize
# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}

D={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=sorted(D.values())
x={}
for i in a:
    for j in D.keys():
        if D[j]==i:
            x[j]=i
print(x)
    

# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}


D={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=sorted(D.values())
b=reversed(a)
x={}
for i in b:
    for j in D.keys():
        if D[j]==i:
            x[j]=i
print(x)