# Code for downloading repo assignments
This code will download github repositories for student projects. 

# Practial information

Before you give out the assignment, you need to make sure that everybody names the repository identically (or at least with not too many variations), so be very specific on what they should call the repository!

If you have a course with multiple assignments, it is a good idea to only use *one* repository, and ask the students to create separate directories within that repo for each assignment. That reduces the number of potential errors considerably. 

If the students keep the repositories private, they will need to give you access. Make sure everybody knows they have to do that, and accept all invitations immediately, since invitations expire. 

Try to download a few days in advance of the deadline, so that you can check that you have access. 

Google forms is an easy way to collect github usernames.

# Settings
You need to change these settings in the download.py file, before you can run it:

## Repo names
REPO_NAMES=['COURSE-101', 'course-101']

The various names that the students can conceivably have called their projects. You should give them a specific name to use, but you can be certain that some students will mess that up


## Directory 
DIRECTORY='put working directory here!!' #os.getcwd()

You can use os.getcwd() once to get the current directory, but since the working directory is changed in the script, DIRECTORY needs to be statically set (os.getcwd() wil depend on where the code exited last time it was run). 

## Token
TOKEN='Enter token here!!!'

Go to https://github.com/settings/tokens/new and generate a token, and set TOKEN to it. 


# Usernames file "usrnames.csv"

Remember to fill "usrnames.csv" with two columns: The git hub usernames of the students and a group identifier. 
"usrnames.csv" is semi comma delimited unless you change it in the code.
