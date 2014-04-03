x = "There are %d types of people." % 10 # Assigns the string to the var x.
binary = "binary" # Assigns the string to var binary
do_not = "don't" #Assigns the string to var do_not
y = "Those who know %s and those who %s." % (binary, do_not) # 2 strings within this 
#string.

print x
print y

print "I said: %r." %x # A string within a string.
print "I also said: '%s'." % y # A string within a string.

hilarious = False # Assigns boolean value False to var hilarious.
joke_evaluation = "Isn't that joke so funny! %r" # Assigns the string to var joke_evaluation.

print joke_evaluation % hilarious # prints joke_evaluation with var hilarious within.

w = "This is the left side of..." # Assigns the string to var w.
e = "a string with a right side." # Assigns the string to var e.

print w + e # Concatenates the two strings.