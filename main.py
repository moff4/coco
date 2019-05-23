#!/usr/bin/env python3

from tkinter import Tk
from interface import APP


def main():
    """
        Application for generation simple relevante passwords depends on known information about user
    """
    root = Tk()
    APP(root)
    root.mainloop()
    try:
        root.destroy()
    except Exception:
        pass


if __name__ == '__main__':
    main()
