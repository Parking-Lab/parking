class Sorter:
    def __init__(self, students: 'list[Student]'):
        """constructor for sorter object. sorts students upon intialization.

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

    def __getitem__(index: 'int|str|Student' = 0):
        """gets an item, using subscript notation like a list. Takes an int (rank), str (student's name), or Student (actual equivalent student object).

        Args:
            index (int|str|Student, optional): if int, returns student in that rank (0 is best, can be negative, return Student). If str, returns rank of student with that name (int). If Student, returns rank of that Student (int). Defaults to -1.

        Raises:
            KeyError: if the str name or Student passed does not exist in the sorter
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

    def delete(student: 'int|str|Student'):
        """deletes the student at the rank, with the name, or equal to the Student.

        Raises:
            KeyError: if the str name or Student passed does not exist in the sorter
            IndexError: if the int rank passed is out of range (ie not that many students exist)
            TypeError: if you try to get the student at rank 2.5

        Args:
            student (int|str|Student): the student to delete. Specify rank (can be negative), name, or an identical Student object.
        """
        pass

    def __add__(other: 'Sorter'):
        """merges this an the other sorter together, and returns the result. Does not modify either sorter.

        Args:
            other (Sorter): the other sorter to merge this one with

        Raises:
            TypeError: if you try to merge with a non-sorter object (if you don't pass a sorter)

        Returns:
            Sorter: the merge result
        """
        pass
