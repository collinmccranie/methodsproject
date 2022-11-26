import User

class create_login_logout:

    def __init__(self, cur_customer = None):
        self.cur_customer = cur_customer

    def setCurrentUser(self, cur_customer):
        self.cur_customer = cur_customer

    def getCurrentUser(self):
        return self.cur_customer

    def createAccount(name, username, password, shippingAddress, paymentInfo):
        new_user = User.User(name, username, password, shippingAddress, paymentInfo)

        with open("shoppingCarts.txt", "a") as f:
            f.write(username + ",\n")

        with open("orderHistory.txt", "a") as f:
            f.write(username + ",\n")

        return new_user


    def login(self):
        with open("user.txt", 'r') as f:
            i = 0
            lines = f.readlines()

            while True:
                username = input("Enter username: ")
                for line in lines:
                    values = line.split(",")
                    if (values[1] == username):
                        password = input("Enter Password: ")
                        if values[2] == password:
                            self.cur_customer = username
                            return
                if i == 2:
                    return
                else:
                    print("Invalid Username or Password. ", 2 - i, " More Attempts.")
                    i = i + 1

    def logout():
        print("Logged out successfully")