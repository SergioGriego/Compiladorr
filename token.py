#la clase token guarda tipo del token y texto original
from tokentype import *
class Token:
    def __init__(self,tokenText,tokenKind):
        self.text=tokenText
        self.kind=tokenKind

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name== tokenText and kind.value>=100 and kind.value<200:
                return kind
        return None
