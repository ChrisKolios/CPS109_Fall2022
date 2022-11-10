import unittest
# Note that this week's Quiz will be a special one :)

# Firstly, instead of creating your own program you'll be operating off this Python file which you can download to your system (or whose contents you can paste on Spyder/etc.)
# Secondly, you will be tasked with implementing two classes and multiple different instance methods, whose intended behaviours are described in their docstrings.
# You ARE NOT to modify the if __name__ == "__main__", or any of the unit tests, EXCEPT the first unit test (where indicated)!
# To get full marks, you must implement both constructors, the first 7 methods, and the first unit test. The final 2 methods in the Workshop class are a bonus (not for marks).

# Quiz Question: CPS109's Ridiculously Early Christmas Special

#     _\/_
#      /\
#      /\
#     /  \
#     /~~\o
#    /o   \
#   /~~*~~~\
#  o/    o \
#  /~~~~~~~~\~`
# /__*_______\
#      ||
#    \====/
#     \__/

# Tired from Halloween festivities, you stumble into your early morning CPS109 lab. All of a sudden, you hear a muffled song. It gradually grows louder, and you start picking up some words here and there...
# "... don't want a lot for Christmas ... just one thing I need ...". Oh no... It's Mariah Carey. She's coming. https://www.youtube.com/watch?v=yXQViqx6GMY
# In today's quiz, you must simulate Santa's Workshop using Python.
# Being a Python expert (and a huge Mariah fan), you think to yourself: "this is gonna be ezpz"

class Elf():
    '''
    Before you program the Workshop class you need to program the class for the actual workers (the elves)!
    Elves are the (arguably exploited) labour force in Santa's Workshops. They all have a name, a rate of productivity, and a specialty product. They also have a favourite Christmas singer/songwriter.
    Fill in the methods according to their docstrings.
    '''
    def __init__(self, name, rate_of_productivity, specialty_product, favourite_christmas_singer): # Constructor 1 (required)
        '''
        Complete the constructor.

        Input Arguments:
            name (string): The name of the elf
            rate_of_productivity (int): The number of toys the elf can produce in one hour
            specialty_product (string): The toy that the elf specializes in making. When making this toy, their rate_of_productivity is tripled!
            favourite_christmas_singer (string:"Mariah Carey" OR string:"Michael Buble"): The favourite singer/songwriter of the elf. If their favourite singer's song is playing in the workshop, their rate_of_productivity is temporarily doubled!
        Return:
            None
        Behaviour:
            Set self.argument to be equal to the constructor's input for each argument.
            Hint: Recall default arguments
        '''
        self.name = name
        self.rate_of_productivity = rate_of_productivity
        self.specialty_product = specialty_product
        self.favourite_christmas_singer = favourite_christmas_singer

    def eat_candycane(self): # Method 1 (required)
        '''
        While elves have a default rate_of_productivity, eating a candycane allows them to permanently increase their rate by one product per hour.

        Input Arguments:
            None (just self, which you always need for instance methods)
        Return:
            None
        Behaviour:
            Increate the elf's rate_of_productivity by one
        '''
        self.rate_of_productivity += 1

    def update_rate_of_productivity(self, new_rate_of_productivity): # Method 2 (required)
        '''
        Sometimes elves can change their default rate_of_productivity through some initiative other than eating candy canes. Complete a method that allows their rate of productivity to be set to a provided input.

        Input Arguments:
            new_rate_of_productivity (int): The new rate_of_productivity of the elf
        Return:
            None
        Behaviour:
            Set the elf's rate_of_productivity to the new_rate_of_productivity
        '''
        self.rate_of_productivity = new_rate_of_productivity

    def create_product(self, product, time_period, current_workshop): # Method 3 (required)
        '''
        The purpose of an elf is to make product. They enjoy it, and require no compensation. It's a capitalist's dream.
        Given an input product, as well as a time period and the current workshop, return the amount of product they create.
        Remember that if an elf is working on their specialty product their rate of productivity is tripled, and if their favourite christmas singer is playing in the workshop they are in, their rate of productivity is doubled. These stack.
        Hint: You may want to implement the constructor for a Workshop before completing this method (and, specifically, look at the Workshop's current_singer attribute)

        Input Arguments:
            product (string): The name of the product the elf is tasked with creating
            time_period (int): The number of hours the elf has to make the product
            current_workshop (Workshop): The current workshop the elf is assigned to
        Return:
            amount_of_product (int): The amount of a product the elf is able to create in the given time
        Behaviour:
            Return the amount of product the elf creates, as determined by multipling the rate of productivity by the time period, and taking into account any productivity modifiers (specialty products, current singer in workshop)
        '''
        amount_of_product =  self.rate_of_productivity * time_period # Pre multipliers
        if (product == self.specialty_product): # *3 if specialty product
            amount_of_product = amount_of_product * 3
        if (current_workshop.current_singer == self.favourite_christmas_singer): # *2 if favourite singer playing
            amount_of_product = amount_of_product * 2
        return amount_of_product
            

