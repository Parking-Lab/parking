'''
Author: Alison

Weekly Info Class (WeeklyInfo):
    Description: accesses information pertaining to student's weekly info from Google Sheets
    Main Functionality: Organizes and outputs information from the weekly info Google Form (weekly form)
    NOTE: Do not use this class directly. It is implemented in the Data class
'''

import gspread

class WeeklyInfo():
    def __init__(self):
        """Creates a new class that represents the base info sheet
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")
        self.wks = self.sh.worksheet("WeeklyInfo")

        self.wks.sort((2, 'asc'))

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
        num = 0
        # print(len(self.allInfo))
        while row < len(self.allInfo):
            user = self.allInfo[row][1]
            time = self.allInfo[row][0]
            if user in usersDict: # previously seen 
                # print(user)
                if time > usersDict[user][0]: # current time is more than previous row (we want current time!)
                    self.allInfo.pop(usersDict[user][1]) # pop that row
                    # print("row popped",usersDict[user][1], " cur row:", row) # the row
                    usersDict[user] = [time, row]
                else: 
                    self.allInfo.pop(row) # pop current row because time is more than previous row
                    # print("row popped",row, " cur row:", usersDict[user][1]) # the row

                num+=1
            else:
                usersDict[user] = [time, row] # first time seen, keep on going
                row += 1
        # print("num popped:", num)

    def generateDict(self):
        """Generates the dictionary
        """
        self.infoDict = {} # based off of email
        for row in self.allInfo:
            self.infoDict[row[1].lower()] = row[2:] 

    def getUserInfo(self, email:'str') -> list:
        """Gets user's base info given name (accesses dictionary)

        Args:
            email (email): student's email

        Returns:
            list: all info for queried user (columns C-H)
        """
        email = email.lower()
        return self.infoDict[email]


    def getKey(self) -> list:
        """Gets the key (first row)

        Returns:
            list: the first row of the worksheet
        """
        return self.key

    def getAllInfo(self) -> list[list]:
        """Gets all info

        Returns:
            list[list]: all values
        """
        return self.allInfo
    
    def userInfoFound(self, email:'str') -> bool:
        """Returns if student's base info is found

        Args:
            email (str): student's email

        Returns:
            bool: true if found, false if not
        """
        email = email.lower()
        return email in self.infoDict

    def userEligible(self, email:'str') -> bool:
        """Returns student's eligibility for driving

        Args:
            email (str): email

        Returns:
            bool: true if user can drive
        """
        email = email.lower()
        return self.infoDict[email][0] == 'Yes'
        

    
def main():
    weeklyInfo = WeeklyInfo()
    # weeklyInfo.clearSheet(True)
    # weeklyInfo.removeDuplicates()
    # weeklyInfo.updateSheet()
    # print(weeklyInfo.getUserInfo("alisonsoong@gmail.com"))
    # print(weeklyInfo.getKey())



if __name__ == '__main__': main()
