'''
Sorter Class

This class holds students, and sorts them based on rank.
'''
import bisect
import pandas as pd
from Student import Student
class Sorter:
    MAX_REG = 20
    MAX_SML = 2
    MAX_PAR = 4
    MAX_CAMPUS = MAX_REG + MAX_SML + MAX_PAR
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #augh why people why
    def __init__(self, students: 'list[Student]') -> 'None':
        """constructor for Sorter object. sorts students upon intialization.

        Args:
            students (list[students]): a list of all students to be sorted
        """
        self.students = dict(zip(students, [[0 for _ in range(5)] for _ in range(len(students))]))
        self.students = pd.df(self.students, orient = 'index', columns = Sorter.DAYS)
        self.students.insert(0, 'name', list(map(lambda x: x.getName(), self._getStudentList())))
        print(self.students.head())
        
        self._addScores()
    def _getStudentList(self):
        return list(self.students.index.values())

    def _addScores(self): #basically, get all the students, sort them separately for each day, then put the rankings into the df
        for s in self._getStudentList():
            for day in Sorter.DAYS:
                self.students[s][day] = s.generateScores(day)

    def add(self, *student: 'Student') -> 'None':
        """Adds `student` to the list of students, and places them in the correct order

        Args:
            student (Student, multiple accepted): the student(s) to add.
        """
        for s in student:
            self.students[s] = list(range(5))
        self._addScores()

    def __getitem__(self, idx: 'int|str|Student', day: int = None) -> 'Student|int':
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
        if day == None:
            return [self[d, idx] for d in range(5)]
        if isinstance(idx, int):
            return self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False).index.values()[idx]
        if isinstance(idx, str):
            return self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False)['name'].to_list().index(idx)
        if isinstance(idx, Student):
            return self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False).iloc(idx, Sorter.DAYS[day])
        raise TypeError(f'Expected idx of type int|str|Student but received {type(idx)}.')

    def delete(self, day: int, student: 'int|str|Student') -> 'None':
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
                self.students.sort_values(Sorter.DAYS[day], axis = 'columns', ascending = False).index.values()[student])
        if isinstance(student, str): # it's a name
            self.students.drop(self.students[self.students['name'] == student]) #drop all columns where the name is student
        if isinstance(student, Student): #it's a student object
            self.students.drop(student) #just drop the column, easy

    def __add__(self, other: 'Sorter') -> 'Sorter':
        """merges this an the other Sorter together, and returns the result. Does not modify either Sorter.

        Args:
            other (Sorter): the other Sorter to merge this one with

        Raises:
            TypeError: if you try to merge with a non-Sorter object (if you don't pass a Sorter)

        Returns:
            Sorter: the merge result
        """
        if not isinstance(other, Sorter):
            raise TypeError(f'Expected `other` of type Sorter but received {type(other)}')
        return Sorter(other._getStudentList()+self._getStudentList())

    def getAssignments(self) -> 'tuple[dict[str, list[Student]]]':
        """gets the final assignments for the week's parking

        Returns:
            tuple[dict[str, list[Student]]]: list of a dict for each day containing {parking zone: list of student objects}
        """
        #for each day
            #get order of students
            #make and append dict of zones based on rank
        output = [dict(zip(['REG', 'SML', 'PAR'], 
                           [[],    [],    []])) for _ in range(5)]
        for students in self:
            for day, student in enumerate(students):
                if student.canParallelPark() and len(output[day]['PAR'])<Sorter.MAX_PAR:
                    output[day]['PAR'].append(student)
                elif student.hasSmallCar() and len(output[day]['SML'])<Sorter.MAX_SML:
                    output[day]['SML'].append(student)
                elif len(output[day]['REG'])<Sorter.MAX_REG:
                    output[day]['REG'].append(student)
                if student.canParallelPark() and not student.hasSmallCar() and len(output[day]['PAR'])==Sorter.MAX_PAR and len(output[day]['SML'])<Sorter.MAX_SML and len(output[day]['REG'])==Sorter.MAX_REG and True in list(map(lambda s: s.canParallelPark() and s.hasSmallCar(), output[day]['PAR'])):
                    pass #panic! there's a problem!
                    # problem: if someone can park in par and small, they get put in par, but if there's someone 
                    # else later who can park in par but not sml, and par and reg is full, but sml is not, they'd 
                    # get put in barts even when they can park on campus
            



    def __iter__(self) -> 'Sorter':
        """initialization method for for loops.

        Returns:
            Sorter: this Sorter object, initialized for iteration
        """
        self.n = -1
        return self

    def __next__(self) -> 'Student':
        """gets the next element in self.

        Returns:
            Student: the next ranked student.
        """
        if self.n < len(self.students)-1:
            self.n+=1
            return self[self.n]
        else:
            raise StopIteration


def main():
    s = Sorter([Student(0,'Monday',2,2)])

if __name__ == '__main__': main()