# Aplicație Tracking AWB - Dragon Star Curier

Aplicație web Python Flask pentru tracking AWB-uri folosind API-ul Dragon Star Curier.

## Caracteristici

- Interface web modern inspirat din pagina oficială DSC
- Tracking AWB cu 4 etape vizuale: Preluată → În tranzit → În livrare → Livrat
- Istoric complet al livrării cu detalii despre fiecare eveniment
- Design responsive (mobile-friendly)
- Tema dark mode
- Date mock pentru testing (până obții credențiale API)

## Structura Proiectului

```
dsc-tracking/
├── app.py                  # Backend Flask
├── requirements.txt        # Dependențe Python
├── README.md              # Acest fișier
├── templates/
│   ├── index.html         # Pagina principală de căutare
│   └── tracking.html      # Pagina de rezultate tracking
└── static/
    ├── css/
    │   └── style.css      # Stiluri personalizate
    └── js/
        └── main.js        # JavaScript pentru animații
```

## Instalare

### 1. Clonează sau descarcă proiectul

```bash
cd "dsc-tracking"
```

### 2. Creează un environment virtual (recomandat)

```bash
# Pe macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Pe Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Instalează dependențele

```bash
pip install -r requirements.txt
```

## Utilizare

### 1. Pornirea aplicației

```bash
python app.py
```

Aplicația va porni pe `http://localhost:5000`

### 2. Testarea cu date mock

Accesează `http://localhost:5000` în browser și folosește unul din AWB-urile de test:

- **290591591** - Status: Livrat (toate etapele complete)
- **123456789** - Status: În livrare (3 etape complete)

## Integrare cu API-ul real DSC

Pentru a folosi API-ul real în loc de date mock:

### 1. Obține credențiale API

Contactează departamentul Customer Service DSC la:
- Email: `api@curierdragonstar.ro`
- Solicită un username și password pentru API

### 2. Configurează credențialele în `app.py`

```python
# În fișierul app.py, la început:
API_USERNAME = "username_tau_aici"
API_PASSWORD = "parola_ta_aici"
```

### 3. Modifică funcția de tracking

În `app.py`, la linia ~150, în funcția `tracking()`:

```python
# Înlocuiește:
data = get_awb_history_mock(awb)

# Cu:
data = get_awb_history_real(awb)
```

## Endpoints API

Aplicația oferă următoarele endpoint-uri:

- `GET /` - Pagina principală cu formular de căutare
- `GET /tracking?awb=<numar>` - Pagina cu rezultatele tracking
- `GET /api/tracking/<awb>` - API JSON pentru tracking (opțional, pentru AJAX)

## Documentație API DSC

Aplicația implementează endpoint-ul:
- **GET /awb/history/:awb** - Returnează istoricul complet al AWB-ului

Pentru detalii complete despre API-ul DSC, consultă documentația oficială.

## Personalizare

### Modificarea culorilor

Editează fișierul `static/css/style.css`, secțiunea `:root`:

```css
:root {
    --bs-primary: #002b5c;      /* Albastru închis DSC */
    --bs-danger: #dc3545;       /* Roșu pentru butoane */
    --bs-body-bg: #1a1a1a;     /* Fundal dark */
    --bs-body-color: #f8f9fa;  /* Text alb */
}
```

### Adăugarea de AWB-uri mock

În `app.py`, adaugă noi AWB-uri în dicționarul `MOCK_DATA`:

```python
MOCK_DATA = {
    "numar_awb": {
        "awb": "numar_awb",
        "status_curent": "Status",
        "istoric": [...]
    }
}
```

## Troubleshooting

### Eroare: "Module not found"

```bash
pip install -r requirements.txt
```

### Aplicația nu pornește

Verifică dacă portul 5000 este liber:

```bash
# Schimbă portul în app.py, ultima linie:
app.run(debug=True, port=5001)  # Folosește alt port
```

### Stilurile nu se încarcă

Verifică că structura de directoare este corectă și că fișierul `style.css` există în `static/css/`.

## Dezvoltare Viitoare

Funcționalități planificate:
- [ ] Autentificare utilizatori
- [ ] Salvarea AWB-urilor favorite
- [ ] Notificări email/SMS pentru schimbări de status
- [ ] Export PDF al istoricului
- [ ] Tracking multiplu (mai multe AWB-uri simultan)
- [ ] Dashboard cu statistici

## Contact

Pentru întrebări despre API-ul DSC:
- Email: api@curierdragonstar.ro
- Website: https://dragonstarcurier.ro

## Licență

Acest proiect este creat pentru uz educațional și testing.
