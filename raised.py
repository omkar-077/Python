
# age calculator
# raise- your own error

try:
    age=int(input("Enter Your Age..."))

    def Demo(a):
        if a<=0:
            raise ValueError("Age cannot be negavtive...")
        
        print("Your Age Is ",a)


    Demo(age)

except Exception as e:
    print("Error", e)
