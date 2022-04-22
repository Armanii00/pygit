#keyword
try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)

    print("done")
except ZeroDivisionError :
    print("dividing by zero is not possible")
except IndexError :
    print("Index error")
#finally use for nonstop code
finally:
    print("successful")