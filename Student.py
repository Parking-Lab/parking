'''
Saahil, James

Student Class
    Functionality:
        Hold information about each student's parking history and information (type of car, strikes, etc.)
        Generate score based on weights
        
        


This class holds information for the student object
'''

class Student:
    def __init__(self,row):
        '''creates a Student object with instance variables corresponding to the student's google sheet information

        Args:
            row: considering Student objects might be defined in a for loop, the row variable will serve
            to access the corresponding GSheet row and access information from it
                   
        
        Actions:
            uses GSheet class to define instance variables (name, type of car, weights, etc.)

        '''

        #the amount of days it has been since the student has been able to park on campus - adjust score based on this variable in generateScore()
        self.spot_since = 0
        
        self.zone = ''
        
        pass

    def generateScore(self):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone

        might use private methods to isolate that calculation of each category's weight'''


        '''To be written by Nambita and Aditya'''


    
