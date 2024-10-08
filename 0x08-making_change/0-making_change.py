#!/usr/bin/python3
"""Making change O(n)"""


def makeChange(coins, total):
    """dynamic programming"""
    no_of_coins = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            no_of_coins += total // coin
            total = total % coin

    return no_of_coins if total == 0 else -1
