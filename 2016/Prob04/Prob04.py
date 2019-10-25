openFile = open("Prob04.in.txt", 'r')
readFile = openFile.readlines()
solutionFile = open("Prob04.solution.txt", "r+")
solutionFile.seek(0)
solutionFile.truncate()
for line in range(int(readFile.pop(0).rstrip())):
    inputLine = readFile.pop(0).rstrip()
    inputWords = inputLine.split('|')
    if inputWords[0] == inputWords[1]:
        solutionFile.write(inputLine + " = NOT AN ANAGRAM\n")
    
    else:
        inputWords[0] = sorted(inputWords[0])
        inputWords[1] = sorted(inputWords[1])
        freqA = {}
        for keys in inputWords[0]:
            freqA[keys] = freqA.get(keys, 0) + 1

        freqB = {}
        for keys in inputWords[1]:
            freqB[keys] = freqB.get(keys, 0) + 1
        
        if freqA == freqB:
            solutionFile.write(inputLine + " = ANAGRAM\n")
        else:
            solutionFile.write(inputLine + " = NOT AN ANAGRAM\n")