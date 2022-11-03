# Code for downloading repo assignments
This code will download github repositories for student projects. You need to edit the user input in the file download.py as follows:

## Before you give out the assignment
Before you give out the assignment, you need to make sure that everybody names the repository identically (or at least with not too many variations), so be very specific on what they should call the repository!

If the students keep the repositories private, they will need to give you access. Make sure everybody knows they have to do that, and accept all invitations immediately, since invitations expire. 

## Collect usernames:
Google forms is an easy way to collect github usernames.

## Repo names
REPO_NAMES=['COURSE-101', 'course-101']

The various names that the students can conceivably have called their projects. You should give them a specific name to use, but you can be certain that some students will mess that up


## Directory 
DIRECTORY='put working directory here!!' #os.getcwd()

You can use os.getcwd() once to get the current directory, but since the working directory is changed in the script, DIRECTORY needs to be statically set

## Token
TOKEN='Enter token here!!!'

Go to https://github.com/settings/tokens/new and generate a token, and set TOKEN to it. 

## usrnames.csv
Remember to fill usrnames.csv with two columns: The git hub usernames of the students and a group identifier. 
usrnmaes.csv is semi comma delimited unless you change it in the code.
