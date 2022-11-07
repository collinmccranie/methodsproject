from optparse import Values
import Book

class Inventory:
    
    def viewInventory(self):
        print("Inventory:\n")
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                #print(value)
                print("ISBN-  " + value[0] + " | Title-  " + value[1] + " | Author-  " + value[2] + " | Price-  " + value[3] + " | Stock-  " + value[4] + "\n")

    def checkIfItemExists(self, isbn):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                if value[0] == isbn:
                    return True
            return False

    def checkStock(self, isbn, amount):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                if value[0] == isbn:
                    if int(value[4]) >= int(amount):
                        return True
            return False
    
    def getItemNameandPrice(self, isbn):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == isbn:
                    returnVals = [values[0], values[1]]
                    return returnVals

    def SubtractItemStock(self, isbn, amount):
        itemLine = 0
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == isbn:
                    newValue = str(int(values[4])-int(amount))
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 4:
                            newLine += newValue + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-1]+"\n"
                    with open("inventory.txt", "w") as file1:
                        file1.write("")
                    with open("inventory.txt", "a") as file2:
                        i = 0
                        for line in lines:
                            if i == itemLine:
                                file2.write(newLine)
                            else:
                                file2.write(line)
                            i+=1
                else:
                    itemLine += 1