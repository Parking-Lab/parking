'''
Saahil, James

Student Class
    Functionality:
       Hold information about each student's parking history and information (type of car, strikes, etc.)
       Generate score based on weights
       
       


This class holds information for the student object
'''

import json
from data import Data

class Student:

    def __init__(self,row,day,name,distance,car):

        self.score = 0
        #day of the week that this program is being run for
        self.day = day
        #self.form_sheet = form_sheet
        #self.row = self.form_sheet.getRow(row,'form_sheet.smth')
        self.name = name
        self.car = car
        self.distance = distance
        self.crash = crash
        self.strike = strike
        
        
        #critical need for days of the week
        self.mon_crit = self.row[3]
        self.tue_crit = self.row[4]
        self.wed_crit = self.row[5]
        self.thur_crit = self.row[6]
        self.fri_crit = self.row[7]
    
        self.sports = self.row[8]    
        self.carpoolUnder = self.row[9]
        self.carpoolSenior = self.row[10]

        #first period and last period free
        self.fpFree = self.row[11]
        self.lpFree = self.row[12]

        #boolean
        self.parallel = self.row[13]
        
       

        #critical need for days of the week
        '''self.mon_crit = 0
        self.tue_crit = 1
        self.wed_crit = 0
        self.thur_crit = 0
        self.fri_crit = 1
        self.sports = 1
        self.carpoolUnder = 1
        self.carpoolSenior = 1

        #first period and last period free

        self.fpFree = 1
        self.lpFree = 0

        #boolean

        self.parallel = 0'''

        #the amount of days it has been since the student has been able to park on campus - adjust score based on this variable in generateScore()

        self.spot_since = 0
        self.zone = ''

        
        #WEIGHTS
        #self.weight_sheet = weight_sheet
       
        #has to retrieve the second column from the weights sheet
        #self.weight_column = self.weight_sheet.getColumn(2,'weight_sheet.smth')

        self.carpoolUnder_weight = self.weight_column[2]
        self.carpoolSenior_weight = self.weight_column[3]
        self.fpfree_weight = self.weight_column[4]
        self.lpfree_weight = self.weight_column[5]

        self.sports_weight = self.weight_column[6]
        self.crit_weight = self.weight_column[7]
       
        self.commute_weight = self.weight_column[8]
        self.strike_weight = self.weight_column[9]
        self.crash_weight = self.weight_column[10]
        """ self.carpoolUnder_weight = 1.25
        self.carpoolSenior_weight = 3.0
        self.fpfree_weight = 16
        self.lpfree_weight = 8
        self.sports_weight = 10
        self.crit_weight = 40
        self.commute_weight = 1.2
        self.strike_weight = -20
        self.crash_weight = -500"""

    def calcDistance(self,score):
        addition = self.distance * self.commute_weight
        scoring = score + addition
        return scoring
    
    def strike_crash(self, score, strike, crash):
        self.wstrike = strike * self.strike_weight
        self.wcrash = crash * self.crash_weight
        scorewstrikes = score + self.wstrike + self.wcrash
        return scorewstrikes
    
    def generateScore(self, day):
        """uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone
        might use private methods to isolate that calculation of each category's weight
        To be written by Nambita and Aditya"""
        if day == 'Monday':
           crit = self.mon_crit
        if day == 'Tuesday':
           crit = self.tue_crit
        if day == 'Wednesday':
           crit = self.wed_crit
        if day == 'Thursday':
           crit = self.thur_crit
        if day == 'Friday':
           crit = self.fri_crit

        student_listing = [self.fpFree,self.lpFree,self.sports,crit,self.strike, self.crash] 
        student_weighting = [self.fpfree_weight,self.lpfree_weight,self.sports_weight, self.crit_weight,self.strike_weight, self.crash_weight] 

        scorelist = []

        for i in range(len(student_listing)):
            num = student_listing[i] * student_weighting[i]
            scorelist.append(num)
        score = sum(scorelist)
            
       
        if self.carpoolUnder == True:
           score = score + (self.carpoolUnder*self.carpoolUnder_weight)
        if self.carpoolSenior == True:
           score = score + (self.carpoolUnder*self.carpoolSenior_weight)
        print(score)
        scoring = self.calcDistance(score)
        print(scoring)
        self.strike = 1
        scorewstrikes = self.strike_crash(scoring, self.strike, self.crash)
        print(scorewstrikes)

    @staticmethod
    def distScore(zipcode: int) -> float:
        """gets the score for a given zip code.

        Args:
            zipcode (int): the zip code to get the score for

        Raises:
            KeyError: if the zipcode is invalid
            
        Returns:
            float: the resulting score, based on the l1 distance to 94010 (school)
        """
        return Student.DISTANCES[zipcode]*1.5

def main():
    student = Student(0,'Monday',2,2)
    student.generateScore()

    sheet_length = len(student.data)
    print(sheet_length)

    student3 = Student(2,'Monday',2,2)
    student3.generateScore()
    
if __name__ == '__main__': main()
