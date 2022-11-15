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
        username = input("Enter username: ")

        with open("user.txt", 'r') as f:
            
            while True:
                try:
                    lines = f.readline()
                    currentline = lines.split(",")
                    if currentline[1] == username:
                        password = input("Enter Password: ")
                        if currentline[2] == password:
                            self.cur_customer = username
                            return
                    
                        else: 
                            print("Incorrect Username or Password. ")
                except IndexError:
                    return 0

    def logout():
        print("Logged out successfully")