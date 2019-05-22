from generator.brick import Word, Date, NickName, Name


class GeneratePassword():
    exclude = ""
    info = {}

    def __init__(self, info):
        self.info = info

    def pswd(self):
        for key, var in self.info.items():
            try:
                if key == "date":
                    brick = Date(var)
                elif key == "nick":
                    brick = NickName(var)
                elif key == "name":
                    brick = Name(var)
                else:
                    brick = Word(var)
                for mutation in brick.mutate():
                    yield mutation
            except (AssertionError, AttributeError):
                pass
            except Exception as e:
                raise e
