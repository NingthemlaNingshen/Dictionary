# Count the total number of items from the values of the dictionary which are in the form 
# of a list.

# Input :-
# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# Visualize
# Output :-
# total count:5


dict1 =  {
    'Alex': ['subj1', 'subj2', 'subj3'], 
    'David': ['subj1', 'subj2']}
c=0
for i in dict1.values():
    c=c+len(i)    
print("count= ",c)  

