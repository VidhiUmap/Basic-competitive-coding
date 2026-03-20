# Question 1
# import re
# var = 'gasgg54@#vscsd!s'
# count = 0
# for i in var :
#     z = re.findall('[a-z.0-9]',i)
#     z = ord(i)
#     if z>=97 and z<=122:
#         continue
#     elif z>= 48 and z <= 57:
#         continue
#     else:
#         count+=1
#     print(count)

# Question 2
# find the common elements in the three arrays
# a = [1,3,4]
# b = [2,3,4]
# c= [4,5,6]
# for i in a:
#     if i in b and i in c:
#         print(i)

# Question 3 
# given an array , move all zeroes to the end without changing the order of non-zero elements
# list = [0,1,0,3,12]
# for i in list:
#     if i == 0:
#         list.remove(i)
#         list.append(i)
# print(list) 

# question 4
# list =[7,3,9,2,6]
# list.sort()
# print(list)
# print(list[-2])

# Question 5
N = int(input("Enter number of elements: "))
total = 0
mylist = []
# Taking input
for i in range(N):
    a = int(input("Enter element value: "))
    mylist.append(a)
# Calculate sum of absolute differences
for j in range(len(mylist) - 1):
    total += abs(mylist[j] - mylist[j + 1])
print(total)
