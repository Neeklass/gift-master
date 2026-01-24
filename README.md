# gift-master

Django Web-App für Geschenkverwaltung - deployed auf Azure App Service.

## Lokales Setup

### 1. Repository klonen
```bash
git clone <repository-url>
cd gift-master
```

### 2. Virtual Environment erstellen
```bash
python -m venv venv
```

### 3. Virtual Environment aktivieren
**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
.\venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 5. Datenbank migrieren
```bash
python manage.py migrate
```

### 6. Static files sammeln (optional)
```bash
python manage.py collectstatic --noinput
```

### 7. Development Server starten
```bash
python manage.py runserver
```

Server läuft auf: **http://127.0.0.1:8000/**

## URLs testen
- **Home**: http://127.0.0.1:8000/
- **Status Check**: http://127.0.0.1:8000/status/
- **Admin**: http://127.0.0.1:8000/admin/

## Lokale vs. Produktion
- **Lokal**: Nutzt SQLite (keine DB_HOST Variable)
- **Azure**: Nutzt PostgreSQL (DB_HOST gesetzt)

Die `.env`-Datei wird nicht ins Repository committed (siehe `.gitignore`).