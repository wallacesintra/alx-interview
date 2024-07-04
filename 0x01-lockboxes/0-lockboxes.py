#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else False
    """

    # check if boxes is a list
    if len(boxes) == 0:
        return False

    keys = [0]

    # check if boxes is a list of lists
    for key in keys:
        # check if key is in boxes
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)

    if len(keys) == len(boxes):
        return True
    return False
