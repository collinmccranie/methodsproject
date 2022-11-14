import Inventory
import create_login_logout

class User:
    
    def __init__(self, name, password, shippingAddress, cardNumber):
        self.Name = name
        self.Pasword = password
        self.ShippingAddress = shippingAddress
        self.CardNumber = cardNumber

    def setName(self, name):
        self.Name = name

    def getName(self):
        return self.Name

    def setShippingAddress(self, username, shippingAddress):
        userLine = 0

        self.ShippingAddress = shippingAddress

        with open("user.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[1] == username:
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 3:
                            newLine += shippingAddress + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-2]+"\n"
                    with open("user.txt", "w") as file1:
                        file1.write("")
                    with open("user.txt", "a") as file2:
                        i = 0
                        for line in lines:
                            if i == userLine:
                                file2.write(newLine)
                            else:
                                file2.write(line)
                            i+=1
                else:
                    userLine += 1

    def getShippingAddress(self):
        return self.ShippingAddress

    def setCardNumber(self, username, card):
        userLine = 0

        self.CardNumber = card

        with open("user.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[1] == username:
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 4:
                            newLine += card + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-2]+"\n"
                    with open("user.txt", "w") as f1:
                        f1.write("")
                    with open("user.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == userLine:
                                f2.write(newLine)
                            else:
                                f2.write(line)
                            i+=1
                else:
                    userLine += 1

    def getCardNumber(self):
        return self.CardNumber

    def setPassword(self, password):
        self.Password = password

    def getPassword(self):
        return self.Password

    def setUsername(self, username):
        self.Username = username

    def getUsername(self):
        return self.Username

    def viewOrderHistory(self, username):
        inventory = Inventory.Inventory()
        firstL = True
        print(username + "'s Order History:\n")
        with open("orderHistory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    orderNum = 1
                    donePrinting = False
                    valueNum = 0
                    x = 1
                    while donePrinting == False:
                        i=1
                        print("Order number "+str(orderNum)+": \n")
                        orderNum += 1
                        moveOn = False
                        while moveOn == False:
                            if x+i != len(values)-1:
                                if values[x+i] != username:
                                    returnValue = inventory.getItemNameandPrice(values[i])
                                    print("Title: " + returnValue[1] + " -- " + returnValue[0] + "\n")
                                    i+=2
                                else:
                                    moveOn = True
                                    x+=i
                            else:
                                moveOn = True
                                donePrinting = True

    def deleteAccount(self, username):
        choice = input("Are you sure you want to delete your account? [y/n]: ")
        if choice == "n":
            return False
        elif choice == "y":
            userLine = 0

            with open("user.txt", "r") as f:
                done = False
                lines = f.readlines()
                for line in lines:
                    values = line.split(",")
                    if values[2] == username:
                        with open("user.txt", "w") as f1:
                            f1.write("")
                        with open("user.txt", "a") as f2:
                            i = 0
                            for line in lines:
                                if i == userLine:
                                    done = True
                                else:
                                    f2.write(line)
                                i+=1
                    else:
                        userLine += 1
            userLine = 0

            with open("shoppingCarts.txt", "r") as f:
                done = False
                lines = f.readlines()
                for line in lines:
                    values = line.split(",")
                    if values[0] == username:
                        with open("shoppingCarts.txt", "w") as f1:
                            f1.write("")
                        with open("shoppingCarts.txt", "a") as f2:
                            i = 0
                            for line in lines:
                                if i == userLine:
                                    done = True
                                else:
                                    f2.write(line)
                                i+=1
                    else:
                        userLine += 1
            userLine = 0

            with open("orderHistory.txt", "r") as f:
                done = False
                lines = f.readlines()
                for line in lines:
                    values = line.split(",")
                    if values[0] == username:
                        with open("orderHistory.txt", "w") as f1:
                            f1.write("")
                        with open("orderHistory.txt", "a") as f2:
                            i = 0
                            for line in lines:
                                if i == userLine:
                                    done = True
                                else:
                                    f2.write(line)
                                i+=1
                    else:
                        userLine += 1
            return True
        else:
            print("Please enter [y/n].")