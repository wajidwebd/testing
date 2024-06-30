# print(10/5)
# num = 5
# num1 = 10.23
# num2 = [5,10.23]
# print(type(num))
# print(type(num1))
# print(type(num2))

# print("user data")

# numberone = int(input())
# numbertwo = int(input())
# values = numberone/numbertwo
# print(type(values))

# print("if else statement:")

# if(condition):
#     True
# else:
#     False

# amount =  int(input("what amount are you having?"))

# if(amount >= 10):
#     print("you can get the ice cream")
# else:
#     print("you cannot get the ice cream")

# print("Operators - Logical operator")

# print(not(10 == 10 and 20==20))
# print("conditional operator")

# print(5<=5)

# amount = int(input("how much amount are you having?"))

# if (amount >=10 and amount<50):
#     print("you can get carnoto")
# elif (amount>=50 and amount<=100):
#     print("you can box ice cream")
# else:
#     print("you cannot get ice cream")

# if (amount >=100000 and amount <300000):
#     print("you are eligibel for 10  lakhs")
# else:
#     print("you are not eligible for any loan")


# age = int(input("enter your age:"))
# if(age >18 and age<=35):
#     print("you are eligible for government job")
# else:
#     print("not eligible for government job")

# for loop

# for name in "kamaludeen":
#     print(name)
# username = str(input("enter your name"))

# for yogeeshwaran in username:
#     print(yogeeshwaran)
# for numbers in range(10,50):
#     print(numbers)
# firstnumber = int(input("enter your firstnumber:"))
# secondnumber = int(input("enter your secondnumber:"))
# for numbers in range(firstnumber,secondnumber):
#     print(numbers)
# for start in range(1,6):
#     print("/",end='')

# a=1
# while (a<10):
#     print(a)
#     a= a+1


# def calculation():
#     a = 5+6
#     print(a)
#     for i in "yogeshwaran":
#         print(i)

# calculation()

# file sytem 

# fileopen = open('content.txt','r')
# contentchecking = fileopen.readline()
# print(contentchecking)


# List,tuple,set,dictionary

# listcreation = [1,2,5,3,4,7,6,1,1,2,10,20]
# listcreation.append(10)
# print(listcreation)
# anotherlist = ['yogesh','kamaludeen']
# print(type(listcreation))
# listcreation.append(10)
# listcreation.clear()
# copy = listcreation.copy()
# print(copy)
# listcreation.clear()
# print(listcreation.count(2))
# listcreation.insert(12,"kamaludeen")
# listcreation.pop()
# listcreation.remove(7)
# listcreation.sort()
# anotherlist.extend(listcreation)
# print(anotherlist)


# tuple

# tuplecreation = (1,2,5,3,4,7,6,1,1,2,10,20)
# print(type(tuplecreation))
# print(tuplecreation.index(20))
# print(tuplecreation.count(1))

# list - [] tuple -() set & dictionary - {}

# setcreation = {1,2,3,1,4,5}
# anothersetcreation = {1,"yogeshwaran","kamaludeen"}
# setcreation.add(10)
# setcreation.clear()
# setcreation.copy()
# setcreation.difference(anothersetcreation)

# print(setcreation.difference(anothersetcreation))
# setcreation.difference_update(anothersetcreation)
# print(setcreation)

# print(setcreation.pop())
# setcreation.remove(5)
# print(setcreation)
# x= setcreation.union(anothersetcreation)
# print(x)
# setcreation.update(anothersetcreation)
# print(setcreation)

# print(type(setcreation))

# name= {"kamaludeen","yogeshwaran","wajid","amazon"}
# anontherset = {"amazon"}

# print(name.difference(anontherset))
# name.difference_update(anontherset)

# x = name.issuperset(anontherset)
# name.discard('amazon')
# print(name)

# dictionarycreation = {
#     "name":"yogeshwaran",
#     "age":21,
#     "role":"full stack"
# }

# print(type(dictionarycreation))
# dictionarycreation.clear()
# print(dictionarycreation.get("role"))
# print(dictionarycreation.pop("name"))
# print(dictionarycreation.popitem())
# x = dictionarycreation.update({"age":40})
# print(x)
# print(dictionarycreation)

# print("function in python")


# def movingtourl():
#     data = int(input("enter your number"))
#     print(data+60)
# movingtourl()

# def movingtourl1():
#     data1 = int(input("enter your number"))
#     print(data1+120)
# movingtourl1()


# Oops -> Class and Inheritance


class calculationprogram:
    name ="yogeshwaran"
    def one(self):
        data = int(input("enter your number"))
        print(data+60)
        print(data+120)
    def two(self):
        print("yogeshwaran is a good boy")
yogesh = calculationprogram()
print(yogesh.name)
yogesh.name="kamudeen"
print(yogesh.name)
yogesh.name="wajid"
print(yogesh.name)
# yogesh.one()
# yogesh.two()