#!/usr/bin/env python3

from tkinter import Tk
from interface import APP


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
