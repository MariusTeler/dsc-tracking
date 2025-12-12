# Deployment pe Railway

Ghid complet pentru deployment-ul aplicației pe Railway.

## Fișiere create pentru Railway

✅ **Procfile** - Comandă pentru pornirea aplicației
✅ **runtime.txt** - Versiunea Python
✅ **requirements.txt** - Actualizat cu gunicorn
✅ **railway.json** - Configurare Railway
✅ **.dockerignore** - Fișiere ignorate în build
✅ **app.py** - Modificat pentru production

## Metoda 1: Deploy cu GitHub (Recomandat)

### Pasul 1: Creează Git Repository

```bash
cd "/Users/telermarius/Library/CloudStorage/Dropbox/GitHub/DSC Webpage/dsc-tracking"

# Inițializează Git (dacă nu e deja)
git init

# Adaugă toate fișierele
git add .

# Creează primul commit
git commit -m "Initial commit - DSC Tracking App"
```

### Pasul 2: Push pe GitHub

```bash
# Creează un repository nou pe GitHub
# Apoi conectează-l la local:

git remote add origin https://github.com/USERNAME/dsc-tracking.git
git branch -M main
git push -u origin main
```

### Pasul 3: Deploy pe Railway

1. **Mergi pe** https://railway.app
2. **Sign Up/Login** cu GitHub
3. **Click pe "New Project"**
4. **Selectează "Deploy from GitHub repo"**
5. **Alege repository-ul** `dsc-tracking`
6. Railway va detecta automat că e Python Flask
7. **Deploy automat** va începe!

### Pasul 4: Configurare (Opțional)

În Railway Dashboard:
- **Settings → Domains** - Generează URL public
- **Variables** - Adaugă variabile de mediu (când ai API credentials):
  - `API_USERNAME` = username-ul tău
  - `API_PASSWORD` = parola ta

## Metoda 2: Deploy cu Railway CLI

### Pasul 1: Instalează Railway CLI

```bash
# Cu npm
npm i -g @railway/cli

# Sau cu brew (macOS)
brew install railway
```

### Pasul 2: Login și Deploy

```bash
cd "/Users/telermarius/Library/CloudStorage/Dropbox/GitHub/DSC Webpage/dsc-tracking"

# Login în Railway
railway login

# Creează proiect nou
railway init

# Deploy
railway up

# Obține URL-ul public
railway domain
```

## Metoda 3: Deploy fără Git

### Deploy direct din local:

```bash
cd "/Users/telermarius/Library/CloudStorage/Dropbox/GitHub/DSC Webpage/dsc-tracking"

railway login
railway init
railway up
```

## Verificare după Deploy

### 1. Verifică Logs

```bash
# Cu CLI
railway logs

# Sau în Dashboard
# Projects → Your Project → Deployments → View Logs
```

### 2. Testează aplicația

- Mergi la URL-ul generat de Railway
- Testează cu AWB-urile mock:
  - `290591591`
  - `123456789`

## Variabile de Mediu (când ai API credentials)

În Railway Dashboard → Variables:

```
API_USERNAME=your_username
API_PASSWORD=your_password
FLASK_ENV=production
```

Apoi în `app.py`, modifică linia 215:

```python
# Înlocuiește:
data = get_awb_history_mock(awb)

# Cu:
data = get_awb_history_real(awb)
```

## Troubleshooting

### Build Failed

```bash
# Verifică logs
railway logs

# Verifică că toate fișierele sunt commit-ate
git status
```

### Application Error

- Verifică că `Procfile` există
- Verifică că `gunicorn` e în `requirements.txt`
- Verifică logs pentru erori Python

### Port Binding Error

- Railway setează automat variabila `PORT`
- `app.py` e deja configurat să o folosească

## Redeploy după modificări

### Cu GitHub:

```bash
git add .
git commit -m "Update: descriere modificări"
git push
```

Railway va face redeploy automat!

### Cu CLI:

```bash
railway up
```

## Comenzi utile Railway CLI

```bash
# Vezi statusul
railway status

# Vezi variabilele
railway variables

# Deschide dashboard
railway open

# Deschide aplicația
railway open --app

# Șterge deployment
railway down
```

## Costuri Railway

**Plan Gratuit:**
- $5 credit lunar
- 500 ore/lună execution
- Perfect pentru testing și proiecte mici

**Dacă depășești:**
- Upgrade la Hobby Plan: $5/lună
- Developer Plan: $20/lună

## Link-uri utile

- **Railway Dashboard**: https://railway.app/dashboard
- **Documentație**: https://docs.railway.app
- **Status Page**: https://status.railway.app

## Next Steps după deploy

1. ✅ Verifică că aplicația rulează
2. ✅ Salvează URL-ul public
3. ✅ Testează toate funcționalitățile
4. 📧 Obține API credentials de la DSC
5. 🔧 Configurează variabilele de mediu
6. 🚀 Activează API-ul real

---

**Need help?** Contactează-mă sau vezi documentația Railway.
