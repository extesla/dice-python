from pyparsing import Literal


def operator():
    token = Literal("+") | Literal("-") | Literal("/") | Literal("*")
    token.setName("operator")
    return token
