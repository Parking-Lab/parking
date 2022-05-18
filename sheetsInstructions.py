'''Hi it's alison ahhh'''

''' steps: 
after downlaoding json key for service account, the json file should be in downloads. move it to .config.

make sure project is cloned to desktop, idk

download parking_service_account_test.json from uh... just get the file from me lol. make sure it's in the downloads folder

cd
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install gspread
mkdir ~/.config/gspread
cp Downloads/parking_service_account.json ~/.config/gspread/service_account.json

TODO:
make this easier by creating an installation packet-like thing...
create an executable instead? One for installation, one for running the program.. if this is possible ;-;

'''

# just me testing stuff out :D

import gspread

def main():
    sa = gspread.service_account()
    sh = sa.open("CSUS Parking Results")

    wks = sh.worksheet("testing")
    values = [['hi', 'hi', 'hi', 'hi'], ['hello','hello','hello']]
    wks.insert_rows(values, 2)

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