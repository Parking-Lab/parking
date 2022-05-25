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