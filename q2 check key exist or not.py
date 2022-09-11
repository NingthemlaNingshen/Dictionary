# Example :-
# dict1={“name”:”Raju”, “marks”:56}
# Visualize
# Note :-
# If input is “name” then output will be “exist”
# If input is “class” then output will be “not exists”.

dict1={"name":"Raju", "marks":56}
user= input("enter your option:")
if user in dict1:
    print("exist")
else:
    print("not exists")
