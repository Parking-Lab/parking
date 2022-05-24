'''
Author: Alison

Strikes Info Class (StrikesInfo):
    Description: accesses information pertaining to student's strike history from Google Sheets
    Main Functionality: Organizes and outputs information from a Google Sheet
    NOTE: Do not use this class directly. It is implemented in the Data class
'''

import gspread

class StrikesInfo():
    def __init__(self):
        """Creates a new class that represents the base info sheet
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")
        self.wks = self.sh.worksheet("Students")
        self.allInfo = self.wks.get_all_values() # NOTE: QUOTA

        self.numRows = len(self.allInfo)
        self.key = self.allInfo[0] # first row (zero indexed) is the key
        self.allInfo.pop(0)

        # print(self.allInfo)
        # print(self.key)

        self.generateDict() # generates a dictionary

    def generateDict(self):
        """Generates the dictionary
        """
        self.infoDict = {} # based off of email
        for row in self.allInfo:
            self.infoDict[row[0].lower()] = row[1:] 

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
    
    def userStrikeHistory(self, email:'str') -> int:
        """Returns if student's strike history

        Args:
            email (str): student's email

        Returns:
            int: number of strikes
        """
        email = email.lower()
        if self.userInfoFound(email):
            return int(self.infoDict[email][2])
        else:
            print("Warning: Student not found!", email)
            return 0

    
def main():
    strikesInfo = StrikesInfo()
    # print(strikesInfo.userStrikeHistory("alisonsoong@gmail.com"))



if __name__ == '__main__': main()
