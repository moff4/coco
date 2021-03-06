import abc
from abc import abstractmethod


class MutationType:
    Full = 1
    Word = 2
    Lexical = 3

    def __init__(self):
        pass


class Mutation(abc.ABC):
    @staticmethod
    @abstractmethod
    def mutate(string):
        pass


class Upper(Mutation):
    type = MutationType.Full

    @staticmethod
    def mutate(string):
        def __magic__bool__(obj):
            obj.value = not obj.value
            return obj.value

        flag = type(
            'MaGiC',
            (),
            {
                'value': False,
                '__bool__': __magic__bool__,
            }
        )()
        return [
            string.upper(),
            ''.join(string[0].upper() + string[1:])
        ] + [
            ''.join(
                [
                    letter if flag else letter.upper()
                    for letter in string
                    if letter.isalpha()
                ]
            )
        ]


class Letter(Mutation):
    type = MutationType.Word

    @staticmethod
    def sub_mutate(results, az, i=0):
        results.add(''.join(az))
        if i >= len(az):
            return results
        elif az[i].lower() == 's':
            bz = list(az)
            bz[i] = '$'
            return results.union(
                Letter.sub_mutate(results, bz, i + 1).union(
                    Letter.sub_mutate(results, az, i + 1)
                )
            )
        elif az[i].lower() == 'a':
            bz = list(az)
            bz[i] = '@'
            return results.union(
                Letter.sub_mutate(results, bz, i + 1).union(
                    Letter.sub_mutate(results, az, i + 1)
                )
            )
        else:
            return Letter.sub_mutate(results, az, i + 1)

    def mutate(string):
        p = Letter.sub_mutate(set(), [i for i in string])
        print(p)
        return p


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

    @staticmethod
    def mutate(string):
        return MonthMutate.mutation_cases.get(string, [])


all_mutations = [Upper, Letter, MonthMutate]
