from flask import Flask, render_template, request, jsonify
import base64
from datetime import datetime

app = Flask(__name__)

# Configurare API (când vei avea credențiale reale)
API_BASE_URL = "https://app.curierdragonstar.ro"
API_USERNAME = "your_username"  # Înlocuiește cu username-ul tău
API_PASSWORD = "your_password"  # Înlocuiește cu parola ta


# Date mock pentru testing (bazate pe exemplul din documentație)
MOCK_DATA = {
    "290591591": {
        "awb": "290591591",
        "status_curent": "Livrat",
        "istoric": [
            {
                "data": "2025-06-11 16:28:11",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-06-11 16:28:11",
                    "centru": "BAIA MARE",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-06-12 09:49:21",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-06-12 09:49:21",
                    "centru": "BAIA MARE",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-06-12 22:29:21",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-06-12 22:29:21",
                    "centru": "BRASOV",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-06-13 17:03:26",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-06-13 17:03:26",
                    "centru": "BRAGADIRU",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-06-13 16:55:20",
                "status": "In livrare",
                "detalii": {
                    "data": "2025-06-13 16:55:20",
                    "centru": "BRAGADIRU",
                    "eveniment": "Pregatit pentru livrare"
                }
            },
            {
                "data": "2025-06-14 14:32:10",
                "status": "Livrat",
                "detalii": {
                    "data": "2025-06-14 14:32:10",
                    "centru": "BUCURESTI",
                    "eveniment": "Livrat catre destinatar"
                }
            }
        ]
    },
    "123456789": {
        "awb": "123456789",
        "status_curent": "In livrare",
        "istoric": [
            {
                "data": "2025-12-11 10:00:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-11 10:00:00",
                    "centru": "CLUJ-NAPOCA",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-12-11 15:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 15:30:00",
                    "centru": "CLUJ-NAPOCA",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-12 08:00:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-12 08:00:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-12 11:00:00",
                "status": "In livrare",
                "detalii": {
                    "data": "2025-12-12 11:00:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Pregatit pentru livrare"
                }
            }
        ]
    },
    "987654321": {
        "awb": "987654321",
        "status_curent": "Colectata",
        "istoric": [
            {
                "data": "2025-12-12 14:15:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-12 14:15:00",
                    "centru": "TIMISOARA",
                    "eveniment": "Coletare efectuata"
                }
            }
        ]
    },
    "555888999": {
        "awb": "555888999",
        "status_curent": "In tranzit",
        "istoric": [
            {
                "data": "2025-12-10 08:30:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-10 08:30:00",
                    "centru": "IASI",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-12-10 12:45:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-10 12:45:00",
                    "centru": "IASI",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-11 05:20:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 05:20:00",
                    "centru": "BACAU",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-11 14:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 14:30:00",
                    "centru": "BACAU",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-12 03:15:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-12 03:15:00",
                    "centru": "PLOIESTI",
                    "eveniment": "Intrare Centru"
                }
            }
        ]
    },
    "111222333": {
        "awb": "111222333",
        "status_curent": "Livrat",
        "istoric": [
            {
                "data": "2025-12-09 09:00:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-09 09:00:00",
                    "centru": "CONSTANTA",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-12-09 16:20:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-09 16:20:00",
                    "centru": "CONSTANTA",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-10 02:45:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-10 02:45:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-10 10:30:00",
                "status": "In livrare",
                "detalii": {
                    "data": "2025-12-10 10:30:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Pregatit pentru livrare"
                }
            },
            {
                "data": "2025-12-10 15:20:00",
                "status": "Livrat",
                "detalii": {
                    "data": "2025-12-10 15:20:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Livrat catre destinatar"
                }
            }
        ]
    },
    "444555666": {
        "awb": "444555666",
        "status_curent": "In tranzit",
        "istoric": [
            {
                "data": "2025-12-08 11:00:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-08 11:00:00",
                    "centru": "ORADEA",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-12-08 17:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-08 17:30:00",
                    "centru": "ORADEA",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-09 08:15:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-09 08:15:00",
                    "centru": "CLUJ-NAPOCA",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-09 15:45:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-09 15:45:00",
                    "centru": "CLUJ-NAPOCA",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-10 06:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-10 06:30:00",
                    "centru": "TARGU MURES",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-10 13:00:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-10 13:00:00",
                    "centru": "TARGU MURES",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-11 04:20:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 04:20:00",
                    "centru": "SIBIU",
                    "eveniment": "Intrare Centru"
                }
            }
        ]
    },
    "777888999": {
        "awb": "777888999",
        "status_curent": "In livrare",
        "istoric": [
            {
                "data": "2025-12-11 07:00:00",
                "status": "Colectata",
                "detalii": {
                    "data": "2025-12-11 07:00:00",
                    "centru": "BRASOV",
                    "eveniment": "Coletare efectuata"
                }
            },
            {
                "data": "2025-12-11 11:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 11:30:00",
                    "centru": "BRASOV",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-11 18:45:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-11 18:45:00",
                    "centru": "PLOIESTI",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-12 07:15:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-12 07:15:00",
                    "centru": "PLOIESTI",
                    "eveniment": "Iesire Centru"
                }
            },
            {
                "data": "2025-12-12 09:30:00",
                "status": "In tranzit",
                "detalii": {
                    "data": "2025-12-12 09:30:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Intrare Centru"
                }
            },
            {
                "data": "2025-12-12 13:45:00",
                "status": "In livrare",
                "detalii": {
                    "data": "2025-12-12 13:45:00",
                    "centru": "BUCURESTI",
                    "eveniment": "Pregatit pentru livrare"
                }
            }
        ]
    }
}


