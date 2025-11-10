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
    assert len(cards) >= 3, "Need at least three cards."
    triples = [
        (c1, c2, c3)
        for c1 in cards
        for c2 in cards
        for c3 in cards
        if c1 < c2 < c3
    ]
    return [t for t in triples if is_set(*t)]


def main():
    print("Hello from set!")


if __name__ == "__main__":
    main()
