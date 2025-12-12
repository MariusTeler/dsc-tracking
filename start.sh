#!/bin/bash

# Script pentru pornirea aplicației de tracking AWB

echo "================================================"
echo "   Aplicație Tracking AWB - Dragon Star Curier"
echo "================================================"
echo ""

# Verifică dacă virtual environment există
if [ ! -d "venv" ]; then
    echo "Creez virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment creat"
fi

# Activează virtual environment
echo "Activez virtual environment..."
source venv/bin/activate

# Instalează dependențe dacă este necesar
echo "Verific dependențele..."
pip install -q -r requirements.txt
echo "✓ Dependențe instalate"

echo ""
echo "Pornesc aplicația Flask..."
echo ""
echo "Aplicația va fi disponibilă la: http://localhost:5000"
echo "Apasă Ctrl+C pentru a opri serverul"
echo ""

# Pornește aplicația
python app.py
