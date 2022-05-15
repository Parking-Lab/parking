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
            uses GSheet class to define instance variables (name, type of car, etc.)

        '''
        
        self.zone = ''
        
        pass

    def generateScore(self):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone'''

        '''To be written by Nambita and Aditya'''


    
