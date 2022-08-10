'''
Saahil, James

Student Class
    Functionality:
        Hold information about each student's parking history and information (type of car, strikes, etc.)
        Generate score based on weights
        
        


This class holds information for the student object
'''
import json
import toml
import numpy as np

class Student: 

    #! this code runs at *definition*, so basically when this file is imported.
    with open('distances.json', 'r') as f: DISTANCES = json.load(f)
    with open('config.toml', 'r') as f:   WEIGHTS =   toml.load(f)['weights']
    
    def __init__(self,row):
        '''creates a Student object with instance variables corresponding to the student's google sheet information

        Args:
            row: considering Student objects might be defined in a for loop, the row variable will serve
            to access the corresponding GSheet row and access information from it

            day: the day of the week the program is being run on
                   
        
        Actions:
            uses GSheet class to define instance variables (name, type of car, weights, etc.)

        '''

        self.data = {
            'name':    row[0],
            'big_car': row[1],
            'zipcode': row[2],
            'crit':    row[3:8],
            'sports':  row[8:13],
            'carpool': row[13:15], #seniors=13, youngns=14
            'free':    row[15:17], #last period: 15, first: 16
            'par':     row[17],
            'strikes': row[18]
        }
        #the amount of days it has been since the student has been able to park on campus - adjust score based on this variable in generateScore()

    def __repr__(self):
        return 'Student: ' + self.name

    def getName(self):
        return self.name

    def canParallelPark(self):
        return bool(self.parallel)

    def hasSmallCar(self):
        return not self.car
        

    def __hash__(self):
        """hash implementation for Student. Don't call, use `hash(Student)`. Based on the name.
        Returns:
            int: the hash for this Student
        """
        return hash(self.name)
    
    def generateScore(self,day):
        '''uses weights to return a score that the Sorter function/class will use to assign the Student a parking zone'''

        student_attrs = np.array([self.data['free'] + 
                                [self.data['sports'][day]] + 
                                [self.data['crit'][day]] + 
                                [self.data['strikes']]])

        weights = np.array([[Student.WEIGHTS[i] for i in [
            "First_Period_Free",
            "Last_Period_Free",
            "Sports_Away_Game",
            "Critical_Need",
            "Strike",
            "Crash"]]])

        score = student_attrs.dot(weights.T) #take dot product (need to transpose because dot is just matmul so u dot v needs to be [u][v]^T)

        #* multiply the score by a the carpool multiplier
        score *= (
                        1 +                                                                                 # start with one, so by default it's x1, so we get same score
                        self.data['carpool'][day]*Student.WEIGHTS['Carpool_Multiplier_Per_Non_Senior'] +    # total minus seniors is num underclassmen, mult by 0.25 bc we weight underclassmen less
                        self.data['carpool'][day]*Student.WEIGHTS['Carpool_Multiplier_Per_Senior']          # add one multiplication per senior, because you're freeing up another spot
                    )
        
        score += np.random.normal(0, Student.WEIGHTS['Random_Factor_STDEV']) #add random stuff, mean 0
        
        return score + Student.distScore(str(self.data['zipcode']))

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
