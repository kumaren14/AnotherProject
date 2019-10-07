# more strings and tests

# these four lines right here use % as type of substitution with the proper letters to insert the phrases into printed lines
x = "There are %d types of people" % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(x)
print(y)

print("I said: %r.:" % x)
print("I also said: '%s'. " % y)

hilarious = True
jokeEvaluation = "Isn't that joke so funny?!?! %r"
print(jokeEvaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"
print(w+e)

# more printing fun
print("Mary had a little lamb.")
print("Its fleece was white as %s" % 'snow')
print("And everywhere that Mary went")
print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1+end2+end3+end4+end5+end6)
print(end7+end8+end9+end10+end11+end12)
print("P.S. - This isn't funny. I did not like typing this out. If this his style of humor, I am seriously concerned")
