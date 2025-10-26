Login) 
git config --global user.name "travispotterAZ"
git config --global user.email "travispotter@arizona.edu"

1) USE bash terminal selected from down arrrow next to + when terminal is open. 

2) Navigate to folder wanting to track with Git
    2a) cd "/c/Users/tsjsp/OneDrive/Desktop/ECE 401c/Vinyl Record Management"\

3) Intialize git
    3a) git init

4) Add all files
    4a) git add .

5) Commit Files
    5a) git commit -m "COMMIT COMMENT"

Linking Local Repo to GitHub)
git remote add origin https://github.com/travispotterAZ/ECE401c_FinalProject.git


Check Link) git remote -v

Make terminal master)
git push -u origin master

PUSH CODE)
git push -u origin main
OR
git push -u origin master