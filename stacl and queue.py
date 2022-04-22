#STACK

books = []
#push

books.append("Learn python")
books.append("learn c")
books.append("learn java")
books.append("learn c#")
print(books)


books.pop()
print("Now the top book is: ", books[-1])

books.pop()
print("Now the top book is: ", books[-1])

books.pop()
print("Now the top book is: ", books[-1])

books.pop()

if not books:
    print("no book available")