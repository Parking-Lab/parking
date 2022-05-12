'''
Sorter Class

This file contains the Sorter class, which uses SingleLotSorter to  
'''
class Sorter:
    def __init__(self, students: 'list[Student]'):
        """creates a new Sorter object

        Args:
            students (list[Student]): the students to start the sorter with
        """
        pass

    @property
    def REG():
        """accessor for REG SingleLotSorter. Allows users to do Sorter.REG[0] to get first rank for reg zone, for example.

        Returns:
            SingleLotSorter: the SingleLotSorter object for the REG zone, but read-only, so the user can't change the different sorters dfferently.
        """
        pass

    @property
    def SMA():
        """Accessor for SMA SingleLotSorter. Allows users to do Sorter.SMA[0] to get the first rank for reg zone, for example.

        Returns:
            SingleLotSorter: the SingleLotSorter object for the SMA zone, but read-only, so the user can't change the different sorters differently.
        """
        pass

    @property
    def PAR():
        """Accessor for PAR SingleLotSorter. Allows users to do Sorter.PAR[0] to get the first rank for reg zone, for example.

        Returns:
            SingleLotSorter: the SingleLotSorter object for the PAR zone, but read-only, so the user can't change the different sorters differently.
        """
        pass
    
    def update(newStudents: 'dict[Student, Student]'):
        """updates the current students matching the keys in `newStudents` with their corrosponding values.

        Raises:
            KeyError: if a key in the newStudents doesn't exist in this SingleLotSorter.

        Args:
            newStudents (dict[Student, Student]): dict of updates, in the form {current: new, current: new, ...}
        """
        pass

    def add(*student: 'Student'):
        """Adds a Student to all of the sorters.

        Args:
            student (Student, multiple accepted): the student(s) to add
        """
        pass
    
    def delete(*student: 'int|str|Student'):
        """deletes the student at the rank, with the name, or equal to the Student.

        Raises:
            KeyError: if the str name or Student passed does not exist in the SingleLotSorter
            IndexError: if the int rank passed is out of range (ie not that many students exist)
            TypeError: if you try to get the student at rank 2.5

        Args:
            student (int|str|Student, multiple accepted): the student to delete. Specify rank (can be negative), name, or an identical Student object.
        """
        pass
    
    def getAssignments():
        """gets the final assignments based on the rankings for this week.
        
        Returns:
            tuple[
                dict[str, list[Student]]
                dict[str, list[Student]]
            ]: first dict is dict of {parking zone: list of students there} representing the assignments, second dict is same thing describing waitlist
        """
        pass