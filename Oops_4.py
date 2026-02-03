

# multilevel Inheritance

# grandparent->parent->child

# A->B->c

# eg

# mobile-> Apps -> Socila Media APps-

# Bank -> Account -> Account Types

# University-> Colleges-> Departments

#

class GrandParent:
    def gp(self):
       print("grand parent class")

class parent(GrandParent):
    def p(self):
      print("parent class")

class Child(parent):
    def c(self):
     print("child class")

c1=Child()
c1.gp()
c1.p()
c1.c()

# ****************************

# gp
class Bank:
   def __init__(self,name,branch):
      self.name=name
      self.branch=branch

   def details(self):
      print(f"Bank details.....{self.name} and {self.branch}")
      

# parent
class Account(Bank):
   def __init__(self,acc_no,acc_type,acc_bal,name,branch):
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.acc_bal=acc_bal

        # parent constructor
        super().__init__(name,branch)

   def details(self):
      super().details()
      print(f"Account Details.....{self.acc_no} {self.acc_type} {self.acc_bal}")
      

# child
# customer
class Customers(Account):
        def __init__(self,cust_name,cust_age ,acc_no, acc_type, acc_bal, name, branch):
            self.cust_name=cust_name
            self.cust_age=cust_age
            super().__init__(acc_no, acc_type, acc_bal, name, branch)
        
        def details(self):
            super().details()
            print(f"Customer Details......{self.cust_name} {self.cust_age}")
     
   
customer1=Customers("Aditya",23,"986587658","Current","10000","HSBC","NYC")
customer1.details()
 
     

