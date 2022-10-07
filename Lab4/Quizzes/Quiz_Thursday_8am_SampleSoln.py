# Note that this week's Quiz will be a special one. :)

# Firstly, instead of creating your own program you'll be operating off this Python file which you can download to your system (or whose contents you can paste on Replit/etc.)
# Secondly, you will be tasked with implementing multiple different functions, whose intended behaviours are described in their docstrings.
# Part of this modification may include adding input arguments to the function definition line (just replace the *arguments).
# You ARE NOT to modify the if __name__ == "__main__"!
# To get full marks, you must implement the first 6 functions, which are (approximately) in order of increasing difficulty.

# Quiz Question: Boarding the Main Train, Riding All Stops to Function Junction Station

#   _____                 . . . . . o o o o o
#  __|[_]|__ ___________ _______    ____      o
# |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
#_|________|_[_________]_[________]_|__|________)<
#  oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def honk_horn():
	"""
	Honk your train's horn.

	Input Arguments: 
		None
	Return: 
		None
	Behaviour: 
		Print a train noise (e.g. "Choo choo!")
	"""
	print("Choo choo!")

def honk_upgraded_horn(horn_noise):
	"""
	You, being the technological genius that you are, decide to upgrade the train's horn to play any noise you want.
	Honk your train's upgraded horn.

	Input Arguments: 
		horn_noise (string): The noise your upgraded horn makes
	Return: 
		None
	Behaviour: 
		Print your horn_noise
	"""
	print(horn_noise)

def add_passenger(train_passenger_list, passenger, maximum_capacity):
	"""
	What good is a train without passengers? Your goal is to add some passenger to the end of your train list.
	However, trains have maximum capacities, so only add the new passenger if it would not exceed the maximum capacity.

	Input Arguments: 
		train_passenger_list (list of strings): The list of passengers currently on the train
		passenger (string): The name of the passenger you're trying to add to the train passenger list
		maximum_capacity (int): The maximum passenger capacity of that specific train
	Return:
		train_passenger_list (list of strings): The updated list of passengers on the train
	Behaviour:
		If adding a passenger to the input train_passenger_list would not cause its length to exceed the maximum_capacity,
		then add passenger to the end of train_passenger_list
		Otherwise, do not add the passenger
		Return the train_passenger_list
	"""
	if (len(train_passenger_list) < maximum_capacity): # If still some capacity left
		train_passenger_list.append(passenger)
	return train_passenger_list

def remove_passenger(train_passenger_list, passenger):
	"""
	Trains are the ultimate party palace. However, passengers can get rowdy from time to time. Given some passenger name, if they are in
	the train passenger list, then remove them, and print appropriately. If no such passenger exists print so. If the passenger's name is "Conductor", then do not
	remove the passenger from the train, and print out some error message, as no matter how rowdy the Conductor gets a train must always have one!

	Input Arguments:
		train_passenger_list (list of strings): The list of passengers currently on the train
		passenger (string): The name of the passenger you are trying to remove from the train passenger list
	Return:
		train_passenger_list (list of strings): The updated list of passengers on the train
	Behaviour:
		If passenger is in your train_passenger_list, remove the passenger from your list. Then, print: passenger + " was removed!"
		If the passenger is not in your train_passenger_list, print: "There is no such passenger aboard!"
		If the passenger is "Conductor", do not remove the passenger, and print: "There must always be a Conductor at the front of the train!"
		Return the updated_train_passenger_list
	"""
	if (passenger in train_passenger_list):
		if (passenger == "Conductor"): # If the passenger is the Conductor...
			print("There must always be a Conductor at the front of the train!")
		else: # If present in the list but not Conductor (i.e. valid to remove)
			train_passenger_list.remove(passenger) # You can use .remove() here, or just iterate through until you find an instance of passenger
			# Via iteration and .pop():
			#passenger_index = 0
			#for i in range(len(train_passenger_list)):
			#	if (train_passenger_list[i] == passenger):
			#		passenger_index = i
			#train_passenger_list.pop(passenger_index)
			print(passenger + " was removed!")
	else: # If not present in the list...
		print("There is no such passenger aboard!")
	return train_passenger_list

