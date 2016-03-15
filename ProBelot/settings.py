import collections

CARD_TYPES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
VALUES = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
BIDDINGS = ['Pass', 'Recontra', 'Contra',
            'All Trumps', 'No Trumps',
            'Spades', 'Hearts', 'Diamonds', 'Clubs']

trump = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 20,
    '10': 10,
    '9': 14,
    '8': 0,
    '7': 0,
}

not_trump = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    '10': 10,
    '9': 0,
    '8': 0,
    '7': 0,
}

card_values_dict = (
    ('7', 0),
    ('8', 1),
    ('9', 2),
    ('10', 3),
    ('J', 4),
    ('Q', 5),
    ('K', 6),
    ('A', 7),
)

cards_values = collections.OrderedDict(card_values_dict)
