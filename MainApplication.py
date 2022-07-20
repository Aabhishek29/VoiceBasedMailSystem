
import tkinter
from LoginWindow import LoginWindow
from Utils import Utility
from MailWindow import MailWindow


def start():
    root = tkinter.Tk()
    util = Utility()
    win = LoginWindow(root,util)
    win.startLoginWindow()
    print("before main")
    root.mainloop()
    root.quit()
    root = tkinter.Tk()
    win = MailWindow(root)
    print("after main")
    root.mainloop()



if __name__ == "__main__":
    start()