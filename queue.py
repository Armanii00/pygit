from collections import deque
bank = deque(["arman", "karim", "joy"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()

if not bank:
    print("no person left")