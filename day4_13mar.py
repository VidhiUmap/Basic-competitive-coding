#break: terminates loop
for i in range(1,5):
    if i==3:
        break
    print(i)

for i in range(1,5):
    if i==3:
        continue
    print(i)    

for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)
print("************************")
for i,j in zip(range(1,6),range(8,0,-1)):
    if i==4 or j==3:
        continue
    print(i," ",j)

# while loop
# intialisation 
# while condition:
#     statement
#     inc/decrement

i=1
while i<=5:
    print(i)
    i=i+1

print("************************")   
username=''
password=''
while username!="admin" and password!="pass1123":
    username=input("Enter username: ")
    password=input("Enter password: ")
print("************************")


n=int(input("Enter number: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("the sum of first",n ,"natural numbers is",sum)

print("************************")
name='VidhiUmap'
newname=''
for i in name:
    if i not in newname:
        newname+=i
print(name)
print(newname)
#wap to rev the string in any loop
name="VidhiUmap"
rev=''
for i in name:
    rev=i+rev
print(rev)
#WAP to reverse the string using for loop
name="VidhiUmap"
rev=''
for i in range(len(name)-1,-1,-1):
    rev=rev+name[i]
print(rev)
#wap to rev string using while loop
name="VidhiUmap"
rev=''
i=len(name)-1
while i>=0:
    rev=rev+name[i]
    i=i-1
print(rev)
#
print("************************")
mycart=[10,20,200,300,800,60,70]
for item in mycart:
    if item>400:
        print("this is my purchased cart item")
        continue
    print(item)

#to check if string is palindrome
abc=input("enter string: ")
xyz=''
for i in abc:
    xyz=i+xyz
if abc==xyz:
    print("palindrome")
else:
    print("not palindrome")
#more optimised
name=input("enter string: ")
if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")


#anagram
name1=input("enter string: ")
name2=input("enter string: ")
if sorted(name1)==sorted(name2):
    print("anagram")
else:
    print("not anagram")

#use any logic but perform with simple string
name1=input("enter string: ")
name2=input("enter string: ")
for ch in name1:
        if name1.count(ch) != name2.count(ch):
            print("Not Anagram")
            break
        else:
             print("Anagram")

#add key value pairs from a dictionary
dictionary={"name":"alice","age":30}
#use pop to remove
#sample input dictionary:{"name":"alice","age":30},key:"age"
#sample output dictionary:{"name":"alice"}

dictionary={"name":"alice","age":30}
dictionary.pop("age")
print(dictionary)

#nested for loop
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()

print("************************")
n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=' ')
    print()

print("************************")
n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=' ')
    print()
