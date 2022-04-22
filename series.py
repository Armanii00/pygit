# 1+ 2 + 3+ ...+n
n = int(input("enter the last number: "))
sum = 1

for x in range(2, n+1, 2):
    sum = sum + x*x
print(sum)