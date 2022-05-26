# first make sure pip is installed
python -m ensurepip --default-pip
python -m pip install --upgrade pip

#then install virtualenv and make a new env
pip install --user virtualenv
python -m virtualenv parking-env

#install stuff
pip install numpy pandas gspread

#make student list
python listStudents.py

#stuff with service acct
mkdir ~/.config/gspread 
cp Downloads/parking_service_account.json ~/.config/gspread/service_account.json

#make an alias in bashrc to the runner file
echo  'alias assignparking="source parking-env/bin/activate; python ~/parking/Sorter.py; deactivate"' >> ~/.zshrc
echo  'alias assignparking="source parking-env/bin/activate; python ~/parking/Sorter.py; deactivate"' >> ~/.bashrc #backwards compatability!

source ~/.bashrc #get those updates

#yay! done!
echo 'Setup complete!'