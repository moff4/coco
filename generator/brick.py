import abc

from generator.mutation import all_mutations, MutationType, Letter, MonthMutate


class Brick(abc.ABC):
    string = ""
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
    mutations = [Letter]

    def __init__(self, string):
        self.validate(string)
        super(Word, self).__init__(string)

    @staticmethod
    def validate(string):
        assert string.isalpha()


class NickName(Brick):
    mutations = [Letter]

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
        day = int(string)
        assert 1 <= day <= 31


class Month(Brick):
    mutations = [MonthMutate]
    def __init__(self, string):
        self.validate(string)
        super(Month, self).__init__(string)

    @staticmethod
    def validate(string):
        month = int(string)
        assert 1 <= month <= 12


class Year(Brick):
    def __init__(self, string):
        self.validate(string)
        super(Year, self).__init__(string)

    @staticmethod
    def validate(string):
        year = int(string)
        assert 1000 <= year <= 3000


class Date:
    day = None
    month = None
    year = None

    def __init__(self, day=None, month=None, year=None, string=None, delimiter="-"):
        if day:
            assert isinstance(day, Day)
            self.day = day
        if month:
            assert isinstance(month, Month)
            self.month = month
        if year:
            assert isinstance(year, Year)
            self.year = year
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
        mutations = []
        mutations.extend(self.day.mutate())
        mutations.extend(self.month.mutate())
        mutations.extend(self.year.mutate())
        return mutations

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
