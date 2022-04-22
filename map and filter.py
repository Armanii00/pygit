
def square(x):
    return x*x

num = [1,2,3,4,5]

result = list(map(square,num))

print(result)

num1 = [4,5,6,7,8]
result1 = list(filter(lambda x: x % 2 == 0,num1))

print(result1)