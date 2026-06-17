# app.py

from fastapi import FastAPI

from routes.booking_routes import router as booking_router
from routes.destination_routes import router as destination_router
from routes.payment_routes import router as payment_router
from routes.user_routes import router as user_router

app = FastAPI(
    title="CRM Commerce API",
    version="1.0.0",
    description=(
        "Backend Python du projet CRM Commerce. "
        "La documentation interactive est disponible sur /docs."
    )
)


@app.get("/")
def home():
    """Retourne un message d'accueil pour verifier que l'API repond."""
    return {
        "success": True,
        "message": "Bienvenue sur l'API CRM Commerce"
    }


@app.get("/health")
def health():
    """Retourne l'etat de sante minimal du serveur."""
    return {
        "status": "OK"
    }

app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(destination_router, prefix="/api/destinations", tags=["Destinations"])
app.include_router(booking_router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(payment_router, prefix="/api/payments", tags=["Payments"])
