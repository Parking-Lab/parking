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

    
    