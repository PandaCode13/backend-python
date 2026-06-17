# config/database.py

import os
from dotenv import load_dotenv

import pymysql
import psycopg2
from pymongo import MongoClient

# Charger les variables d'environnement
load_dotenv()


# -----------------------------
# Connexion MySQL
# -----------------------------
def connect_mysql():
    try:
        connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("✅ Connecté à MySQL")
        return connection
    except Exception as e:
        print(f"❌ Erreur MySQL : {e}")
        return None


# -----------------------------
# Connexion PostgreSQL
# -----------------------------
def connect_postgresql():
    try:
        connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", 5432),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DATABASE"),
        )
        print("✅ Connecté à PostgreSQL")
        return connection
    except Exception as e:
        print(f"❌ Erreur PostgreSQL : {e}")
        return None


# -----------------------------
# Connexion MongoDB
# -----------------------------
def connect_mongodb():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        client.admin.command("ping")  # Vérifie la connexion
        print("✅ Connecté à MongoDB")
        return client
    except Exception as e:
        print(f"❌ Erreur MongoDB : {e}")
        return None