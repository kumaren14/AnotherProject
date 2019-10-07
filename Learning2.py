# more strings and tests

# these six lines right here use % as type of substitution with the proper letters to insert the phrases into printed lines
x = "There are %d types of people" % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(x)
print(y)

# these use quotations in quotations and
print("I said: %r.:" % x)
print("I also said: '%s'. " % y)

#once again, more substitution to make it easier and cleaner when printing
hilarious = False
jokeEvaluation = "Isn't that joke so funny?!?! %r"
print(jokeEvaluation % hilarious)

# oh look, we're adding strings together now
w = "This is the left side of..."
e = "a string with a right side"
print(w+e)

# more printing fun
print("Mary had a little lamb.")
print("Its fleece was white as %s" % 'snow')
print("And everywhere that Mary went")
# look, we can even repeat strings a certain number of times
print("." * 4)

#now we creating a separate substition for each letter
end1 = "N"
end2 = "o"
end3 = "t"
end4 = "f"
end5 = "u"
end6 = "n"
end7 = "n"
end8 = "y"

# now we can add all these substituted letters to make a full sentence
print(end1+end2+end3)
print(end4+end5+end6+end7+end8)
print("P.S. - Not Funny. Didn't Laugh.")

formatter = "%r %r %r %r %r"
print(formatter & (1, 2, 3, 4))
print(formatter % (True, False, True, False))
print(formatter % ((formatter, formatter, formatter, formatter))
