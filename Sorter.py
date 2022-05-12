class Sorter:
    def __init__(self, students: 'list[Student]'):
        """constructor for sorter object

        Args:
            students (list[students]): a list of all students to be sorted
        """
        pass

    def add(*student: 'Student'):
        """Adds `student` to the list of students, and places them in the correct order

        Args:
            student (Student, multiple accepted): the student(s) to add.
        """
        pass

    def update(newStudents: 'dict[Student, Student]'):
        """updates the current students matching the keys in `newStudents` with their corrosponding values.

        Args:
            newStudents (dict[Student, Student]): dict of updates, in the form {current: new, current: new, ...}
        """
        pass

    def __getitem__(index: 'int|String|Student' = 0):
        """gets an item, using subscript notation like a list. Takes an int (rank), String (student's name), or Student (actual equivalent student object).

        Args:
            index (int|String|Student, optional): if int, returns student in that rank (0 is best, can be negative, return Student). If String, returns rank of student with that name (int). If Student, returns rank of that Student (int). Defaults to -1.

        Raises:
            KeyError: if the String or Student passed does not exist in the sorter.
            IndexError: if the int rank passed is out of range (ie not that many students exist)
            TypeError: if you try to get the student at rank 2.5

        Returns:
            Student|int : the rank or student requested
        """

        return
    
    def pop():
        """returns (and deletes) top ranked student, like pop function in a standard queue.

        Returns:
            tuple[Student, int]: tuple in the format (Student (Student object), rank (int))
        """
        pass

    
