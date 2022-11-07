import User
import ShoppingCart
import Inventory
import create_login_logout

cur_customer = create_login_logout.create_login_logout()

def shop_menu():

    cur_inventory = Inventory.Inventory()
    cur_shoppingCart = ShoppingCart.ShoppingCart()

    while True:
        print("\nView Inventory - 1")
        print("Add Item to Cart - 2")
        print("Go Back - 3")
        print("Exit Program - 4")

        u_input = input("Choose from the options 1, 2, 3, 4: ")

        if u_input == "1":
            cur_inventory.viewInventory()

        elif u_input == "2":
            isbn_input = input("What is the ISBN of the book? ")
            if cur_inventory.checkIfItemExists(isbn_input) == True:
                numInput = input("How many of this book do you want? ")
                if cur_inventory.checkStock(isbn_input, numInput) == True:
                    cur_shoppingCart.addItem(cur_customer.getCurrentUser(),isbn_input,numInput)
                else:
                    print("Not enough stock available.\n")
            else:
                print("ISBN does not exist.\n")

        elif u_input == "3":
            return

        elif u_input == "4":
            return 0

        else:
            print("Not a valid input")

def cart_menu():
    cur_shoppingCart = ShoppingCart.ShoppingCart()
    cur_inventory = Inventory.Inventory()

    while True:
        print("\nView Cart - 1")
        print("Remove Item from Cart - 2")
        print("Checkout - 3")
        print("Go Back - 4")

        userinput = input("Choose from the options 1, 2, 3, 4: ")

        if userinput == "1":
            cur_shoppingCart.viewCart(cur_customer.getCurrentUser())

        elif userinput == "2":
            isbn_input = input("What is the ISBN for the book you would like to remove? ")
            if cur_inventory.checkIfItemExists(isbn_input) == True:
                cur_shoppingCart.removeItem(cur_customer.getCurrentUser(), isbn_input)
            else:
                print("ISBN is not valid.\n")

        elif userinput == "3":
            cur_shoppingCart.checkout(cur_customer.getCurrentUser())

        elif userinput == "4":
            return

        else:
            print("Not a valid input")

def account_menu():
    cur_user = User.User()

    while True:
        print(cur_customer.getCurrentUser(), "'s Account:")

        print("Edit Shipping Info - 1")
        print("Edit Payment Info - 2")
        print("Delete Account - 3")
        print("Logout - 4")

        u_input = input("Choose from the options 1, 2, 3, 4: ")

        if u_input == '1':
            shipInput = input("What is your new Address? ")
            cur_user.setShippingAddress(cur_customer.getCurrentUser(), shipInput)
        
        elif u_input == '2':
            paymentInput = input("What is your new Card Number? ")
            cur_user.setCardNumber(cur_customer.getCurrentUser(), paymentInput)

        elif u_input == '3':
            if cur_user.deleteAccount(cur_customer.getCurrentUser()) == True:
                login_menu()

            else:
                store_menu()

        elif u_input == '4':
            print("Logging out.")
            login_menu()

        else:
            print("Not a valid input")

def store_menu():
    cur_user = User.User()

    while True:
        print("\nWelcome", str(cur_customer.getCurrentUser()), "\n")

        print("Shop - 1")
        print("Cart Information - 2")
        print("Order History - 3")
        print("Account - 4")
        print("Exit Program - 5")

        u_input = input("Choose from the options 1, 2, 3, 4, 5: ")

        if u_input == '1':
            shop_menu()
        
        elif u_input == '2':
            cart_menu()

        elif u_input == '3':
            cur_user.viewOrderHistory(cur_customer.getCurrentUser())

        elif u_input == '4':
            account_menu()

        elif u_input == '5':
            print("Exiting program.")
            return 0

        else:
            print("Not a valid input")

def login_menu():
    print("Welcome to the Book Store!\n")

    print("Login - 1")
    print("Create Account - 2")
    print("Exit Program - 3")

    u_input = input("Select from the above options 1, 2, 3: ")

    while(True):
        if u_input == '1':
                cur_customer.login()
                if cur_customer.getCurrentUser() == "":
                    print()
                else:
                    store_menu()
                    return


        elif u_input == '2':
            print("You decided to create an account with us!")

            full_name = str(input("Enter your full name: "))
            username = str(input("Enter your new username:"))
            password = str(input("Enter your password: "))
            shippingaddress = str(input("Enter your shipping address: "))
            cardnumber = str(input("Enter your card number for payment: "))

            writeToFile = (full_name + "," + username + "," + password + "," + shippingaddress + "," + cardnumber + ",\n")

            write_to_file("user.txt", writeToFile)

            with open("shoppingCarts.txt", "a") as f:
                f.write(username + ",\n")

            with open("orderHistory.txt", "a") as f:
                f.write(username + ",\n")

            cur_customer.setCurrentUser(username)
            print("Account Created! Logged in as " + cur_customer.getCurrentUser() + '\n')
            
            store_menu()


        elif u_input == '3':
            print("Exiting Program...")
            exit()

        else:
            u_input = input("Invalid. Select either 1, 2, or 3: ")

def write_to_file(filename, input):
    with open(filename, 'a') as f:
        f.write(input)
        f.close()

def main():
    login_menu()

if __name__ == "__main__":
    main()
