inputString = "17694 18469 16452 19748 19134 16289"

amts = [int(i) for i in inputString.split(" ")]

probability = [1, 1, 1, .75, .5, 0]

print(2 * sum(a * b for a, b in zip(amts, probability)))
