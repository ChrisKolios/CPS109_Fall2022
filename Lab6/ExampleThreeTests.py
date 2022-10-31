import unittest
import ExampleThree

class my_tests(unittest.TestCase):
    def test1(self):
        car_one = ExampleThree.Car("Honda Civic", "Red", 14000)
        car_two = ExampleThree.Car("Toyota RAV4", "Green", 14000)
        self.assertEqual(ExampleThree.compare_price(car_one, car_two), True)
    def test2(self):
        car_three = ExampleThree.Car("Chrysler Malibu", "Blue", 9000)
        car_one = ExampleThree.Car("Honda Civic", "Red", 14000)
        self.assertNotEqual(ExampleThree.compare_price(car_one, car_three), True)

if __name__ == '__main__':
    unittest.main(exit=True)
