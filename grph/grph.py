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


K = 3

fasta = parseFasta()

# O(KN)
nodes = [(v[:K], k, v[len(v) - K:len(v)]) for k, v in fasta.items()]

# O(KN)
affixes = dict((k, i) for i, k in enumerate(
    [a for p in nodes for a in [p[0], p[2]]]))

# O(KN)
remappedNodes = [(affixes[n[0]], n[1], affixes[n[2]]) for n in nodes]

edges = []
# O(N^2)
for i in range(len(remappedNodes)):
    for j in range(len(remappedNodes)):
        # O(1)
        if i != j and remappedNodes[i][2] == remappedNodes[j][0]:
            edges.append((remappedNodes[i][1], remappedNodes[j][1]))


print("\n".join([" ".join(p) for p in edges]))
