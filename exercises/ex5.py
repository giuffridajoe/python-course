myName = 'Joe Giuffrida'
myAge = 33
myHeight = 67
myWeight = 185
myEyes = 'Brown'
myTeeth = 'White'
myHair = 'Black'

print "Let's talk about %s." % myName
print "He's %d inches (%d centimeters) tall." % (myHeight, myHeight * 2.54)
print "He's %d pounds heavy." % myWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the coffee." % myTeeth

print "If I add %d, %d, and %d I get %d." %(myAge, myHeight, myWeight, myAge + myHeight + myWeight)