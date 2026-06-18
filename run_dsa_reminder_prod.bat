@echo off

cd /d C:\Users\pbhuv\Desktop\Project\2.PERSONAL\dsa_reminder

call venv\Scripts\activate.bat

python main.py >> logs\daily.log 2>&1

exit