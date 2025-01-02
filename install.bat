@echo off

:menu

color F

cls
title Zero-Grab Installer
echo Are you...
echo 1. Installing
echo 2. Uninstalling

set /p prompt=""
if %prompt%==1 goto install
if %prompt%==2 goto uninstall
goto invalid

:install
pip install -r requirements.txt
exit

:uninstall
pip3 uninstall -r requirements.txt
exit

:invalid
color C
echo Invalid prompt, try again...
pause
goto menu

