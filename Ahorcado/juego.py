
import random




def chooseWord(dif):
    ## open file and create array

    words = []
    f = open(r"C:\Users\joaoo\DWES\DWES\Ahorcado\palabras.txt", "r")
    
    ##define range of words
    
    sizeMin = 0
    sizeMax = 0

    if dif == 0:
        sizeMin = 3
        sizeMax = 5
    elif dif == 1:
        sizeMin = 6
        sizeMax = 9
    elif dif == 2:
        sizeMin = 10
        sizeMax = 1000
    
    ##populate an array with the words that fit the length
    counter = 0
    for x in f:
        aux = remove_accent((str(x).lower()))

        if len(aux) >= sizeMin and len(aux) <= sizeMax:
            words.append(aux)
            counter = counter + 1
            
            
    f.close()
    
    ##choose a random word from this array and returns it
    
    return(words[random.randint(0,len(words))])


def transformWordInArray(word):
    characters = []
    for char in word:
     characters.append(char)
    return(characters)

def printUI(counter, errorCounter, lines):
    
    linePrint = ""
    
    for x in lines:
        linePrint = linePrint + x
            
        
    
    
    print(" \n \n \nRodada numero " + str(counter) +"\n\nError: " + str(errorCounter) + "\n\n            "  + linePrint + "\n\n")
        


dif = input("Seleciona una dificuldade Facil(0) Nomral(1) Dificl(2): ")
errorCounter = 0
finish = 0   

wordString = chooseWord(int(dif))

print(wordString)

word = transformWordInArray(wordString)
attempt = 0
counter = 1



lines = []
for x in range(len(word)):
    lines.append("_")

while finish == 0:
    
    ##Print UI and asks for a letter
    
    printUI(counter, errorCounter, lines )
    
    attempt = input("Selecione una letra: ")
    
    
    #Verify if letter in word
    aux = False
    
    for x in range(len(lines)):
        if word[x] == attempt:
            lines[x] = word[x]
            aux = True
    
    ##if wrong add to counter and finish the game if reach limit
    if aux == False:
        errorCounter = errorCounter + 1
        if errorCounter == 6:
            finish = 1    
            
            
    ## check if word is complete
    
    aux = False
    for x in range(len(word)):
        if word[x] != lines[x]:
            aux = True
            
    if aux == False:
        finish = 1
        
    counter = counter + 1
    


               

if (errorCounter != 6):
    print("\n\n\n\n Usted encontro la palabra \n La palabra es: " + wordString + "\nTentativas: " + str(counter) + "\nErrores: " + str(errorCounter))
else:
    print("\n\n\n\n Usted no encontro la palabra \n La palabra es: " + wordString + "\nTentativas: " + str(counter) + "\nErrores: " + str(errorCounter))
    



        
        
        
        
        