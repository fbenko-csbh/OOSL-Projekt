from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk

class Nav(tk.Frame):
    """
    Nav class used to create the navigation

    ...

    Attributes
    ----------
    buttons : dictionary
        to store buttons

    Methods
    -------
    create_view():
        to initialise the creation of the view elements
    create_buttons(frame, row, column, columnspan, padx, pady)
        to create the view elements
    """
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        """
        Parameters
        ----------
        parent : tk.Frame 
            Parent frame for the Table class 
        controller : Controller instance 
            Controller class instance to handle logic 
        """

        self.buttons = {}

    def create_view(self):
        """to initialise the creation of the view elements

        """
        self.create_button(self, "Tabelle", row=0, column=0, padx=10, pady=5)
        self.create_button(self, "Formular", row=0, column=1, padx=10, pady=5)
        self.create_button(self, "Grafik", row=0, column=2, padx=10, pady=5)

    def create_button(self, frame, name, row, column, padx=0, pady=0):
        """to create the view elements

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        name : str
            name for element
        row : int
            input for grid manager
        column : int
            input for grid manager
        padx : int
            input for grid manager
        pady : int
            input for grid manager
        """

        self.buttons[name] = ttk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column, padx=padx, pady=pady)


