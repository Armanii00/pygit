def add(*details):
    sum = 0
    for num in details:
        sum = sum + num
    return sum
print(add(10, 20))