# first make sure pip is installed
/usr/bin/python2.7 -m ensurepip --default-pip
/usr/bin/python2.7 -m pip install --upgrade pip

#install stuff
/usr/bin/python2.7 -m pip install nose tornado toml
/usr/bin/python2.7 -m pip install --upgrade numpy pandas gspread

#stuff with service acct
mkdir ~/.config/gspread 
mv Downloads/parking_service_account.json ~/.config/gspread/service_account.json

#make student list
cd parking
/usr/bin/python2.7 listStudents.py
cd

#make an alias in bashrc to the runner file
echo  "alias parksort=\"f(){ cd ~/parking; /usr/bin/python2.7 Sorter.py \"\$@\"; cd - > /dev/null; unset -f f;}; f\"" >> ~/.zshrc
echo  "alias parksort=\"f(){ cd ~/parking; /usr/bin/python2.7 Sorter.py \"\$@\"; cd - > /dev/null; unset -f f;}; f\"" >> ~/.bash_profile #backwards compatability!

source ~/.zshrc #get those updates

#yay! done!
echo 'Setup complete! Close and re-open terminal now to use parksort.'
