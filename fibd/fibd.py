from collections import deque

N = 12
M = 5

dp = N * [0]
dp[0] = 1


for i in range(1, N):

    # 1. kill all rabbits of M age. 2. all living rabbits produce heirs
    # dp[i] = rabbits born on day i
    # dp[i] = rabbits older than maturity dp[i - 2] to rabbits from M days ago i.e. dp[i - M]

    dp[i] = sum([dp[i - j] for j in range(2, M + 1) if (i - j) >= 0])


# print everything from the past M days
print(sum(dp[N - M: N]))


dpEfficient = deque([0] * (M + 1))
dpEfficient[1] = 1
for i in range(1, N):

    # 1. kill all rabbits of M age. 2. all living rabbits produce heirs
    # dp[i] = rabbits born on day i
    # dp[i] = rabbits older than maturity dp[i - 2] to rabbits from M days ago i.e. dp[i - M]

    dpEfficient[0] = sum([dpEfficient[j] for j in range(2, M + 1)])

    dpEfficient.pop()
    dpEfficient.appendleft(0)


# print everything from the past M days
print(sum(dpEfficient))


large = deque([0] * (M + 2))
large[M-1] = 1

# time = O(N), space = O(M)
for i in range(1, N):
    large[M + 1] = large[M - 1] + large[M] - large[0]
    large.popleft()
    large.append(0)


# print everything from the past M days
print(large[-2] + large[-3])
