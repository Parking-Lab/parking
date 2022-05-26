'''
Author: Alison

Data Class (Data):
    Description: Data class to be used by rest of parking program. Few methods for all needs
    Main functionality: Brings together multiple sheets and provides an interface to handle all of them easily
'''

from baseInfo import BaseInfo
from weeklyInfo import WeeklyInfo 
from resultsInfo import ResultsInfo
from strikesInfo import StrikesInfo

class Data:
    def __init__(self):
        self.baseInfo = BaseInfo() # create the object, automatically gets info and formats it
        self.weeklyInfo = WeeklyInfo() # create the object, automatically gets info and formats it
        self.resultsInfo = ResultsInfo() # create the object...
        self.strikesInfo = StrikesInfo() # creates the object
        self.key = [
                        'Name',
                        'Car Size',
                        'Distance (zipcode)',
                        'Monday Critical Access',
                        'Tuesday Critical Access',
                        'Wednesday Critical Access',
                        'Thursday Critical Access',
                        'Friday Critical Access',
                        'Monday Sports/School Ecs',
                        'Tuesday Sports/School Ecs',
                        'Wednesday Sports/School Ecs',
                        'Thursday Sports/School Ecs',
                        'Friday Sports/School Ecs', 
                        'Carpool Multiple',
                        'Carpool Seniors',
                        'First Period Free',
                        'Last Period Free',
                        'Parallel Parking',
                        'Strike History'
                    ]
        self.finalData = []
        self._formatAllInfo()

        # at the end, delete everything on the weekly sheet

    def _formatAllInfo(self):
        """Formats all info
        """
        self.finalData = []
        for person in self.weeklyInfo.getAllInfo():
            formattedRow = []
            # ignore if not eligible to drive
            name = person[1]
            # print(name)
            if not self.baseInfo.userInfoFound(name): continue
            if not(person[2] or self.baseInfo.userEligible(name)): continue # if not eligible, don't include them
            
            # 'Name',
            formatName = name[:name.find('@')]
            formattedRow.append(formatName)

            # 'Car Size',
            if self.baseInfo.getCarSize(name): formattedRow.append(1)
            else: formattedRow.append(0)
            
            # 'Distance (time)', 
            zipcode = self.baseInfo.getAddress(name)
            formattedRow.append(zipcode)
            
            # 'Monday Critical Access',
            if 'Monday' in person[5]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Tuesday Critical Access',
            if 'Tuesday' in person[5]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Wednesday Critical Access',
            if 'Wednesday' in person[5]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Thursday Critical Access',
            if 'Thursday' in person[5]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Friday Critical Access',
            if 'Friday' in person[5]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Monday Sports/School Ecs',
            if 'Monday' in person[7]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Tuesday Sports/School Ecs',
            if 'Tuesday' in person[7]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Wednesday Sports/School Ecs',
            if 'Wednesday' in person[7]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Thursday Sports/School Ecs',
            if 'Thursday' in person[7]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Friday Sports/School Ecs', 
            if 'Friday' in person[7]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Carpool Multiple',
            if 'multiple' in person[3]: formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Carpool Seniors',
            if person[4] == 'Yes': formattedRow.append(1)
            else: formattedRow.append(0)

            # 'First Period Free',
            if self.baseInfo.getFirstPeriod(name): formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Last Period Free',
            if self.baseInfo.getLastPeriod(name): formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Parallel Parking',
            if self.baseInfo.getPara(name): formattedRow.append(1)
            else: formattedRow.append(0)

            # 'Strike History'
            formattedRow.append(self.strikesInfo.userStrikeHistory(name))

            self.finalData.append(formattedRow)

    
    def getFormattedInfo(self):
        """Gets all information in a formatted fashion (not ordered by name, but abides by set format in TRUE_WEIGHTS)

        Returns:
            list[list]: final, formatted data
        """
        return self.finalData
    
    def getKey(self):
        """Gets the key

        Returns:
            list: a list describing the order of the info outputted
        """
        return self.key

    def loadResults(self, newResults):
        """Given an array of the new parking results, updates the Google sheet

        Args:
            newResults (list[list]): new parking results
        """
        self.resultsInfo.updateSheet(newResults) # that's it!
        
def main():
    data = Data()
    # print(data.getKey())
    # print(data.getFormattedInfo())
    # values = [['hi', 'hi', 'hi', 'hi'], ['hello','hello','hello']]
    # data.loadResults(values)

if __name__ == '__main__': main()