class Workshop():
    '''
    Workshops are pretty complex, but they essentially consist of a name, some elves, a current singer, and a dictionary containing the amount of each toy/product created
    Fill in the instance methods according to their docstrings.
    '''
    def __init__(self, name, elves, current_singer): # Constructor 2 (required)
        '''
        Complete the constructor.

        Input Arguments:
            name (string): The name of the Workshop
            elves (list of Elfs): A list of all Elfs at the workshop
            current_singer (string:"Mariah Carey" OR string:"Michael Buble"): The current singer of the song playing in the workshop
        Return:
            None
        Behaviour:
            Set self.argument to be equal to the constructor's input for each argument.
            Also, set self.toys_created to some empty dictionary. (see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
        '''
        self.name = name
        self.elves = elves
        self.current_singer = current_singer
        self.toys_created = {} # Empty dictionary by default, per behaviour

    def dj_santa_in_the_house(self): # Method 4 (required)
        '''
        When DJ Santa comes to the workshop he switches the current singer. Remember there are only two possible Christmas singers in a Workshop: Mariah Carey or Michael Buble

        Input Arguments:
            None
        Return:
            None
        Behaviour:
            If the current_singer is "Mariah Carey", switch the current_singer to "Michael Buble", and vice versa.
        '''
        if (self.current_singer == "Mariah Carey"):
            self.current_singer = "Michael Buble"
        elif (self.current_singer == "Michael Buble"): # Technically could just be an else (more efficient)
            self.current_singer = "Mariah Carey"

    def add_to_workshop(self, elf_to_add): # Method 5 (required)
        '''
        What use is a workshop without its labourers? Create a method to add an elf to a workshop (if they are not already at the workshop!)

        Input Arguments:
            elf_to_add (Elf): The Elf you want to add to the elves list
        Return:
            None
        Behaviour:
            If elf_to_add is not already in elves
                First, call their eat_candycane() method as a signing bonus
                Then, add them to the elves list for this workshop
            Otherwise
                Do nothing, as they're already at the workshop
        '''
        if elf_to_add not in self.elves:
            elf_to_add.eat_candycane()
            self.elves.append(elf_to_add)

    def remove_from_workshop(self, elf_to_remove): # Method 6 (required)
        '''
        Sometimes you need to remove an elf from a workshop (perhaps they have been discussing unionization). When elves get sacked their rate_of_productivity decreases by one (due to morale).

        Input Arguments:
            elf_to_remove (Elf): The Elf you want to remove
        Return:
            None
        Behaviour:
            If elf_to_remove is in the elves list
                Decrement their rate_of_productivity by 1 using their update_rate_of_productivity method, and accessing their rate_of_productivity attribute. Note that an Elf should never have a negative rate_of_productivity.
                Remove them from the elves list
                Hint: Recall list.remove()
            Otherwise
                Do nothing, as they are not at this workshop
        '''
        if elf_to_remove in self.elves:
            current_rop = elf_to_remove.rate_of_productivity
            if (current_rop > 0):
                elf_to_remove.update_rate_of_productivity(current_rop - 1)
            self.elves.remove(elf_to_remove)

    def create_products(self, product, time_assigned): # Method 7 (required)
        '''
        The purpose of a Workshop is to create product. When an order comes from the top of the North Pole (directly from Santa himself), all elves working at the workshop must immediately begin working on creating the desired product for the time assigned.
        Once the time is up, using the product as a key, add the sum of all products created by the elves to the value in the toys_created dictionary.

        Input Arguments:
            product (string): The product you want the elves to create
            time_assigned (int): The amount of hours the elves must work on this product for
        Return:
            None
        Behaviour:
            For all Elfs in the elves list
                Call their create_product method, passing in the appropriate inputs (read the method Input Arguments and their expected types closely!)
                Add the output of that method to some running sum
            Add the sum to the toys_created dictionary, with the key being the product, and the value being the existing value plus the running sum
        '''
        current_sum = 0
        for elf in self.elves:
            current_sum += elf.create_product(product, time_assigned, self) # Notice how we pass in self here (as self is the Workshop instance)
        if (product not in self.toys_created): # We must check if already in dictionary
            self.toys_created[product] = current_sum
        else:
            self.toys_created[product] = self.toys_created[product] + current_sum

    def roll_call(self): # Method 8 (bonus)
        '''
        When Supervisor Rudolph blows his magic horn, all elves in the workshop are required to "sound off", and then at the end the current toys_created dictionary must be printed.

        Input Arguments:
            None
        Return:
            None
        Behaviour:
            For all Elfs in the elves list
                print: "My name is" followed by their name "and my specialty is" followed by their specialty product
            For each product in the toys_created dictionary
                print: product ":" num_product_created
        '''
        for elf in self.elves:
            print("My name is", elf.name, "and my specialty is", elf.specialty_product)
        for k, v in self.toys_created.items():
            print(k, ":", v)

    def celebrity_visit(self, mariah_or_michael): # Method 9 (bonus)
        '''
        Sometimes, when morale is really low, Santa flies either Mariah Carey or Michael Buble to the Workshops via his sleigh to increase productivity.
        Whenever this happens, all elves whose favourite singer is the one who visited will permanently increase their rate of productivity by 3.

        Input Arguments:
            mariah_or_michael (string:"Mariah Carey" OR string:"Michael Buble"): The visiting artist
        Return:
            None
        Behaviour:
            For all Elfs in the elves list
                If their favourite singer is the one visiting
                    Increate their rate of productivity by 3 using their update_rate_of_productivity method, and accessing their rate_of_productivity attribute.
        '''
        for elf in self.elves:
            if elf.favourite_christmas_singer == mariah_or_michael:
                current_rop = elf.rate_of_productivity
                elf.update_rate_of_productivity(current_rop + 3)
        