def get_awb_history_mock(awb):
    """Returnează date mock pentru istoric AWB"""
    if awb in MOCK_DATA:
        return MOCK_DATA[awb]
    return None


def get_awb_history_real(awb):
    """
    Funcție pentru apelarea API-ului real DSC
    Deocamdată comentată, o vei folosi când vei avea credențiale
    """
    import requests

    # Creare header cu Basic Authentication
    credentials = f"{API_USERNAME}:{API_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.get(
            f"{API_BASE_URL}/awb/history/{awb}",
            headers=headers
        )

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Eroare la apelarea API: {e}")
        return None


def determine_progress_status(istoric):
    """Determină statusul progresului în cele 4 etape"""
    if not istoric:
        return {
            "colectata": False,
            "in_tranzit": False,
            "in_livrare": False,
            "livrat": False
        }

    status_curent = istoric[-1]["status"].lower()

    progress = {
        "colectata": False,
        "in_tranzit": False,
        "in_livrare": False,
        "livrat": False
    }

    # Setăm toate statusurile până la cel curent
    if "colectat" in status_curent or any("colectat" in item["status"].lower() for item in istoric):
        progress["colectata"] = True

    if "tranzit" in status_curent or any("tranzit" in item["status"].lower() for item in istoric):
        progress["colectata"] = True
        progress["in_tranzit"] = True

    if "livrare" in status_curent or any("livrare" in item["status"].lower() for item in istoric):
        progress["colectata"] = True
        progress["in_tranzit"] = True
        progress["in_livrare"] = True

    if "livrat" in status_curent:
        progress["colectata"] = True
        progress["in_tranzit"] = True
        progress["in_livrare"] = True
        progress["livrat"] = True

    return progress


@app.route('/')
def index():
    """Pagina principală"""
    return render_template('index.html')


@app.route('/tracking')
def tracking():
    """Pagina de tracking AWB"""
    awb = request.args.get('awb', '')

    if not awb:
        return render_template('tracking.html', error="Te rugăm să introduci un număr AWB")

    # Folosim date mock pentru testing
    # Când vei avea credențiale, înlocuiește cu: data = get_awb_history_real(awb)
    data = get_awb_history_mock(awb)

    if not data:
        return render_template('tracking.html',
                             error=f"AWB-ul {awb} nu a fost găsit",
                             awb=awb)

    # Determină progresul
    progress = determine_progress_status(data["istoric"])

    return render_template('tracking.html',
                         awb=awb,
                         status=data["status_curent"],
                         istoric=data["istoric"],
                         progress=progress)


@app.route('/api/tracking/<awb>')
def api_tracking(awb):
    """API endpoint pentru tracking (opțional, pentru AJAX)"""
    data = get_awb_history_mock(awb)

    if not data:
        return jsonify({"error": "AWB not found"}), 404

    progress = determine_progress_status(data["istoric"])

    return jsonify({
        "awb": awb,
        "status": data["status_curent"],
        "istoric": data["istoric"],
        "progress": progress
    })


if __name__ == '__main__':
    import os
    # Pentru Railway/Heroku - citește portul din variabila de mediu
    port = int(os.environ.get('PORT', 5000))
    # Debug = False pentru production
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
