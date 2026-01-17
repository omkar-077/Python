
# tuple- is a collection of similar or different type of elements
# starts indexing from 0
# syntax - ()
# immutable- we cant change , add, remove
# is a faster than list because fixed size length


# syntax

skill=("HTML","CSS","JS","Python")
print(skill)
print(skill[2])
# skill[2]="Tailwind"

# 2 - without ()
emp="HTML","CSS","JS"
print(type(emp))
print(emp)

# 3- for single element
# emp=("Pratik") # consider string by default
emp=("Pratik", )
print(type(emp))
print(emp)

# *******************************************


# looping

users=("John","Motu","Patlu","Ninja","Shiva","Aditya","Singchan")
print(users)
for x in users:
    print(x)




# slicing- extra data
print(users[1:6])
print(users[:3]) # John Motu Patlu
print(users[2:]) # Patlu.....


# range function
for x in range(2,6):
    print(users[x])



for i in range(len(users)):
    print(users[i])


# ****************************************

# built in function
# sum()
# len()
# min()
# max()

tuple_1=("AWS","Next JS","Nest JS","AWS","Expres JS","Node JS")
print(tuple_1)
print(len(tuple_1))

tuple_2=(20,23,25,27,21)

print(min(tuple_2))
print(max(tuple_2))
print(sum(tuple_2))


# searching

# in and not in
res="JS" not in tuple_1
print(res)

# sorted
print(sorted(tuple_2))

# count
print(tuple_2.count("AWS"))
print(tuple_1.count("AWS"))

# *******************************

# Packing and unpacking

brands=("Samsung","Lenevo","Apple","Toshiba","Xiaomi","Realme")
print(brands)
print(brands[0])
print(brands[2])


# unpacking
# modern way
brand1,brand2,brand3,brand4,brand5,brand6=brands
print(brand1)
print(brand3)

# *****************
user=("Om","Pune",23)
# print(user[0])
# print(user[1])

name,address,age=user
print(name)
print(address)
print(age)



# list to tuple

list_1=[10,30,40,50]
print(type(list_1))
print(list_1)

print(tuple(list_1))

tuple_4=(10,40,50,80,100)
print(tuple_4)
print(type(tuple_4))
print(list(tuple_4))
