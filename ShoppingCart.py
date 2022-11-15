import Book
import Inventory
import create_login_logout

class ShoppingCart:
    
    def viewCart(self, username):
        inventory = Inventory.Inventory()
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    print("\n"+username+"'s Cart:\n")
                    name = True
                    skip = False
                    i = 0
                    x = 0
                    numItems = (len(values) - 2)/2
                    for value in values:
                        if name == False and x != numItems:
                            if skip == False:
                                returnValue = inventory.getItemNameandPrice(value)
                                print("Title: " + returnValue[1] + " -- " + value + " | Amount: " + values[i+1] + "\n")
                                skip = True
                                x += 1
                            else:
                                skip = False
                        else:
                            name = False
                        i+=1

    def addItem(self, username, isbn, Amount):
        cartline = 0
        alreadyExists = False
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    x = 0
                    for value in values:
                        if value == isbn:
                            newValue = str(int(values[x+1])+int(Amount))
                            alreadyExists = True
                        x+=1
                    if alreadyExists == False:
                        newline = line[0:len(line)-1]+isbn+","+Amount+",\n"
                    else:
                        newline = ""
                        updated = False
                        for value in values:
                            if value == isbn:
                                newline += value + ","+ newValue + ","
                                updated = True
                            elif updated == True:
                                updated = False
                            else:
                                newline += value + ","
                        newline = newline[0:len(newline)-2]+"\n"
                        
                    with open("shoppingCarts.txt", "w") as f1:
                        f1.write("")
                    with open("shoppingCarts.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == cartline:
                                f2.write(newline)
                            else:
                                f2.write(line)
                            i+=1
                    print("\nAdded Item to cart\n")
                else:
                    cartline += 1

    def removeItem(self, username, isbn):
        cartline = 0
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                newline = ""
                removed = False
                skip = False
                usernameCheck = True
                if values[0] == username:
                    newline += values[1] + ","

                    for value in values:
                        if value == isbn:
                            removed  = True
                            skip = True
                        else:
                            if skip == False:
                                if usernameCheck == False:
                                    newline += value + ","
                                else:
                                    usernameCheck = False
                            else:
                                skip = False
                    
                    if removed == False:
                        print("Item does not exist in your cart.\n")
                        return
                    else:
                        newline = newline[0:len(newline)-2]+"\n"
                        with open("shoppingCarts.txt", "w") as f1:
                            f1.write("")
                        with open("shoppingCarts.txt", "a") as f2:
                            i = 0
                            for line in lines:
                                if i == cartline:
                                    f2.write(newline)
                                else:
                                    f2.write(line)
                                i+=1
                        print("\nRemoved Item from cart\n")
                else:
                    cartline += 1

    def checkout(self, username):
        inventory = Inventory.Inventory()
        cart = ""
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    # create new line without username
                    cart_noUser = values[1] + "," + values[2] + ",\n"
                    cart += line
                    skip = False
                    i = 0
                    x = 0
                    numItems = (len(values)-2)/2
                    for value in values:
                        if value != username and skip == False and x != numItems:
                            inventory.SubtractItemStock(value, values[i+1])
                            skip = True
                            x+=1
                        else:
                            skip = False
                        i+=1
        
        with open("orderHistory.txt", "r") as f:
            userLine = 0
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    # changed from newLine = line[0:len(line)-1] + cart
                    newLine = line[0:len(line)-1] + cart_noUser
                    newLine = newLine[0:len(newLine)-1]+"\n"
                    with open("orderHistory.txt", "w") as f1:
                        f1.write("")
                    with open("orderHistory.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == userLine:
                                f2.write(newLine)
                            else:
                                f2.write(line)
                            i+=1
                else:
                    userLine += 1
        
        cartLine = 0
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    with open("shoppingCarts.txt", "w") as f1:
                        f1.write("")
                    with open("shoppingCarts.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == cartLine:
                                f2.write(username+",\n")
                            else:
                                f2.write(line)
                            i+=1
                else:
                    cartLine += 1
        print("Checkout Complete!")
