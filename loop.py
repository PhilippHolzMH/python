import random
print ("Welcome to MWP - magic with Philipp")
number = random.randint(1,10)

isguessrigth = False
while isguessrigth != True:
    guess = input ("Samma ne nummer von 1 - 10 ")
    if int(guess) == number:
        print ("Du hast {} genommen. Dat is richtig. Gewonnen!".format(guess))
        isguessrigth = True
    else:
        print("Deine Zahl ist {}. Scusi - is falsch".format(guess))
