class bike(object):
    def __init__(self, name, price, max_speed, miles):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def display_info(self):
        print self.name, self.price, self. max_speed, self.miles

    def ride(self):
        print "riding"
        self.miles += 10
        return self

    def reverse(self):
        print "reversing"
        self.miles -= 5
        return self

HarleyDavidson = bike("Harley", 1000, 100, 0)
Kawasaki = bike("Kawasaki", 3000, 90, 0)
Schwinn = bike("Schwinn", 100, 15, 0)

HarleyDavidson.ride().ride().ride().reverse().display_info()
Kawasaki.ride().ride().reverse().reverse().display_info()
Schwinn.reverse().reverse().reverse().display_info()
