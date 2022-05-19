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

    #! this code runs at *definition*, so basically when this file is imported.
    with open('distances.json', 'r') as f:
        DISTANCES = json.load(f)
    
    def __init__(self,row,day,form_sheet,weight_sheet):
        '''creates a Student object with instance variables corresponding to the student's google sheet information

        Args:
            row: considering Student objects might be defined in a for loop, the row variable will serve
            to access the corresponding GSheet row and access information from it

            day: the day of the week the program is being run on
                   
        
        Actions:
            uses GSheet class to define instance variables (name, type of car, weights, etc.)

        '''
        #do we run the program for the specific day or for all days at once?

        #save the weights sheet to the computer every time for up to dateness?

        #score
        self.score = 0


        #day of the week that this program is being run for
        self.day = day
            
        self.data = Data()
        self.data = self.data.getFormattedInfo()

        print(self.data)
        
        self.row = self.data[row]

        #print(self.row)

        self.name = self.row[0]
        self.car = self.row[1]
        self.distance = self.row[2]

        #critical need for days of the week
        self.mon_crit = self.row[3]
        self.tue_crit = self.row[4]
        self.wed_crit = self.row[5]
        self.thur_crit = self.row[6]
        self.fri_crit = self.row[7]
        
        self.sports_mon = self.row[8]
        self.sports_tue = self.row[9]
        self.sports_wed = self.row[10]
        self.sports_thu = self.row[11]
        self.sports_fri = self.row[12]
        
        self.carpoolMult = self.row[13]
        self.carpoolSeniors = self.row[14]

        #first period and last period free
        self.fpFree = self.row[15]
        self.lpFree = self.row[16]

        #boolean
        self.parallel = self.row[17]

        #the amount of days it has been since the student has been able to park on campus - adjust score based on this variable in generateScore()
        self.spot_since = 0
        
        self.zone = ''
        
##        #WEIGHTS
##        self.weight_sheet = weight_sheet
##        
##        #has to retrieve the second column from the weights sheet
##        self.weight_column = self.weight_sheet.getColumn(2,'weight_sheet.smth')
##
##        self.carpoolUnder_weight = self.weight_column[2]
##        self.carpoolSenior_weight = self.weight_column[3]
##        self.fpfree_weight = self.weight_column[4]
##        self.lpfree_weight = self.weight_column[5]
##
##        self.sports_weight = self.weight_column[6]
##        self.crit_weight = self.weight_column[7]
##        
##        self.commute_weight = self.weight_column[8]
##        self.strike_weight = self.weight_column[9]
##        self.crash_weight = self.weight_column[10] 
##        
    
    def generateScore(self):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone

        might use private methods to isolate that calculation of each category's weight'''


        '''To be written by Nambita and Aditya'''

        if self.day == 'Monday': 
            crit = self.mon_crit
        if self.day == 'Tuesday':
            crit = self.tue_crit
        if self.day == 'Wednesday':
            crit = self.wed_crit
        if self.day == 'Thursday':
            crit = self.thur_crit
        if self.day == 'Friday':
            crit = self.fri_crit
            
        #listing = [self.fpfree,self.lpfree,self.sports,crit,self.strike, self.crash]
            
        listing = [self.fpFree,self.lpFree,self.sports_mon,self.sports_tue,self.sports_wed,self.sports_thu,self.sports_fri]
        
        #convertResponse = convertResponses(listing)
        weighting = [16,8,10, 40,-40, -40] 
        scorelist = []
        print(listing)
        for i in listing:
            num = listing[i] * weighting[i]
            scorelist.append(num)
        score = sum(scorelist)
                
        
        if self.carpoolMult == 1:
                score = score + (self.carpoolMult*1.25)
        if self.carpoolSeniors == 1:
                score = score + (self.carpoolSeniors*3)
                
        print(score)
        #scoring = distance(score, self.commute)
        #print(scoring)
        #scorewstrikes = self.strike(score, self.strike, self.crash)
        scorewstrikes = score
        print(scorewstrikes)

    def strike(self,score, strike, crash):
        strike = strike * -20
        crash = crash * -500
        scorewstrikes = score + strike + crash
        return scorewstrikes

   

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
    student = Student(1,'Monday',2,2)
    student.generateScore()
    
if __name__ == '__main__': main()
    
