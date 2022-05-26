# Parking Program

## Project Overview
For more information on the program, visit the PRD:
[Project Requirements Document](https://docs.google.com/document/d/10XjM5ys3_QfG48dqYhJT48CZliQvoncWu97uxb0euo8/edit# )

## Parking Results
SML: On-campus parking, spots 38-46 (Small spots)

REG: On-campus parking, spots 52-89

PAR: On-campus parking, 90-93 (Parallel spots)

BART: Parking at St. Barts

[This week's parking results](https://docs.google.com/spreadsheets/d/1nRXzXrlvIBJL-9Wj8XlBryqW488KrLgA9EKvBSnCaSg/edit#gid=1448752000)

## Our goal
Our goal is to make a transparent, equitable, and accessible system to organize the parking scheme at Crystal. From survey data about students’ specific parking needs, our system allows us to optimize for the best distribution of parking spots based on students’ needs. This will be accessible to any student who can park on campus.

## Why

We aim to create a system where the students that have the most need for parking will always have spots to park in. With this in mind, our system will also ensure that students with specific and variable needs can be accommodated on a weekly basis. While the situation requires that not every student may park on campus at the same time we also will not designate the same students to park off campus for the entire year. By understanding students' specific need for parking, we aim to prioritize those with greater needs in an equitable way that is fair to all.

Logistically, by making our program compatible with updating a live Google Sheet, our users can see in real-time the parking spots that are open and not, ultimately creating the most efficient system. We also hope to facilitate communication between parkers so that when any spots open up, we can easily communicate that to the rest of the community. 

Additionally, we are open-sourcing our entire algorithm. This choice was made because we want to prioritize our system being as transparent as possible so no students are unaware of why the decision for them to park where they did was made.

----------

# Installation
This information is also available in the Instructions doc.

## 1. Download the code:
1. Open the Terminal application by searching for Terminal in Spotlight Search.
2. paste this line in, and run it with enter:

```
wget https://github.com/Parking-Lab/parking/archive/refs/heads/py2.7-release.zip; unzip py2.7-release.zip; rm -rf py2.7-release.zip; mv parking-py2.7-release/ parking/; chmod +x parking/setup.sh
```

## 2. Download the parking_service_account.json:
1. Get the parking_service_account.json file from asoong23@csus.org
3. Download parking_service_account.json and make sure the file is in Downloads

## 3. Install everything:
1. Go to the directory tab on MyCSUS and select your grade in list view. 
2. select and copy all names and emails (just click and drag alll the way down)
3. In terminal, run this command. A text editor should open up, with a file repeating these instructions. Paste the copied data into the editor after the instructions, and SAVE THE FILE. Then close the text editor.  

```
open parking/students.txt
``` 

4. Finally, run this command in Terminal.

```
./parking/setup.sh
```

Once you have run that command, close Terminal. This ensures that the shell updates before you try to run the program.  

The program is now ready to use. Further instructions and documentation are available on the PRD and Instructions document.

----------

If you have any questions or problems, email rdye23@csus.org, asoong23@csus.org, or consult the internet.
