#!/usr/bin/env python3

from tkinter import Tk
from interface import APP
from interface.saver import Saver
from generator.passwords import GeneratePassword


def main():
    root = Tk()
    APP(root)
    root.mainloop()
    try:
        root.destroy()
    except Exception:
        pass


if __name__ == '__main__':
    main()
    saver = Saver('results.txt')
    #Todo: put info here. Fill info structure in GeneratePassword. The example is present.
    info = {}
    generator = GeneratePassword(info)
    for pswd in generator.pswd():
        saver.output(pswd)
