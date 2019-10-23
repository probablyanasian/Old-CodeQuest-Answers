openFile = open('Prob07.in.txt', 'r')
readFile = openFile.readlines()
solutionFile = open("Prob07.solution.txt", "w")
solutionFile.seek(0)
solutionFile.truncate()
messagesNum = int(readFile.pop(0))
for message in range(messagesNum):
    messageLines = int(readFile.pop(0))
    messageRevealed = []
    messageHidden = []
    messageMask = []
    for lineNum in range(messageLines):
        messageHidden.append(readFile.pop(0).rstrip()) 
    messageOffset = tuple([int(i) for i in readFile.pop(0).rstrip().split(',')])
    maskLines = int(readFile.pop(0))
    for lineNum in range(maskLines):
        messageMask.append(readFile.pop(0).rstrip())
    for y in range(len(messageMask)):
        for x in range(len(messageMask[y])):
            if messageMask[y][x] == "O":
                messageRevealed.append(messageHidden[y+messageOffset[0]][x+messageOffset[1]])
    print("".join(messageRevealed))
    solutionFile.write("".join(messageRevealed)+'\n')