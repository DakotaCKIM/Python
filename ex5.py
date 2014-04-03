my_name = 'Dakota C. Kim'
my_age = 18 # not a lie
my_height = 69 # inches
my_weight = 260 # pounds
my_eyes = 'Light Brown'
my_teeth = 'White'
my_hair = 'Brown'
my_height_cm = my_height * 2.54
my_weight_kg = my_weight * 0.453

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d centimeters talls." % my_height_cm
print "He's %d pounds heavy." % my_weight
print "He's %d kilograms heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are actually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.

print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + 
my_height + my_weight)