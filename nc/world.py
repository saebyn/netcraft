
BLOCK_DEFAULTS = {'falls': False, 'breakable': True, 'clear': False, 'solid': True}

BLOCK_TYPES = {
    '#': {'name': 'Bedrock', 'breakable': False},
    ' ': {'name': 'Air', 'breakable': False, 'clear': True, 'solid': False},
    's': {'name': 'Sand', 'falls': True}
}


def apply_gravity(world):
    """
    >>> apply_gravity(["sss",
    ...                "   ",
    ...                "###"])
    ["   ", "sss", "###"]
    >>> apply_gravity(["sss",
    ...                "  #",
    ...                "###"])
    ["  s", "ss#", "###"]
    >>> apply_gravity(["   ",
    ...                "sss",
    ...                "###"])
    ["   ", "sss", "###"]
    >>> apply_gravity(["sss",
    ...                "   ",
    ...                "   ",
    ...                "###"])
    ["   ", "sss", "   ", "###"]
    >>> apply_gravity(["ss ",
    ...                "  s",
    ...                "   ",
    ...                "###"])
    ["   ", "ss ", "  s", "###"]
    """
    return world


if __name__ == '__main__':
    import doctest
    doctest.testmod()
