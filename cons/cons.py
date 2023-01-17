from collections import Counter


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


codes = list(fasta.values())
K = len(codes[0])


ret = ""
for i in range(K):
    consensus = Counter([c[i] for c in codes]).most_common(1)[0][0]

    ret += consensus


print(ret)
