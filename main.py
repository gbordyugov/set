from dataclasses import dataclass
from enum import IntEnum, StrEnum


class Colour(StrEnum):
    RED = 'red'
    GREEN = 'green'
    PURPLE = 'purple'


class Shape(StrEnum):
    DIAMOND = 'diamond'
    SQUIGGLE = 'squiggle'
    OVAL = 'oval'


class Number(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class Shading(StrEnum):
    SOLID = 'solid'
    STRIPED = 'striped'
    OPEN = 'open'


@dataclass(frozen=True, order=True)
class Card:
    colour: Colour
    shape: Shape
    number: Number
    shading: Shading


cards = [
    Card(colour=c, shape=s, number=n, shading=sh)
    for c in Colour
    for s in Shape
    for n in Number
    for sh in Shading
]


def is_set(c1: Card, c2: Card, c3: Card) -> bool:
    cards = {c1, c2, c3}
    assert len(cards) == 3, "Need three distinct cards."

    colours = {c.colour for c in cards}
    shapes = {c.shape for c in cards}
    numbers = {c.number for c in cards}
    shadings = {c.shading for c in cards}

    properties = [colours, shapes, numbers, shadings]
    return all(len(p) != 2 for p in properties)


def find_sets_brute_force(cards: set[Card]) -> list[set[Card]]:
    cards = set(cards)
    assert len(cards) >= 3, "Need at least three cards."
    triples = [
        (c1, c2, c3)
        for c1 in cards
        for c2 in cards
        for c3 in cards
        if c1 < c2 < c3
    ]
    return [t for t in triples if is_set(*t)]



def complement(c1: Card, c2: Card) -> Card:
    assert c1 != c2, "Two distinct cards are expected."

    if c1.colour == c2.colour:
        colour = c1.colour
    else:
        colour, = set(Colour) - {c1.colour, c2.colour}

    if c1.shape == c2.shape:
        shape = c1.shape
    else:
        shape, = set(Shape) - {c1.shape, c2.shape}

    if c1.number == c2.number:
        number = c1.number
    else:
        number, = set(Number) - {c1.number, c2.number}

    if c1.shading == c2.shading:
        shading = c1.shading
    else:
        shading, = set(Shading) - {c1.shading, c2.shading}

    return Card(colour=colour, shape=shape, number=number, shading=shading)


def find_sets_n2(cards: set[Card]) -> list[set[Card]]:
    cards = set(cards)
    assert len(cards) >= 3, "Need at least three cards."

    pairs = [(c1, c2) for c1 in cards for c2 in cards if c1 < c2]

    result = []

    for c1, c2 in pairs:
        c3 = complement(c1, c2)
        if c3 in cards and c2 < c3:
            result.append({c1, c2, c3})

    return result
