student = open("student.txt","r+")
#print(student.writable)
text = student.read()
print(text)
size = len(text)
print(size)

for line in student:
    print(line)


student.close()
