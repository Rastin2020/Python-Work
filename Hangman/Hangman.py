'''--------------------------- Initialization: ---------------------------'''
wordToGuessList = list("Apple".lower())
lives = 5
blankList = ["_"] * len(wordToGuessList)
finalAnswer = ("".join(wordToGuessList)).capitalize()

print("The word contains {} characters:".format(len(wordToGuessList)))
print("")

'''--------------------------- Method to reduce life: ---------------------------'''
def takeLife():
    global lives
    lives -= 1
'''--------------------------- Main loop: ---------------------------'''
while True:
    print("Your word = {}".format(blankList))
    print("")
    
    charCounter = 0
    userGuess = input("Guess a character or the entire word. You have {} lives: ".format(lives))
    print("")
    
    if list(userGuess) == wordToGuessList:
        print("---------------------You win!---------------------")
        print("")
        print("Your word was = {}".format(finalAnswer))
        break
    
    for i in range(len(wordToGuessList)):
        if wordToGuessList[i] == userGuess and wordToGuessList[i] != blankList[i]:
            blankList[i] = userGuess
            charCounter += 1
        elif wordToGuessList[i] == userGuess and wordToGuessList[i] == blankList[i]:
            print("Already found...")
            print("")
            charCounter += 1
            
    if charCounter == 0:
        takeLife()
        print("Incorrect...")
        print("")
    
    if lives == 0:
        print("---------------------You lose...---------------------")
        print("Your word was = {}".format(finalAnswer))
        break
        
    if blankList == wordToGuessList:
        print("---------------------You win!---------------------")
        print("Your word was = {}".format(finalAnswer))
        break
