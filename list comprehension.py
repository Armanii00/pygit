num = [1,2,3,4,5]
result = list(map(lambda x: x*x,num))
print(result)

num1 = [1,2,3,4]


result1 = [x * x for x in num1]

print(result1)


num2 = [2,3,4,6,8,9]

result3 = [x for x in num2 if x%2==0]
print(result3)