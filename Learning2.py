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





#some more basic printing
periods = "Band Alg2 Bio Eng HuGeo Geom Deb Pro"

#By adding \n, we can create a new line between each word

months = "Jan\nFed\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOCt\nNOv\nDec"

print("Here are my periods", periods)
print("Here are the months", months)

# """ enables us to write a lot more across multiple lines
print(""" 
Oh look
With the triple double quotations, 
we can write things on multiple lines
as long as we want
hahahhahahhhahahahahahahahahahahahhaha""")

# hey look we can use %r to directly print all the code we have, even with other things in there that are actual code, not just words
print("here are the months: %r" % months)

code = "print(""here are the months: %r"" % months)"
print("Here is the code for the previous command: %r" % code)

# %r isnt the friendliest with quotations

# we can use /n to go onto new line, \\ to put in a backslash, and and \t to tab the line forward
# we can also use """ to write on separate lines

#escape senquences redux
tabbyCat = "\tIm tabbed in"
persianCat = ("Im split\non a line")
backslashCat = ("Im \\ a \\ cat")
topCat = """
Ill do a list
\t* cat food
\t* fish
\t* milk
\t* catnip 
\t* mice"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# escape seq     what it does?
# \\                  add backslash
#\'                   adds '
#\"                   adds "
#\a                   adds a bell sound
#\b                   backscpace
#\f                   new line and indent
#\n                   new line
#\N{name}             can add characters from unicode
# \r                  deletes anything on that comes before it on the same line
#\t                   tabs the line
#\uxxx                all of these below are used to print unicode characters, but you need to know the code
#\Uxxx
#\Uxxxxxxx
#\v
#\ooo
#\xhh


# cool look this shows us our keystrokes
#   while true
#       for i in ["/", "-", "|" "\\", "|"]:
#            print("%s\r" % i, ends='')

# you can use ''' instead of """

#

print(''' hello
my name is kumaren''')

age = input("How old are you?")
height = input("how tall are you?")

print("So, you are %r old and %r tall." % (age, height)