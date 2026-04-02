from pyparsing import OneOrMore

from dice.grammar.term import term


def expression():
    def transformer(string, location, tokens):
        return tokens.asList()

    token = OneOrMore(term())
    token.setName("expression")
    token.setParseAction(transformer)
    return token
