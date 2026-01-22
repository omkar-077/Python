
# # exception handling

# def Calci(a,b):
#     return a/b

# print(Calci(5,5))


# # res=Calci(50,0)
# # print(res)



# # *********************
# def Demo(a,b):
#     # print(a+"ABC")
#     print("hello")

# Demo(100,200)

# # next
# def User():
#     print("hello user")
# User()


# print("Hello Welcome....dear")


# *****************************************


# Exception handling helps you:

# ✅ Prevent program crashes
# ✅ Handle wrong user input
# ✅ Continue execution even after an error
# ✅ Make programs more professional


try:
    a=20
    b="Pratik"
    print(a+b)
except:
    print("Error Occured..")


print("Hello Pratik")


# ***************************


try:
    def Calci(a,b):
        return a/b

    print(Calci(5,5))

    res=Calci(50,0)
    print(res)

except Exception as err:
    print("Error Occured..", err)



print("hello")


# ***********************

# 


try:
    a=100
    # b="200"
    # b=int("abc")
    print(a+b)
except ValueError:
    print("Invalid data type ")
except ZeroDivisionError:
    print("Invalid data type")
except TypeError:
    print("wrong data type")



# ************************************

# eg


try: 
    x=100
    y="50"
    print(x+y)

except Exception as err:
    print("error occured ",err)

finally:
    print("Code Executed successfully...")



# *******************
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid Number")
else:
    print("You Entered ", num)
finally:
    print("Task Completed")



