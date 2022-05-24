'''
Author: Alison

Results Info Class (ResultsInfo):
    Description: accesses the Google Sheet where the final results of the sorting program will be displayed 
    Main Functionality: Outputs information from the program onto the Google Sheet
    NOTE: Do not use this class directly. It is implemented in the Data class
'''

import gspread


class ResultsInfo:
    def __init__(self):
        """Creates a new class that represents the results sheet
        """
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Results")
        self.wks = self.sh.worksheet("ParkingResults")
        # print("results info constructor, to be created")

    def updateSheet(self, values:list[list]):
        """Updates sheet with new results. First clears the sheet then adds them

        Args:
            values (list[list]): new results
        """
        self.clearSheet()
        self.wks.insert_rows(values, 2)

    def clearSheet(self):
        """Clears the sheet of all rows, excluding the key
        """
        self.wks.delete_rows(2,self.wks.row_count-1)

def main():
    results = ResultsInfo()
    # values = [['hi', 'hi', 'hi', 'hi'], ['hello','hello','hello'], ['it works!!!']]
    # results.updateSheet(values)
    # results.clearSheet()

if __name__ == '__main__': main()