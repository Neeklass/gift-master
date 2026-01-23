from django.http import HttpResponse
from django.db import connection
from django.conf import settings
import os


def home(request):
    return HttpResponse('<h1>GiftMaster Live</h1><p>Die Web-App ist erfolgreich deployed!</p>')


def status_check(request):
    """System-Status-Check für Deployment-Validierung"""
    
    # Datenbank-Check
    db_status = "✓ Verbindung OK"
    db_engine = "Unbekannt"
    try:
        connection.ensure_connection()
        db_engine = settings.DATABASES['default']['ENGINE']
        if 'postgresql' in db_engine:
            db_type = "PostgreSQL"
        elif 'sqlite' in db_engine:
            db_type = "SQLite"
        else:
            db_type = db_engine
    except Exception as e:
        db_status = f"✗ Fehler: {str(e)}"
        db_type = "Verbindung fehlgeschlagen"
    
    # Environment-Check
    debug_mode = settings.DEBUG
    db_host_set = bool(os.environ.get('DB_HOST'))
    
    # HTML-Response mit CSS
    html = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GiftMaster Status Check</title>
        <link rel="stylesheet" href="/static/css/status.css">
    </head>
    <body>
        <div class="container">
            <h1>GiftMaster Status Check</h1>
            
            <div class="section">
                <h2>Datenbank-Status</h2>
                <p><strong>Status:</strong> {db_status}</p>
                <p><strong>Typ:</strong> {db_type}</p>
                <p><strong>Engine:</strong> {db_engine}</p>
            </div>
            
            <div class="section">
                <h2>Environment-Konfiguration</h2>
                <p><strong>DEBUG-Modus:</strong> <span class="{'active' if debug_mode else 'inactive'}">{debug_mode}</span></p>
                <p><strong>DB_HOST gesetzt:</strong> <span class="{'active' if db_host_set else 'inactive'}">{db_host_set}</span></p>
                <p><strong>Allowed Hosts:</strong> {', '.join(settings.ALLOWED_HOSTS)}</p>
            </div>
            
            <div class="section">
                <h2>Static Files Check</h2>
                <p><strong>WhiteNoise:</strong> {'Aktiv (CSS wird geladen)' if 'whitenoise' in str(settings.MIDDLEWARE) else 'Nicht aktiv'}</p>
                <p><strong>STATIC_URL:</strong> {settings.STATIC_URL}</p>
                <p><strong>STATIC_ROOT:</strong> {settings.STATIC_ROOT}</p>
                <p class="static-test">Wenn diese Box grün ist, funktionieren Static Files!</p>
            </div>
            
            <div class="footer">
                <a href="/">← Zurück zur Startseite</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)
