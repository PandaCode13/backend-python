# server.py

import os
from dotenv import load_dotenv
import uvicorn

from app import app
from config.database import (
    connect_mysql,
    connect_postgresql,
    connect_mongodb,
)

load_dotenv()

DATABASE_TYPE = os.getenv("DATABASE_TYPE", "mongodb").lower()

if DATABASE_TYPE == "mysql":
    connect_mysql()
elif DATABASE_TYPE == "postgresql":
    connect_postgresql()
elif DATABASE_TYPE == "mongodb":
    connect_mongodb()
else:
    print("⚠️ Aucune base de données valide sélectionnée.")

PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    print(f"🚀 Serveur démarré sur http://127.0.0.1:{PORT}")
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=True)