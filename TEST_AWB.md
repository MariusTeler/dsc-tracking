# 🧪 AWB-uri de Test

Lista completă de AWB-uri mock disponibile pentru testing.

## 📦 AWB-uri Livrate (Status: Livrat)

### 290591591 - Baia Mare → București
**Status**: ✅ Livrat
**Traseu**: Baia Mare → Brașov → Brăgădiru → București
**Istoric**:
- 2025-06-11 16:28 - Colectată (Baia Mare)
- 2025-06-12 09:49 - Ieșire Centru (Baia Mare)
- 2025-06-12 22:29 - Intrare Centru (Brașov)
- 2025-06-13 17:03 - Ieșire Centru (Brăgădiru)
- 2025-06-13 16:55 - Pregătit pentru livrare
- 2025-06-14 14:32 - **Livrat** (București)

**Testează**: http://localhost:5000/tracking?awb=290591591

---

### 111222333 - Constanța → București
**Status**: ✅ Livrat
**Traseu**: Constanța → București (livrare rapidă)
**Istoric**:
- 2025-12-09 09:00 - Colectată (Constanța)
- 2025-12-09 16:20 - Ieșire Centru (Constanța)
- 2025-12-10 02:45 - Intrare Centru (București)
- 2025-12-10 10:30 - Pregătit pentru livrare
- 2025-12-10 15:20 - **Livrat** (București)

**Testează**: http://localhost:5000/tracking?awb=111222333

---

## 🚚 AWB-uri În Livrare (Status: In livrare)

### 123456789 - Cluj-Napoca → București
**Status**: 🚛 În livrare
**Traseu**: Cluj-Napoca → București
**Etapă curentă**: 3/4 (Pregătit pentru livrare)
**Istoric**:
- 2025-12-11 10:00 - Colectată (Cluj-Napoca)
- 2025-12-11 15:30 - Ieșire Centru (Cluj-Napoca)
- 2025-12-12 08:00 - Intrare Centru (București)
- 2025-12-12 11:00 - **Pregătit pentru livrare**

**Testează**: http://localhost:5000/tracking?awb=123456789

---

### 777888999 - Brașov → București
**Status**: 🚛 În livrare
**Traseu**: Brașov → Ploiești → București
**Etapă curentă**: 3/4 (Pregătit pentru livrare)
**Istoric**:
- 2025-12-11 07:00 - Colectată (Brașov)
- 2025-12-11 11:30 - Ieșire Centru (Brașov)
- 2025-12-11 18:45 - Intrare Centru (Ploiești)
- 2025-12-12 07:15 - Ieșire Centru (Ploiești)
- 2025-12-12 09:30 - Intrare Centru (București)
- 2025-12-12 13:45 - **Pregătit pentru livrare**

**Testează**: http://localhost:5000/tracking?awb=777888999

---

## 🔄 AWB-uri În Tranzit (Status: In tranzit)

### 555888999 - Iași → București (traseu lung)
**Status**: 🔄 În tranzit
**Traseu**: Iași → Bacău → Ploiești → București
**Etapă curentă**: 2/4 (Multiple opriri în centre)
**Istoric**:
- 2025-12-10 08:30 - Colectată (Iași)
- 2025-12-10 12:45 - Ieșire Centru (Iași)
- 2025-12-11 05:20 - Intrare Centru (Bacău)
- 2025-12-11 14:30 - Ieșire Centru (Bacău)
- 2025-12-12 03:15 - **Intrare Centru (Ploiești)**

**Testează**: http://localhost:5000/tracking?awb=555888999

---

### 444555666 - Oradea → Sibiu (traseu foarte lung)
**Status**: 🔄 În tranzit
**Traseu**: Oradea → Cluj → Târgu Mureș → Sibiu
**Etapă curentă**: 2/4 (Multiple centre de sortare)
**Istoric**:
- 2025-12-08 11:00 - Colectată (Oradea)
- 2025-12-08 17:30 - Ieșire Centru (Oradea)
- 2025-12-09 08:15 - Intrare Centru (Cluj-Napoca)
- 2025-12-09 15:45 - Ieșire Centru (Cluj-Napoca)
- 2025-12-10 06:30 - Intrare Centru (Târgu Mureș)
- 2025-12-10 13:00 - Ieșire Centru (Târgu Mureș)
- 2025-12-11 04:20 - **Intrare Centru (Sibiu)**

**Testează**: http://localhost:5000/tracking?awb=444555666

---

## 📥 AWB-uri Abia Colectate (Status: Colectata)

### 987654321 - Timișoara (abia început)
**Status**: 📥 Colectată
**Etapă curentă**: 1/4 (Abia preluată)
**Istoric**:
- 2025-12-12 14:15 - **Colectare efectuată** (Timișoara)

**Testează**: http://localhost:5000/tracking?awb=987654321

---

## 📊 Rezumat AWB-uri de Test

| AWB | Status | Oraș pornire | Etapă | Centre traversate |
|-----|--------|--------------|-------|-------------------|
| `290591591` | ✅ Livrat | Baia Mare | 4/4 | 4 centre |
| `111222333` | ✅ Livrat | Constanța | 4/4 | 2 centre |
| `123456789` | 🚛 În livrare | Cluj-Napoca | 3/4 | 2 centre |
| `777888999` | 🚛 În livrare | Brașov | 3/4 | 3 centre |
| `555888999` | 🔄 În tranzit | Iași | 2/4 | 3 centre |
| `444555666` | 🔄 În tranzit | Oradea | 2/4 | 4 centre |
| `987654321` | 📥 Colectată | Timișoara | 1/4 | 1 centru |

## 🎯 Scenarii de Test

### Test 1: Livrare completă
```
AWB: 290591591 sau 111222333
Verifică: Toate cele 4 etape sunt bifate
```

### Test 2: Pachet în curs de livrare
```
AWB: 123456789 sau 777888999
Verifică: 3 etape bifate, ultima în curs
```

### Test 3: Pachet cu multiple opriri
```
AWB: 555888999 sau 444555666
Verifică: Istoric lung cu multe centre
```

### Test 4: Pachet abia colectat
```
AWB: 987654321
Verifică: Doar prima etapă bifată
```

### Test 5: AWB inexistent
```
AWB: 000000000
Verifică: Mesaj de eroare "AWB-ul nu a fost găsit"
```

## 🚀 Link-uri Rapide

- [290591591 - Livrat](http://localhost:5000/tracking?awb=290591591)
- [111222333 - Livrat (Constanța)](http://localhost:5000/tracking?awb=111222333)
- [123456789 - În livrare](http://localhost:5000/tracking?awb=123456789)
- [777888999 - În livrare (Brașov)](http://localhost:5000/tracking?awb=777888999)
- [555888999 - În tranzit](http://localhost:5000/tracking?awb=555888999)
- [444555666 - În tranzit (Oradea)](http://localhost:5000/tracking?awb=444555666)
- [987654321 - Colectată](http://localhost:5000/tracking?awb=987654321)

---

💡 **Tip**: Pentru testing cu API real, înlocuiește aceste date mock cu credențialele API DSC în `app.py`.
