import random

class product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    
    def display_info(self):
        print "Item name: ", self.item_name
        print "Price: ", self.price
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status 
        return self

    def sold(self):
        self.status = "Sold!"
        print "Status: ", self.status
        return self

    def add_tax(self):
        tax = random.random()
        self.price += tax
        print "Tax added. Price is now ", self.price
        return self

    def return_item(self, reason):
        if reason == 'defect':
            self.price = 0
            self.status = "Defective" 
            print 'Product is defective. Price is now ', self.price
            return self
        
        elif reason == 'in box':
            self.status = "For Sale Again"
            print "Item returned and status is ", self.status
            return self
        
        elif reason == 'open':
            discount = self.price * .2
            self.price = self.price - discount
            self.status = "For Sale again"
            print "Item returned open. Price is now ", self.price
            return self

        else:
            print "Return options: open, defect, in box"
            return self
        



Apple = product(.5, "Red delicious apple", "5 grams", "Wilson Farms", "For Sale")

Apple.return_item("open").add_tax().display_info()
