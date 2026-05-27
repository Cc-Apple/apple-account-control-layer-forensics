@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ==========================================
echo Finalize TTP result CSV only
echo ==========================================
echo.
echo Input:
echo   E:\Result\2026-05-27\My_Device\TTP_STRUCTURED_ONCE_*
echo   E:\Result\2026-05-27\Friend_Device\TTP_STRUCTURED_ONCE_*
echo.
echo Output:
echo   E:\Result\2026-05-27\_FINAL_REVIEW_PACKAGE
echo.
echo Safety:
echo   This script reads existing result CSV files only.
echo   It does not read raw logs.
echo   It does not delete, modify, rename, move, or overwrite source files.
echo.
echo Note:
echo   These paths reflect the original local execution environment.
echo   Reviewers may adjust them before rerunning the script.
echo.

if not exist "%~dp0finalize_ttp_results.py" (
  echo ERROR: finalize_ttp_results.py not found.
  pause
  exit /b 1
)

python --version
if errorlevel 1 (
  echo ERROR: python command not found.
  pause
  exit /b 1
)

python "%~dp0finalize_ttp_results.py"

echo.
echo FINISHED OR STOPPED.
pause
