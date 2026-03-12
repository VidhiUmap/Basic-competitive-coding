#wap to accept three paper marks and check maximum marks using nested if else
# Nested if-else
#m1 = int(input("Enter marks of Paper 1: "))
#m2 = int(input("Enter marks of Paper 2: "))
#m3 = int(input("Enter marks of Paper 3: "))

#if m1 > m2:
 #   if m1 > m3:
  #      print("Maximum marks =", m1)
 #   else:
 #       print("Maximum marks =", m3)
#else:
#    if m2 > m3:
 #       print("Maximum marks =", m2)
 #   else:
 #       print("Maximum marks =", m3)

# WAP to accept percentage and if per 
#per = float(input("Enter percentage: "))

#if per > 90:
#    print("Grade: A")
#elif per > 80:
#    print("Grade: B")
#elif per > 60:
#    print("Grade: C")
#else:
#    print("Fail")

# indexing and slicing are not possible in dictionary 
#mydict = {
 #   "name" : "Prashantjha",
 #   "professional" : "developer",
  #  "empid": 1001
#} 
#print(mydict)
#print(type(mydict))

# #mydict={
#     101:"prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104":"trivani",
#     101: "ashish",
#     104:"ashish"
# }
# print(mydict)
# a=mydict[102]
# print(a)


mydict = {
    101:"Vidhi",
   102:"prashantjha",
    103:"Ridhima",
    104:"Apoorva",
    101:"Kanak",
}
print(mydict)
a= mydict[102]
print(a)

for x in mydict:
  print(x)
for x in mydict.values():
  print(x)
for x,y in mydict.items():
  print(x,y)

mydict["mobile_no"]=5486748574
print(mydict)

name = "VidhiUmap"
#indexing = 012345678910
print(name[0])
print(name[1])
print(name[-1])
print(name[0:5])
print(name[1:])
print(name[1:8:2])
print(name[::-1])

s = "help4code is a best platform for practicing programming"
print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))

s = "Vidhi","Sharad","Umap"
m = '|'.join(s)
print(m)

s = "Python is a high level programming language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print('Subject marks :')
phy = 50
chem = 60
math = 70
print("physics={} chemistry={} math={}".format(phy,chem,math))
print("physics={0} chemistry={1} math={2}".format(phy,chem,math))
print("physics={x} chemistry={y} math={z}".format(x=phy,y=chem,z=math))
total = phy+chem+math
print("Total Marks",f"{total}")
print("Roll No=", "7".zfill(4))

# print('VidhiUmap01'.isalnum())
# print('VidhiUmap'.isalpha())
# print('3001K'.isdigit())
# print('sdsdsd'.islower())
# print('VIDHIUMAP'.isupper())
# print('VidhiUmap01'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

a =50
b= 30
c=40
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

x = ['a','b','c']
y = ['a','b','c']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)

name = "Vidhi"
v = 0
c = 0
for i in name:
    if i in "aeiouAEIOU":
        v = v + 1
    else:
        c = c + 1
print("Vowels:", v)
print("Consonants:", c)
