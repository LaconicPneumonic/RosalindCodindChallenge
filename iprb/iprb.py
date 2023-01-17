K = 15
M = 25
N = 30
total = K + M + N


finalProbability = 0
# HomoDom x hetero
finalProbability += 2 * (K/total) * (M/(total - 1))
# HomoDom x HomoDom
finalProbability += (K/total) * ((K - 1)/(total - 1))
# Hetero x Hetero
finalProbability += (M/total) * ((M-1)/(total - 1)) * 0.75
# HomoDom x HomoRecessive
finalProbability += 2 * (K/total) * (N/(total - 1))
# Hetero x HomoRecessive
finalProbability += 2 * (M/total) * (N/(total - 1)) * 0.5


print(finalProbability)
