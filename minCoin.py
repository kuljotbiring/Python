
coins = [1, 2, 5]

amount = 11


def coinCount(cc, amount, coins):
    outputarray = [0] * len(coins)
    coinCheck = amount

    while coinCheck > 0:
        coinCheck = coinCheck - coins[cc[coinCheck]]
        outputarray[cc[coinCheck]] += 1

    return outputarray

def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount

    cc = [-1] * (amount + 1)

    for j in range(len(coins)):
        for i in range(0, amount + 1):
            if dp[i] > (dp[i - coins[j]] + 1):
                dp[i] = (dp[i - coins[j]] + 1)
                cc[i] = j

    print(coins, "coin denominations used")
    print((coinCount(cc, amount, coins), 'Frequency of coins used: '))

    return dp[-1] if dp[-1] != float('inf') else -1


print(coinChange(coins, 11))
