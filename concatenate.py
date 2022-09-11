# You have been given two dictionaries, You need to concatenate them.

# Now you have to debug the code
# And your output should be like this :-

# {'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,
# "karan":43}

s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}    ##we can solve it without using update
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)