#why python is called dynamiclay typed 
math=40
pi = 3.14
name='vidhi'
print(math)
print(pi)
print(name)
print(type(math))
print(type(pi))
print(type(name))

#what is typecasting
print(2+2)
print("2"+"2")
val1= int(input("enter first number"))
val2= int(input("enter second number"))
print(val1+val2)

#
print("********")
print(int(3.14))
print(int(True))
print(int(False))
print(int(4.22))
print(int("4"))

print("********")
print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))

print("********")
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex(4.22))
print(complex("4"))

print("********")
print(bool(0))   #0 in any format gives false
print(bool(15))
print(bool(3.14))
print(bool(4.1+2j))
print(bool("4"))
print(bool(False))
print(bool(None))

print("********")

#simple interst
p=1000000
roi=10
time=7
si=(p*roi*time)/100
print(si)


##centigrade input into farehnheit 
#print(input("enter centigrade"))
#print()

#swapping two num without usig 3 var
ab=20
cs=63
ab=ab+cs
cs=ab-cs
ab=ab-cs
print(ab)
print(cs)

#to enter height in feet and convert in inch and centimeter
#height=input(int("enter height in feet"))
height= 6
print("height in inch",height*12)
print("height in centimeter",height*2.54)

#reverse number
num=1234567
print(num)
a=num%10
num=num//10
b=num%10
c=num//10
d=num//100
e=num//1000
f=num//10000
g=num//100000
rev= a*100000+b*10000+c*1000+d*100+e*10+f*1

print("reverse number",rev)
