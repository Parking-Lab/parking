# first make sure pip is installed
python -m ensurepip --default-pip
python -m pip install --upgrade pip

#install stuff
python -m pip install nose tornado
python -m pip install --upgrade numpy pandas gspread

#stuff with service acct
mkdir ~/.config/gspread 
mv Downloads/parking_service_account.json ~/.config/gspread/service_account.json

#make student list
cd parking
python listStudents.py
cd

#make an alias in bashrc to the runner file
echo  'alias assignparking="cd ~/parking; python Sorter.py; cd"' >> ~/.zshrc
echo  'alias assignparking="cd ~/parking; python Sorter.py; cd"' >> ~/.bash_profile #backwards compatability!

source ~/.zshrc #get those updates

#yay! done!
echo 'Setup complete!'
