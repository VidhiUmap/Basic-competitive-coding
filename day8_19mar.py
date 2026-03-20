#WAP to perform arithmatic operation using functional programming approach 
#Functions helps us to achieve modularity approach
# import sys
# def addition(num1, num2): #called function
#     print("Addition=", num1+num2)

# def substraction(num1, num2):#called function
#     print("Substraction=", num1 - num2)

# def multiplication(num1, num2):#called function
#     print("Multiplication=", num1 * num2)

# def division():# called function
#     pass

# while True:
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Multiplication")
#     print("4. division ")
#     print("5. Exit")
#     choice = int(input("Enter your choice from above options :"))
#     if choice == 5:
#         sys.exit()
#     val1   = int(input("Enter First Value :"))
#     val2   = int(input("Enter Second Value :"))
#     if choice == 1:
#         addition(val1, val2)
#     elif choice == 2:
#         substraction(val1, val2)
#     elif choice == 3:
#         multiplication(val1, val2)
#     elif choice == 4:
#         pass
#     else:
#         print("You have entered wrong choice :")

#Program 2 :- 
# def outerFunction():
#     print("this is my outer function:")
#     def innerFunction():
#         print("inner Function")
#     innerFunction()
# outerFunction()

#Program 3:-
# WAP to count the word
# name = "Vidhi Umap"
# count = 1
# for i in name:
#     if i == " ":
#         count += 1
#     else:
#         continue
# print("Total word count =",count)

# init_Tuple_a = 'a','b'
# init_Tuple_b = ('a','b')
# print(init_Tuple_a == init_Tuple_b)

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),) * 7
# print(len(init_tuple[3:8]))

# 
# s = ""
# s1 = s.replace("difficult","easy")
# print(s1)
# s = "adadadadadad"
# s1 = s.replace("a","b")
# print(s1)

#
# city = input("Enter the city name:")
# scity = city.strip()
# if scity == 'Hyderabad':
#     print("Hello Hyderabad")
# elif scity == 'Chennai':
#     print("Chennai")
# elif scity == "Bangalore":
#     print("Bangalore")
# else:
#     print("Your entered city is invalid")

# 
# s = [i*i for i in range (1,11)]
# print(s)

# val = [2**i for i in range(1,6)]
# print(val)

# val2 = [i for i in s if i%2 == 0]
# print(val2)

# 
squares = {x:x*x for x in range(1,6)}
print(squares)

doubles = {x:2*x for x in range(1,6)}
print(doubles)