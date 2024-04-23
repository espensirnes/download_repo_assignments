#Requires PyGithub

from github import Github
import numpy as np
import os
import subprocess

#      USER INPUT:
#***********************

#Type the various names that the students can concivabley have called thir projects 
#You should give them a specific name to use, but you can be certain that some students will mess it up
REPO_NAMES=['SOK-1005', 'sok-1005']


#write the directory here. You can use os.getcwd() once to get the current directory, but since the 
#working directory is changed in the script, DIRECTORY needs to be statically set:
DIRECTORY = r"B:\Undervisning\SOK-1005\download_repo_assignments" #os.getcwd()
START_ROW = 1

#Go to https://github.com/settings/tokens/new and generate a token, and enter it here:
TOKEN=<your github token here>

#Remember to fill usrnames.csv with two columns: the git hub user names of the students and a name identifier


#        CODE:
#*********************



uncloned=[]
revision_dates=[]


def main():
    g=Github(TOKEN)
    f = np.genfromtxt(DIRECTORY+'\\'+r'usrnames.csv', delimiter=";",dtype=str,encoding='utf-8-sig')
    for row in f[START_ROW:]:
        un, name = [str(i) for i in row[:2]]
        name = name.strip()
        print(f'Fetching {un}, name {name}')
        try:
            r=get_repo(g, un, REPO_NAMES, row)
            path=DIRECTORY+'\\'+name
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
            revision_dates.append([name,rvdt])
        except Exception as e:
            print(e)
            print(f"Repository not found for {un}, name{name}")
            uncloned.append(un)
    os.chdir(DIRECTORY)
    np.savetxt('rev.csv',revision_dates,fmt='%s',delimiter=";")
    np.savetxt('uncloned.csv',uncloned,fmt='%s',delimiter=";")
    print(uncloned)


def get_repo(g,un,reponames, row):
    repo = None
    if len(row)>2:
        try:
            r=g.get_user(un).get_repo(row[2])
            return r
        except:
            pass
    for i in reponames:
        try:
            r=g.get_user(un).get_repo(i)
            return r
        except:
            pass

main()
