#!/usr/bin/python3
"""function validUtf8 method"""


def validUTF8(data):
    """
    Determines if given data represents valid UTF-8 encoding
    @params Args:
        data: list of integers
    @Returns:
        True if valid UTF-8 encoding, False if not
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for i in data:

        mask = 1 << 7
        if n_bytes == 0:
            while mask & i:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character, then we
            # simply have to look at the two most significant bits and we make
            # use of the masks we defined before.
            if not (i & mask1 and not (i & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
