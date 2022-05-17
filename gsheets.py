'''
Alison

Google Sheets Class (GSheet):
    Main Functionality:
        Get and set values on Google Sheet
        Provide information for sorting classes
        Maintain and format Google Sheet
    NOTE 1: Google Sheets API has limits to usage. Must keep under 60 read and 60 write requests
    NOTE 2: To get around NOTE 1, only read entire sheet once and write to a file. Sort, edit, read, do whatever. 
            Then at the very end, update the Google Sheet. lol...

Notes:
- more functionality such as formatting can be added later once we have an idea of what the sheet will look like
- worksheets are different from the larger Google Sheet: 
    wks = individual sheets, 
    GSheet = the Google Sheet that holds individual sheets

'''

import gspread

class GSheet():
    def __init__(self, sa, name, wks=None):
        """
        Creates a GSheet class

        Args:
            sa (gspread client): the service account, credentials for accessing Google Sheets API
            name (str): name of Google Sheet that the GSheet represents
        
        Raises:
            AssertionError: raises an error if sheet does not exist
        """
        self.sa = sa #service account
        self.sh = self.sa.open(name)
        if (wks == None):
            self.createWorksheet(wks)
        else: self.wks = self.sh.worksheet(wks)
        

    def getCell(self, row, col):
        """Returns the value of a sheet 

        Args:
            row (int): cell's row
            col (int): cell's column

        Raises:
            AssertionError: raises an error if cell does not exist
        """
        try:
            coord = self.getCoord(row, col)
            return self.wks.get_values(coord)[0][0]
        except:
            print("getCell Error: Not a valid cell")
            return []

    def setCell(self, row, col, value):
        """Changes a cell's value given row, col, and new value

        Args:
            row (int): cell's row
            col (int): cell's column
            value (str): new value for cell

        Raises:
            AssertionError: raises an error if cell does not exist
        """
        try:
            self.wks.update_cell(row, col, value)
        except:
            print("setCell Error: Not a valid cell")

    
    def getRow(self, row):
        """Gets a row from the sheet and returns its values as a list

        Args:
            row (int): row to be returned

        Raises:
            AssertionError: raises an error if row does not exist

        Returns:
            list of values
        """
        try:
            return self.wks.row_values(row)
        except:
            print("getRow Error: Not a valid row")
            return []
        

    def setRow(self, row, values):
        """Given a list, input the new values into an already existing row (OVERWRITES THE ROW)

        Args:
            row (int): row where the new values will be stored
            values (list): new values for list

        Raises:
            AssertionError: raises an error if row does not exist
        """
        try:
            # first delete the row
            self.deleteRow(row)
            # then create a new row
            self.createRow(row, values)
        except:
            print("setRow Error: Something went wrong")

    def createRow(self, row, values):
        """Given a list, input the new values into a NEW row

        Args:
            row (int): new row will be indexed here
            values (list): new values for list
        """
        try:
            self.wks.insert_row(values, row)
        except:
            print("createRow Error: Not a valid row")


    def deleteRow(self, row):
        """Deletes a row from a worksheet

        Args:
            row (int): row to be deleted
        """
        try:
            self.wks.delete_row(row)
        except:
            print("deleteRow Error: Not a valid row")

    def clearRow(self, row):
        """Clears a row of values

        Args:
            row (int): row to be cleared
        """
        try:
            self.wks.delete_row(row)
            self.wks.insert_row([], row)
        except:
            print("clearRow Error: Not a valid row")
    
    def deleteColumns(self, startCol, endCol=None):
        """Deletes columns from a worksheet

        Args:
            startCol (int): first column to be deleted
            endCol (int): last column to be deleted (inclusive)
        """
        try:
            if endCol == None: self.wks.delete_columns(startCol)
            else: self.wks.delete_columns(startCol, endCol)
        except:
            print("deleteColumns Error: Not a valid range")

    def clearWorksheet(self):
        """Clears the cells in a worksheet
        """
        self.wks.clear()

    def createWorksheet(self, wks):
        """Creates a worksheet (100x25 worksheet)

        Args:
            wks (str): creates worksheet with title wks
        """
        self.sh.add_worksheet(wks,100,25)

    def getCoord(self, row, col):
        """Generates a string of a cell's coordinate

        Args:
            row (int): row
            col (int): col
        """
        col = chr(ord('A') + (col-1))
        row = str(row)
        return col + row

    
    
        

    