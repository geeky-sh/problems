from __future__ import annotations
from typing import List
from dataclasses import dataclass, field
import pytest
from enum import Enum

"""

Token:
    color

Card
    tokens: list

    prop: white_count
    prop: blue_count
    prop: green_count
    prop: red_count
    prop: black_count

    get_token_count(color)

    can_purchase(tokens)

Player:
    tokens: list
    cards: list

    purchase(card):
        - card.can_purchase
        - minus_tokens
            for each token in card:
                remove ctoken from ctokens if ctoken == token
        - add_card
"""

## final version
class Color(Enum):
    WHITE = '0'
    GREEN = '1'
    RED = '2'
    BLUE = '3'
    BLACK = '4'

@dataclass
class Token:
    color: Color

@dataclass
class TokenCollection:
    tokens: List[Token] = field(default_factory=list)

    def get_token_count(self, color: Color):
        return [token for token in self.tokens if token.color == color]

    @property
    def white_tokens(self):
        return self.get_token_count(Color.WHITE)

    @property
    def blue_tokens(self):
        return self.get_token_count(Color.BLUE)

    @property
    def green_tokens(self):
        return self.get_token_count(Color.GREEN)

    @property
    def red_tokens(self):
        return self.get_token_count(Color.RED)

    @property
    def black_tokens(self):
        return self.get_token_count(Color.BLACK)


def can_purchase(tokens, card):
    other_card = Card(tokens)
    return (
        other_card.white_tokens >= card.white_tokens and
        other_card.blue_tokens >= card.blue_tokens and
        other_card.green_tokens >= card.green_tokens and
        other_card.red_tokens >= card.red_tokens and
        other_card.black_tokens >= card.black_tokens
    )

@dataclass
class Card(TokenCollection):
    pass

@dataclass
class Player(TokenCollection):
    cards: List[Card] = field(default_factory=list)

    def remove_token(self, color: Color):
        for i, rtoken in enumerate(self.tokens):
            if rtoken.color == color:
                del self.tokens[i]
                break

    def purchase(self, card: Card):
        if not can_purchase(self.tokens, card):
            return False

        for token in card.tokens:
            self.remove_token(token.color)

        self.cards.append(card)
        return True

# @dataclass
# class Player
# ##

# @dataclass
# class Card:
#     white_count: int = 0
#     green_count: int = 0
#     blue_count: int = 0
#     red_count: int = 0
#     black_count: int = 0

# @dataclass
# class WhiteToken:
#     value: int

# @dataclass
# class BlueToken:
#     value: int

# @dataclass
# class GreenToken:
#     value: int

# @dataclass
# class RedToken:
#     value: int

# @dataclass
# class BlackToken:
#     value: int


# def can_purchase(card: Card, tokens: list):
#     cwhite, cred, cgreen, cblue, cblack = 0, 0, 0, 0, 0

#     for token in tokens:
#         if isinstance(token, WhiteToken):
#             cwhite += token.value
#         elif isinstance(token, GreenToken):
#             cgreen += token.value
#         elif isinstance(token, RedToken):
#             cred += token.value
#         elif isinstance(token, BlueToken):
#             cblue += token.value
#         elif isinstance(token, BlackToken):
#             cblack += token.value


#     return (
#         card.white_count <= cwhite and card.green_count <= cgreen and
#         card.red_count <= cred and card.blue_count <= cblue and
#         card.black_count <= cblack
#     )

# @dataclass
# class Player:
#     cards: List[Card] = field(default_factory=list)
#     white_tokens: List[WhiteToken] = field(default_factory=list)
#     black_tokens: List[BlackToken] = field(default_factory=list)
#     red_tokens: List[RedToken]  = field(default_factory=list)
#     green_tokens: List[GreenToken] = field(default_factory=list)
#     blue_tokens: List[BlueToken] = field(default_factory=list)

#     def get_all_tokens(self):
#         tokens = self.white_tokens + self.black_tokens + self.red_tokens + self.green_tokens + self.blue_tokens
#         return tokens

