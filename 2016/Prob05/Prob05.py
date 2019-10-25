openFile = open("Prob05.in.txt", 'r')
readFile = openFile.readlines()
solutionFile = open("Prob05.solution.txt", "r+")
solutionFile.seek(0)
solutionFile.truncate()

def roundr(value):
    roundRule = int(str(int(value))[-2:])
    if roundRule >= 50:
        value += 100
        value -= roundRule
    else:
        value -= roundRule
    return ('{:.2f}'.format(value/10000))
for line in range(int(readFile.pop(0).rstrip())):
    origValue = readFile.pop(0).rstrip()
    value = float(origValue.strip("$"))
    solutionFile.write(f'Total of the bill: {origValue}\n')
    solutionFile.write(f'15% = ${roundr(value*1500)}\n')
    solutionFile.write(f'18% = ${roundr(value*1800)}\n')
    solutionFile.write(f'20% = ${roundr(value*2000)}\n')