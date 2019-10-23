openFile = open("Prob02.in.txt", 'r+')
readFile = openFile.readlines()
solutionFile = open("Prob02.solution.txt", "r+")
solutionFile.seek(0)
solutionFile.truncate()
for line in range(int(readFile.pop(0).rstrip())):
    coins = [0,0,0,0]
    origValue = readFile.pop(0).rstrip()
    value = int(origValue.strip("$").replace('.', ""))
    while value >= 25:
        value -= 25
        coins[0] += 1
    while value >= 10:
        value -= 10
        coins[1] += 1
    while value >= 5:
        value -= 5
        coins[2] += 1
    while value >= 1:
        value -= 1
        coins[3] += 1
    solutionFile.write(f'{origValue}\nQuarters:{coins[0]}\nDimes:{coins[1]}\nNickel:{coins[2]}\nPennies:{coins[3]}\n')

openFile.close()
solutionFile.close()