# Membership Operator

#  in and not in = check whether element is present or not

data=[20,30,40,60,100,"Om","Aditya", "Sunmesh",True,None,23.6]



print("Om"in data)  #True
print("Abc" not in data) #True

# ********************************

# Identity Operator
# is and not - check whether same object memory or not 

a=10
b=a
c=[10,20,30]
print( a is b)  #True
print(a is c)   #False
print(a is not b) #False