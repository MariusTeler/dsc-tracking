# 📦 DSC AWB Tracking Application

Aplicație web Flask pentru tracking AWB-uri Dragon Star Curier cu integrare API completă.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

🔗 **Live Demo**: [Deploy pe Railway](https://railway.app) (coming soon)

## 📸 Preview

Aplicație modernă de tracking AWB cu:
- ✅ 4 etape vizuale de livrare
- ✅ Istoric complet al expedițiilor
- ✅ Design responsive (mobile & desktop)
- ✅ Tema dark mode inspirată din DSC
- ✅ Date mock pentru testing
- ✅ Integrare API gata configurată

## 🚀 Quick Start

### Instalare Locală

```bash
# Clonează repository-ul
git clone https://github.com/MariusTeler/dsc-tracking.git
cd dsc-tracking

# Creează virtual environment
python3 -m venv venv
source venv/bin/activate  # Pe Windows: venv\Scripts\activate

# Instalează dependențele
pip install -r requirements.txt

# Pornește aplicația
python app.py
```

Accesează: **http://localhost:5000**

### Script de pornire automată

```bash
# macOS/Linux
./start.sh

# Windows
start.bat
```

## 🧪 Testing

AWB-uri de test disponibile:

| AWB | Status | Descriere |
|-----|--------|-----------|
| `290591591` | Livrat | Toate cele 4 etape complete |
| `123456789` | În livrare | 3 din 4 etape complete |

## 🌐 Deploy pe Railway

### Opțiunea 1: Cu Railway CLI (3 comenzi)

```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### Opțiunea 2: Cu GitHub

1. Fork acest repository
2. Mergi pe [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Selectează `dsc-tracking`
5. Deploy automat! 🎉

📖 **Ghid complet**: Vezi [DEPLOYMENT.md](DEPLOYMENT.md) sau [QUICK_START_RAILWAY.md](QUICK_START_RAILWAY.md)

## 📁 Structura Proiectului

```
dsc-tracking/
├── app.py                  # Backend Flask
├── requirements.txt        # Dependențe Python
├── Procfile               # Railway/Heroku config
├── runtime.txt            # Python version
├── railway.json           # Railway settings
├── templates/
│   ├── index.html         # Pagina de căutare
│   └── tracking.html      # Pagina de rezultate
├── static/
│   ├── css/style.css      # Stiluri custom
│   └── js/main.js         # Animații JS
└── docs/
    ├── DEPLOYMENT.md      # Ghid deployment complet
    └── QUICK_START_RAILWAY.md  # Deploy rapid
```

## 🔌 Integrare API DSC

### Obținere Credențiale

Contactează DSC pentru API credentials:
- 📧 Email: **api@curierdragonstar.ro**
- 🌐 Website: **https://dragonstarcurier.ro**

### Configurare API Real

1. **În Railway Dashboard → Variables**:
   ```
   API_USERNAME=your_username
   API_PASSWORD=your_password
   ```

2. **În `app.py` linia 215**, modifică:
   ```python
   # Înlocuiește:
   data = get_awb_history_mock(awb)

   # Cu:
   data = get_awb_history_real(awb)
   ```

3. **Redeploy aplicația**

### Endpoint-uri API DSC Implementate

- ✅ `GET /awb/history/:awb` - Istoric complet AWB
- 🔜 `GET /awb/status/:awb` - Status curent
- 🔜 `POST /awb/send` - Generare AWB nou

## 🛠️ Tehnologii Folosite

- **Backend**: Flask 3.0.0
- **Frontend**: Bootstrap 5.3 (Dark theme)
- **Icons**: Bootstrap Icons
- **Deployment**: Railway / Heroku ready
- **Server**: Gunicorn (production)

## 📋 Features

### Implementate ✅

- [x] Tracking AWB cu 4 etape vizuale
- [x] Istoric complet al livrării
- [x] Design responsive
- [x] Tema dark mode DSC
- [x] Date mock pentru testing
- [x] API endpoint structure
- [x] Railway deployment ready
- [x] Animații și transitions

### Coming Soon 🔜

- [ ] Autentificare utilizatori
- [ ] Salvare AWB-uri favorite
- [ ] Notificări email/SMS
- [ ] Export PDF istoric
- [ ] Tracking multiplu (bulk)
- [ ] Dashboard cu statistici
- [ ] Integrare completă API DSC

## 🤝 Contribuții

Contribuțiile sunt binevenite! Pentru schimbări majore:

1. Fork repository-ul
2. Creează branch nou (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Deschide Pull Request

## 📝 Licență

Acest proiect este licențiat sub MIT License - vezi fișierul [LICENSE](LICENSE) pentru detalii.

## 👤 Autor

**Marius Teler**

- GitHub: [@MariusTeler](https://github.com/MariusTeler)
- Email: contact@example.com

## 🙏 Mulțumiri

- [Dragon Star Curier](https://dragonstarcurier.ro) pentru API
- [Flask](https://flask.palletsprojects.com/) pentru framework
- [Bootstrap](https://getbootstrap.com/) pentru UI
- [Railway](https://railway.app) pentru hosting

## 📞 Support

Pentru întrebări despre API-ul DSC:
- 📧 Email: **api@curierdragonstar.ro**
- 🌐 Website: **https://dragonstarcurier.ro**

Pentru issues legate de aplicație:
- 🐛 [Deschide un Issue](https://github.com/MariusTeler/dsc-tracking/issues)

---

⭐ Dacă acest proiect te-a ajutat, lasă un star pe GitHub!
