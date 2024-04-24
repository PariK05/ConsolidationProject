#By: Pari Kansara
#4/23/24
#INS 126
#call this program in the command line as "python WordGuessingGame.py x" where x is the number of players

import sys; args = sys.argv[1:] #this program takes command line arguments
import re

numPlayers = args[0]
if numPlayers<1: exit(0)


wL = open("WordleWords.txt", 'r').read() #list of words