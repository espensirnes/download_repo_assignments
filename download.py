#Requires PyGithub

from github import Github
import numpy as np
import os
import subprocess

#      USER INPUT:
#***********************

#Type the various names that the students can concivabley have called thir projects 
#You should give them a specific name to use, but you can be certain that some students will mess it up
REPO_NAMES=['COURSE-101', 'course-101']


#write the directory here. You can use os.getcwd() once to get the current directory, but since the 
#working directory is changed in the script, DIRECTORY needs to be statically set:
DIRECTORY='put working directory here!!' #os.getcwd()

#Go to https://github.com/settings/tokens/new and generate a token, and enter it here:
TOKEN='Enter token here!!!'

#Remember to fill usrnames.csv with two columns: the git hub user names of the students and a group identifier


#        CODE:
#*********************



uncloned=[]
revision_dates=[]


def main():
    g=Github(TOKEN)
    f = np.genfromtxt(DIRECTORY+'\\'+'usrnames.csv', delimiter=";",dtype=str,encoding='utf-8-sig')
    for name,grp in f:
        print(f'Fetching {name}, group {grp}')
        try:
            r=get_repo(g, name, REPO_NAMES)
            path=DIRECTORY+'\\'+grp
            cloneurl=r.clone_url.replace('https://github',f'https://{TOKEN}@github')
            try:
                os.chdir(path+'\\'+r.name)
                os.system(f"git pull {cloneurl}")
            except:
                if not os.path.exists(path):
                    os.makedirs(path)
                os.chdir(path)
                a=os.system(f"git clone {cloneurl}")
            rvdt=subprocess.getoutput("git log -1 --format=%cd")
            revision_dates.append([grp,rvdt])
        except Exception as e:
            print(e)
            print(f"Repository not found for {name}, group{grp}")
            uncloned.append(name)
    os.chdir(DIRECTORY)
    np.savetxt('rev.csv',revision_dates,fmt='%s',delimiter=";")
    np.savetxt('uncloned.csv',uncloned,fmt='%s',delimiter=";")
    print(uncloned)


def get_repo(g,name,reponames):
    for i in reponames:
        try:
            r=g.get_user(name).get_repo(i)
            return r
        except:
            pass

main()
