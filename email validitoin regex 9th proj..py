#a - z
#0-9
#. _ time 1

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"  #? mean 1 time
user_email = input("Enter your Email: ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email ")