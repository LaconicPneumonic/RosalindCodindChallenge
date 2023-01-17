from collections import Counter


def calculateContent(s: str) -> float:
    counts = Counter(s)

    return (counts['C'] + counts['G']) / counts.total()


with open('input.txt', 'r') as f:
    curr = None
    currDnaString = ""
    maxPair = (None, -1 * float('inf'))

    for line in f:
        if line[0] == '>':

            if curr != None:

                percentage = calculateContent(currDnaString)

                currDnaString = ""

                if percentage > maxPair[1]:
                    maxPair = (curr, percentage)
            curr = line.strip()[1:]

        else:
            currDnaString += line.strip()

    percentage = calculateContent(currDnaString)

    if percentage > maxPair[1]:
        maxPair = (curr, percentage)

    print(maxPair[0])
    print(100 * maxPair[1])
