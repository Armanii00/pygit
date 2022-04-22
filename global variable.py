a = 50
def show():
    x = 10
    print(x)
    print(a)
show()


#global keyword
i = 10
def show():
    global i
    i = i + 1
    print("A: ", i)
show()
print("A: ", i)