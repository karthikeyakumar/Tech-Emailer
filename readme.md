# Daily-Puzzle
A simple python script using web scraping to send a mail containing a puzzle to recipients every 24 hrs.
I have deployed the code on Heroku using Heroku CLI. APScheduler runs the worker process at regular intervals (every 24 hours)


**Folder Structure:**
- clock.py: This file schedules the app to run at specified regular intervals (eg : everyday at 10 am etc)
- run.py: This file contains the code that does web scraping and sending mail.
- data.txt: This file stores the number of the next puzzle to send.

### NOTE : If you decide to use a Gmail account to send your emails, you'll need to set 'Allow less secure apps' to ON. Be aware that this makes it easier for others to gain access to your account, so it will be better to use a throwaway account for development.



**Steps to deploy using Heroku CLI**
- Go to the directory containing the files ( If not initialized as a git repo : git init --> git add . --> git commit -m "commit message" )
- Login to your Heroku Account
```
heroku login -i
```
- Connect to the App
```
heroku git:remote -a app_name
```
-Push to Heroku 
```
git push heroku master
```
- Scale up the clock process 
```
heroku ps:scale clock=1
```

-----------------------------------------Once Deployed the Script will run on its own----------------------------------------
