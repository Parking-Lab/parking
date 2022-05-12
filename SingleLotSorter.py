'''
SingleLotSorter Class

This class holds students, and sorts them based on rank. Each SingleLotSorter is specific to one 
parking zone, so they all sort slightly differently. This class is used by the SingleLotSorter
class, which actually sorts students into zones based on their score for each zone.
'''
class SingleLotSorter:
    def __init__(self, students: 'list[Student]', zone: str):
        """constructor for SingleLotSorter object. sorts students upon intialization.

        Args:
            students (list[students]): a list of all students to be sorted
            zone (str): the zone this SingleLotSorter represents. can be 'REG', 'SMA', or 'PAR'
        """
        pass

    def add(self, *student: 'Student'):
        """Adds `student` to the list of students, and places them in the correct order

        Args:
            student (Student, multiple accepted): the student(s) to add.
        """
        pass

    def update(self, newStudents: 'dict[Student, Student]'):
        """updates the current students matching the keys in `newStudents` with their corrosponding values.

        Raises:
            KeyError: if a key in the newStudents doesn't exist in this SingleLotSorter.

        Args:
            newStudents (dict[Student, Student]): dict of updates, in the form {current: new, current: new, ...}
        """
        pass

    def __getitem__(self, day: int, index: 'int|str|Student' = 0):
        """gets an item, using subscript notation like a list. Takes an int (rank), str (student's name), or Student (actual equivalent student object).

        Args:
            day (int): int in [0, 4] describing the day of the week requested.
            index (int|str|Student, optional): if int, returns student in that rank (0 is best, can be negative, return Student). If str, returns rank of student with that name (int). If Student, returns rank of that Student (int). Defaults to -1.

        Raises:
            KeyError: if the str name or Student passed does not exist in the SingleLotSorter
            IndexError: if the int rank passed is out of range (ie not that many students exist) or if you entered a day that doesn't exist
            TypeError: if you try to get the student at rank 2.5

        Returns:
            Student|int : the rank or student requested
        """

        return
    
    def pop(self, day: int):
        """returns (and deletes) top ranked student, like pop function in a standard queue.

        Args:
            day (int): the day of the week you want the rankings from, in range [0, 4]

        Returns:
            tuple[Student, int]: tuple in the format (Student (Student object), rank (int))
        """
        pass

    def delete(self, day: int, student: 'int|str|Student'):
        """deletes the student at the rank, with the name, or equal to the Student.

        Raises:
            KeyError: if the str name or Student passed does not exist in the SingleLotSorter
            IndexError: if the int rank passed is out of range (ie not that many students exist)
            TypeError: if you try to get the student at rank 2.5

        Args:
            day (int): the day of the week you want the rankings to reference, in range [0, 4]
            student (int|str|Student): the student to delete. Specify rank (can be negative), name, or an identical Student object.
        """
        pass

    def __add__(self, other: 'SingleLotSorter'):
        """merges this an the other SingleLotSorter together, and returns the result. Does not modify either SingleLotSorter.

        Args:
            other (Sorter): the other SingleLotSorter to merge this one with

        Raises:
            TypeError: if you try to merge with a non-SingleLotSorter object (if you don't pass a SingleLotSorter)

        Returns:
            SingleLotSorter: the merge result
        """
        pass

    def _insert(self, student: 'Student'):
        """Uses binary search to insert a Student into the correct position in the sorted list.

        Args:
            student (Student): the student to insert into the SingleLotSorter.
        """