def remove_multiple_passengers(train_passenger_list, passengers_to_remove):
	"""
	Sometimes you want to kick out a whole list of passengers (as they often get rowdy in groups). Using the remove_passenger() function you just
	created above, try to remove all passengers in the input list from the train.

	Input Arguments:
		train_passenger_list (list of strings): The list of passengers currently on the train
		passengers_to_remove (list of strings): The list of passengers you're trying to remove from the train
	Return:
		train_passenger_list (list of strings): The updated list of passengers on the train.
	Behaviour:
		For all passengers in the passengers_to_remove list, call the remove_passenger() function using that passenger
		Return the updated train_passenger_list
	"""
	for passenger in passengers_to_remove:
		remove_passenger(train_passenger_list, passenger) # We simply loop over and call our function
	return train_passenger_list

def find_missing_passenger(list_of_train_passenger_lists, passenger_to_find):
	"""
	Trains are vast - networks of trains even more so. Sometimes a passenger goes missing, and your must find them from among the trains, lest they continue, forgotten, past the end of the world...
	Given some passenger, and a list of train lists of passengers, return the index of the train that they are on, and the index of their location on that train. 
	If multiple occurrences of the same passenger appear across the trains, then return the index of the passenger which occurs closest to the end of their train, and at the latest train in the list.
	Those who go missing tend to get pushed towards the end of the trains, never to return...
	
	Input Arguments:
		list_of_train_passenger_lists (list of (list of strings)): The list of train_passenger_lists from different trains
		passenger_to_find (string): The name of the passenger you're trying to find
	Return:
		train_index, within_train_index (int, int): The index of the train the passenger you're trying to find is on, and their location (index) within that train
	Behaviour:
		Try to locate passenger_to_find from within the lists of passengers in the list of trains
		In the case of multiple passengers having the same name within a single train list, break ties by picking the backmost instance of the passenger (i.e. the one latest in the list of passengers)
		In the case of multiple passengers having the same name from among multiple trains, pick the passenger who occurs latest in their respective train, and in the case of ties,
		the passenger who occurs in the backmost train (i.e. the one latest in the list of trains)
		If the passenger does not appear in any of the lists, return -1, -1
		If the passenger has been successfully located, return the index of the train they are on, then the index of their location within that train
	"""

	train_index = -1
	within_train_index = -1
	max_len = 0
	for train_passenger_list in list_of_train_passenger_lists:
		if (len(train_passenger_list) > max_len):
			max_len = len(train_passenger_list)
	distance_to_end_of_train = max_len # We set our initial distance to end of train to the maximum length across all lists...

	for i in range (len(list_of_train_passenger_lists)): # For each train passenger list...
		train_passenger_list = list_of_train_passenger_lists[i]

		for j in range(len(train_passenger_list)):
			if (train_passenger_list[j] == passenger_to_find): # If the passenger at that index is the one we want to find...
				temp_distance_to_end_of_train = len(train_passenger_list) - j
				if (temp_distance_to_end_of_train < distance_to_end_of_train): # If strictly less (i.e. comes closest to end of list)
					train_index = i
					within_train_index = j
					distance_to_end_of_train = temp_distance_to_end_of_train # Update our minimum distance
				elif (temp_distance_to_end_of_train == distance_to_end_of_train): # In the case of a tie...
					if (i > train_index): # We pick the greatest train index
						train_index = i
						within_train_index = j
						distance_to_end_of_train = temp_distance_to_end_of_train
	return train_index, within_train_index

def yeetus_deletus_the_teletubby_menace(list_of_train_passenger_lists): # Bonus / Optional
	"""
	Cuddly, fuzzy, loveable creatures. The Teletubbies appear to be a docile species, happy to lazily feast on Tubby Custard under the watchful eye of Sun Baby.
	However, as the students of CPS109 from last year can attest to, they harbour a dark and terrible secret. These creatures, under the direction of their leaders, seek to eliminate the human race.
	While last year's students have destroyed the vast majority of the Teletubby threat, a few that remain have snuck aboard the network of trains, hoping, like the replicants in Blade Runner, to avoid the
	detection of their hunters by getting lost in the sprawling network of locomotion.
	You must find them. You must end them.

	Input Arguments:
		list_of_train_passenger_lists (list of (list of strings)): The list of train_passenger_lists from different trains
	Return:
		list_of_train_passenger_lists (list of (list of strings)): The updated list of train_passenger_lists from different trains, with all Teletubbies removed
	Behaviour:
		Recall that the Teletubbies are: ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]
		For each occurance of a Teletubby within any of the trains in the list_of_train_passenger_lists, remove the Teletubby from that train's passenger list
		and print: teletubby + " has been yeeted off the train, Leonidas style. THIS! IS! CPS109!" (replace teletubby with the name of the Teletubby you're yeeting)
		https://www.youtube.com/watch?v=4Prc1UfuokY :)
		Return the updates list_of_train_passenger_lists, with all Teletubbies removed
	"""
	teletubby_list = ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]
	for i in range(len(list_of_train_passenger_lists)):
		list_of_train_passenger_lists[i] = [passenger for passenger in list_of_train_passenger_lists[i] if passenger not in teletubby_list] # Using list comprehension... (one-line solution)
		# Without list comprehension, we can use a for loop
		#temp_list = []
		#for j in range(len(list_of_train_passenger_lists[i])):
		#	if (list_of_train_passenger_lists[i][j] not in teletubby_list):
		#		temp_list.append(list_of_train_passenger_lists[i][j])
		#list_of_train_passenger_lists[i] = temp_list

	return list_of_train_passenger_lists

