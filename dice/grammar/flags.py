from pyparsing import CaselessLiteral


def flags():
    token = (
        CaselessLiteral("!advantage")
        | CaselessLiteral("!adv")
        | CaselessLiteral("!disadvantage")
        | CaselessLiteral("!dis")
        | CaselessLiteral("!drop")
        | CaselessLiteral("!grow")
        | CaselessLiteral("!keep")
        | CaselessLiteral("!shrink")
        | CaselessLiteral("!take")
    )

    token.setName("flags")
    token.setResultsName("flags")
    return token
