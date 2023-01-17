from typing import Set


def parseFasta():

    ret = {}
    with open('input.txt', 'r') as f:

        curr = None
        code = ""

        for line in f:
            if line[0] == '>':
                if curr != None:

                    ret[curr] = code
                    code = ""

                curr = line.strip()[1:]

            else:

                code += line.strip()

        ret[curr] = code

    return ret


fasta = parseFasta()


def getSubstringSet(dna: str) -> Set[str]:

    return set([dna[i: j] for i in range(len(dna)) for j in range(i + 1, len(dna) + 1)])


dnaCodes = list([getSubstringSet(s) for s in fasta.values()])


initial = dnaCodes[0]
for i, value in enumerate(dnaCodes[1:]):

    print(i, len(value))

    initial.intersection_update(value)

print(max(initial, key=lambda x: len(x)))
