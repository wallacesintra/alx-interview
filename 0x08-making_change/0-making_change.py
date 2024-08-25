#!/usr/bin/python3
"""Making change O(n)"""


def makeChange(coins, total):
    """dynamic programming"""
    holder = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            holder += total // coin
            total = total % coin

    return holder if total == 0 else -1
