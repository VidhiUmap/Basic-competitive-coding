# Trying new list instructions
mylist = ["Vidhi","Shreeya","Ridhima","Apoorva","7.77","Om","Tanishka","Sharwari","4.19"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])
mylist.append('Rrujula')
mylist.append('Veera')
print(mylist)
mylist.insert(1,'Ruhan')
print(mylist)
mylist.remove("4.19")
print(mylist)
newlist = mylist.copy()
print(newlist)
print(newlist)

# new list
mylist = [['Vidhi','Ridhima','Apoorva'],['4.19'],[2007,'3001']]
print("example of multidimensional list :")
print(mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

# printing list in a different way 
list1 = ["Vidhi","Umap"]
print(list1*2)
list2 = [77,4.19]
print(list1+list2)
del list2[1]
print(list2)

# clearing a list
list2.clear()
print(list2)

# name
name = "Ruhan"
mylist = list(name)
myname = list(name)
print(myname)

# sorting example
mylist = [44,56,33,148]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# checking the ids
math = 60
physics = 60
print(id(math))
print(id(physics))

# Aliasing
mylist = [44,56,33,148]
newlist = mylist
print(id(mylist))
print(id(newlist))

# spacial operators 
# 1. membership  operator  a. in  b. not in
name = "Vidhi"
print("z" in name)
print("z" not in name)

for i in range(1,11):
    print(i*2)
#i=0 

for i in range(1, 11):        # numbers 1 to 10
    print(i*2,"",i*3,"",i*4,"",i*5,"",i*6,"",i*7,"",i*8,"",i*9,"",i*10)

    print("\n\n-----------\n\n")

for i in range(1,11):
    print(i*11,"",i*12,"",i*13,"",i*14,"",i*15,"",i*16,"",i*17,"",i*18,"",i*19,"",i*20)


no = int(input("Enter any digit:"))
if no>0:
    print('Positive')
if no<0:
    print('Negative')
if no == 0:
    print('Zero')

# WAP to accept days and check the working days and weekend 
day = print(input("Enter the day:"))
if day == "Saturday" or "Sunday":
 print('Weekend')
else:
    print('Working days')

# wap to accept 3 PAPER marks and calculate total, percentage and if percentage is greater than equal to 60 then he/she is eligible for placement
# WAP to accept 3 paper marks and calculate total, percentage and placement eligibility

m1 = int(input("Enter marks of Paper 1: "))
m2 = int(input("Enter marks of Paper 2: "))
m3 = int(input("Enter marks of Paper 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 60:
    print("Eligible for Placement")
else:
    print("Not Eligible for Placement")

# wap to accept five different value in 5 different var and check max value and pirnt by using "simple if statement"
# WAP to accept five different values and print the maximum using simple if

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print("Maximum value is:", max)
