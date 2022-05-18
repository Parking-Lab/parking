'''
Saahil, James

Student Class
    Functionality:
        Hold information about each student's parking history and information (type of car, strikes, etc.)
        Generate score based on weights
        
        


This class holds information for the student object
'''

import json
from Data import Data

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
        self.data.getFormattedInfo()
        
        self.row = self.data[row]

        self.name = self.row[0]
        self.car = self.row[1]
        self.distance = self.row[2]

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

        #the amount of days it has been since the student has been able to park on campus - adjust score based on this variable in generateScore()
        self.spot_since = 0
        
        self.zone = ''
        
        #WEIGHTS
        self.weight_sheet = weight_sheet
        
        #has to retrieve the second column from the weights sheet
        self.weight_column = self.weight_sheet.getColumn(2,'weight_sheet.smth')

        self.carpoolUnder_weight = self.weight_column[2]
        self.carpoolSenior_weight = self.weight_column[3]
        self.fpfree_weight = self.weight_column[4]
        self.lpfree_weight = self.weight_column[5]

        self.sports_weight = self.weight_column[6]
        self.crit_weight = self.weight_column[7]
        
        self.commute_weight = self.weight_column[8]
        self.strike_weight = self.weight_column[9]
        self.crash_weight = self.weight_column[10] 
        
    
        

    def generateScore(self):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone

        might use private methods to isolate that calculation of each category's weight'''


        '''To be written by Nambita and Aditya'''
        pass

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


