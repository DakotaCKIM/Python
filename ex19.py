def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:"
# The follow call to the function uses 20 and 30 as parameters.
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = (int)(raw_input("How much cheese do you have!? "))
amount_of_crackers = (int)(raw_input("How many crackers? "))

# This shows that you can use variables in the place of integers.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"

# This shows that simple arithmetic is able to work with the function.
cheese_and_crackers(10 + 20, 5 + 6)

# This shows that variables can work with simple math.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
