# 15/15

from functools import reduce
def NimWinner(arr):
    """
    """
    xor = reduce(lambda x, y: x ^ y, arr)
    return 1 if xor != 0 else 2