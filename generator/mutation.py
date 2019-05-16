from abc import ABCMeta, abstractmethod

class MutationType:
    Full = 1
    Word = 2
    Lexical = 3

    def __init__(self):
        pass

class Mutation(ABCMeta):
    type = None
