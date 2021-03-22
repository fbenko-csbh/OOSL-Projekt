from tkinter.constants import DISABLED
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import READABLE, ttk


class Form(tk.Frame):
    """
    Form class used to take user input 

    ...

    Attributes
    ----------
    labels : dictionary
        to store labels
    calendars : dictionary
        to store calendars
    entries : dictionary
        to store entries
    buttons : dictionary
        to store buttons
    comboboxes : dictionary
        to store comboboxes

    Methods
    -------
    create_view(transaction_type)
        to initialise the creation of the view elements
    create_calendar(frame, name, row, column, textvar)
        to create the calendar element 
    create_label(frame, text, row, column, padx=0, pady=0)
        to create the label elements 
    create_entry(frame, label, row, column)
        to create the entry elements 
    create_button(frame, name, row, column, padx=0, pady=0)
        to create the button elements 
    create_combobox(frame, label, values, row, column, padx=0, pady=0)
        to create the button elements 
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

        self.labels = {}
        self.calendars = {}
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.datevar = tk.StringVar()


    def create_view(self, transaction_type):
        """to initialise the creation of the view elements

        Parameters
        ----------
        transaction_type : list 
            types of transactions
        """

        self.ff = ttk.Frame(self, padding=40)
        self.ff.pack()
        self.bf = ttk.Frame(self)
        self.bf.pack()
        self.create_calendar(self.ff, "Datum", row=1, column=1, textvar=self.datevar)
        self.create_entry(self.ff, "Name", row=2, column=1)
        self.create_entry(self.ff, "Preis", row=3, column=1)
        self.create_combobox(self.ff, "Typ", row=4, column=1, values=transaction_type)
        self.create_button(self.bf, "Neu", row=5, column=0, padx=10)
        self.create_button(self.bf, "Aendern", row=5, column=1, padx=10)
        self.create_button(self.bf, "Loeschen", row=5, column=2, padx=10)


    def create_calendar(self, frame, name, row, column, textvar):
        """to create the calendar element 

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        name : str
            name for the element
        row : int
            input for grid manager
        column : int
            input for grid manager
        """

        label_frame = tk.LabelFrame(frame, text=name)
        self.calendars[name] = DateEntry(label_frame,
                            width=20, background='darkblue', foreground='white', 
                            borderwidth=2, year=2021, 
                            date_pattern='dd.mm.y', locale='de_DE', textvariable=textvar)
        self.calendars[name].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky='nsew')
    
    def create_label(self, frame, text, row, column, padx=0, pady=0):
        """to create the label elements 

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        text : str
            text for the element
        row : int
            input for grid manager
        column : int
            input for grid manager
        padx : int
            input for grid manager
        pady : int
            input for grid manager
        """

        self.labels[text] = ttk.Label(frame, text=text)
        self.labels[text].grid(row=row, column=column, padx=padx, pady=pady)

    def create_entry(self, frame, label, row, column):
        """to create the entry elements 

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        label : str
            label for the element
        row : int
            input for grid manager
        column : int
            input for grid manager
        """

        label_frame = tk.LabelFrame(frame, text=label)
        self.entries[label] = tk.Entry(label_frame)
        self.entries[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky='nsew')

    def create_button(self, frame, name, row, column, padx=0, pady=0):
        """to create the button elements 

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        label : str
            label for the element
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

    def create_combobox(self, frame, label, values, row, column, padx=0, pady=0):
        """to create the button elements 

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        label : str
            label for the element
        values : str
            values for the element
        row : int
            input for grid manager
        column : int
            input for grid manager
        padx : int
            input for grid manager
        pady : int
            input for grid manager
        """

        label_frame = tk.LabelFrame(frame, text=label)
        self.comboboxes[label] = ttk.Combobox(label_frame, values=values, state='readonly')
        self.comboboxes[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, padx=padx, pady=pady, sticky='nsew')
         
