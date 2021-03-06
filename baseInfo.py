'''
Author: Alison

Base Info Class (BaseInfo):
    Description: accesses information pertaining to student's base info from Google Sheets
    Main Functionality: Organizes and outputs information from the base info Google Form (yearly form)
    NOTE: Do not use this class directly. It is implemented in the Data class
'''

import gspread

class BaseInfo:
    def __init__(self):
        """Creates a new class that represents the base info sheet
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")
        self.wks = self.sh.worksheet("BaseInfo")
        
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

    def dummy(self):
        self.allInfo = [['hi','hi','hi'],['pls work'],['ahhhhhh'],['lol', 'ahh']]
    
    def clearSheet(self, resetInfo=False):
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
            self.infoDict[row[1].lower()] = row[2:] # make sure usernames are all lowercase 

    def getUserInfo(self, email):
        """Gets user's base info given name (accesses dictionary)

        Args:
            email (email): _description_

        Returns:
            list: all info for queried user (columns C-H)
        """
        email = email.lower()
        return self.infoDict[email]


    def getKey(self):
        """Gets the key (first row)

        Returns:
            list: the first row of the worksheet
        """
        return self.key

    def userInfoFound(self, email):
        """Returns if student's base info is found

        Args:
            email (str): _description_

        Returns:
            bool: true if found, false if not
        """
        email = email.lower()
        return email in self.infoDict

    def userEligible(self, email):
        """Returns student's eligibility for driving

        Args:
            email (str): email

        Returns:
            bool: true if user can drive
        """
        email = email.lower()
        return self.infoDict[email][0] == 'Yes'
    
    def getCarSize(self, email):
        """Returns student's car size (true if Large, false if small)

        Args:
            email (str): email

        Returns:
            bool: true if user has a large car
        """
        email = email.lower()
        return self.infoDict[email][4] == 'Large'
    
    def getAddress(self, email):
        """Returns student's zip code

        Args:
            email (str): email

        Returns:
            int: the zip code
        """
        email = email.lower()
        return int(self.infoDict[email][5])
    
    def getPara(self, email):
        """Returns student's ability to parallel park

        Args:
            email (str): email

        Returns:
            bool: True if can park
        """
        email = email.lower()
        return self.infoDict[email][3] == 'Yes'

    def getFirstPeriod(self, email):
        """Returns student's first period status

        Args:
            email (str): email

        Returns:
            bool: True if first period free
        """
        email = email.lower()
        return self.infoDict[email][1] == 'Yes'

    def getLastPeriod(self, email):
        """Returns student's last period status

        Args:
            email (str): email

        Returns:
            bool: True if last period free
        """
        email = email.lower()
        return self.infoDict[email][2] == 'Yes'

        

    
def main():
    baseInfo = BaseInfo()
    # baseInfo.clearSheet(True)
    # baseInfo.removeDuplicates()
    # baseInfo.updateSheet()
    # print(baseInfo.getUserInfo("alisonsoong@gmail.com"))
    # print(baseInfo.getKey())
    # print(baseInfo.userEligible('alisonsoong@gmail.com'))



if __name__ == '__main__': main()