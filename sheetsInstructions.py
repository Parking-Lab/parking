'''
Author: Alison
'''

''' 
Installation steps: 
1. make sure parking project is cloned to desktop:

cd
cd desktop
git clone https://github.com/Parking-Lab/parking.git

2. download parking_service_account_test.json from Alison. Make sure it's located in the downloads folder
3. type the following commands in command line:

cd
pip3 install --upgrade pip
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install gspread
mkdir ~/.config/gspread
cp Downloads/parking_service_account.json ~/.config/gspread/service_account.json

4. if the above doesn't work, try this:

cd
pip install --upgrade pip
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install gspread
mkdir ~/.config/gspread
cp Downloads/parking_service_account.json ~/.config/gspread/service_account.json
'''

'''
Other things that Alison needs to do D:
TODO:
make this easier by creating an installation packet-like thing...
create an executable instead? One for installation, one for running the program.. if this is possible ;-;
'''

# just me testing stuff out :D

import gspread

def main():
    print("------start of tests------")
    # sa = gspread.service_account()
    # sh = sa.open("CSUS Parking Results")

    # wks = sh.worksheet("testing")
    # values = [['hi', 'hi', 'hi', 'hi'], ['hello','hello','hello']]
    # wks.insert_rows(values, 2)

    # print("rows:", wks.row_count)
    # print('5/17/2022 10:54:13' > '5/17/2022 10:33:29')
    # print("columns:", wks.col_count)

    # cellList = wks.range('A2:I4')
    # for cell in cellList:
    #     cell.value = 'O_o'

    # wks.update_cells(cellList)

    # print(wks.get_all_values())
    # numRows = len(wks.get_all_values())
    # print(wks.row_values(1))
    # wks.get_values()

    # row = 1
    # col = 6

    # wks.update_cell(row, col, "lol")
    # wks.delete_row(2)
    # wks.insert_row(['hi','hi','hi','hi'], 2)
    # wks.delete_columns(1,6)
    # wks.delete_row(2)
    # wks.insert_row([], 2)

    # wks.delete_rows(2,numRows)

    # print(wks.row_values(1))
    # wks.get_values()


    # col = chr(ord('A') + (col-1))
    # row = str(row)
    # coord = col + row
    # print(coord)
    # print(wks.get_values(coord)[0][0])

    # weeklyInfo = open("weeklyInfo.txt", "w")
    # weeklyData = wks.get_all_values()
    # for row in weeklyData:
    #     weeklyInfo.write("\t".join(row) + "\n")

    # weeklyInfo.close()

    # wks.update_cell(2,2,'blub')

    # for i in range(40):
    #     wks.get_values('C3')
    # print("DONE")
    


if __name__ == '__main__':
    main()