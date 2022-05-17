'''
Alison

Data class to be used by rest of program

Encapsulation goes brr
'''

from baseInfo import BaseInfo
from weeklyInfo import WeeklyInfo 

class Data:
    def __init__(self):
        self.baseInfo = BaseInfo()
        self.weeklyInfo = WeeklyInfo()
    
    # make this as nice as possible :)

