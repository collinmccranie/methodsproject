class Book:

    def __init__(self, isbn, title, author, price, stock):

        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def GetISBN(self):
    
        return self.isbn 
    
    def GetTitle(self):
    
        return self.title
    
    def GetAuthor(self):
    
        return self.author
    
    def GetPrice(self):
    
        return self.price
    
    def GetStock(self):
    
        return self.stock