'''
Alison

Data class to be used by rest of program

Encapsulation goes brr


NOTE: 
- other than running the program, there are a few steps still needed by the person managing this program (so 12th grade presidents? idk I forgot who would be running this)
- on the weekly form, we may want to indicate for what week the weekly form is for (like dates or smth)
- after the program finishes, the WEEKLY form needs all of its responses cleared (I can’t seem to find a way to do this programmatically)
    - (navigate to edit form, responses tab, three dots, delete all responses is the bottom most option)
    - this will prevent people from editing forms that the program can no longer see (currently, the ‘cleaning up’ part of the code completely gets rid of those earlier forms… so might as well encourage people to submit a new form after every week)
- it is completely okay if the base info form responses are accidentally deleted! It would just prevent people from editing their forms, but they can just submit a new form because our program cleans up the information by only keeping the most recent entries
'''

from baseInfo import BaseInfo
from weeklyInfo import WeeklyInfo 

class Data:
    def __init__(self):
        self.baseInfo = BaseInfo()
        self.weeklyInfo = WeeklyInfo()
    
    # make this as nice as possible :)

