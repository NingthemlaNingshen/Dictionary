# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" 
# to a dictionary, were the letters are the keys and their frequencies are the values.

# Example:-
# Output :-
# {'M':1,'I':4,'S':4,'P':2}
words="MISSISSIPPI" 
mc=0
ic=0
sc=0
pc=0
dic={}
for i in words:
    if i=='M':
        mc=mc+1
        dic[i]=mc 
    if i=='I':
        ic=ic+1
        dic[i]=ic
    if i=='S':
        sc=sc+1
        dic[i]=sc
    if i=='P':
        pc=pc+1
        dic[i]=pc    
print(dic)

##or

word="MISSISSIPPI" 
d={}
i=0
while i<len(word):
    j=0
    c=0
    while j<len(word):
        if word[i]==word[j]:
            c=c+1
        d[word[i]]=c
        j=j+1
    i=i+1
print(d)

    