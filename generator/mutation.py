from abc import ABCMeta, abstractmethod


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
        mutations = []
        for letter in string.lower():
            if letter == "a":
                mutations.append(string.replace('a', "@"))
                mutations.append(string.replace('A', "@"))
                mutations.append(string.replace('A', "@").replace('a','@'))
            elif letter == "s":
                mutations.append(string.replace('s', "$"))
                mutations.append(string.replace('S', "$"))
                mutations.append(string.replace('s', "$").replace('S','$'))


class MonthMutate(Mutation):
    def __init__(self):
        super(Mutation, self).__init__(MutationType.Lexical)

    def mutate(self, string):
        mutations = []
        string = string.lower()
        if string == "01":
            mutations.append("Jan")
            mutations.append("1")
        elif string == "02":
            mutations.append("Feb")
            mutations.append("2")
        elif string == "03":
            mutations.append("March")
            mutations.append("Mart")
            mutations.append("3")
        elif string == "04":
            mutations.append("April")
            mutations.append("Aprl")
            mutations.append("4")
        elif string == "05":
            mutations.append("May")
            mutations.append("5")
        elif string == "06":
            mutations.append("June")
            mutations.append("6")
        elif string == "07":
            mutations.append("July")
            mutations.append("7")
        elif string == "08":
            mutations.append("Aug")
            mutations.append("8")
        elif string == "09":
            mutations.append("Sept")
            mutations.append("Sent")
            mutations.append("9")
        elif string == "10":
            mutations.append("Oct")
            mutations.append("October")
        elif string == "11":
            mutations.append("Nov")
            mutations.append("November")
        else:
            mutations.append("Dec")
            mutations.append("December")

all_mutations = [Upper, Letter, MonthMutate]
