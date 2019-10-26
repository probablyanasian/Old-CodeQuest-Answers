openFile = open("Prob03.in.txt", 'r')
readFile = openFile.readlines()
solutionFile = open("Prob03.solution.txt", "r+")
solutionFile.seek(0)
solutionFile.truncate()
for line in range(int(readFile.pop(0).rstrip())):
    numbers = readFile.pop(0).split(',')
    for number in range(len(numbers)):
        numbers[number] = int(numbers[number].rstrip().strip())
    numbers.sort()

    if len(numbers) > 3:
        solutionFile.write("Not a Triangle")
    elif (int(numbers[0])+int(numbers[1])) <= int(numbers[2]):
        solutionFile.write("Not a Triangle")
    elif (int(numbers[0]) == int(numbers[1]) and int(numbers[1]) == int(numbers[2])):
        solutionFile.write("Equilateral")
    elif (int(numbers[0]) == int(numbers[1]) or int(numbers[1]) == int(numbers[2])):
        solutionFile.write("Isosceles")
    else:
        solutionFile.write("Scalene")
    solutionFile.write("\n")

openFile.close()
solutionFile.close()