class phone:
    def call(self):
        print("you can call ")
    def message(self):
        print("you can message")


class network:
    def sim(self):
        print("your sim airtel")


class samsung(phone,network):
    def photo(self):
        print("you can take photo")
    def call(self):
        print("you can call")


s = samsung()
s.call()
s.message()
s.photo()
s.sim()