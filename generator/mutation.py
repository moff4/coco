from abc import ABCMeta, abstractmethod
from functools import reduce


class MutationType:
    Full = 1
    Word = 2
    Lexical = 3

    def __init__(self):
        pass


class Mutation(ABCMeta):
    type = None

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def mutate(self, string):
        pass


class Upper(Mutation):

    def __init__(self):
        super(Mutation, self).__init__(MutationType.Full)

    def mutate(self, string):
        return string.upper()


class Letter(Mutation):

    def __init__(self):
        super(Mutation, self).__init__(MutationType.Word)

    def mutate(self, string):
        return reduce(
            lambda x, y: x + y,
            (
                [
                    string.replace('a', '@'),
                    string.replace('A', '@'),
                    string.replace('A', '@').replace('a', '@'),
                ] if letter == 'a' else [
                    string.replace('s', '$'),
                    string.replace('S', '$'),
                    string.replace('s', '$').replace('S', '$'),
                ]
                for letter in string.lower()
                if letter in {'a', 's'}
            )
        )


class MonthMutate(Mutation):
    mutation_cases = {
        '01': ['Jan', '1'],
        '02': ['Feb', '2'],
        '03': ['March', 'Mart', '3'],
        '04': ['April', 'aprl', '4'],
        '05': ['May', '5'],
        '06': ['June', '6'],
        '07': ['July', '7'],
        '08': ['Aug', '8'],
        '09': ['Sept', 'Sent', '9'],
        '10': ['Oct', 'October', '10'],
        '11': ['Nov', 'November', '11'],
        '12': ['Dec', 'December', '12'],
    }

    def __init__(self):
        super(Mutation, self).__init__(MutationType.Lexical)

    def mutate(self, string):
        return self.mutation_cases.get(string, [])


all_mutations = [Upper, Letter, MonthMutate]
