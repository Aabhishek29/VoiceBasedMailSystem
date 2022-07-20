from threading import Thread
import threading
import tkinter
from tkinter import *
import os
import Colors
import re
from MailWindow import MailWindow
from Utils import Utility
import smtplib

class LoginWindow():
    def __init__(self , root , util) -> None:
        self.root = root
        self.util = util
        root.title("Login - VoiceBasedMailSystem - "+os.getcwd())
        root.geometry("1080x720")
        root.maxsize(1080,720)
        root.minsize(1080,720)
        self.e_state = 0
        self.p_state = 0
        self.emailId = StringVar()
        self.pswd = StringVar()

    def mainCanvas(self): 
        self.canvas1 = Canvas( self.root,background=Colors.color['themedark'])
        self.canvas1.pack(fill = "both", expand = True)
        self.canvas1.background =PhotoImage(file = "./assets/login_canvas_bg.png")
        self.canvas1.create_image( 0, 0, image = self.canvas1.background,anchor = "nw")


    def loginView(self):
    
        self.loginCan = self.canvas1
        Label(self.loginCan, text="Welcome !", fg=Colors.color['white'],background=Colors.color['themedark'] , font=('Times',40,'bold')).place(x=300,y=150)

        Label(self.loginCan, text="Email", fg=Colors.color['white'], background=Colors.color['themedark'],font=('Times',18,'bold')).place(x=350,y=280)
        framenamefield = Frame(self.loginCan)
        framenamefield.place(x = 350, y=320)
        Entry(framenamefield,textvariable=self.emailId,bd=0, width=40,font=('Times',16),bg=Colors.color['white']).pack(padx=5,pady=5)
        
        Label(self.loginCan, text="Password", fg=Colors.color['white'],background=Colors.color['themedark'], font=('Times',18,'bold')).place(x=350,y=390)
        framepassfield = Frame(self.loginCan)
        framepassfield.place( x = 350, y=430)
        Entry(framepassfield,show="*",textvariable=self.pswd,bd=0,  width=40,fg=Colors.color['black'],font=('Times',16),bg=Colors.color['white']).pack(padx=5,pady=5)

        framebtn = Frame(self.loginCan)
        framebtn.place(x= 480, y=550 )
        self.btn = Button(framebtn, text="Login", bg=Colors.color['primaryblue'], fg=Colors.color['white'],font=('Times',20),command=self.loginUser)
        self.btn.pack(ipadx=35,ipady=5,fill='both')

    def loginUser(self):
        userId = self.emailId.get()
        pswd = self.pswd.get()
        if not (self.checkEmail(userId) and self.checkpassword(pswd)):
            print("Bad Credentials Not Passed by ")
            return
        print(f"User id = {userId}")
        print(f"Password = {pswd}")

        if not self.authenticate(userId,pswd):
            Label(self.canvas1,text="wrong email/password",bg=Colors.color['themedark'],fg=Colors.color['red'],font=('Times',18)).place(x=440,y=500)
        print("Id and Password Authenticated")
        self.root.quit()
        win = MailWindow(tkinter.Tk())
        win.startActivity()        

    def checkEmail(self,mail) -> bool:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(not re.fullmatch(regex, mail)):
            self.p_state+=1
            if self.p_state == 1:
                Label(self.canvas1,text="please re-enter your email address",bg=Colors.color['themedark'],fg=Colors.color['red']).place(x=350,y=360)
            return False
        return True

    def checkpassword(self,pswd) -> bool:
        if not len(pswd) > 2:
            self.p_state+=1
            if self.p_state == 1:
                Label(self.canvas1,text="please re-enter your email address",bg=Colors.color['themedark'],fg=Colors.color['red']).place(x=350,y=470)
            return False
        return True

    def authenticate(self,mailId,pswd) -> bool:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        try:
            server.login(mailId,pswd)
        except Exception as e:
            return False
        server.close()
        return True

    def startLoginWindow(self):
        self.mainCanvas()
        self.loginView()


if __name__ == '__main__':
    root = tkinter.Tk()
    util = Utility()
    win = LoginWindow(root,util)

    win.startLoginWindow()

    root.mainloop()