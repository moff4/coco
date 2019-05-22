import abc
from abc import abstractmethod
from functools import reduce


class MutationType:
    Full = 1
    Word = 2
    Lexical = 3

    def __init__(self):
        pass


class Mutation(abc.ABC):
    @abstractmethod
    def mutate(self, string):
        pass


class Upper(Mutation):
    type = MutationType.Full

    def mutate(self, string):
        mutations = []
        mutations.append(string.upper())
        mutations.append(string[0].upper()+string[1:])
        result = ""
        flag = True
        for letter in string:
            if letter.isalpha():
                flag = not flag
                if flag:
                    result += letter.upper()
                else:
                    result += letter
        mutations.append(result)
        return mutations


class Letter(Mutation):
    type = MutationType.Word

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
    type = MutationType.Lexical
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

    def mutate(self, string):
        return self.mutation_cases.get(string, [])


all_mutations = [Upper, Letter, MonthMutate]
