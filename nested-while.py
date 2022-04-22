#nested while loop
i = 1
while i <= 2:
    print("outer loop" , i)
    i = i + 1
    j = 1
    while j<=3:
        print("inner loop", j)
        j = j + 1
print("end")