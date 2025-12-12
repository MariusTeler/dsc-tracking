# 🚀 Quick Start - Deploy pe Railway (5 minute)

## Varianta ULTRA-RAPIDĂ cu Railway CLI

### 1. Instalează Railway CLI

```bash
npm i -g @railway/cli
```

### 2. Deploy în 3 comenzi

```bash
cd "/Users/telermarius/Library/CloudStorage/Dropbox/GitHub/DSC Webpage/dsc-tracking"

railway login
railway init
railway up
```

### 3. Obține URL-ul

```bash
railway domain
```

**GATA!** Aplicația ta e live! 🎉

---

## Varianta cu GitHub (mai organizat)

### 1. Creează Git repo

```bash
cd "/Users/telermarius/Library/CloudStorage/Dropbox/GitHub/DSC Webpage/dsc-tracking"
git init
git add .
git commit -m "Initial commit"
```

### 2. Push pe GitHub

- Mergi pe https://github.com/new
- Creează repo nou: `dsc-tracking`
- Apoi:

```bash
git remote add origin https://github.com/USERNAME/dsc-tracking.git
git branch -M main
git push -u origin main
```

### 3. Deploy pe Railway

1. Mergi pe https://railway.app
2. Login cu GitHub
3. New Project → Deploy from GitHub
4. Selectează `dsc-tracking`
5. **GATA!** 🎉

---

## Ce să verifici după deploy

✅ **Verifică că rulează:**
- Click pe deployment URL
- Testează cu AWB: `290591591`

✅ **Vezi logs:**
```bash
railway logs
```

✅ **Generează domeniu public:**
- În Dashboard → Settings → Generate Domain

---

## Următorii pași

📧 **Obține API credentials** de la DSC:
- Email: api@curierdragonstar.ro

🔧 **Adaugă credentials în Railway:**
- Dashboard → Variables:
  - `API_USERNAME`
  - `API_PASSWORD`

🚀 **Activează API real:**
- În `app.py` linia 215, schimbă:
```python
data = get_awb_history_real(awb)  # În loc de mock
```

---

## Need Help?

📖 Vezi **DEPLOYMENT.md** pentru detalii complete
🆘 Railway Docs: https://docs.railway.app

**Happy Deploying! 🚂**
