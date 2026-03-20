# Question 1
# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1, fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

# Question 2
# def f(i,values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

# Question 3
# def func(value , values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])

# Question 4
# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# Question 4
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

# Question 5 :- Given an array , return an array where each element is the product of all elements in the array except itself.
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
nums = list(map(int, input().split()))
# Output
print(productExceptSelf(nums))