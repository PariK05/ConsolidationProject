#By: Pari Kansara
#4/23/24
#INS 126
#call this program in the command line as "python WordGuessingGame.py x" where x is the number of players
#words are all length 5 and are from the Wordle word bank

import sys; args = sys.argv[1:] #this program takes command line arguments
import random



numPlayers = args[0]
if numPlayers<1: exit(0)

playerStats = [[0, 0] for i in range(numPlayers)] # each player has a list of [num letter guesses, num word guesses]

wL = open("WordleWords.txt", 'r').read() #list of words

rInt = random.randint(0, len(wL))
word = wL[rInt]
endedGames = set()

while True:
    for i in range(1, numPlayers+1):
        if i in endedGames: continue
        
        inp = input("Player " + str(i) + "\Word Guess? (y/n)")
        if inp.lower() not in {*"yn"}:
            print("Invalid input")
            exit(0)  
        
        
        letterGuess = input("Give a letter guess")
        print("Number of " + letterGuess + " in word is " + str(word.count(letterGuess.lower())))
        playerStats[i][0]+=1
            
        if inp.lower() == "y":
            wordGuess = input("Give a word guess")
            if wordGuess == word:
                print("Congratulations you guessed the correct word: " + word)
                print("Score for player " + str(i)+ ": " + str(playerStats[i][0]))
                
            else:
                print("Incorrect guess")
                playerStats[i][1]+=1
                if playerStats[i][1] >=3:
                    print("You have used all your word guesses and your game is over.")
                    endedGames.add(i)
            
            
        

