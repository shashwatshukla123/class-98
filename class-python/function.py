def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0
    
    #The split() method splits a string into a list.
    #You can specify the separator, default separator is any whitespace.

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()
