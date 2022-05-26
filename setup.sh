# first make sure pip is installed
python -m ensurepip --default-pip
python -m pip install --upgrade pip

#install stuff
pip install numpy pandas gspread

#stuff with service acct
mkdir ~/.config/gspread 
mv Downloads/parking_service_account.json ~/.config/gspread/service_account.json

#make student list
python parking/listStudents.py

#make an alias in bashrc to the runner file
echo  'alias assignparking="python ~/parking/Sorter.py"' >> ~/.zshrc
echo  'alias assignparking="python ~/parking/Sorter.py"' >> ~/.bash_profile #backwards compatability!

source ~/.zshrc #get those updates

#yay! done!
echo 'Setup complete!'