#     def minus_white_token(self, count):
#         if count == 0:
#             return
#         icount = 0
#         for token in self.white_tokens:
#             count -= token.value
#             icount += 1
#             if count == 0:
#                 break
#         self.white_tokens = self.white_tokens[icount:]

#     def minus_green_token(self, count):
#         if count == 0:
#             return
#         icount = 0
#         for token in self.green_tokens:
#             count -= token.value
#             icount += 1
#             if count == 0:
#                 break
#         self.green_tokens = self.green_tokens[icount:]

#     def minus_red_token(self, count):
#         if count == 0:
#             return
#         icount = 0
#         for token in self.red_tokens:
#             count -= token.value
#             icount += 1
#             if count == 0:
#                 break
#         self.red_tokens = self.red_tokens[icount:]

#     def minus_blue_token(self, count):
#         if count == 0:
#             return
#         icount = 0
#         for token in self.blue_tokens:
#             count -= token.value
#             icount += 1
#             if count == 0:
#                 break
#         self.blue_tokens = self.blue_tokens[icount:]

#     def minus_black_token(self, count):
#         if count == 0:
#             return
#         icount = 0
#         for token in self.black_tokens:
#             count -= token.value
#             icount += 1
#             if count == 0:
#                 break
#         self.black_tokens = self.black_tokens[icount:]

#     def purchase(self, card: Card) -> bool:
#         if not can_purchase(card, self.get_all_tokens()):
#             return False

#         self.minus_white_token(card.white_count)
#         self.minus_black_token(card.black_count)
#         self.minus_green_token(card.green_count)
#         self.minus_red_token(card.red_count)
#         self.minus_blue_token(card.blue_count)

#         self.cards.append(card)

#         return True


# def test_can_purchase():
#     card = Card(white_count=1, blue_count=4, green_count=2)
#     tokens = [
#         WhiteToken(value=2),
#         BlueToken(value=4),
#         GreenToken(value=2)
#     ]

#     assert can_purchase(card, tokens)


#     card = Card(white_count=4, blue_count=4, green_count=2)
#     tokens = [
#         WhiteToken(value=2),
#         BlueToken(value=4),
#         GreenToken(value=2)
#     ]

#     assert not can_purchase(card, tokens)

# def test_purchase():
#     player = Player(
#         white_tokens=[WhiteToken(value=1), WhiteToken(value=1)],
#         blue_tokens=[BlueToken(value=1), BlueToken(value=1)]
#     )
#     card = Card(white_count=2, blue_count=2)
#     assert player.purchase(card)

#     assert player.white_tokens == []
#     assert player.blue_tokens == []
#     assert card in player.cards

#     player = Player(
#         white_tokens=[WhiteToken(value=1), WhiteToken(value=1)],
#         blue_tokens=[BlueToken(value=1), BlueToken(value=1)]
#     )
#     card = Card(white_count=3, blue_count=2)
#     assert not player.purchase(card)

def test_can_purchase():
    card = Card(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.GREEN),
        Token(color=Color.GREEN),
    ])
    tokens = [
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.GREEN),
        Token(color=Color.GREEN),
    ]

    assert can_purchase(tokens, card)


    card = Card(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.GREEN),
        Token(color=Color.GREEN),
    ])
    tokens = [
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
        Token(color=Color.GREEN),
        Token(color=Color.GREEN),
    ]

    assert not can_purchase(tokens, card)

def test_purchase():
    player = Player(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE)
    ])
    card = Card(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
    ])
    assert player.purchase(card)

    assert player.white_tokens == []
    assert player.blue_tokens == []
    assert card in player.cards

    player = Player(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.BLUE)
    ])
    card = Card(tokens=[
        Token(color=Color.WHITE),
        Token(color=Color.WHITE),
        Token(color=Color.BLUE),
        Token(color=Color.BLUE),
    ])
    assert not player.purchase(card)