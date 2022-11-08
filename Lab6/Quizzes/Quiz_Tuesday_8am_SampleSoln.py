import unittest
# Note that this week's Quiz will be a special one :)

# Firstly, instead of creating your own program you'll be operating off this Python file which you can download to your system (or whose contents you can paste on Replit/etc.)
# Secondly, you will be tasked with implementing two classes and multiple different instance methods, whose intended behaviours are described in their docstrings.
# You ARE NOT to modify the if __name__ == "__main__", or any of the unit tests, EXCEPT the last unit test (where indicated)!
# To get full marks, you must implement both constructors, the first 6 methods, and the first unit test. The final 2 methods in the HalloweenParty class are a bonus (not for marks).

# Quiz Question: CPS109's Halloween Haunt

#                  ___
#               ___)__|_
#          .-*'          '*-,
#         /      /|   |\     \
#        ;      /_|   |_\     ;
#        ;   |\           /|  ;
#        ;   | ''--...--'' |  ;
#         \  ''---.....--''  /
#          ''*-.,_______,.-*'   

# Tired from yesterday's festivities, you stumble into your early morning CPS109 lab. After the first hour of (totally captivating) lecture, it is revealed that you must simulate a party using Python.
# Being a Python expert (and a party expert), you think to yourself: "this is gonna be ezpz"

class Partygoer():
    '''
    Before you program the party class you need to program the class for the constituents of parties!
    Partygoers are go-ers of parties. They all have a name, a costume, and a location (either "home" or an instance of a party). They also have a bedtime.
    Fill in the methods according to their docstrings.
    '''
    def __init__(self, name, costume, location="home", bedtime=2): # Constructor 1 (required)
        '''
        Complete the constructor.

        Input Arguments:
            name (string): The name of the partygoer
            costume (string): The costume the partygoer is wearing
            location (string:"home" OR HalloweenParty [default "home"]): Either "home" (if they are at home) or an instance of a HalloweenParty if they are at a party
            bedtime (float [default 2.00]): The bedtime of the partygoer (2:00 am is the default, using a 24-hour clock) (0.00 = midnight)
        Return:
            None
        Behaviour:
            Set self.argument to be equal to the constructor's input for each argument.
            Hint: Recall default arguments
        '''
        self.name = name
        self.costume = costume
        self.location = location
        self.bedtime = bedtime

    def change_costume(self, new_costume): # Method 1 (required)
        '''
        Partygoers often have many costumes at their disposal. Give them the ability to change costumes on the fly.

        Input Arguments:
            new_costume (string): The new costume for the partygoer to wear
        Return:
            None
        Behaviour:
            Set the partygoer's costume to the new_costume
        '''
        self.costume = new_costume

    def go_home(self): # Method 2 (required)
        '''
        Sometimes when a partygoer is all partied-out they just have to go home.

        Input Arguments:
            None (just self, which you always need for instance methods)
        Return:
            None
        Behaviour:
            If the partygoer is currently at a party (i.e. their location is some HalloweenParty instance)
                Set their location to "home"
            Otherwise
                Do nothing, as they are already at "home"
        '''
        if (self.location != "home"): # if at party
            self.location = "home"

    def go_to_party(self, halloween_party_to_go_to): # Method 3 (required)
        '''
        Typically a partygoer goes to parties. Hence the name.

        Input Arguments:
            halloween_party_to_go_to (HalloweenParty): The party the partygoer wants to go to
        Return:
            True if it was successful
            False otherwise (see Behaviour)
        Behaviour:
            Partygoers need some time to rest before going to another party. Therefore, they can only go to another party if they are currently at home.
            If the partygoer is currently at a party
                return False, as they cannot go directly from party to party
            Otherwise
                Set the partygoer's location to that party
                Then return True
        '''
        if (self.location != "home"): # Currently at a party
            return False
        else:
            self.location = halloween_party_to_go_to
            return True

