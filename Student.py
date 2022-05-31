'''
Saahil, James

Student Class
    Functionality:
        Hold information about each student's parking history and information (type of car, strikes, etc.)
        Generate score based on weights
        
        


This class holds information for the student object
'''
from data import Data
import json

class Student: 

    #! this code runs at *definition*, so basically when this file is imported.
    with open('distances.json', 'r') as f:
        DISTANCES = json.load(f)
    
    def __init__(self,row,data):
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
        
        self.carpoolSeniors = self.row[13]
        self.carpoolYoungns = self.row[14]

        #first period and last period free
        self.fpFree = self.row[15]
        self.lpFree = self.row[16]

        #boolean
        self.parallel = self.row[17]

        self.strikes = self.row[18]

        

        

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
##        self.lpfree_weight = self.weight_column[5]
##
##        self.sports_weight = self.weight_column[6]
##        self.crit_weight = self.weight_column[7]
##        
##        self.commute_weight = self.weight_column[8]
##        self.strike_weight = self.weight_column[9]
##        self.crash_weight = self.weight_column[10]
##
    def __repr__(self):
        return 'Student: ' + self.name

    def getName(self):
        return self.name

    def canParallelPark(self):
        if self.parallel == 1:
            return True
        return False

    def hasSmallCar(self):
        return not self.car
        

    def __hash__(self):
        """hash implementation for Student. Don't call, use `hash(Student)`. Based on the name.
        Returns:
            int: the hash for this Student
        """
        return hash(self.name)
    
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
                
        
        #! start reid's code, sorry for editing your method aditya and nambita
        dayIdx = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].index(day)
        #* multiply the score by a the carpool multiplier
        score *= (
                        1 +                                  # start with one, so by default it's x1, so we get same score
                        self.carpoolYoungns[dayIdx]*0.25 +   # total minus seniors is num underclassmen, mult by 0.25 bc we weight underclassmen less
                        self.carpoolYoungns[dayIdx]          # add one multiplication per senior, because you're freeing up another spot
                    )
        #! end reid's code

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
    def distScore(zipcode):
        """gets the score for a given zip code.

        Args:
            zipcode (int): the zip code to get the score for

        Raises:
            KeyError: if the zipcode is invalid
            
        Returns:
            float: the resulting score, based on the l1 distance to 94010 (school)
        """
        try:
            return Student.DISTANCES[zipcode]*0.9
        except: #hehe general except go brrrrrrrrr (i don't want to put KeyError cause idk if that's what this raises, idek if this is a dict or json object or what)
            return 0 #not a valid zipcode, their fault, score 0

def main():
    data = Data()
    student = Student(0,data)
    student_score = student.getData()
    print(student.name)
    print(student_score)

    print(len(student.data))

    print(student.hasSmallCar())

    for i in range(len(student.data)-1):
        student2 = Student(i+1,data)
        student2_score = student2.getData()
        print(student2.name)
        print(student2_score)
        
    

if __name__ == '__main__': main()
