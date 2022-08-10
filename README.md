# Parksort
# Table of Contents
- [Parksort](#parksort)
- [Table of Contents](#table-of-contents)
- [Quick Links](#quick-links)
- [Parking Results Legend](#parking-results-legend)
- [Installation Instructions](#installation-instructions)
  - [1. Download the code:](#1-download-the-code)
  - [2. Download the parking_service_account.json:](#2-download-the-parking_service_accountjson)
  - [3. Install everything:](#3-install-everything)
- [Using the program](#using-the-program)
- [Uninstalling parksort](#uninstalling-parksort)

# Quick Links
[This week's parking results](https://docs.google.com/spreadsheets/d/1nRXzXrlvIBJL-9Wj8XlBryqW488KrLgA9EKvBSnCaSg/edit#gid=1448752000)  
[Project Requirements Document (project overview)](https://docs.google.com/document/d/10XjM5ys3_QfG48dqYhJT48CZliQvoncWu97uxb0euo8/edit# )
# Parking Results Legend
SML: On-campus parking, spots 38-46 (Small spots)  
REG: On-campus parking, spots 52-89  
PAR: On-campus parking, 90-93 (Parallel spots)  
BART: Parking at St. Barts


# Installation Instructions
These instructions are for people with macs. If you have windows, this won't work, and you should find someone with a mac. If you have linux, this might work, or might not, but you can figure it out yourself like you do for everything else. 

> **Note**
> This installation guide requires Python 2.7, which is installed by default on Macs running anything before MacOS Monterey. We chose Python 2.7, even though it is deprecated, because of this ease-of-installation benefit. If you have updated to (or past) Monterey, use the MacOS installer [here](https://www.python.org/downloads/release/python-2718/) to restore python before continuing.

> **Warning**
> If you've messed with your `~/.bash_profile` or `~/.zshrc`, make sure everyone has read and write access: `sudo chmod 666 [file]`. This technically gives execute access too, but I don't remember the numbers for only r/w, it's not a security problem, and is confirmed to work.


## 1. Download the code:
1. Open the Terminal application by searching for Terminal in Spotlight Search.
2. paste this line in, and run it with enter:

```shell
~$ wget https://github.com/Parking-Lab/parking/archive/refs/heads/py2.7-release.zip; unzip py2.7-release.zip; rm -rf py2.7-release.zip; mv parking-py2.7-release/ parking/; chmod +x parking/setup.sh
```
> **Note:**
> `~$` is a shorthand for the terminal prompt. When you see a code snippet starting with `~$`, it usually means you should run that code in terminal. When copying the code, copy from after the space after the `$`. ie, `wget https://github.com/...` for this snippet.

## 2. Download the parking_service_account.json:
1. Get the parking_service_account.json file from asoong23@csus.org or rdye23@csus.org
2. Download parking_service_account.json and make sure the file is in Downloads
> **Warning**
> Never share this file with anyone or upload it anywhere. It contains sensitive information.

## 3. Install everything:
1. Go to the directory tab on MyCSUS and select your grade in list view. 
2. select and copy all names and emails (just click and drag allllll the way down)
3. In terminal, run this command. A text editor should open up, with a file repeating these instructions. Paste the copied data into the editor after the instructions, and SAVE THE FILE. Then close the text editor.  

```shell
~$ open parking/students.txt
``` 

4. Finally, run this command in Terminal.

```shell
~$ ./parking/setup.sh
```

Once you have run that command, close Terminal. This ensures that the shell updates before you try to run the program.  

The program is now ready to use. Further instructions and documentation are available on the PRD and Instructions document.  


# Using the program
This program is a command line utility, meaning that it runs in terminal and has a text-based interface. It is called `parksort`.
To run the sort, just run this command:
```shell
~$ parksort run
```
For a general blurb:
```shell
~$ parksort
```
For quick reference, either of these work:
```shell
~$ parksort -h
~$ parksort --help
```
And to change the sort settings:
```shell
~$ parksort config
```
And that's it!

---------  
# Uninstalling parksort
To uninstall parksort, just run this:
```shell
~$ parksort uninstall
```
This will remove the software and the configuration files, and will remove the lines added to `~/.bash_profile` and `~/.zshrc`.  
This does not remove any installed python libraries (nose, tornado, toml, numpy, pandas, gspread) or python itself. 

---------

If you have any questions or problems, email rdye23@csus.org, asoong23@csus.org, or consult the internet.
