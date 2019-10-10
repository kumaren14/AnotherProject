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

# what that code does is print our the keystrokes you typed, as a kind of animation

# you can use ''' instead of """

print(''' hello
my name is kumaren''')

# cool you can ask questions and what gets printed afterwards is based off your response
print("Hey there, my name is Kumaren. I'm going to write a short biography about you. I need some information, so I'll ask you some questions, okay?")

name = input("What is your first name?")
print("Sweet, now we have a title for the book.")
print("""Average or Amazing: The Life of %r   
Arranged by Kumaren Anand"""
      % name)

print("Aight, time for some more questions.")

age = input("How old are you?")
grade = input("What grade are you in?")
pronoun = input("Do you want to be called he or she?")
school = input("What school do you go too?")
height = input("How tall are you?")
friend = input("what is the name of one of your friends?")

print("So, you are %r years old and %r tall." % (age, height))
print("And you are in grade %r at %r. One of your friends is %r. Good, we're getting information." % (grade, school, friend))

favoriteClass = input("What is your favorite class?")
print("I assume you enjoy going to %r" % (favoriteClass))

feeling = input("How are you feeling today?")
print("You're %r? Well, as long as you're not dead, you're fine." % feeling)

food = input("What is your favorite food?")
print("Hey, I like %r too!" % food)

sky = input("What color is the sky?")
print("%r? You think the sky is %r? Well, if you say so..." % (sky, sky) )

artist = input("Who's your favorite artist. I mean like paintings, not music")
gender = input("Is it a he or a she?")
print("%r, huh? Yeah, %r has some pretty good paintings" % (artist, gender))

print("All right, now we have enough to compile your book.")
print("""Ready?...
3...
2...
1...
""")

print("""Average or Amazing: The Life of %r
Arranged By Kumaren Anand

Welcome back to the Average or Amazing Series, arranged by Kumaren Anand,
where examine the lives of everyday people, and judge if they are...
average or amazing!!! Lets get right to it.

This book is about %r. %r is in grade %r at %r. %r is %r years old, 
and is currently %r. %r's favorite class is %r, and %r enjoys going to 
that class. Concerning %r's personal life, %r likes to eat %r and enjoys
paintings by %r. Surprisingly, %r believes that the color of the sky is 
%r (which we all now is just plain silly). When asked how %r was feeling 
at the time of the writing of the book, %r said %r was feeling %r.

Based on the information laid out in front of us, we must decide - is %r's 
life average, or amazing. In the case of %r year old %r, %r's life is
...
AVERAGE!!!

Check out other books in the series such as 
Average or Amazing: The Life of %r"""
% (name, name, grade, school, pronoun, age, height, name, favoriteClass, pronoun, name, name, food, artist, name, sky, name, name, pronoun, feeling, name, age, name, name, friend))