class HalloweenParty():
    '''
    Halloween Parties are pretty complex, but they essentially consist of some partygoers and a current time.
    Fill in the instance methods according to their docstrings.
    '''
    def __init__(self, partyname, partygoers, current_time): # Constructor 2 (required)
        '''
        Complete the constructor.

        Input Arguments:
            partyname (string): The name of the party
            partygoers (list of Partygoer): A list of all Partygoers at the party
            current_time (float): The current time (using a 24-hour clock) (0.00 = midnight)
        Return:
            None
        Behaviour:
            Set self.argument to be equal to the constructor's input for each argument.
        '''
        self.partyname = partyname
        self.partygoers = partygoers
        self.current_time = current_time

    def remove_from_party(self, partygoer): # Method 4 (required)
        '''
        Sometimes you need to remove a partygoer from a party and send them home.

        Input Arguments:
            partygoer (Partygoer): The Partygoer you want to send home
        Return:
            None
        Behaviour:
            If partygoer is in the partygoers list
                First call their go_home method
                Then remove them from the partygoers list
            Otherwise
                Do nothing, as they are not at this party
        '''
        if partygoer in self.partygoers:
            partygoer.go_home()
            self.partygoers.remove(partygoer)

    def add_to_party(self, partygoer): # Method 5 (required)
        '''
        What use is a party without its partygoers? Create a method to add a partygoer to a party (if they are not already at the party!)

        Input Arguments:
            partygoer (Partygoer): The Partygoer you want to add to the partygoers list
        Return:
            None
        Behaviour:
            If partygoer is not already in partygoers
                Try to send them to this HalloweenParty via their go_to_party() method
                    If it returns True (success)
                        Add them to the party
                    Otherwise
                        Do not add them to the party
            Otherwise
                Do nothing, as they're already at the party
        '''
        if partygoer not in self.partygoers:
            result = partygoer.go_to_party(self) # Key observation here is that we pass in self
            if (result == True):
                self.partygoers.append(partygoer)

    def party_police_bedtime_check(self): # Method 6 (required)
        '''
        To make sure that people attend their morning labs, you've hired party police to check every partygoer at the party, and if the current time is greater
        than their bedtime, you must send them home.

        Input Arguments:
            None
        Return:
            None
        Behaviour:
            For all Partygoer instances in partygoers
                If the curent party's time is past their bedtime (you can assume parties go until midnight (0.00) at the earliest, and end at 23.59 at the latest, and that nobodies bedtime is before midnight)
                    Send them home via their go_home method
                    Then remove them from the partygoers list
                Otherwise
                    Do nothing - party on!!! (woot woot)
        '''
        partygoers_to_remove = []
        for i in range(len(self.partygoers)):
            if (self.current_time > self.partygoers[i].bedtime):
                partygoers_to_remove.append(self.partygoers[i])

        for partygoer in partygoers_to_remove:
            self.remove_from_party(partygoer)
                

    def check_if_party_lit(self): # Method 7 (bonus)
        '''
        According to my sister, for a party to be "lit" there must be at least 4 people there, it must be past midnight (0.00) and before 8 am (8.00), and the party must have Longevity
        Longevity is defined as: in 1 hour from the current time, at least 50% of the partygoers must still be there
        You can assume that partygoers will not leave a party unless it is past their bedtime for longevity checks

        Input Arguments:
            None
        Return:
            True if party is lit
            False otherwise
        Behaviour:
            Check if the party is lit.
            First ensure there are at least 4 people there (partygoers)
            Then ensure that it is currently past midnight and before 8 am (current_time)
            Then, for all current partygoers, ensure that for at least half of current partygoers, in 1 hour it is not past their bedtime
            If any of the above criteria fails the party is not lit. Otherwise it is.
        '''
        if (len(self.partygoers)) < 4:
            return False
        if (self.current_time >= 8.00):
            return False
        current_len = len(self.partygoers)
        num_to_remove = 0
        for partygoer in self.partygoers:
            if (self.current_time + 1.00) > partygoer.bedtime:
                num_to_remove += 1
        if (num_to_remove > current_len//2):
            return False
        return True

    def total_teletubby_takeover(self): # Method 8 (bonus)
        '''
        I'd like to believe that Teletubbies are popular at parties. My mom always said, "be the change you want to see in the world".

        Input Arguments:
            None
        Return:
            None
        Behaviour:
            For all Partygoer instances in partygoers,
                Set their costume to some Teletubby ["Tinky Winky", "Laa-Laa", "Dipsy", "Po"]. Trends are contagious!
        '''
        for partygoer in self.partygoers:
            partygoer.costume = "Tinky Winky" # Easy pass here cause I'm tired, but you could use random to make this cooler
        

class HalloweenPartyTestCases(unittest.TestCase):
    def test_1_change_costume(self): # YOU DO THIS (required)
        tp = Partygoer("Chris", "Teletubby")
        tp.change_costume("Alien")
        self.assertEqual(tp.costume, "Alien")
    def test_2_partygoer_initialization(self):
        tp = Partygoer("Chris", "Teletubby")
        self.assertEqual(tp.name, "Chris")
        self.assertEqual(tp.costume, "Teletubby")
        self.assertEqual(tp.location, "home") # Recall default home
        self.assertEqual(tp.bedtime, 2) # Recall default bedtime
    def test_3_partygoer_nondefault_initialization(self):
        tp = Partygoer("Chris", "Teletubby", bedtime=3)
        self.assertEqual(tp.name, "Chris")
        self.assertEqual(tp.costume, "Teletubby")
        self.assertEqual(tp.location, "home") # Recall default home
        self.assertEqual(tp.bedtime, 3) # Should override default bedtime
    def test_4_partygoer_go_home_already_home(self):
        tp = Partygoer("Chris", "Teletubby")
        tp.go_home()
        self.assertEqual(tp.location, "home")
    def test_5_partygoer_go_home_at_party(self):
        party = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        party.partygoers = [tp] # Manual set
        tp.location = party # Manual set
        tp.go_home()
        self.assertEqual(tp.location, "home")
    def test_6_partygoer_go_party_from_home(self):
        party = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        tp.location = "home" # Manual set
        return_val = tp.go_to_party(party)
        self.assertTrue(return_val)
        self.assertEqual(tp.location, party)
    def test_7_partygoer_go_party_from_party(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        party2 = HalloweenParty("Saghar's Fantastic Party", [], 1.30)
        tp = Partygoer("Chris", "Teletubby")
        tp.location = party1 # Manual set
        return_val = tp.go_to_party(party2)
        self.assertFalse(return_val)
        self.assertEqual(tp.location, party1)
    def test_8_halloweenparty_initialization(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        self.assertEqual(party.partyname, "Chris' Awesome Party")
        self.assertEqual(party.partygoers, [tp, tp2])
        self.assertEqual(party.current_time, 0.00)
    def test_9_remove_from_party_present(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        tp.location = party # Manual set
        tp2.location = party # Manual set
        party.remove_from_party(tp)
        self.assertEqual(tp.location, "home") # Check sent home
        self.assertEqual(party.partygoers, [tp2]) # Check removed from party
    def test_10_remove_from_party_not_present(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        party2 = HalloweenParty("Saghar's Fantastic Party", [tp], 1.30)
        tp.location = party2 # Manual set
        party1.remove_from_party(tp)
        self.assertEqual(tp.location, party2) # Check not removed from other party
        self.assertEqual(party1.partygoers, [])
    def test_11_add_to_party_present(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        tp.location = party # Manual set
        tp2.location = party # Manual set
        party.add_to_party(tp2)
        self.assertEqual(tp2.location, party)
        self.assertEqual(party.partygoers, [tp, tp2])
    def test_12_add_to_party_not_present_at_home(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp2.location = "home" # Manual set
        party = HalloweenParty("Chris' Awesome Party", [tp], 0.00)
        tp.location = party # Manual set
        party.add_to_party(tp2)
        self.assertEqual(tp2.location, party)
        self.assertEqual(party.partygoers, [tp, tp2])
    def test_13_add_to_party_not_present_other_party(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        party2 = HalloweenParty("Saghar's Fantastic Party", [], 1.30)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party1.partygoers = [tp] # Manual set
        party2.partygoers = [tp2] # Manual set
        tp.location = party1 # Manual set
        tp2.location = party2 # Manual set
        party1.add_to_party(tp2)
        self.assertEqual(tp2.location, party2)
        self.assertEqual(party1.partygoers, [tp])
    def test_14_party_police_bedtime_check(self): # I'm only adding one test here but in a full suite there would be more...
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp.bedtime = 0.30 # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 4.00
        tp3.bedtime = 2.30
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        party1.partygoers = [tp, tp2, tp3]
        party1.party_police_bedtime_check()
        self.assertEqual(tp.location, "home")
        self.assertEqual(tp2.location, party1)
        self.assertEqual(party1.partygoers, [tp2, tp3])
    def test_15_bonus_check_if_party_lit(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp4 = Partygoer("Alex", "Supervillain")
        tp.bedtime = 0.30 # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 4.00
        tp3.bedtime = 3.30
        tp4.bedtime = 5.00
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        tp4.location = party1
        party1.partygoers = [tp, tp2, tp3, tp4]
        self.assertTrue(party1.check_if_party_lit())
    def test_16_bonus_check_if_party_not_lit(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 3.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp4 = Partygoer("Alex", "Supervillain")
        tp.bedtime = 0.30 # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 3.25
        tp3.bedtime = 3.30
        tp4.bedtime = 5.00
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        tp4.location = party1
        party1.partygoers = [tp, tp2, tp3, tp4]
        self.assertFalse(party1.check_if_party_lit())
    def test_17_bonus_check_if_all_teletubbies(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party1.partygoers = [tp, tp2]
        party1.total_teletubby_takeover()
        all_good_switch = True
        for partygoer in party1.partygoers:
            if partygoer.costume not in ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]:
                all_good_switch = False
        self.assertTrue(all_good_switch)
        
if __name__ == "__main__":
    unittest.main(exit=True)
