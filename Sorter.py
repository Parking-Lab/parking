'''
Sorter Class

This class holds students, and sorts them based on rank.
'''
import pandas as pd
from Student import Student
from data import Data
import numpy as np
class Sorter:
    MAX_REG = 41
    MAX_SML = 8
    MAX_PAR = 4
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #augh why people why

    def __init__(self, students):
        """constructor for Sorter object. sorts students upon intialization.

        Args:
            students (list[students]): a list of all students to be sorted
        """
        self.students = [[0 for _ in range(5)] for _ in range(len(students))]
        self.students = pd.DataFrame(self.students, index = students, columns = Sorter.DAYS)
        self.students.insert(0, 'name', list(map(lambda x: x.getName(), self._getStudentList())))

        self._addScores()
        # print(self.students.head())
        
    def _getStudentList(self):
        """gets a list of the students in the current df's order

        Returns:
            list[Student]: list of students
        """
        return self.students.index.values.tolist()

    def _addScores(self): #basically, get all the students, sort them separately for each day, then put the rankings into the df
        """adds people's scores to the df
        """
        for s in self._getStudentList():
            for day in Sorter.DAYS:
                self.students.at[s, day] = s.generateScore(day)

    def add(self, *student):
        """Adds `student` to the list of students, and places them in the correct order

        Args:
            student (Student, multiple accepted): the student(s) to add.
        """

        self.students = pd.concat(self.students, pd.DataFrame(dict(zip(student, [[0 for _ in range(5)] for _ in range(len(student))]))))
        self._addScores()

    def __getitem__(self, idx, day = None):
        """gets an item, using subscript notation like a list. Takes an int (rank), str (student's name), or Student (actual equivalent student object).

        Args:
            day (int): int in [0, 4] describing the day of the week requested. Defaults to None, returning list of all days.
            idx (int|str|Student): if int, returns student in that rank (0 is best, can be negative, return Student). If str, returns rank of student with that name (int). If Student, returns rank of that Student (int).

        Raises:
            ValueError: if the str name or Student passed does not exist in the Sorter
            IndexError: if the int rank passed is out of range (ie not that many students exist) or if you entered a day that doesn't exist
            TypeError: if you try to get the student at rank 2.5

        Returns:
            Student|int : the rank or student requested
        """
        if isinstance(idx, tuple): #hack because you can't actually have two args in __getitem__, just ignore this
            idx, day = idx
        if day == None:
            return [self[idx, d] for d in range(5)]
        if isinstance(idx, int):
            return self.students.sort_values(Sorter.DAYS[day], ascending = False).index.values.tolist()[idx]
        if isinstance(idx, str):
            return self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False)['name'].to_list().index(idx)
        if isinstance(idx, Student):
            return self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False).iloc(idx, Sorter.DAYS[day])
        raise TypeError('Expected idx of type int|str|Student but received ' + str(type(idx)))

    def delete(self, day, student):
        """deletes the student at the rank, with the name, or equal to the Student.

        Raises:
            KeyError: if the str name or Student passed does not exist in the Sorter
            IndexError: if the int rank passed is out of range (ie not that many students exist)
            TypeError: if you try to get the student at rank 2.5

        Args:
            day (int): the day of the week you want the rankings to reference, in range [0, 4]
            student (int|str|Student): the student to delete. Specify rank (can be negative), name, or an identical Student object.
        """
        if isinstance(student, int): # it's a rank
            self.students.drop(#        sort by rank on day                 in descending order        get index at rank
                self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False).index.values.tolist()[student])
        if isinstance(student, str): # it's a name
            self.students.drop(self.students[self.students['name'] == student]) #drop all columns where the name is student
        if isinstance(student, Student): #it's a student object
            self.students.drop(student) #just drop the column, easy

    def __add__(self, other):
        """merges this an the other Sorter together, and returns the result. Does not modify either Sorter.

        Args:
            other (Sorter): the other Sorter to merge this one with

        Raises:
            TypeError: if you try to merge with a non-Sorter object (if you don't pass a Sorter)

        Returns:
            Sorter: the merge result
        """
        if not isinstance(other, Sorter):
            raise TypeError('Expected `other` of type Sorter but received ' + str(type(other)))
        return Sorter(other._getStudentList()+self._getStudentList())

    def getAssignments(self):
        """gets the final assignments for the week's parking

        Returns:
            list[list[str]]: arr[][] where arr[n][0] is student N's name, and arr[n][1:6] is student N's parking assignment by day
        """
        # for each day (5x):
        #   {
        #       reg: [student, student, student]
        #       sml: [student, student, student]
        #       par: [student, student, student]
        #   }

        #for each day
            #get order of students
            #make and append dict of zones based on rank
        results = [dict(zip(['REG', 'SML', 'PAR', 'BART'], 
                            [[],    [],    [],    []])) for _ in range(5)]
        for students in self:
            for day, student in enumerate(students):
                if student.canParallelPark() and len(results[day]['PAR'])<Sorter.MAX_PAR:
                    results[day]['PAR'].append(student)
                elif student.hasSmallCar() and len(results[day]['SML'])<Sorter.MAX_SML:
                    results[day]['SML'].append(student)
                elif len(results[day]['REG'])<Sorter.MAX_REG:
                    results[day]['REG'].append(student)
                else:
                    results[day]['BART'].append(student)



        # problem: if someone can park in par and small, they get put in par, but if there's someone 
        # else later who can park in par but not sml, and par and reg is full, but sml is not, they'd 
        # get put in barts even when they can park on campus

        #this block here fixes that problem
        for day in range(5):
            while len(results[day]['SML'])<Sorter.MAX_SML: #keep doing this until sml is filled

                try: 
                    doubleAbilityStudent = list(map(lambda s: s.hasSmallCar(),     results[day]['PAR'] )).index(True)
                    parallelBartStudent =  list(map(lambda s: s.canParallelPark(), results[day]['BART'])).index(True)
                except ValueError: #this means one of the required students was not found
                    break
                

                results[day]['SML'].append(results[day]['PAR'].pop(doubleAbilityStudent))
                results[day]['PAR'].append(results[day]['BART'].pop(parallelBartStudent))

        
        output = pd.DataFrame(np.zeros((len(self._getStudentList()), 6)), columns = ['Student', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

        output.loc[:, 'Student'] = np.array([x.getName() for x in self._getStudentList()])

        output.set_index('Student', inplace=True)

        for day, data in enumerate(results):
            for zone, students in data.items():
                for student in students:
                    output.at[student.getName(), Sorter.DAYS[day]] = zone
        
        # print(output.head())

        output.reset_index(inplace=True)
        return output.values.tolist()

    def __iter__(self):
        """initialization method for for loops, allowing looping through students by rank

        Returns:
            Sorter: this Sorter object, initialized for iteration
        """
        self.n = -1
        return self

    def next(self):
        """gets the next ranked student in self.

        Returns:
            Student: the next ranked student.
        """
        if self.n < len(self.students)-1:
            self.n+=1
            return self[self.n]
        else:
            raise StopIteration


def main():
    print('Fetching data...')
    data = Data()
    print('Loading data...')
    students = [Student(i, data) for i in range(len(data.getFormattedInfo()))]
    sorter = Sorter(students)
    print('Assigning parking zones and uploading results...')
    data.loadResults(sorter.getAssignments())
    print('Parking Assignments Complete!')

if __name__ == '__main__': main()