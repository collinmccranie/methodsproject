class ShoppingCart:

    def __init__(self, username, isbn, num):

        self.username = username
        self.isbn = isbn
        self.num = num

    def viewCart(self, username):
        
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == username:
                    tkns.pop(0)
                    print("Shopping Cart:")

                    i = 0
                    while i + 1 < len(tkns):
                        print("Title: ", tkns[i], " , Amount: ", tkns[i + 1])
                        i += 2

        return
        

    def addItem(self, username, isbn, num):
        newCarts = []

        with open("inventory.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == isbn:
                    title = tkns[1]

        with open("shoppingCart.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == username:
                    i = 0
                    while i + 1 < len(tkns):
                        if tkns[i] == title:
                            tkns[i + 1] += num
                            exist = True
                            break
                        else:
                            exist = False
                            i += 1
                    
                    if exist:
                        line = ",".join(tkns)

                    else:
                        line += title, ",", num
                
                newCarts = "\n".join(lines)

        with open("shoppingCarts.txt", "w") as f:
            f.write(newCarts)

        return

    def removeItem(self, username, isbn, num):
        newCarts = []

        with open("inventory.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == isbn:
                    title = tkns[1]

        with open("shoppingCart.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == username:
                    i = 0
                    while i + 1 < len(tkns):
                        if tkns[i] == title:
                            if tkns[i + 1] > num:
                                tkns[i + 1] -= num

                            elif tkns[i + 1] == num:
                                tkns.pop(i)
                                tkns.pop(i + 1)

                            else:
                                print("You are attempting to remove more copies of ", title, " than are in your cart.\n")

                            break
                        else:
                            i += 1
                        
                    line = ",".join(tkns)
                
                newCarts = "\n".join(lines)

        with open("shoppingCarts.txt", "w") as f:
            f.write(newCarts)

        return
     
    def checkout(self, username):
        newOrders = []
        orders = []

        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == username:
                    tkns.pop(0)

                    i = 0
                    while i + 1 < len(tkns):
                        j = 0
                        while j < int(tkns[i + 1]):
                            newOrders.append(tkns[i])
                            j += 1
                        i += 2

        with open("orderHistory.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                tkns = line.split(",")

                if tkns[0] == username:
                    for book in newOrders:
                        tkns.append(book)

                line = ",".join(tkns)

            orders = "\n".join(lines)

        with open("orderHistory.txt", "w") as f:
            f.write(orders)

        return
