@echo off
:loop
color 0b 
title LocalTalk Chat Room
cls
type chatfile.log
ping localhost -w 50>nul
goto loop