class SantasWorkshopTestCases(unittest.TestCase):
    def test_1_eat_candycane(self): # YOU DO THIS (required)
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        te.eat_candycane()
        self.assertEqual(te.rate_of_productivity, 2)
    def test_2_elf_initialization(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        self.assertEqual(te.name, "Chris")
        self.assertEqual(te.rate_of_productivity, 1)
        self.assertEqual(te.specialty_product, "Hats")
        self.assertEqual(te.favourite_christmas_singer, "Mariah Carey")
    def test_3_update_rate_of_productivity(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        te.update_rate_of_productivity(3)
        self.assertEqual(te.rate_of_productivity, 3)
    def test_4_create_product_no_multipliers(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [], "Michael Buble")
        self.assertEqual(te.create_product("Boots", 3, tw), 3)
    def test_5_create_product_specialty(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [], "Michael Buble")
        self.assertEqual(te.create_product("Hats", 4, tw), 12)
    def test_6_create_product_favoured_singer(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [], "Mariah Carey")
        self.assertEqual(te.create_product("Boots", 5, tw), 10)
    def test_7_create_specialty_product_favoured_singer(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [], "Mariah Carey")
        self.assertEqual(te.create_product("Hats", 5, tw), 30)
    def test_8_workshop_initialization(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        te2 = Elf("Buddy", 2, "Gumdrops", "Michael Buble")
        tw = Workshop("North Pole 1", [te, te2], "Mariah Carey")
        self.assertEqual(tw.name, "North Pole 1")
        self.assertEqual(tw.elves, [te, te2])
        self.assertEqual(tw.current_singer, "Mariah Carey")
        self.assertEqual(tw.toys_created, {}) # Empty dictionary
    def test_9_dj_santa_mariah_to_buble(self):
        tw = Workshop("North Pole 1", [], "Mariah Carey")
        tw.dj_santa_in_the_house()
        self.assertEqual(tw.current_singer, "Michael Buble")
    def test_10_dj_santa_buble_to_mariah(self):
        tw = Workshop("North Pole 1", [], "Michael Buble")
        tw.dj_santa_in_the_house()
        self.assertEqual(tw.current_singer, "Mariah Carey")
    def test_11_add_to_workshop_present(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [te], "Mariah Carey")
        tw.add_to_workshop(te)
        self.assertEqual(te.rate_of_productivity, 1) # Should be unchanged
        self.assertEqual(tw.elves, [te]) # Should be unchanged
    def test_12_add_to_workshop_not_present(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [], "Mariah Carey")
        tw.add_to_workshop(te)
        self.assertEqual(te.rate_of_productivity, 2) # Should be increased (relies on Elf's eat_candycane method)
        self.assertEqual(tw.elves, [te]) # Should be modified
    def test_13_remove_from_workshop_present(self):
        te = Elf("Chris", 2, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [te], "Mariah Carey")
        tw.remove_from_workshop(te)
        self.assertEqual(te.rate_of_productivity, 1) # Should be decreased (relies on Elf's update_rate_of_productivity method)
        self.assertEqual(tw.elves, []) # Should be modified
    def test_14_remove_from_workshop_present_ensure_nonnegative(self):
        te = Elf("Chris", 0, "Hats", "Mariah Carey")
        tw = Workshop("North Pole 1", [te], "Mariah Carey")
        tw.remove_from_workshop(te)
        self.assertEqual(te.rate_of_productivity, 0) # Should be the same as cannot reduce to negative
        self.assertEqual(tw.elves, []) # Should be modified
    def test_15_remove_from_workshop_not_present(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey")
        te2 = Elf("Buddy", 2, "Gumdrops", "Michael Buble")
        tw = Workshop("North Pole 1", [te2], "Mariah Carey")
        tw.remove_from_workshop(te)
        self.assertEqual(te.rate_of_productivity, 1) # Should be unchanged
        self.assertEqual(tw.elves, [te2]) # Should be unchanged
    def test_16_create_products_1(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey") # Should make 6 gumdrops in 3 hours with Mariah Carey
        te2 = Elf("Buddy", 2, "Gumdrops", "Michael Buble") # Should make 18 gumdrops in 3 hours with MC
        te3 = Elf("Saghar", 3, "Gumdrops", "Mariah Carey") # Should make 54 gumdrops in 3 hours with MC
        tw = Workshop("North Pole 2", [te, te2, te3], "Mariah Carey")
        tw.create_products("Gumdrops", 3)
        self.assertEqual(tw.toys_created, {"Gumdrops":78})
    def test_17_create_products_2(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey") # Should make 4 gumdrops in 2 hours with Mariah Carey
        te2 = Elf("Buddy", 2, "Gumdrops", "Michael Buble") # Should make 12 gumdrops in 2 hours with MC
        te3 = Elf("Saghar", 3, "Gumdrops", "Mariah Carey") # Should make 36 gumdrops in 2 hours with MC
        tw = Workshop("North Pole 2", [te, te2, te3], "Mariah Carey")
        tw.create_products("Gumdrops", 2)
        self.assertEqual(tw.toys_created, {"Gumdrops":52})
        tw.dj_santa_in_the_house() # Switching to Michael Buble
        tw.create_products("Gumdrops", 1)
        # Chris should make 1 gumdrop in 1 hour with Michael Buble
        # Buddy should make 12 gumdrops in 1 hour with MB
        # Saghar should make 9 gumdrops in 1 hour with MB
        self.assertEqual(tw.toys_created, {"Gumdrops":74})
    def test_18_create_products_3(self):
        te = Elf("Chris", 1, "Hats", "Mariah Carey") # Should make 6 gumdrops in 3 hours with Mariah Carey
        te2 = Elf("Buddy", 2, "Gumdrops", "Michael Buble") # Should make 18 gumdrops in 3 hours with MC
        te3 = Elf("Saghar", 3, "Gumdrops", "Mariah Carey") # Should make 54 gumdrops in 3 hours with MC
        tw = Workshop("North Pole 2", [te, te2, te3], "Mariah Carey")
        tw.create_products("Gumdrops", 3)
        self.assertEqual(tw.toys_created, {"Gumdrops":78})
        tw.create_products("Hats", 1)
        # Chris should make 6 hats in 1 hour with MC
        # Buddy should make 2 hats in 1 hour with MC
        # Saghar should make 6 hats in 1 hour with MC
        self.assertEqual(tw.toys_created, {"Gumdrops":78, "Hats":14})
        
        #tw.celebrity_visit("Mariah Carey") # Example informal celebrity_visit "test"
        #print(te.rate_of_productivity)
        #print(te2.rate_of_productivity)
        #tw.roll_call() # Example informal roll call "test"
    # Note: I'm not providing test cases for the bonus methods. Think of how you might design them as an exercise.
        
if __name__ == "__main__":
    unittest.main(exit=True)
