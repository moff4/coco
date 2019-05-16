from snc import FacebookAPI, VKAPI
from brick import Word, Date, NickName, Name


class GeneratePassword():
    saver = open("res","w")
    exclude = ""
    info = {}

    def __init__(self, info):
        self.info = info

    def pswd(self):
        for key, var in self.info:
            self.saver.write(str(var))
            if key == "date":
                brick = Date(var)
            elif key == "nick":
                brick = NickName(var)
            elif key == "name":
                brick = Name(var)
            else:
                brick = Word(var)
            