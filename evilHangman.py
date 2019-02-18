#David Kim 2/17/19

from collections import Counter 

def main():
    file = open('dictionary.txt', 'r') 
    strOfWords = file.read() 
    listOfWords = strOfWords.splitlines()
    availableWordLen = checkAvailableWordLen(listOfWords)
   
    replay = True
    while(replay): 
        targetWordLen = askWordLen(availableWordLen)
        numGuesses = askNumGuesses()
        wordsRemaining = findWordsRemaining(listOfWords, targetWordLen)
        guessedList = list()
        wordProgress = updateProgress(wordsRemaining[0], guessedList)
        
        while(True):
            print("Used Letters: " + str(guessedList))
            print("Wrong guesses remaining: " + str(numGuesses))
            print("Game progress: " + str(wordProgress))  
           
            guess = askGuess(guessedList)            
            guessedList.append(guess)

            wordsRemaining = updateWordsRemaining(guess, wordsRemaining)
            wordProgress = updateProgress(wordsRemaining[0], guessedList)
            print()
            if(guess not in wordProgress):
                numGuesses -= 1
            if("-" not in wordProgress or numGuesses == 0):
                break
        if(numGuesses == 0):
            print(f'You lose!. The word was {wordsRemaining[0]}')
        else:
            print(f'You Win! The word was {wordProgress}')

        replay = askPlayAgain()

    print("Thank you for playing!")

   
def checkAvailableWordLen(listOfWords):
    wordLengths = list()  
    for word in range(len(listOfWords)):
        length = len(listOfWords[word])
        if(length not in wordLengths):
            wordLengths.append(length)
    wordLengths.sort()
    return wordLengths
    
def askWordLen(availableWordLen):
    print("Choose the length of the word you would like to guess:")
    print(availableWordLen)
    length = int(input("Enter word Length:")) #input returns string
    while(length not in availableWordLen):
        print("Invalid input. Please try again.")
        length = int(input("Enter word Length:"))
    return length 
           

def askNumGuesses():
    guesses = int(input("Enter number of guesses(1-15):"))
    while(guesses < 1 or guesses > 15):
        print("Invalid input.")
        guesses = int(input("Enter number of guesses(1-15):"))
    return guesses

def findWordsRemaining(listOfWords, targetWordLen):
    words = list()
    for word in range(len(listOfWords)):
        if(targetWordLen == len(listOfWords[word])):
            words.append(listOfWords[word])
    return words

def askGuess(guessedList):
    letter = str(input("Guess a letter: " )).lower()   
    while (letter in guessedList or not (letter.isalpha() and len(letter) == 1)):
        if(letter in guessedList):
            print(f'You already guessed "{letter}"')
        else:
            print(f'Invalid guess. Please enter an alphabet.')
        letter = str(input("Guess a letter: " )).lower() 
    return letter  

def updateWordsRemaining(guess, wordsRemaining):  
    wordGroups = findWordGroups(guess, wordsRemaining)
    groupToReturn = Counter(wordGroups).most_common(1) #returns a list of one tuple.
    groupToReturn = (groupToReturn[0])[0]  
    words = list()
    for word in wordsRemaining:
        wordGroup = ""
        for letter in word:
            if(letter == guess):
                wordGroup += guess
            else:
                wordGroup += "-"
        if(wordGroup == groupToReturn):
            words.append(word)
    return words


def findWordGroups(guess, wordsRemaining):
    wordGroups = list()
    for word in wordsRemaining:
        progress = ""
        for letter in word:
            if(letter == guess):
                progress += guess
            else:
                progress += "-"
        wordGroups.append(progress)
    return wordGroups

def updateProgress(word,guessedList):
    progress = ""
    for letter in word:
        if(letter in guessedList):
            progress += letter
        else: 
            progress += "-"
    return progress
 
def askPlayAgain():
    replay = input("Play again? Enter 1 for yes, 0 for no: ")
    while not (replay == '1' or replay == '0'):
        replay = input("Invalid Input. Play again? Enter 1 for yes, 0 for no: ")
    if (replay == '1'):
        return True
    else:
        return False

if __name__ == '__main__':
    main()