@echo off
del chatfile.log
echo NUL > chatfile.log
cd privacy
del -s -q *.*
cd ..\users
del -s -q *.*
cd ..
exit
