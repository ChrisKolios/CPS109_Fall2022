class Car:
    '''
    This is a very basic class. All it has is three properties:
    make, colour, price. Why does it have a "self"?
    Well, let's, instead, look at our method.
    '''
    def __init__(self, m, c, p):
        self.make = m
        self.colour = c
        self.price = p
    
    '''
    Notice how we have to call self again? And how there is only
    one argument, and it's self?

    Let's go look at its implementation
    '''

    def age_price(self):
        self.price = self.price - 500

def compare_price(car_one, car_two):
    return car_one.price == car_two.price

if __name__ == "__main__":
    our_car = Car("Honda Civic", "Blue", 12000)
    our_car.price
    our_car_2 = Car("Honda Civic", "Red", 14000)
    print("Our car is a: " + our_car.make)
    print("The colour is: " + our_car.colour)
    print("It costs: " + str(our_car.price))

    print(compare_price(our_car, our_car_2))

    '''
    Notice how when we call this method, that it has no arguments?
    Well, python actuall reads it as: age_price(our_car) (sorta).
    The "self" is the current object we're dealing with!
    '''
    our_car.age_price()
    print("It now costs: " + str(our_car.price))

    our_car.age_price()
    print("It now costs: " + str(our_car.price))
