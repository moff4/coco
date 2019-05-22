import abc

from generator.mutation import all_mutations, MutationType, Letter, MonthMutate


class Brick(abc.ABC):
    string = ''
    mutations = {}

    @abc.abstractmethod
    def __init__(self, string):
        self.string = string.lower()

    @staticmethod
    @abc.abstractmethod
    def validate(string):
        pass

    def mutate(self):
        for mutation in all_mutations:
            if mutation.type == MutationType.Full:
                yield from mutation.mutate(self.string)
            else:
                if mutation in self.mutations:
                    yield from mutation.mutate(self.string)


class Word(Brick):
    mutations = {Letter}

    def __init__(self, string):
        self.validate(string)
        super(Word, self).__init__(string)

    @staticmethod
    def validate(string):
        assert string.isalpha()


class NickName(Brick):
    mutations = {Letter}

    def __init__(self, string):
        self.validate(string)
        super(NickName, self).__init__(string)

    @staticmethod
    def validate(string):
        assert string.isalnum()


class Day(Brick):

    def __init__(self, string):
        self.validate(string)
        super(Day, self).__init__(string)

    @staticmethod
    def validate(string):
        assert 1 <= int(string) <= 31


class Month(Brick):
    mutations = {MonthMutate}

    def __init__(self, string):
        self.validate(string)
        super(Month, self).__init__(string)

    @staticmethod
    def validate(string):
        assert 1 <= int(string) <= 12


class Year(Brick):

    def __init__(self, string):
        self.validate(string)
        super(Year, self).__init__(string)

    @staticmethod
    def validate(string):
        assert 1000 <= int(string) <= 3000


class Date:
    day = None
    month = None
    year = None

    def __init__(self, string, delimiter='.'):
        if string:
            assert len(delimiter) == 1
            date = string.split(delimiter)
            i = 0
            try:
                day = Day(date[i])
                self.day = day
                i += 1
            except AssertionError:
                pass
            try:
                month = Month(date[i])
                self.month = month
                i += 1
            except AssertionError:
                pass
            try:
                year = Year(date[i])
                self.year = year
            except AssertionError:
                pass

    def mutate(self):
        return {
            j
            for i in {self.day, self.month, self.year}
            for j in i.mutate()
        }


class Name:
    name = []

    def __init__(self, string, delimiter=" "):
        for part in string.split(delimiter):
            try:
                name = Word(part)
                self.name.append(name)
            finally:
                pass

    def mutate(self):
        return (
            i
            for one_name in self.name
            if isinstance(one_name, Word)
            for i in one_name.mutate()
        )
