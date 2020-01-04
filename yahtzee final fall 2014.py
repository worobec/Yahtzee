#This program plays a one-player Yahzee game

#Global variables
#dieSize is the number of sides on each die
#dieCount is the number of dice in play
#rollsPerHand is the number of rolls per hand
#hand is a list that stores the curent hand with one element for each die in play
#openLine is boolean that is true if any lines in the scorecard are unused
#cardList is a list of lists that stores the current scorecard
#   each list is a line in the scorecard with elements name, used, section, and score
#possbileList is a list of lists that stores the unused lines scorecard
#   each list is a line in the scorecard with elements name, score, and section

#Change log
#
#10/23/14  B Worobec  Solution to lab 4
#10/29/14  B Worobec  Add full house function
#11/03/14  B Worobec  Add conbfiguration file
#11/11/14  B Worobec  Full working version
#11/13/14  B Worobec  Add scorecard
#
#
#random is used to roll dice
import random

#declare functions ###########################################
    
def rollDie(sideCount):
    #this function simulates the roll of a die with sideCount sides
    roll = random.randint(1,sideCount)
    return roll

def totalAllDice():
    #this function calculates the total of all dice in the 'hand' list
    total = 0
    for rollN in range (0, dieCount):
         total = total + hand[rollN]
    return total

def maxStraightFound(listName):
    #this function returns the length of the longest straight found
    listName.sort()
    listLength = len(listName)
    maxLength = 1
    curLength = 1
    for counter in range (1, listLength):
        if listName[counter - 1] + 1 == listName[counter]: #value at position counter 1 larger predessor
            curLength = curLength + 1
        else:
            if listName[counter - 1] + 1 < listName[counter]:
                #jump of 2 or more, start new straignt
                curLength = 1
        if curLength > maxLength :
            maxLength = curLength
    return maxLength
                
def maxOfAKindFound(listName):
    #this function returns n for the largest n of a kind found
    #does not return the die value or values occuring n times
    maxOfAKind = 1
    for dieValue in range (1,dieSize+1):
       if listName.count(dieValue) > maxOfAKind:
           maxOfAKind = listName.count(dieValue)
    return maxOfAKind
    
def fullHouseFound(listName):
    #this function returns True if a full house is found, False otherwise
    #a full house is a 3 of a kind and a 2 of a kind in the same hand
    #  a 5 of a kind is also a full house
    #
    FHFound = False
    ThreeKFound = False
    #check for 5 of a kind
    for dieValue in range (1,dieSize+1):
       if listName.count(dieValue) >= 5:
           FHFound = True
    #if 5 of a kind not found
    if not FHFound:
        #check for 3 of a kind
        for dieValue in range (1,dieSize+1):
           if listName.count(dieValue) >= 3:
              ThreeKFound = True
              ThreeKValue = dieValue
              dieValue = dieSize + 1
        if ThreeKFound:
            #check for 2 of a kind
            for dieValue in range (1,dieSize+1):
               if listName.count(dieValue) >= 2 and dieValue != ThreeKValue:
                  FHFound = True
    return FHFound

def createScorecard(sideCount):
    #this function overwirtes any existing scorecard.txt file with
    #   a file ready to start a new game
    #the file is comma delimited and the order of fields is
    #   name, used, section, score
    scorecard_file = open('scorecard.txt','w')
    #loop for upper section
    for upperCounter in range (1, sideCount+1):
        scorecard_file.write(str(upperCounter))
        scorecard_file.write(',n,u,0\n')
    #individual writes for lower section
    scorecard_file.write('3K,n,l,0\n')
    scorecard_file.write('4K,n,l,0\n')
    scorecard_file.write('FH,n,l,0\n')
    scorecard_file.write('SS,n,l,0\n')
    scorecard_file.write('LS,n,l,0\n')
    scorecard_file.write('Y,n,l,0\n')
    scorecard_file.write('C,n,l,0\n')
    #close the file
    scorecard_file.close()