if __name__ == "__main__": # DO NOT MODIFY!
	print("All aboard the Main Train, riding all station stops to Function Junction station!")

	#### Function 1 Test ####
	print("\nFunction 1 test:")
	print("You should print: train noises on the next line")
	honk_horn() 
	# You should print "Choo choo!" (or something to that effect) here


	#### Function 2 Test ####
	print("\nFunction 2 Test")
	print("You should print: Hyonk hyonk! on the next line")
	honk_upgraded_horn("Hyonk hyonk!") 
	# You should print "Hyonk hyonk!" here


	#### Function 3 Tests ####
	print("\nFunction 3 Tests")
	my_starting_train = ["Conductor", "Miley Cyrus", "Hannah Montanah", "Leonidas"] 
	passenger_to_add = "Chris"
	my_starting_train_capacity = 5

	my_starting_train = add_passenger(my_starting_train, passenger_to_add, my_starting_train_capacity) # Valid add test
	print("Function 3 (add passenger):", my_starting_train == ["Conductor", "Miley Cyrus", "Hannah Montanah", "Leonidas", "Chris"]) # Should print True

	second_passenger_to_add = "Xerxes"
	my_starting_train = add_passenger(my_starting_train, second_passenger_to_add, my_starting_train_capacity) # Maximum exceeded test
	print("Function 3 (add passenger exceeds maximum):", my_starting_train == ["Conductor", "Miley Cyrus", "Hannah Montanah", "Leonidas", "Chris"]) # Should print True


	#### Function 4 Tests ####
	print("\nFunction 4 Tests")
	my_remove_test_train = ["Conductor", "Miley Cyrus", "Hannah Montanah", "Leonidas", "Chris"] 
	passenger_to_remove = "Hannah Montanah"

	my_remove_test_train = remove_passenger(my_remove_test_train, passenger_to_remove) # Valid remove test
	# You should print: "Hannah Montanah was removed!" here
	print("Function 4 (remove passenger):", my_remove_test_train == ["Conductor", "Miley Cyrus", "Leonidas", "Chris"]) # Should print True
	
	second_passenger_to_remove = "Lilly Truscott"
	my_remove_test_train = remove_passenger(my_remove_test_train, second_passenger_to_remove) # Invalid remove test
	# You should print: "There is no such passenger aboard!" here
	print("Function 4 (remove not-present passenger):", my_remove_test_train == ["Conductor", "Miley Cyrus", "Leonidas", "Chris"]) # Should print True

	third_passenger_to_remove = "Conductor"
	my_remove_test_train = remove_passenger(my_remove_test_train, third_passenger_to_remove) # Try to remove Conductor test
	# You should print: "There must always be a Conductor at the front of the train!" here
	print("Function 4 (remove conductor):", my_remove_test_train == ["Conductor", "Miley Cyrus", "Leonidas", "Chris"]) # Should print True


	#### Function 5 Tests ####
	print("\nFunction 5 Tests")
	my_remove_test_train = ["Conductor", "Miley Cyrus", "Hannah Montanah", "Leonidas", "Chris"] 
	passengers_to_remove = ["Hannah Montanah", "Leonidas"]
	my_remove_test_train = remove_multiple_passengers(my_remove_test_train, passengers_to_remove) # Valid remove test
	# You should print: "Hannah Montanah was removed!" here
	# You should print: "Leonidas was removed!" here
	print("Function 5 (remove passengers):", my_remove_test_train == ["Conductor", "Miley Cyrus", "Chris"]) # Should print True

	second_passengers_to_remove = ["Miley Cyrus", "Jackson Stewart"]
	my_remove_test_train = remove_multiple_passengers(my_remove_test_train, second_passengers_to_remove) # Single valid single invalid remove test
	# You should print: "Miley Cyrus was removed!" here
	# You should print: "There is no such passenger aboard!" here
	print("Function 5 (remove 1 present 1 not):", my_remove_test_train == ["Conductor", "Chris"]) # Should print True

	third_passengers_to_remove = ["Alien", "Conductor", "The Thing"]
	my_remove_test_train = remove_multiple_passengers(my_remove_test_train, third_passengers_to_remove) # Multiple invalid remove test
	# You should print: "There is no such passenger aboard!" here
	# You should print: "There must always be a Conductor at the front of the train!" here
	# You should print: "There is no such passenger aboard!" here
	print("Function 5 (multiple invalid removes):", my_remove_test_train == ["Conductor", "Chris"]) # Should print True


	#### Function 6 Tests ####
	print("\nFunction 6 Tests")
	my_first_train = ["Conductor", "Chris", "Saghar", "Daniel", "Emilia", "Chang"]
	my_second_train = ["Conductor", "Matthews", "Tavares", "Bunting", "Marner", "Rielly"]
	my_third_train = ["Conductor", "Deckard", "Daniel"]
	my_fourth_train = ["Conductor", "Billy", "Joey", "Billy", "Marner", "Lilly"]

	my_list_of_train_passenger_lists = [my_first_train, my_second_train, my_third_train, my_fourth_train]
	passenger_to_find = "Emilia"

	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Once-present passenger test
	print("Function 6 (once-present passenger):", train_index == 0 and position_index == 4) # Should print True
	#print(passenger_to_find, "is on train", train_index, "at position", position_index) # Just for illustration purposes (can uncomment once implemented)

	passenger_to_find = "Aniki"
	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Not-present passenger test
	print("Function 6 (not-present passenger):", train_index == -1 and position_index == -1) # Should print True

	passenger_to_find = "Billy"
	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Multi-present single list passenger
	print("Function 6 (multi-present single list passenger):", train_index == 3 and position_index == 3) # Should print True (we get closest to end)
	#print(passenger_to_find, "is on train", train_index, "at position", position_index) # Just for illustration purposes (can uncomment once implemented)

	passenger_to_find = "Daniel"
	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Multi-present in multiple lists passenger (no tie)
	print("Function 6 (multi-present multi-list passenger (no tie)):", train_index == 2 and position_index == 2) # Should print True (we get closest to end (NOT GREATEST INDEX) across all lists)
	#print(passenger_to_find, "is on train", train_index, "at position", position_index) # Just for illustration purposes (can uncomment once implemented)

	passenger_to_find = "Marner"
	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Multi-present multi-list tie passenger
	print("Function 6 (multi-present multi-list passenger (tie)):", train_index == 3 and position_index == 4) # Should print True (we get latest closest to end across all lists, then in the latest list, for ties)
	#print(passenger_to_find, "is on train", train_index, "at position", position_index) # Just for illustration purposes (can uncomment once implemented)

	my_first_train = ["Conductor", "Me", "You"]
	my_second_train = ["Conductor", "You", "Forsen"]
	my_list_of_train_passenger_lists = [my_first_train, my_second_train]
	passenger_to_find = "You"
	train_index, position_index = find_missing_passenger(my_list_of_train_passenger_lists, passenger_to_find) # Multi-present in multiple lists passenger (no tie) v2 (catches error in implementation)
	print("Function 6 (multi-present multi-list passenger (no tie) 2):", train_index == 0 and position_index == 2) # Should print True (we get closest to end (NOT GREATEST INDEX) across all lists)
	#print(passenger_to_find, "is on train", train_index, "at position", position_index) # Just for illustration purposes (can uncomment once implemented)


	#### Function 7 Tests ####
	# Bonus!
	print("\nBonus Function 7 Test")
	my_first_train = ["Conductor", "Chris"]
	my_second_train = ["Conductor", "Po", "Saghar", "Tinky Winky"]
	my_third_train = ["Conductor", "Dipsy", "Laa-Laa"]
	my_fourth_train = ["Conductor", "Daniel", "Deckard", "Leonidas", "Po"]

	my_list_of_train_passenger_lists = [my_first_train, my_second_train, my_third_train, my_fourth_train]

	my_list_of_train_passenger_lists = yeetus_deletus_the_teletubby_menace(my_list_of_train_passenger_lists)
	print("Bonus Function 7:", my_list_of_train_passenger_lists == [["Conductor", "Chris"], ["Conductor", "Saghar"], ["Conductor"], ["Conductor", "Daniel", "Deckard", "Leonidas"]]) # Should print True