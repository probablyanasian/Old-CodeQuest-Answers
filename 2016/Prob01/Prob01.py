openFile = open("Prob01.in.txt", 'r')
readFile = openFile.readlines()
solutionFile = open("Prob01.solution.txt", "r+")
solutionFile.seek(0)
solutionFile.truncate()
for line in range(int(readFile.pop(0).rstrip())):
    value = int(readFile.pop(0))
    for i in range(value):
        solutionFile.write(("# "*value).rstrip()+'\n')