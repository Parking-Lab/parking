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
    def __init__(self, sa, name):
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
    
    def getRow(self, row, wks):
        """Gets a row from the sheet and returns its values as a list

        Args:
            row (int): row to be returned
            wks (str): specific worksheet

        Raises:
            AssertionError: raises an error if row does not exist

        Returns:
            list of values
        """

    def getCell(self, row, col, wks):
        """Returns the value of a sheet 

        Args:
            row (int): cell's row
            col (int): cell's column
            wks (str): specific worksheet

        Raises:
            AssertionError: raises an error if cell does not exist
        """

    def setCell(self, row, col, value, wks):
        """Changes a cell's value given row, col, and new value

        Args:
            row (int): cell's row
            col (int): cell's column
            value (str): new value for cell
            wks (str): specific worksheet

        Raises:
            AssertionError: raises an error if cell does not exist
        """

    def setRow(self, row, values, wks):
        """Given a list, input the new values into a row

        Args:
            row (int): row where the new values will be stored
            values (list): new values for list
            wks (str): specific worksheet

        Raises:
            AssertionError: raises an error if row does not exist
        """

    def deleteRow(self, row, wks):
        """Deletes a row from a worksheet

        Args:
            row (int): row to be cleared
            wks (str): specific worksheet
        """
    
    def deleteCol(self, col, wks):
        """Deletes a column from a worksheet

        Args:
            col (int): row to be cleared
            wks (str): specific worksheet
        """

    def clearWorksheet(self, wks):
        """Clears the cells in a worksheet

        Args:
            wks (str): specific worksheet
        """

    def createWorksheet(self, wks):
        """Creates a worksheet

        Args:
            wks (str): creates worksheet with title wks
        """

    
    
        

    