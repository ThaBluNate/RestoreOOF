@echo off
SETLOCAL EnableDelayedExpansion
RD /S /Q compile 2>nul
set Silent=0
set Distro=0
if [%1] NEQ [] (
	if [%1] EQU [-H] (
		echo Compiler Help
		echo.
		echo -H: Show this help message
		echo -Q: Quiet mode
		echo -FD: 7z and Zips Compiled folder
		echo -DQ: The equivalant of using -Q and -FD
		goto :re
	) else (
		if /I [%1] EQU [-Q] (set Silent=1) else (
			if /I [%1] EQU [-FD] (set Distro=1) else (
				if /I [%1] EQU [-DQ] (set Distro=1&set Silent=1) else (
					echo Invalid param "%~1"
					goto :re
				)
			)
		)
	)
)
title Compile

if %Silent% NEQ 1 (
echo.
echo Compiling py to pyc...
)
py -m py_compile pylnk.py

if %Silent% NEQ 1 (
echo.
echo Rename pycache to compile folder...
)
ren __pycache__ compile
if %errorlevel% == 1 (cls&&echo Delete .\Compile\&&rd /s /q __pycache__&&goto :re)

if %Silent% NEQ 1 (
echo.
echo Copy main.py and icon.ico...
)
copy /Y oof.py ".\compile\oof.py">nul
copy /Y icon.ico ".\compile\icon.ico">nul
copy /Y oof.ogg ".\compile\oof.ogg">nul
cd compile

if %Silent% NEQ 1 (
echo.
echo Rename ".cpython-310.pyc" to ".pyc"...
)
ren PyLnk.cpython-310.pyc PyLnk.pyc

if %Silent% NEQ 1 (
echo.
echo Run Pyinstaller for main.py...
%appdata%\python\python310\Scripts\pyinstaller --noconfirm --onedir --windowed --icon "icon.ico" --clean --log-level "INFO" --add-data "PyLnk.pyc;."  "oof.py"
) else (
%appdata%\python\python310\Scripts\pyinstaller --noconfirm --onedir --windowed --icon "icon.ico" --clean --log-level "WARN" --add-data "PyLnk.pyc;."  "oof.py">nul
)

if %Silent% NEQ 1 (
echo.
echo delete temporary files...
)
rd /S /Q build
del /Q PyLnk.pyc
del /Q icon.ico
del /Q oof.py
del /Q oof.spec

if %Silent% NEQ 1 (
echo.
echo Copy compiled files to /compile, now that it's empty...
)
xcopy ".\dist\oof\*" ".\" /E>nul
rd /S /Q dist

copy ..\icon.png .\ >nul

:e
if %Silent% NEQ 1 (
echo.
echo Done
pause>nul
)
:re