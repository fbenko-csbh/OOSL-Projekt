from sqlite_backend import DBConnection


class SQLiteCRUD(object):
    """
    SQLiteCRUD class used as model to connect to database

    ...

    Methods
    -------
    create_item(date, name, price, quality)
        to save a item in the database
    read_items()
        read all items from database table
    update_item(id, date, name, price, quantity)
        update a item in the database
    delete_item(id)
        delete a item in the database
    """

    def __init__(self):
        self.table_name = 'myTransactions'
        self._connection = DBConnection('transactions')
        self._connection.create_table(self.table_name)


    def create_item(self, date, name, price, quality):
        """to save a item in the database

        Parameters
        ----------
        date : str 
            Date input 
        name : str
            name input
        price : float
            price inpute 
        quality : str
            type of expenditure 
        """
        
        self._connection.insert_one(
            date, name, price, quality, table_name=self.table_name)
        
    def read_items(self):
        """read all items from database table

        """
        return self._connection.select_all(
            table_name=self.table_name)

    def update_item(self, id, date, name, price, quantity):
        """update a item in the database

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
        """
        
        self._connection.update_one(
            id, date, name, price, quantity, table_name=self.table_name)


    def delete_item(self, id):
        """delete a item in the database

        Parameters
        ----------
        id : int
            ID
        """

        self._connection.delete_one(
            id, table_name=self.table_name)

