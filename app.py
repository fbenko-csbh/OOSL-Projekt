import sys

from tkinter import *

from controller import tkinterApp
from model import SQLiteCRUD


class Application():
    """
    Application class used to start the tkinter App

    """
    def __init__(self, *args, **kwargs):

        app = tkinterApp(SQLiteCRUD())
        app.title("FiN Planer")
        app.geometry("1000x450+100+100") 
        # select Icon File for Windows or Linux Machine
        if (sys.platform.startswith('win')):
            app.iconbitmap('icons/icon.ico')
        else:
            logo = PhotoImage(file = 'icons/icon.gif')
            app.call('wm', 'iconphoto', app._w, logo)
        app.mainloop()


if __name__ == '__main__':
    Application()


