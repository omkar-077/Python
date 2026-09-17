 


a = ()
print(type(a))

# empty set
# s = set()

# set = {"thor", "iron" ,1, "om", 1.2}
# set.pop()
# print(set)
# print(set)
# print(set)
# print(set)

# swap 2 no. without temp

# a= 10
# b = 20
# a,b = b,a

# remove duplicate value in list 

# def removeduplicate(st):
#     unique = []
#     for item in st:
#         if item not in unique:
#             unique.append(item)
#     return unique
# print(removeduplicate([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))


# remove duplicate word from sentence

# sentence =  " python is easy and python is powerful"
# words  = sentence.split()
# def removeduplicate(words):
#     unique_words = []   
#     for item in words:
#         if item not in unique_words:
#             unique_words.append(item)
#     return unique_words
# print(removeduplicate(words))

# ṣpace complexity ??

# lambda function
# names =  ["thor","loki" ]
# upper = list(map(lambda x:x.upper(),names))
# print(upper)

# num = [1,2,3,4]
# sq = list(map(lambda x:x**2,num))
# print(sq)

# nums = [1,2,3,4,5,6,7,8,9,10]
# greater = list(map(lambda x:x>4,nums))
# print(greater)

# nums2 = [1,2,3,4,5,6,7,8,9,10]
# greater2 = list(filter(lambda x:x>4,nums2))
# print(greater2)

# nums3 = [1,2,3,4,5,6,7,8,9,10]
# even = list(map(lambda x : x%2==0,nums3))
# print(even)

# str = "thor"
# convert = list(filter(lambda x : list(str),str))
# print(convert)

# startwith("a") // function

# args

def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1,2,3,4,5,6,7,8,9,10))

# kwargs

def f(**kwargs):
    print(kwargs)
f(greet="hello",name="omkar",sublect="cse")


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# decorator
def mydecorator(hello):
    def wrapper():
        print("before function execution")
        hello()
        print("after function execution")
    return wrapper
@mydecorator
def hello():
    print("hello world")
hello()


def deco(add):
    def wrapper():
        return a+b
def add(a,b):
    return a+b
add(2,3)