def readScorecard():
   #this function reads the scordcard.txt file and stores in in a list named cardList
   sc_file = open('scorecard.txt','r')
   line = sc_file.readline()
   while line != '':
      #print(line)
      name = ''
      pointer = 0
      #parse name
      while line[pointer] != ',':
         name = name + line[pointer]
         pointer = pointer + 1
      #print(name)
      pointer = pointer + 1
      #parse used
      used = ''
      while line[pointer] != ',':
         used = used + line[pointer]
         pointer = pointer + 1
      #print(used)
      pointer = pointer + 1
      #parse section
      section = ''
      while line[pointer] != ',':
         section = section + line[pointer]
         pointer = pointer + 1
      #print(section)
      pointer = pointer + 1
      #parse score
      scoreStr = ''
      while line[pointer] != '\n':
         scoreStr = scoreStr + line[pointer]
         pointer = pointer + 1
      score = int(scoreStr)
      #print(score)
      lineList = [name,used,section,score]
      cardList.append(lineList)
      line = sc_file.readline()
        
def possiblePlaces(listName):
    #this function reads the scordcard.txt file and stores
    #   unused lines in the scorecard in a list named possibleList
    scorecard_file = open('scorecard.txt','r')
    line = scorecard_file.readline()
    while line != '':
        #print(line)
        name = ''
        pointer = 0
        #parse name
        while line[pointer] != ',':
           name = name + line[pointer]
           pointer = pointer + 1
        #print(name)
        pointer = pointer + 1
        #parse used
        used = ''
        while line[pointer] != ',':
           used = used + line[pointer]
           pointer = pointer + 1
        #print(used)
        pointer = pointer + 1
        #parse section
        section = ''
        while line[pointer] != ',':
           section = section + line[pointer]
           pointer = pointer + 1
        #print(section)
        pointer = pointer + 1
        if used == 'n':
           listName.append([name, 0, section])
        line = scorecard_file.readline()

def writeScorecard():
    #this function overwirtes any existing scorecard.txt file with
    #   the contents of the cardList
    #the file is comma delimited and the order of fields is
    #   rowname, used, section, score
    scorecard_file = open('scorecard.txt','w')
    for loopLine in cardList:
        scorecard_file.write(loopLine[0] + ',' + loopLine[1] + ',' + loopLine[2] + ',' + str(loopLine[3]) +'\n')
    #close the file
    scorecard_file.close()

def printScorecard():
    #this function prints a scorecard from the cardList
    print('Line          Score')
    print('-------------------')
    upperTotal = 0
    bonus = 0
    lowerTotal = 0
    grandTotal = 0
    #loop looking for upper section lines
    for loopLine in cardList:
        if loopLine[2] == 'u':
            upperTotal = upperTotal + loopLine[3]
            rightJustScore = '        ' + str(loopLine[3])
            print((loopLine[0]+'           ')[0:12] + rightJustScore[len(rightJustScore) -6:len(rightJustScore) +1])
    if upperTotal >= 63:
        bonus = 35

    #upper sub total
    print('-------------------')
    rightJustScore = '        ' + str(upperTotal)
    print('Sub Total   ' + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])
    #bonus
    rightJustScore = '        ' + str(bonus)
    print('Bonus       ' + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])
    #upper tot
    print('-------------------')
    rightJustScore = '        ' + str(upperTotal + bonus)
    print('Upper Total ' + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])
    print()

    #loop looking for lower section lines
    for loopLine in cardList:
        if loopLine[2] == 'l':
            lowerTotal = lowerTotal + loopLine[3]
            rightJustScore = '        ' + str(loopLine[3])
            print((loopLine[0]+'           ')[0:12] + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])
    #lower total
    print('-------------------')
    rightJustScore = '        ' + str(lowerTotal)
    print('Lower Total ' + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])
    #grand total
    print('-------------------')
    rightJustScore = '        ' + str(upperTotal + bonus + lowerTotal)
    print('Grand Total ' + rightJustScore[len(rightJustScore) - 6:len(rightJustScore) +1])

#start of main program ############################################

#cofig file stores game parameters
config_file = open('yahtzeeConfig.txt','r')
#first record in file is number of sides on a die
dieSize = int(config_file.readline())
#second record in the file is the number odf dice in play
dieCount = int(config_file.readline())
#third record is the number of rolls allowed per hand
rollsPerHand = int(config_file.readline())

