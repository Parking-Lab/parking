'''
Author: Alison

Data Class (Data):
    Description: Data class to be used by rest of parking program. Few methods for all needs
    Main functionality: Brings together multiple sheets and provides an interface to handle all of them easily

Encapsulation goes brr

NOTE from Alison: 
- other than running the program, there are a few steps still needed by the person managing this program (so 12th grade presidents? idk I forgot who would be running this)
- on the weekly form, we may want to indicate for what week the weekly form is for (like dates or smth)
- after the program finishes, the WEEKLY form needs all of its responses cleared (I can't seem to find a way to do this programmatically)
    - (navigate to edit form, responses tab, three dots, delete all responses is the bottom most option)
    - this will prevent people from editing forms that the program can no longer see (currently, the 'cleaning up' part of the code completely gets rid of those earlier forms… so might as well encourage people to submit a new form after every week)
- it is completely okay if the base info form responses are accidentally deleted! It would just prevent people from editing their forms, but they can just submit a new form because our program cleans up the information by only keeping the most recent entries
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

    
    def getFormattedInfo(self) -> list[list]:
        """Gets all information in a formatted fashion (not ordered by name, but abides by set format in TRUE_WEIGHTS)

        Returns:
            list[list]: final, formatted data
        """
        return self.finalData
    
    def getKey(self) -> list:
        """Gets the key

        Returns:
            list: a list describing the order of the info outputted
        """
        return self.key

    def loadResults(self, newResults:list[list]):
        """Given an array of the new parking results, updates the Google sheet

        Args:
            newResults (list[list]): new parking results
        """
        self.resultsInfo.updateSheet(newResults) # that's it!

    def reset(self):
        """Resets sheets at the end of calculations (notably, clears the weekly sheet of data for the new week)
        """
        self.weeklyInfo.clearSheet(True)

        
def main():
    data = Data()
    # print(data.getKey())
    # print(data.getFormattedInfo())
    # values = [['hi', 'hi', 'hi', 'hi'], ['hello','hello','hello']]
    # data.loadResults(values)
    # data.reset()

if __name__ == '__main__': main()