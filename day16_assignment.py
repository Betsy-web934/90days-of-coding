dictionary = {
    "name": "John",
    "age": 21,
    "university": "Zetech University",
    "course": "Software Engineering",
    "favourite_programming_language": "Python"
}

print(dictionary["name"])
print(dictionary.get("university"))

#add a new key called email
dictionary["email"] = "jk@gmail.com"
print(dictionary["email"])

#update the value of the key age to 22
dictionary["age"] = 22

#remove the key called favourite_programming_language
del dictionary["favourite_programming_language"]

print(dictionary)

#LIBRARY MANAGEMENT SYSTEM
dictionary2 = {
    "title" : "Psychlogy of Money",
    "author" : "Morgan Housel",
    "year" : 2020,  
    "price" : 25.99,
    "available" : True
}

dictionary2["price"] = 20.99
dictionary2["genre"] = "Finance"

#dispaly all the keys in the dictionary
print(dictionary2.keys())

#Display all the values in the dictionary
print(dictionary2.values())


print(dictionary2)

#Display every key together with its value using a for loop
for key, value in dictionary2.items():
    print(key, ":", value)


