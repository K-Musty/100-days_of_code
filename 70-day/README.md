# Day 70 of 100 - Day 70: Git, Github, Version Control, Hosting blog on Railway(instead of heroku)

## Challenges

- Topics: Summary of Git, Github, and Version Control 
- Git Commands, Creating a Remote Repository, Creating Files (.gitignore), Branching, Merging, Cloning, Forking, Pull vs Push Requests
-  Add a .gitignore file 
- Use git to add version control to project
- Use environment variables to store sensitive information
- Set up a WSGI server with gunicorn
- Push to remote on Github
- Host on web service provider
- Upgrade SQLite Database to PostgreSQL

### Commands
Git Commands (Windows)
- ```git status```
- ```git init```
- ```git add .```
- ```git commit -m```
- ```git push```  Pushes to github
- ```git push origin main -u```  Pushes to github
- ```git rm --cached -r .```  Use this to remove files from my staging area / undo the last step. 
- ```git log```  This lets you see what commits you have made
- ```clear``` (to clear terminal)
- To exit the “git log” operation, press the “q” key

Create Remote Repository
- ```git remote add <name> <url>```
- ```git push -u <remote name>  <branch name>```  Pushes local repository to the remote repository. 

To Create a file:
- ```touch name-of-file.filetype```

To Create a GitIgnore File:
- ```touch .gitignore```
- ```code .gitignore```  (Open GitIgnore for Windows)

To Clone a repository
  - ```git clone url```

To Create a BRANCH
- git branch name-of-branch
- git branch (Use this to see which branch you are on)

TO MERGE the branches
- git merge name-of-branch
- Steps:
1. Go back to the main branch
git checkout main
2. Merge
git merge name-of-branch
Note: if VIM comes out, type ```:q!```  (to save and quit)

To SWITCH to BRANCH
- git checkout name-of-branch

GIT CLONE vs FORKING
- Git clone is  grabbing at the entirety of the repository and then cloning it to your local work environment. Git clone is useful with a trusted team that has read and write permissions, they can work on it locally/ push it and resolve conflicts 
- Forking is copying / duplicating a remote repository that's hosted on GitHub and keeping the copy under your own GitHub account where you can make changes to it. Once you've forked a remote repository, then you can do whatever you want to it.
- Forking allows an external user to do what they want: add features / improve code base, add more code etc.

PULL REQUESTS
- If external user wants the original creator of the repo to incorporate any changes they made, then make a pull request. Original owner decides whether or not to incorporate aka "merge" those requests.

vs PUSH REQUESTS
- You can do this with your own repository or your own copy of a repository
