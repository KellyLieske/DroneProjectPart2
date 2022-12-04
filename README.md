# Drone Project Part2: DynamoDB

This project assumes you have Python 3.x installed
(Wherever you see a reference to Python3.x, replace the x with the version you have installed I.e Python3.11)
Pycharm is optional but highly recomended.

Step 0: Install credentials for AWS in the correct location

AWS will look for credentials file at the root of the user directory

Make sure you have valid aws credentials before proceeding and they're in the correct location


Step 1: Download the repo

Step 2: Open the repo in pycharm or navitagate there with a cmd window


Step 3: Using pycharm terminal or command line, install boto3

Pycharm terminal: pip install boto3

Terminal: Python3.x pip install boto3

Step 4: this program uses Command line arguments to add data to the dynamo db table

For pycharm: click the run option in the top menu bar, then click edit configurations, in the parameters section paste in

"N" "00:05" "13:02" "KellyLieske@emich.edu" "Kelly Lieske" "CompSci"

for terminal 

python .\main.py Y 00:25 13:01 KellyLieske@emich.edu "kelly lieske" Cs

Parameters:

Parameter 1: values are Y or N for valid and invalid flight repectively

Parameter 2: the total time of the flight MM:SS

Parameter 3: the time in 24 hour format that the flight started

Parameter 4: the email of the pilot

Parameter 5: the full name of the pilot

Paraameter 6: the Department of the pilot

After running the program, you will successfully add a row to the database with your data

Step 5:

The data from the table will print automatically, but it can be accessed without adding a new record but omitting comand line parameters at run time



