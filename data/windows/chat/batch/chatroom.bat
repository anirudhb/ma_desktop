@echo off
color 0b
title LocalTalk Chat Client
:home
echo _______________
echo LocalTalk 1.1.2
echo Talk,Talk,Talk  
echo _______________
echo   Options:
echo 1. Login
echo 2. Make An Account
echo 3. Anoymous Session
echo 4. Exit
echo _______________
set /p option=Option:
if %option% == 1 goto login
if %option% == 2 goto account
if %option% == 3 goto sessionstart
if %option% == 4 goto exit

:login
cls
set /p un=Username:
set /p pn=Password:
echo %pn%>>.\privacy\pn.tmp
fc ".\privacy\pn.tmp" ".\users\%un%.profile"
if errorlevel == 3 goto incor
cd privacy
del pn.tmp
cd ..
goto chatstart
:account
cls
set /p nu=New Username:
set /p np=New Password:
echo %np%>>"./users/%nu%.profile"
goto login
:exit
cls
del chatfile.log
(NUL(set/p,z=) > chatfile.log
taskkill /im cmd.exe
exit
:chatstart
start msgbox.bat
echo To quit, type quit at the message prompt.
:chat
cls
set /p msg=Message:
cls
if "%msg%" == quit goto exit
echo "%un% : %msg%">"chatfile.log"
goto chat
:incor
echo The username or password is incorrect or the user does not exist.
pause
cls
cls
goto home
:sessionstart
start msgbox.bat
echo To quit, type quit at the message prompt.
:session
cls
set /p text=Text:
if %text% == quit goto exit
echo anoymous : %text%>chatfile.log
cls
goto session





