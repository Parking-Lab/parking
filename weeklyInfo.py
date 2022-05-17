'''
Alison

Weekly Info Class (WeeklyInfo):
    Main Functionality:
        Organizes and outputs information from the weekly info Google Form (weekly form)
'''

import gspread

class WeeklyInfo:
    def __init__(self):
        """Creates a new class that represents the base info sheet
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")
        self.wks = self.sh.worksheet("WeeklyInfo")
        self.allInfo = self.wks.get_all_values() # NOTE: QUOTA

        self.numRows = len(self.allInfo)
        self.key = self.allInfo[0] # first row (zero indexed) is the key
        self.allInfo.pop(0)

        # print(self.allInfo)
        # print(self.key)

        self.removeDuplicates() # remove duplicates
        self.generateDict() # generates a dictionary
        self.updateSheet() # updates sheet after duplicates are removed

    def clearSheet(self, resetInfo:'bool'=False):
        """Clears the sheet (excludes the key! Never clear the key, or the first row)
        """
        self.wks.delete_rows(2,self.numRows)
        if resetInfo: self.allInfo = []

    def updateSheet(self):
        """Updates the sheet with all info
        NOTE: QUOTA
        NOTE: inserts the info into the sheet, but subsequent form entries are put at the top...
        """
        self.clearSheet()
        self.wks.insert_rows(self.allInfo,2)

    def removeDuplicates(self):
        """Removes duplicate form entries
        """
        usersDict = {} # key : value where value is [time, row]
        row = 0
        while row < len(self.allInfo):
            user = self.allInfo[row][1]
            time = self.allInfo[row][0]
            if user in usersDict: # previously seen 
                if time > usersDict[user][0]: # current time is more than previous row (we want current time!)
                    self.allInfo.pop(usersDict[user][1]) # pop that row
                    usersDict[user] = [time, row]
                else: 
                    self.allInfo.pop(row) # pop current row because time is more than previous row
                row -= 1 # move back one
            else: usersDict[user] = [time, row] # first time seen, keep on going
            row += 1

    def generateDict(self):
        """Generates the dictionary
        """
        self.infoDict = {} # based off of email
        for row in self.allInfo:
            self.infoDict[row[1]] = row[2:] 

    def getUserInfo(self, email:'str') -> list:
        """Gets user's base info given name (accesses dictionary)

        Args:
            email (email): _description_

        Returns:
            list: all info for queried user (columns C-H)
        """
        return self.infoDict[email]


    def getKey(self) -> list:
        """Gets the key (first row)

        Returns:
            list: the first row of the worksheet
        """
        return self.key
        

    
def main():
    weeklyInfo = WeeklyInfo()
    # baseInfo.clearSheet(True)
    # baseInfo.removeDuplicates()
    # baseInfo.updateSheet()
    # print(baseInfo.getUserInfo("alisonsoong@gmail.com"))
    # print(baseInfo.getKey())



if __name__ == '__main__': main()
