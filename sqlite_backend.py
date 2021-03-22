import sqlite3
from sqlite3 import OperationalError, IntegrityError
import mvc_exceptions as mvc_exc

DB_NAME = 'myDB'


class DBConnection:
    """
    DBConnection class used to handle database queries

    ...

    Attributes
    ----------
    name : str
        database name
    conn : 
        database connection
    cursor : 
        database cursor

    Methods
    -------
    connect()
        to connect to the database
    create_table(table_name)
        create table
    insert_one(date, name, price, quantity, table_name)
        insert a record in the database
    select_all(table_name)
        select all records in the database
    delete_one(id, table_name)
        delete a record in the database
    update_one(id, date, name, price, quantity, table_name)
        update a record in the database
    """
    
    instance = None

    def __new__(cls, *args, **kwargs):
        """singleton class to deal with database

        """
        if cls.instance is None:
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, db_name=DB_NAME):
        """
        Parameters
        ----------
        db_name : str 
            name of database 
        """

        self.name = '{}.db'.format(db_name)
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        """to connect to the database

        """
        try:
            return sqlite3.connect(self.name)
        except sqlite3.Error as e:
            pass

    def __del__(self):
        """close connection

        """

        self.cursor.close()
        self.conn.close()

    def create_table(self, table_name):
        """create table

        Parameters
        ----------
        table_name : str
            name of the database table
            
        Raises
        ------
        OperationalError
        """

        sql = f'CREATE TABLE {table_name}( \
            rowid INTEGER PRIMARY KEY AUTOINCREMENT, \
            idate TEXT, \
            name TEXT, \
            price REAL, \
            type TEXT);'
        try:
            self.cursor.execute(sql)
        except OperationalError as e:
            print(e)

    def insert_one(self, date, name, price, quantity, table_name):
        """insert a record in the database

        Parameters
        ----------
        id : int
            ID
        date : str 
            Date input 
        name : str
            name input
        price : float
            price inpute 
        quality : str
            type of expenditure 
        table_name : str
            name of the database table

        Raises
        ------
        IntegrityError
        """
        
        sql = "INSERT INTO {} ('idate', 'name', 'price', 'type') VALUES (?, ?, ?, ?)"\
            .format(table_name)
        try:
            self.cursor.execute(sql, (date, name, price, quantity))
            self.conn.commit()
        except IntegrityError as e:
            print(e)

    def select_all(self, table_name):
        """select all records in the database

        Parameters
        ----------
        table_name : str
            name of the database table
        """
        
        sql = "SELECT * FROM {}".format(table_name)
        self.cursor = self.conn.execute(sql)
        results = self.cursor.fetchall()
        return results 

    def delete_one(self, id, table_name):
        """delete a record in the database

        Parameters
        ----------
        id : int
            ID
        date : str 
            Date input 
        name : str
            name input
        price : float
            price inpute 
        quality : str
            type of expenditure 
        table_name : str
            name of the database table

        Raises
        ------
        ItemNotStored 
            If no record is found
        """
        
        sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE rowid=? LIMIT 1)'\
            .format(table_name)
        sql_delete = "DELETE FROM {} WHERE rowid=?".format(table_name)
        self.cursor = self.conn.execute(sql_check, (id,))  
        result = self.cursor.fetchone()
        if result[0]:
            self.cursor.execute(sql_delete, (id,))  
            self.conn.commit()
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t delete "{}" because it\'s not stored in table "{}"'
                .format(id, table_name))

    def update_one(self, id, date, name, price, quantity, table_name):
        """update a record in the database

        Parameters
        ----------
        id : int
            ID
        date : str 
            Date input 
        name : str
            name input
        price : float
            price inpute 
        quality : str
            type of expenditure 
        table_name : str
            name of the database table

        Raises
        ------
        ItemNotStored 
            If no record is found
        """
        
        sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE rowid=? LIMIT 1)'\
            .format(table_name)
        sql_update = 'UPDATE {} SET idate=?, name=?, price=?, type=? WHERE rowid=?'\
            .format(table_name)
        self.cursor = self.conn.execute(sql_check, (id,))  # comma needed
        result = self.cursor.fetchone()
        if result[0]:
            self.cursor.execute(sql_update, (date, name, price, quantity, id))
            self.conn.commit()
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored in table "{}"'
                .format(name, table_name))

