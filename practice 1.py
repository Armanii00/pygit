#quiz game
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

score = 0
answer = input("what's does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what's does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what's does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions answer!")
print("You got " + str((score / 3) * 100) + " % .")