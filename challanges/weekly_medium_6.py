# 9/10
import sys
def CoinDeterminer(num):
    coins = [11, 9, 7, 5, 1]
    m = len(coins)
    if num == 0:
        return 0

    res = sys.maxsize

    for i in range(0, m):
        if coins[i] <= num:
            sub_res = CoinDeterminer(num-coins[i])

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    return res


print(CoinDeterminer(16))
print(CoinDeterminer(25))
print(CoinDeterminer(100))  # failed case (takes too long)
