from .parsers import ExpressionParser

def roll(expr):
    """
    """
    # 1. parse the expression
    parser = ExpressionParser()
    token = parser.parse(expr)
    raise NotImplementedError()
