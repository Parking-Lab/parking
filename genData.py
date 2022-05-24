''''
Author: Alison

Generate random data for testing purposes

NOTE: Run this file once to generate new info (note that it WILL NOT be cleaned up, so 
duplicate entries from the same person will still be there. Once a Datta object is created, process will be done :)
'''

import gspread
import random


class GenData():
    def __init__(self):
        """Creates a new class to generate random data
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")

        self.wWks = self.sh.worksheet("WeeklyInfo") # weekly
        self.wAllInfo = self.wWks.get_all_values() # NOTE: QUOTA

        self.wNumRows = len(self.wAllInfo)
        self.wKey = self.wAllInfo[0] # first row (zero indexed) is the key
        self.wAllInfo.pop(0)

        self.bWks = self.sh.worksheet("BaseInfo") # weekly
        self.bAllInfo = self.bWks.get_all_values() # NOTE: QUOTA

        self.bNumRows = len(self.bAllInfo)
        self.bKey = self.bAllInfo[0] # first row (zero indexed) is the key
        self.bAllInfo.pop(0)

        self.sWks = self.sh.worksheet("Students") # weekly
        self.sAllInfo = self.sWks.get_all_values() # NOTE: QUOTA

        self.sNumRows = len(self.sAllInfo)
        self.sKey = self.sAllInfo[0] # first row (zero indexed) is the key
        self.sAllInfo.pop(0)

    def clearWeeklySheet(self, resetInfo:'bool'=False):
        """Clears the sheet (excludes the key! Never clear the key, or the first row)
        """
        self.wWks.delete_rows(2,self.wNumRows)

        if resetInfo: 
            self.wAllInfo = []
    
    def clearBaseSheet(self, resetInfo:'bool'=False):
        """Clears the sheet (excludes the key! Never clear the key, or the first row)
        """
        self.bWks.delete_rows(2,self.bNumRows)

        if resetInfo: 
            self.bAllInfo = []
    
    def genWeeklyData(self, cap):
        """Generates new weekly data

        Args:
            cap (int): number of rows
        """
        self.clearWeeklySheet(True)
        sz = len(self.sAllInfo)-1
        newInfo = []
        for i in range(cap):
            newRow = []

            timestamp = "generated" + str(random.randint(0,5))
            newRow.append(timestamp)

            person = random.randint(0,sz)
            email = self.sAllInfo[person][0]
            newRow.append(email)

            qualify = 'Yes'
            newRow.append(qualify)

            val = random.random()
            if val < 0.3: # carpool
                carpool = 'Yes, I take one person'
            elif val < 0.6:
                carpool = 'Yes, I take multiple people'
            else: carpool = 'No'
            newRow.append(carpool)

            if random.random() < 0.3: # only one third of people actually carpool with seniors
                senior = 'Yes'
            else: senior = 'No'
            newRow.append(senior)

            critAccess = []
            if random.random() < 0.5: # critical access monday
                critAccess.append("Monday")
            if random.random() < 0.5: # critical access tuesday
                critAccess.append("Tuesday")
            if random.random() < 0.5: # critical access wednesday
                critAccess.append("Wednesday")
            if random.random() < 0.5: # critical access thursday
                critAccess.append("Thursday")
            if random.random() < 0.5: # critical access friday
                critAccess.append("Friday")
            newRow.append(", ".join(critAccess))

            newRow.append("critical access explanation")

            sports = []
            if random.random() < 0.5: # sports access monday
                sports.append("Monday")
            if random.random() < 0.5: # sports access tuesday
                sports.append("Tuesday")
            if random.random() < 0.5: # sports access wednesday
                sports.append("Wednesday")
            if random.random() < 0.5: # sports access thursday
                sports.append("Thursday")
            if random.random() < 0.5: # sports access friday
                sports.append("Friday")
            newRow.append(", ".join(sports))

            newRow.append("sports/ecs access explanation")

            newInfo.append(newRow)

        self.wWks.insert_rows(newInfo,2)
        # print(newInfo)


        print("generated new WEEKLY data :)")

    
    def genBaseData(self):
        """Generate base data for all 
        """
        self.clearBaseSheet(True)
        newInfo = []
        for row in self.sAllInfo:
            newRow = []

            timestamp = "generated"
            newRow.append(timestamp)

            email = row[0]
            newRow.append(email)

            if random.random() < 0.7: # more probability to be able to drive
                qualify = 'Yes'
            else: qualify = 'No'
            newRow.append(qualify)

            if random.random() < 0.2: # 2/10 people have first period free, idk
                firstFree = 'Yes'
            else: firstFree = 'No'
            newRow.append(firstFree)

            if random.random() < 0.2: # 2/10 people have last period free, idk
                lastFree = 'Yes'
            else: lastFree = 'No'
            newRow.append(lastFree)

            if random.random() < 0.3: # only one third of people can parallel park
                para = 'Yes'
            else: para = 'No'
            newRow.append(para)

            if random.random() < 0.3: # only one third of people have large cars
                size = 'Large'
            else: size = 'Small'
            newRow.append(size)

            # get zipcode
            n = random.random() 
            if n < 0.2: # just choose from these zipcodes
                zip = '94010' # Burlingame
            elif n < 0.4:
                zip = '94002' # Belmont
            elif n < 0.6:
                zip = '94025' # Menlo Park
            elif n < 0.8:
                zip = '94105' # San Francisco
            else: zip = '95014' # Los Altos
            newRow.append(zip)

            newInfo.append(newRow)

        self.bWks.insert_rows(newInfo,2)
        # print(newInfo)


        print("generated new BASE data :)")

def main():
    data = GenData()
    # COMMENT OUT THE BELOW ACCORDING TO WHAT YOU WANT TO SIMULATE!
    data.genWeeklyData(150)
    data.genBaseData()


if __name__ == '__main__': main()




