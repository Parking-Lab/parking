'''
Saahil, James

Student Class
    Functionality:
<<<<<<< HEAD
        Hold information about each student's parking history and information (type of car, strikes, etc.)
        Generate score based on weights
        
        
=======
       Hold information about each student's parking history and information (type of car, strikes, etc.)
       Generate score based on weights
       
       
>>>>>>> 9f1e785df331d06057afc7fb6e1f995441a22683


This class holds information for the student object
'''
<<<<<<< HEAD
from data import Data
import json

class Student: 

    #! this code runs at *definition*, so basically when this file is imported.
    with open('distances.json', 'r') as f:
        DISTANCES = json.load(f)
    
    def __init__(self,row,data):
        '''creates a Student object with instance variables corresponding to the student's google sheet information

        Args:s
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
            
        self.data = data
        self.data = self.data.getFormattedInfo()
        
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

        self.strikes = self.row[18]

        print('len')
        print(len(self.row))

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

        
        
    
    def generateScore(self,day):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone

        might use private methods to isolate that calculation of each category's weight'''


        '''To be written by Nambita and Aditya'''

        self.day = day
        

        #print(self.name)

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

        if self.day == 'Monday': 
            sport = self.sports_mon
        if self.day == 'Tuesday':
            sport = self.sports_tue
        if self.day == 'Wednesday':
            sport = self.sports_wed
        if self.day == 'Thursday':
            sport = self.sports_thu
        if self.day == 'Friday':
            sport = self.sports_fri        



        listing = [self.fpFree,self.lpFree,crit,sport]

        
        #convertResponse = convertResponses(listing)
        weighting = [16,8,10, 40,-40, -40]

        #listing = [self.fpfree,self.lpfree,self.sports,crit,self.strike, self.crash]
            
        
        #convertResponse = convertResponses(listing)
        scorelist = []
        
        for i in range(len(listing)):
            num = listing[i] * weighting[i]
            scorelist.append(num)


        score = sum(scorelist)
                
        
        if self.carpoolMult == 1:
                score = score + (self.carpoolMult*1.25)
        if self.carpoolSeniors == 1:
                score = score + (self.carpoolSeniors*3)

        #print('name')
        #print(self.name)
                

        #scoring = distance(score, self.commute)
        #print(scoring)
        #scorewstrikes = self.strike(score, self.strike, self.crash)
        scorewstrikes = score

        return scorewstrikes

    def strike(self,score, strike, crash):
        strike = strike * -20
        crash = crash * -500
        scorewstrikes = score + strike + crash
        return scorewstrikes

    def getData(self):
        '''returns student score as a list'''
        
        score1 = self.generateScore('Monday')
        score2 = self.generateScore('Tuesday')
        score3 = self.generateScore('Wednesday')
        score4 = self.generateScore('Thursday')
        score5 = self.generateScore('Friday')

        

        return [score1,score2,score3,score4,score5]



   

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
    data = Data()
    student = Student(0,data)
    student_score = student.getData()
    print(student.name)
    print(student_score)

    print(len(student.data))

    for i in range(len(student.data)-1):
        student2 = Student(i+1,data)
        student2_score = student2.getData()
        print(student2.name)
        print(student2_score)

        
                   
    
##
##    student2 = Student(1,'Monday',2,2)
##    student2.generateScore()
##
##    student3 = Student(2,'Monday',2,2)
##    student3.generateScore()

=======

import json
from data import Data

class Student:
    #! this code runs at *definition*, so basically when this file is imported.
    with open('distances.json', 'r') as f:
        DISTANCES = json.load(f)

    def __init__(self,row,day,name,distance,car):

        self.score = 0
        #day of the week that this program is being run for
        self.day = day
        #self.form_sheet = form_sheet
        #self.row = self.form_sheet.getRow(row,'form_sheet.smth')
        self.name = name
        self.car = car
        self.distance = distance
        self.crash = 0 #TODO: get actual data for these two things
        self.strike = 0
        
        
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
    def __hash__(self) -> int:
        """hash implementation for Student. Don't call, use `hash(Student)`. Based on the name.

        Returns:
            int: the hash for this Student
        """
        return hash(self.name)

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
    
>>>>>>> 9f1e785df331d06057afc7fb6e1f995441a22683
if __name__ == '__main__': main()
