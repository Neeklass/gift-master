#!/usr/bin/env python
"""
Azure PostgreSQL Migration Script
Führt Django-Migrationen auf dem Azure PostgreSQL-Server aus
"""
import os
import sys
import django

# Setze Umgebungsvariablen für Azure PostgreSQL
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giftmaster.settings')

# Überschreibe mit Azure-Datenbank-Credentials
os.environ['DB_HOST'] = 'az-pg-db.postgres.database.azure.com'
os.environ['DB_NAME'] = 'postgres'
os.environ['DB_USER'] = 'postgresql_admin'
os.environ['DB_PASSWORD'] = input('Datenbank-Passwort eingeben: ')
os.environ['DB_PORT'] = '5432'

# Django Setup
django.setup()

from django.core.management import call_command
from django.db import connection

print("\nTeste Datenbankverbindung...")
try:
    connection.ensure_connection()
    print("Verbindung zu Azure PostgreSQL erfolgreich!\n")
except Exception as e:
    print(f"Verbindungsfehler: {e}")
    sys.exit(1)

print("Zeige ausstehende Migrationen...")
try:
    call_command('showmigrations')
except Exception as e:
    print(f"Fehler beim Anzeigen der Migrationen: {e}")

print("\nFühre Migrationen aus...")
try:
    call_command('migrate', interactive=False)
    print("\nMigrationen erfolgreich ausgeführt!")
except Exception as e:
    print(f"Migrations-Fehler: {e}")
    sys.exit(1)

print("\nFertig! Die Azure-Datenbank ist jetzt bereit.")
