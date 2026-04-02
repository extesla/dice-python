from dice.tokens import Integer
from pyparsing import Word, nums


def integer():
    token = Word(nums)
    token.setParseAction(Integer.parse)
    token.setName("integer")
    return token
