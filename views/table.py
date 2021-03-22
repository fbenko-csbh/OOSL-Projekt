import tkinter as tk
from tkinter import ttk


class Table(tk.Frame):
    """
    Table class used to display detailed view of database records 

    ...

    Methods
    -------
    create_view():
        to initialise the creation of the view elements
    create_table(frame, row, column, columnspan, padx, pady)
        to create the view elements
    update(transactions)
        to update the Treeview element
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

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
    
    def create_view(self):
        """to initialise the creation of the view elements

        """
        self.create_table(self, row=1, column=0, columnspan=3, padx=10)

    def create_table(self, frame, row, column, columnspan=0, padx=0, pady=0):
        """to create the view elements

        Parameters
        ----------
        frame : tk.Frame
            parent Object for the elements
        row : int
            input for grid manager
        column : int
            input for grid manager
        columnspan : int
            input for grid manager
        padx : int
            input for grid manager
        pady : int
            input for grid manager
        """
        self.trv = ttk.Treeview(frame,
                    columns=("count", "id", "idate", "name","price", "type"),
                    displaycolumns=("count", "idate", "name", "price", "type"),
                    height=("14"),
        )
        # Columns Format
        self.trv.column("#0", width=0, stretch=0)
        self.trv.column("count", width=30, minwidth=25)
        self.trv.column("idate", width=100, minwidth=20, anchor="center")
        self.trv.column("name", width=170, minwidth=100)
        self.trv.column("price", width=100, minwidth=40, anchor="e")
        self.trv.column("type", width=100, minwidth=100)
        # Columns Heading
        self.trv.heading("id", text="ID")
        self.trv.heading("count", text="Nr.")
        self.trv.heading("idate", text="Datum")
        self.trv.heading("name", text="Bezeichnung")
        self.trv.heading("price", text="Betrag")
        self.trv.heading("type", text="Typ")
        # place treeview widget
        self.trv.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky="nsew")
  
    def update(self, transactions):
        """to update the Treeview element

        Parameters
        ----------
        transactions : list with tuples
            list with transaction details (id, date, name, price, type) 
        """
        self.trv.delete(*self.trv.get_children())
        for i, value in enumerate(transactions):
            self.trv.insert('', 'end', values=(i+1, value[0], value[1], value[2], value[3], value[4]))

    
