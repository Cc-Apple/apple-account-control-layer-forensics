@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ==========================================
echo TTP structured once
echo ==========================================
echo.
echo Input folders:
echo   E:\My_Device\12G
echo   E:\My_Device\15G
echo   E:\My_Device\iPad
echo   E:\My_Device\iPhone11Pro
echo   E:\My_Device\mini1
echo   E:\My_Device\mini2
echo   E:\Friend_Device
echo.
echo Output folders:
echo   E:\Result\2026-05-27\My_Device
echo   E:\Result\2026-05-27\Friend_Device
echo   E:\Result\2026-05-27\_COMBINED
echo.
echo Safety:
echo   This script reads input folders only.
echo   It does not delete, modify, rename, move, or overwrite source files.
echo.
echo Note:
echo   These paths reflect the original local execution environment.
echo   Reviewers may adjust them before rerunning the script.
echo.

if not exist "%~dp0ttp_structured_once.py" (
  echo ERROR: ttp_structured_once.py not found in this folder.
  echo.
  echo Please place ttp_structured_once.py in the same folder as this batch file.
  pause
  exit /b 1
)

if not exist "E:\My_Device\12G" (
  echo ERROR: E:\My_Device\12G not found.
  pause
  exit /b 1
)

if not exist "E:\My_Device\15G" (
  echo ERROR: E:\My_Device\15G not found.
  pause
  exit /b 1
)

if not exist "E:\My_Device\iPad" (
  echo ERROR: E:\My_Device\iPad not found.
  pause
  exit /b 1
)

if not exist "E:\My_Device\iPhone11Pro" (
  echo ERROR: E:\My_Device\iPhone11Pro not found.
  pause
  exit /b 1
)

if not exist "E:\My_Device\mini1" (
  echo ERROR: E:\My_Device\mini1 not found.
  pause
  exit /b 1
)

if not exist "E:\My_Device\mini2" (
  echo ERROR: E:\My_Device\mini2 not found.
  pause
  exit /b 1
)

if not exist "E:\Friend_Device" (
  echo ERROR: E:\Friend_Device not found.
  pause
  exit /b 1
)

if not exist "E:\Result\2026-05-27" (
  mkdir "E:\Result\2026-05-27"
)

python --version
if errorlevel 1 (
  echo ERROR: python command not found.
  pause
  exit /b 1
)

echo.
echo Running...
python "%~dp0ttp_structured_once.py"

echo.
echo FINISHED OR STOPPED.
pause
