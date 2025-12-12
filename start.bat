@echo off
REM Script pentru pornirea aplicației pe Windows

echo ================================================
echo    Aplicatie Tracking AWB - Dragon Star Curier
echo ================================================
echo.

REM Verifică dacă virtual environment există
if not exist "venv" (
    echo Creez virtual environment...
    python -m venv venv
    echo Virtual environment creat
)

REM Activează virtual environment
echo Activez virtual environment...
call venv\Scripts\activate.bat

REM Instalează dependențe
echo Verific dependentele...
pip install -q -r requirements.txt
echo Dependente instalate

echo.
echo Pornesc aplicatia Flask...
echo.
echo Aplicatia va fi disponibila la: http://localhost:5000
echo Apasa Ctrl+C pentru a opri serverul
echo.

REM Pornește aplicația
python app.py

pause