#show user current configuration
print("you are playing with ",dieCount," ",dieSize,"-sided dice",sep='')
print("you get",rollsPerHand,"rolls per hand")
print()

#ask user if they want to change config, if yes ask for new values and write to file
changeConfig = input("enter 'y' if you would like to change the configuration ")
if changeConfig == 'y':
    dieSize = int(input("enter the number of sides on each die "))
    dieCount = int(input("enter the number of dice in play "))
    rollsPerHand = int(input("enter the number of rolls per hand "))
    config_file = open('yahtzeeConfig.txt','w')
    config_file.write(str(dieSize) + '\n')
    config_file.write(str(dieCount) + '\n')
    config_file.write(str(rollsPerHand) + '\n')
    config_file.close()

#set up the blank scorecard
createScorecard(dieSize)

##### play a game ################################################################

#all lines are unused at beginning of the game
openLine = True

##### beginning of game loop
#play another hand when any lines in scorecard are still unused
while openLine:
    cardList = []
    #read the scorecard
    readScorecard()
    #set up the keep list so all dice get rolled on the first roll of the hand    
    keep = ['n'] * dieCount
    hand = [0] * dieCount

    #loop through each roll of the hand
    currentRoll = 1
    print()
    print('starting a new hand')
    print()
    while currentRoll <= rollsPerHand:
        #loop that rolls the dice needing to be rolled
        for keepN in range (0, dieCount):
           if keep[keepN] != 'y':
               hand[keepN] = rollDie(dieSize)
        print("your hand is ",hand)
        #do this only if not the final roll in this hand
        if currentRoll < rollsPerHand:
            keep = input("enter keep string - 'y' to keep or 'S' for scorecard ")
            #check if the user want to see the scorecard
            if keep[0] == 'S':
                printScorecard()
                print()
                print("your hand is ",hand)
                keep = input("enter keep string - 'y' to keep ")

            #stop rolling if all y's
            if keep == 'y' * dieCount:
                currentRoll = rollsPerHand
        currentRoll = currentRoll + 1

    #evaluate hand and show all eligible places to put the hand on scorecard
    possibleList = []
    possiblePlaces(possibleList)
    for loopLine in possibleList:
        #print(loopLine)
        if loopLine[2] == 'u':
            loopLine[1] = int(loopLine[0]) * hand.count(int(loopLine[0]))
        else: #lower section
            if loopLine[0] == '3K':
                if maxOfAKindFound(hand) >= 3:
                    loopLine[1] = totalAllDice()
            if loopLine[0] == '4K':
                if maxOfAKindFound(hand) >= 4:
                    loopLine[1] = totalAllDice()
            if loopLine[0] == 'FH':
                if fullHouseFound(hand):
                    loopLine[1] = 25
            if loopLine[0] == 'SS':
                if maxStraightFound(hand) >= 4:
                    loopLine[1] = 30
            if loopLine[0] == 'LS':
                if maxStraightFound(hand) >= 5:
                    loopLine[1] = 40
            if loopLine[0] == 'Y':
                if maxOfAKindFound(hand) >= 5:
                    loopLine[1] = 50
            if loopLine[0] == 'C':
                    loopLine[1] = totalAllDice()               
    #show the user their scoring options       
    print('your scoring options are as follows:')
    for loopLine in possibleList:
        print('score is ',loopLine[1], ' if you choose the ',loopLine[0],' line')
    
    #let use pick where to place the hand
    choice = input('enter the code for the line where you would like your score placed ')

    #get score and update scorecard list
    for loopLine in possibleList:
        if loopLine[0] == choice:
            scoreOfChoice = loopLine[1]
    for loopLine in cardList:
        if loopLine[0] == choice:
            loopLine[3] = scoreOfChoice
            loopLine[1] = 'y'

    writeScorecard()
    #set condition to play another hand if any scorecard lines still not used
    openLine = False
    openCount = 0
    for loopLine in cardList:
        if loopLine[1] == 'n':
            openCount += 1
    if openCount > 0:
        openLine = True
        print()
        print(openCount, ' scorecard lines are still available')
##### end of game loop
        
#scorecard is full
print('game over')
#print the final scorecard
printScorecard()


