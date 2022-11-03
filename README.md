# Code for downloading repo assignments
This code will download github repositories for student projects

# Use

##      USER INPUT:

You need to edit the user input in the file download.py as follows:

### Repo names
REPO_NAMES=['COURSE-101', 'course-101']

The various names that the students can concivabley have called thir projects. You should give them a specific name to use, but you can be certain that some students will mess it up


### Dierctory 
DIRECTORY='put working directory here!!' #os.getcwd()

You can use os.getcwd() once to get the current directory, but since the working directory is changed in the script, DIRECTORY needs to be statically set

### Token
TOKEN='Enter token here!!!'

Go to https://github.com/settings/tokens/new and generate a token, and set TOKEN to it. 

## usrnames.csv
Remember to fill usrnames.csv with the git hub user names of the students.
