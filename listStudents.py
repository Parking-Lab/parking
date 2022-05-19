'''
Author: Alison

Generate list of students (StrikesInfo):
    Description: sets up Google Sheet about all student info
    Main Functionality: just updates Google Sheet
    NOTE: DON'T USE THIS CLASS PLS!
'''

import gspread

class ListStudents():
    def __init__(self):
        """Creates a new class that represents the base info sheet
        """
        
        self.sa = gspread.service_account()
        self.sh = self.sa.open("CSUS Parking Data")
        self.wks = self.sh.worksheet("Students")
        self.file = open("students.txt", "r")
        self.info = self.file.readlines()
        
        self._outputToSheet()

        self.file.close()

    def _outputToSheet(self):
        reformatted = []
        
        for i in range(len(self.info)):
            obj = self.info[i]
            if '@' in obj: # found email
                row = []
                if obj[-1] == '\n': row.append(obj[:-1].lower())
                else: row.append(obj.lower())

                curInfo = self.info[i-1] # firstname lastname '2_
                lst = curInfo.split() # split by white space
                name = lst[1]
                if (lst[2][0] != '\''): name = lst[1] + " " + lst[2]
                row.append(name) # second object is always last name

                ind = curInfo.find("\'")
                row.append(curInfo[ind+1:ind+3]) # third object is always class

                row.append(0) # start with zero strikes
                
                reformatted.append(row)

        
        # print(reformatted)

        self.wks.delete_rows(2,self.wks.row_count-1)
        self.wks.insert_rows(reformatted, 2)

            
   
    
def main():
    listStudents = ListStudents()
    # print(strikesInfo.userStrikeHistory("alisonsoong@gmail.com"))



if __name__ == '__main__': main()
