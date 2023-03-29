#!/usr/bin/env python3
"""Some util functions.
"""
from __future__ import annotations
from typing import Union
from pathlib import Path
import sys


def rust_files(pattern="src/**/*.rs") -> Iterable[Path]:
    paths = Path().glob(pattern)
    return (path for path in paths if "/.ipynb_checkpoints/" not in str(path))


def format_suit(suit: int) -> str:
    return {0: "d", 1: "c", 2: "h", 3: "s", 4: "j"}[suit]


def format_rank(rank) -> str:
    if rank <= 9:
        return str(rank)
    if rank == 10:
        return "T"
    if rank == 11:
        return "J"
    if rank == 12:
        return "Q"
    if rank == 13:
        return "K"
    return "A"


def format_index(index: int) -> str:
    suit, rank = divmod(index, 13)
    rank += 2
    return format_rank(rank) + format_suit(suit)


def format_id(id_: Union[int, list[int], tuple[int]]) -> str:
    if isinstance(id_, (list, tuple)):
        return " ".join(format_id(i) for i in id_).strip()
    indexes = []
    index = 0
    while id_ > 0:
        if (id_ & 1) == 1:
            indexes.append(index)
        index += 1
        id_ >>= 1
    return " ".join(format_index(index) for index in indexes)


def to_suit(suit: str) -> int:
    return {
        "d": 0,
        "c": 1,
        "h": 2,
        "s": 3,
        "j": 4,
    }[suit.lower()]


def to_rank(value) -> int:
    value = value.upper()
    if value == "T":
        return 10
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value == "K":
        return 13
    if value == "A":
        return 14
    return int(value)


def to_index(card: str) -> int:
    rank = to_rank(card[0])
    suit = to_suit(card[1])
    return suit * 13 + rank - 2


def to_id(cards: str) -> int:
    cards = cards.strip()
    if cards:
        return sum(2**to_index(card) for card in cards.split(" "))
    return 0