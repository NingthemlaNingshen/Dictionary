# You have been given a dictionary in which you have to print the value of some key. 
# Debug the code.
details={
"name":"Shanti",
"age":12,
"email":"shanti@navgurukul.org",
}
details.update({"lastname":"kumari"})

print(details["name"])
print(details["lastname"])
print(details["age"])



car = {                         ###examples
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)