# first make sure pip is installed
python -m ensurepip --default-pip
python -m pip install --upgrade pip

#install stuff
pip install numpy pandas gspread

#make student list
python parking/listStudents.py

#stuff with service acct
mkdir ~/.config/gspread 
cp Downloads/parking_service_account.json ~/.config/gspread/service_account.json

#make an alias in bashrc to the runner file
echo  'alias assignparking="python ~/parking/Sorter.py"' >> ~/.zshrc
echo  'alias assignparking="python ~/parking/Sorter.py"' >> ~/.bashrc #backwards compatability!

source ~/.zshrc #get those updates

#yay! done!
echo 'Setup complete!'