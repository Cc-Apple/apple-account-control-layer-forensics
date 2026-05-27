@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ==========================================
echo TTP 2026-05 3 devices
echo ==========================================
echo.
echo Input folders:
echo   C:\Users\Administrator\Desktop\05\12G
echo   C:\Users\Administrator\Desktop\05\15G
echo   C:\Users\Administrator\Desktop\05\iPhone11Pro
echo.
echo Output folder:
echo   C:\Users\Administrator\Desktop\05\Result
echo.
echo Safety:
echo   This script reads input folders only.
echo   It does not delete, modify, rename, move, or overwrite source files.
echo.
echo Note:
echo   These paths reflect the original local execution environment.
echo   Reviewers may adjust them before rerunning the script.
echo.

if not exist "%~dp0ttp_2026_05_3devices.py" (
  echo ERROR: ttp_2026_05_3devices.py not found.
  pause
  exit /b 1
)

python --version
if errorlevel 1 (
  echo ERROR: python command not found.
  pause
  exit /b 1
)

echo.
echo Running...
python "%~dp0ttp_2026_05_3devices.py"

echo.
echo FINISHED OR STOPPED.
pause
