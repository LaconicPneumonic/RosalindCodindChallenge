N = 31
K = 3

# Fn = Fn-1 + k * Fn-2


prevPrev = 1
prev = 1 + K * prevPrev
curr = prev + K * prevPrev

for i in range(3, N):

    curr = prev + K * prevPrev

    prevPrev = prev
    prev = curr


print(curr)
