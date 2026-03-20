# #functions : predefined, userdefined, lambda, generics, decorators
#1.
# def msg():
#     print("Hello, World!")
# msg()

#2.
# def add():
#     n1 = int(input("Enter the value of n1: "))
#     n2= int(input("Enter the value of n2: "))
#     print("Addition: ",n1+n2)
# add()

#3.
# #returning multiple values from a function
# def operation():
#     n1 = int(input("Enter the value of n1: "))
#     n2= int(input("Enter the value of n2: "))
#     sum = n1+n2
#     sub = n1-n2
#     mul = n1*n2
#     div = n1/n2

#     return sum, sub, mul, div
# result = operation()
# print(result)

#4.
# #we can pass 4 arguments in python : positional, keyword, default, variable length/ variable number, unknown argument(extra).
# #positional argument : positions of arguments from left to right are fixed.
# def personalInfo(fname, lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)

# personalInfo("Vidhi", "Umap") #positions are fixed.

#5.
# #keyword argument : the value that is passed, the keyword should match with it.
# def personalInfo(fname, lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)

# fname = "Vidhi" 
# lname = "Umap"
# personalInfo(fname, lname) #the arguments are same as that of passed above.

# #6.
# #default argument : default argument is added in order to prevent errors in case no arguments are passed.
# def cityName(city="Delhi"): #default argument is added
#     print(city)

# cityName("Mumbai") #positional arguement
# cityName("Nagpur") #positional argument
# cityName() # no argument is here, therefore there is a need of default argument.

# #7.
# #variable length argument/variable number of argument : accepts all the arguments at once.
# def studentNames(*name): #astric is used so that we can access all of the varibales at once.
#     print(name)
# studentNames("Vidhi", "Umap", "Abc", "Xyz")

# #8.
# #to search an element.
# myList = [5,2,9,8,6,4,7]
# def SearchElement(target):
#     for i in range(len(myList)):
#         if target == myList[i]:
#             return i
#     return -1
# result = SearchElement(10)
# if result!=-1:
#     print("Element is found at index: ", result)
# else:
#     print("Element not found")