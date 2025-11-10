from dataclasses import dataclass
from enum import Enum


class Colour(Enum):
    RED = 'red'
    GREEN = 'green'
    PURPLE = 'purple'


class Shape(Enum):
    DIAMOND = 'diamond'
    SQUIGGLE = 'squiggle'
    OVAL = 'oval'


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Shading(Enum):
    SOLID = 'solid'
    STRIPED = 'striped'
    OPEN = 'OPEN'


@dataclass(frozen=True)
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
    colours = {c.colour for c in cards}
    shapes = {c.shape for c in cards}
    numbers = {c.number for c in cards}
    shadings = {c.shading for c in cards}

    properties = [colours, shapes, numbers, shadings]

    return all(len(p) == 1 or len(p) == 3 for p in properties)


def main():
    print("Hello from set!")


if __name__ == "__main__":
    main()
