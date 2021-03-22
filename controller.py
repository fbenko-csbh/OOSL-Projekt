import datetime
import re

from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as tkmsg

from views.form import Form 
from views.table import Table
from views.graph import Graph
from views.nav import Nav


class tkinterApp(tk.Tk):
    """
    Controller class used to handle business logic

    ...

    Attributes
    ----------
    model : instance of Model-class 
        handles connection to database

    Methods
    -------
    show_frame(cont)
        lifts frame to front        
    add_transaction()
        gets user data to store in the database
    get_table_row()
        get item detail from table view und populate form 
    update_transaction()
        get item detail and save changes to database
    delete_transaction()
        get item detail and delete item
    validate(data)
        validate if price into is a number
    update_all()
        update views when chages occurred
    convert_price(input_price, input_type)
        convert only expenditures to negativ number
    update_pie_graph()
        calculate data and update pie view
    update_bar_graph()
        calculate data and update bar view
    """
     
    def __init__(self, model, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        """
        Parameters
        ----------
        model : instance of Model-class 
            handles connection to database
        frames : dictionary
            to organize views
        """

        self.model = model
        self.transactions = self.model.read_items()
        self.transaction_types = [
            "Gehalt",
            "Lebenshaltung",
            "Mobilität",
            "Sonstiges",
            "Telekommunikation",
            "Wohnen",
        ]
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(1, weight = 1)

        self.nav_bar = Nav(container, self)
        self.nav_bar.create_view()
        self.nav_bar.grid(row=0, column=0, sticky="new")
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting of the different page layouts
        for F in (Table, Form, Graph):
            frame = F(container, self)
            # initializing frames for views 
            self.frames[F] = frame 
            frame.grid(row=1, column=0, sticky="nsew")
        
        # View "Nav" initialise and configure
        self.nav_bar.buttons["Tabelle"].configure(command=lambda : self.show_frame(Table))
        self.nav_bar.buttons["Grafik"].configure(command=lambda : self.show_frame(Graph))
        self.nav_bar.buttons["Formular"].configure(command=lambda : self.show_frame(Form))
        
        # View "Form" initialise  and configure
        self.frames[Form].create_view(self.transaction_types)
        self.frames[Form].buttons["Neu"].configure(command=lambda : self.add_transaction())
        self.frames[Form].buttons["Aendern"].configure(command=lambda : self.update_transaction())
        self.frames[Form].buttons["Loeschen"].configure(command=lambda : self.delete_transaction())

        # View "Table" initialise and configure
        self.frames[Table].create_view()
        self.frames[Table].update(self.transactions)
        self.frames[Table].trv.bind('<Double 1>', lambda e: self.get_table_row())

        # View "Graph" initialise and configure
        self.frames[Graph].create_view()
        self.update_pie_graph()
        self.update_bar_graph()

        # show initial View
        self.show_frame(Table)
  
    def show_frame(self, cont):
        """to display the current frame passed as parameter

        Parameters
        ----------
        cont : View class
            tk.Frame to show on top 
        """
        
        frame = self.frames[cont]
        frame.tkraise()
    
    def add_transaction(self):
        """to add a new transaction to the database an display
        the updated list
        """
        input_date = self.frames[Form].calendars["Datum"].get_date()
        input_name = self.frames[Form].entries["Name"].get()
        input_price = self.frames[Form].entries["Preis"].get()
        input_type = self.frames[Form].comboboxes["Typ"].get()
        if not input_name or not input_price or not input_type:
            tkmsg.showerror(title="Eingabefehler", message=f'bitte alle Felder ausfüllen')
        elif not datetime.datetime.strptime(str(input_date), '%Y-%m-%d'):
            tkmsg.showerror(title="Eingabefehler", message=f'falsches Datumsformat bitte tt.mm.yyyy verwenden')
        elif not self.validate(input_price):
            tkmsg.showerror(title="Preiseingabe", message="bitte Dezimalzahlen mit Punkt eingeben")
            return
        else:
            input_price = self.convert_price(input_price,input_type)
            self.model.create_item(str(input_date), input_name, input_price, input_type)
            tkmsg.showinfo(title='Neue Transaktion', message=f'{input_name} vom Typ {input_type} mit {input_price} EUR wurde hinzugefügt')
        self.update_all()
        # clear form input-fields
        self.frames[Form].calendars["Datum"].delete(0, 'end')
        self.frames[Form].entries["Name"].delete(0, 'end')
        self.frames[Form].entries["Preis"].delete(0, 'end')
        self.frames[Form].comboboxes["Typ"].set('')

    def get_table_row(self):
        """get item detail from table view und populate form 

        """
        self.show_frame(Form)
        self.frames[Form].entries["Name"].delete(0, 'end')
        self.frames[Form].entries["Preis"].delete(0, 'end')

        item = self.frames[Table].trv.item(self.frames[Table].trv.focus())
        self.frames[Form].datevar.set(item['values'][2])
        self.frames[Form].entries["Name"].insert(0, item['values'][3])
        input_price = self.convert_price(item['values'][4], item['values'][5])
        self.frames[Form].entries["Preis"].insert(0, input_price)
        self.frames[Form].comboboxes["Typ"].set(item['values'][5])
        
    def update_transaction(self):
        """get item detail and save changes to database

        """
        item = self.frames[Table].trv.item(self.frames[Table].trv.focus())
        input_id = item['values'][1]
        input_date = self.frames[Form].calendars["Datum"].get_date()
        input_name = self.frames[Form].entries["Name"].get()
        input_price = self.frames[Form].entries["Preis"].get()
        input_type = self.frames[Form].comboboxes["Typ"].get()
        if not input_name or not input_price or not input_type:
            tkmsg.showerror(title="Eingabefehler", message=f'bitte alle Felder ausfüllen')
        elif not datetime.datetime.strptime(str(input_date), '%Y-%m-%d'):
            tkmsg.showerror(title="Eingabefehler", message=f'falsches Datumsformat bitte tt.mm.yyyy verwenden')
        elif not self.validate(input_price):
            tkmsg.showerror(title="Preiseingabe", message="bitte Dezimalzahlen mit Punkt eingeben")
            return
        else:
            if tkmsg.askokcancel(title="Aendern", message="Wirklich ändern?"):
                input_price = self.convert_price(input_price,input_type)
                self.model.update_item(input_id, input_date, input_name, 
                        input_price, input_type)
        self.update_all()
        self.show_frame(Table)

    def delete_transaction(self):
        """get item detail and delete item

        """
        item = self.frames[Table].trv.item(self.frames[Table].trv.focus())
        if tkmsg.askokcancel(title="Loeschen", message="Wirklich entfernen?"):
            self.model.delete_item(item['values'][1])
        self.update_all()
        self.show_frame(Table)
    
    def validate(self, data):
        """validate if price into is a number

        Parameters
        ----------
        data : str
            price to validate
        """
        match = re.compile('^\d*\.?\d?\d?$').match(data)
        if match is not None:
            return True            

    def update_all(self):
        """update views when chages occurred

        """
        self.transactions = self.model.read_items()
        self.frames[Table].update(self.transactions)
        self.update_pie_graph()
        self.update_bar_graph()

    def convert_price(self, input_price, input_type):
        """convert only expenditures to negativ number

        Parameters
        ----------
        input_price : str
            price to convert
        input_type : str
            type to check
        """
        for index, line in enumerate(self.transaction_types):
            if index > 0 and input_type==line:
                return float(input_price) * -1        
        return float(input_price)

    def update_pie_graph(self):
        """calculate data and update pie view

        """
        mylist = []
        for tt in self.transaction_types[1:]: # dismiss 'Gehalt' from list -> income not expenditure!
            sum_counter = 0
            for i in self.transactions:
                if tt == i[4]:# and tt != 'Gehalt':
                    sum_counter += i[3]
            if sum_counter < 0:
                mylist.append([tt, abs(sum_counter)])
        self.frames[Graph].draw_pie(mylist)
    
    def update_bar_graph(self):
        """calculate data and update bar view

        """
        mylist = []
        sum_total = 1
        sum_expenditure = 0
        sum_income = 0
        for ta in self.transactions:
            sum_total += abs(ta[3])
            if ta[3] < 0:
                sum_expenditure += ta[3]
            else:
                sum_income += ta[3]
        mylist.append(['Ausgaben', abs(sum_expenditure / sum_total)])
        mylist.append(['Einnahmen', sum_income / sum_total])
        self.frames[Graph].draw_bar(mylist)
