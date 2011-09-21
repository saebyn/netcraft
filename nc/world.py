
BLOCK_DEFAULTS = {
    'falls': False, 'breakable': True, 'clear': False,
    'solid': True, 'light': 0.0, 'liquid': False
}

BLOCK_TYPES = {
    '#': {'name': 'Bedrock', 'breakable': False},
    ' ': {'name': 'Air', 'breakable': False, 'clear': True, 'solid': False},
    's': {'name': 'Sand', 'falls': True},
    '~': {'name': 'Water', 'falls': True, 'liquid': True, 'clear': True, 'solid': False},
    '@': {'name': 'Latern', 'clear': True, 'solid': False, 'light': 0.8},
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


def calculate_lights(world):
    """
    >>> calculate_lights(['   ',
    ...                   ' @ ',
    ...                   '   '])
    [[0.2, 0.4, 0.2], [0.4, 0.8, 0.4], [0.2, 0.4, 0.2]]
    >>> calculate_lights(['   ',
    ...                   '@ @',
    ...                   '   '])
    [[0.5, 0.4, 0.5], [0.8, 0.8, 0.8], [0.5, 0.4, 0.5]]
    >>> calculate_lights(['@ @',
    ...                   '~~~',
    ...                   '   '])
    [[0.8, 0.8, 0.8], [0.5, 0.4, 0.5], [0.25, 0.2, 0.25]]
    """
    return [[0.0] * len(level) for level in world]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
