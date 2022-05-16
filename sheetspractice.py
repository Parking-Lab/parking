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
create an executable instead? One for installation, one for running the program

'''

import gspread

def main():
    sa = gspread.service_account()
    sh = sa.open("CSUS Parking")

    wks = sh.worksheet("BaseInfo")

    print("rows:", wks.row_count)
    print("columns:", wks.col_count)

    # cellList = wks.range('A1:C7')
    # for cell in cellList:
    #     cell.value = 'O_o'

    # wks.update_cells(cellList)

    print(wks.get_values('A1:C1'))

    # wks.update_cell(2,2,'blub')

    for i in range(40):
        wks.get_values('C3')
    print("DONE")
    


if __name__ == '__main__':
    main()