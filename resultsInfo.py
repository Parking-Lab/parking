'''

Alison

hi

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