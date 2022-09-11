# Take input of name and marks of 10 students and store to a dictionary.

# dict={
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# }
# print(dict)

n=int(input("Enter n: ")) 
dic={}
for i in range(n): 
    name=input("Enter name: ") 
    marks=int(input("Enter marks: ")) 
    dic[name]=marks
print(dic)
