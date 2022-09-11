d={"name":"nim","place":"L.A"}
x = d.get("gender")     ###output will be none since there is no gender
print(x)

d={"name":"kim","place":"U.S"}
y=d.get("address","Imphal")          ###output will be Imphal in get method if 
print(y)                             ###we have second value that will be the output
# ###get() method will only take two argument at the most

car ={
"brand":  "ford",
"model":  "mustang",
"year":  1964
}
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary.")
else:
    print("No, 'model' key dictionary mai nahi hai.")

