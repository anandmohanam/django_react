@echo off

start cmd /k "python manage.py runserver"
timeout /t 2
cd myapp
start cmd /k "npm start"
timeout /t 4
start http://localhost:3000
