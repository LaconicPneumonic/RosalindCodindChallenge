from typing import Dict
import requests


def requestFasta(name: str) -> str:

    id = name.split("_")[0]

    response = requests.get(f"https://rest.uniprot.org/uniprotkb/{id}.fasta")

    return id, response.text


def parseFasta(text: str) -> Dict[str, str]:

    curr = None
    code = ""

    for line in text.strip().split("\n"):
        if line[0] == '>':
            if curr != None:

                code = ""

            curr = line.strip()[1:]

        else:

            code += line.strip()

    return curr, code


def findMotif(motif: str, sequence: str):
    # general motif parser

    # use dynamic programming in the matrix to determine how to match these patterns arbitrarily
    # https://rosalind.info/problems/mprt/
    # https://leetcode.com/problems/regular-expression-matching/solutions/127565/regular-expression-matching/?orderBy=most_votes
    # https://leetcode.com/problems/wildcard-matching/solutions/294659/wildcard-matching/?orderBy=most_votes

    # process motif

    finalMotif = []
    wordBag = set()

    EXCLUSIVE = "EXCLUSIVE"
    INCLUSIVE = "INCLUSIVE"

    for m in motif:
        if m in ["]", "}"]:
            finalMotif.append(wordBag)
            wordBag = set()

        elif m == "[":
            wordBag.add(INCLUSIVE)

        elif m == "{":
            wordBag.add(EXCLUSIVE)

        elif len(wordBag) != 0:
            wordBag.add(m)
        else:
            finalMotif.append(m)

    dp = [[False for _ in range(len(finalMotif) + 1)]
          for _ in range(len(sequence) + 1)]

    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(len(dp[0])):
        dp[0][i] = True

    for s in range(1, len(dp)):
        for m in range(1, len(dp[0])):

            patternChar = finalMotif[m - 1]
            seqChar = sequence[s - 1]

            if len(patternChar) == 1 and patternChar == seqChar:
                dp[s][m] = dp[s - 1][m - 1]
            elif INCLUSIVE in patternChar and seqChar in patternChar:
                dp[s][m] = dp[s - 1][m - 1]
            elif EXCLUSIVE in patternChar and seqChar not in patternChar:
                dp[s][m] = dp[s - 1][m - 1]

    return [i - len(finalMotif) + 1 for i in range(len(finalMotif), len(dp)) if dp[i][len(dp[0]) - 1]]


with open('./input.txt', 'r') as f:

    for line in (l.strip() for l in f):

        try:
            name, fastaText = requestFasta(line)

            _, code = parseFasta(fastaText)

            occurrences = findMotif("N{P}[ST]{P}", code)

            if len(occurrences):

                print(line)
                print(" ".join((str(o) for o in occurrences)))

        except:

            print(f"Failed on {line}")
