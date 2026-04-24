@echo off
echo Running Git add...
git add .

set /p msg="Enter your commit message: "
echo Running Git commit...
git commit -m "%msg%"

echo Running Git push...
git push

echo.
echo Done! Code pushed to GitHub.
pause
