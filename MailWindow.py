import tkinter
from tkinter import *

class MailWindow():
    def __init__(self,root) -> None:
        self.root = root



if __name__ == '__main__':
    root = tkinter.Tk()
    win = MailWindow(root)
    root.mainloop()
